Python tip of the week 2, access speed of data structures
==========================================================

Python has 3 main types of data structures for storing collections of items - lists, sets, and dictionaries. It's important to know that the access speed of a list is O(n), that is it takes longer and longer to check something as the list gets longer. Sets and dictionaries have O(1) access, which means that the access speed is the same regardless of the size of the collection.

Consider if we have a list of ground-truth items and a list of candidates and we want to check if each of the candidates is in the ground truth:

.. code-block:: python

    import random
    import timeit

    # This is a list of 10k random items as an example
    small_groundtruth = [random.randint(1, 1000000) for x in range(10000)]

    def check_candidates(groundtruth, n_candidates):
        """Check which of the candidates in the range [0-n_candidates]
           are present in the collection `groundtruth`"""
        yes = [] 
        no = [] 
        for candidate in range(n_candidates): 
            if candidate in groundtruth:
                # This is just an example about what to do with the result
                yes.append(candidate) 
            else: 
                no.append(candidate) 

We can use the timeit module (from tip 1!) to see how long our method takes:

.. code-block:: python

    timeit.timeit('check_candidates(small_groundtruth, 100)', number=10, globals=globals())
    0.13829218316823244

OK, so checking 100 candidates in a list of 10k items 10 times (the `number` parameter) takes 0.14 seconds (0.01 seconds per iteration), this seems pretty fast.
What happens if we want to check 1000 items?

.. code-block:: python

    timeit.timeit('check_candidates(small_groundtruth, 1000)', number=10, globals=globals())
    1.3406621366739273

Time increases linearly. However, what happens if our groundtruth grows by some orders of magnitude?

.. code-block:: python

    # 100k items
    groundtruth = [random.randint(1, 1000000000) for x in range(100000)]

    timeit.timeit('check_candidates(groundtruth, 100)', number=10, globals=globals())
    1.36269876267761

    timeit.timeit('check_candidates(groundtruth, 1000)', number=10, globals=globals())
    13.427033469080925

    # 1m items?
    groundtruth = [random.randint(1, 1000000000) for x in range(1000000)]

    timeit.timeit('check_candidates(groundtruth, 1000)', number=10, globals=globals())
    122.46592588163912

This is getting longer and longer. Why is this the case? When testing for membership in a list, we have to check every item in the list in order to see if a candidate exists. If the item doesn't exist in the list we have to check all items in the list before we can say that it doesn't exist. As this list gets longer and longer, this operation takes longer.
We can speed up the process by checking if the item is in a set instead of a list:

.. code-block:: python

    groundtruth_set = set(groundtruth)

    timeit.timeit('check_candidates(groundtruth_set, 1000)', number=10, globals=globals())
    0.0022530462592840195

The same operation which took 122 seconds above (12 seconds per `number`) only took 0.002 seconds! (60,000 times faster!)
What happens if we make the groundtruth 100x larger?

.. code-block:: python

    # These two lines take a while to run, but it's just one-time setup for the demo
    groundtruth100m = [random.randint(1, 1000000000000) for x in range(1000000000)]
    groundtruth100m_set = set(groundtruth100m)

    timeit.timeit('check_candidates(groundtruth100m_set, 1000)', number=10, globals=globals())
    0.0023570358753204346

It takes the same amount of time! No increase as the size of our groundtruth grows. This is because the check uses the hash of its value to quickly see if the item exists in the set (https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset)

The key of a dictionary is also a hash, and so your groundtruth in this example could also be a dictionary mapping {value: class} and the lookups would still be fast.

Note that the process of changing a list to a set may take some time, but the tradeoff is worth it to get fast lookups multiple times. Make sure that you only do it once! It will cause you to use more memory. Remember that a set is not ordered, and can only contain a value once. To save time and memory, consider generating the set initially instead of making a list and converting it.