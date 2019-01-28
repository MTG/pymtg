Python tip of the week 3, Python Lists
=======================================

One of the Python data structures is List.
In Python, a list:

    is ordered
    is mutable (elements inside can change)
    contains elements that can be accessed by index
    allows for duplicate elements
    can contain any arbitrary objects (integers, strings, lists, ...)
    can be nested (can contain lists with more lists inside)
    is dynamic (can grow as needed)


Processing elements in lists
-----------------------------

We often have to store elements in a list and apply some processing to the values.
Consider if we have a list of positive float values that we would like to scale between 0 and 1.
When you want to do such processing, it is always a good idea to check the time-complexity (aka "Big O") of list operations.
As getting and appending elements operations in lists are in O(1), we can expect to solve the problem in O(n) by iterating through all the elements, and create a new list with the processed elements.
You could do something like this:

.. code-block:: python

import random

    random_floats = [random.uniform(0,100) for _ in range(100)]

    def scale(values):
        max_value = max(values)
        scaled_values = []
        for value in values:
            scaled_values.append(value/max_value)
        return scaled_values

However, we can do better in terms of code readability.
List comprehensions provide a concise way to create lists.
We could even say that they are one of the most important tools in a*Pythonista*’s toolbox.
Moreover, using them will often lead to better performances.
This is how we can rewrite our function:

.. code-block:: python

    def scale(values):
        max_value = max(values)
        return [value/max_value for value in values]

Furthermore, for the ones that love functional style, Python offers some functions which facilitate a functional approach to programming.
Here is how we solve our problem with the *map()* and *lambda* functions:

.. code-block:: python

    def scale(values):
        max_value = max(values)
        return map(lambda x: x/max_value, values)

Be aware that this last approach will be different in Python 2 and Python 3.
In Python 2, map() returns a list, whereas in Python 3, it returns an *iterator* that applies the function given as first argument, to every items in *values*.


Filtering elements in lists
----------------------------

Let's now consider another example to be sure things are understood.
We have now a list of float numbers, and we would like to get only the values that are higher than a threshold value. With a list comprehension, here is a function that does the trick:

.. code-block:: python

    def filter_threshold(values, threshold):
        return [value for value in values if value > threshold]

And the functional approach:

.. code-block:: python

    def filter_threshold(values, threshold):
        return filter(lambda x: x > threshold, values)


Flatten a nested list
----------------------

List comprehensions can be very useful, but sometimes they can be hard to understand. If you practice, you will get better at it, and it will simplify your *Pythonic* life. Here is a more complicated example:

.. code-block:: python

    nested_list = [[1, 2, 3], [1, 2], [1], [5, 4]]
    flat_list = [item for sublist in nested_list for item in sublist]

Pay attention to the order in which the iteration variables are declared in the list comprehension, it is not very intuitive at first!


Combining multiple lists
-------------------------

Finally, another common thing is to have several lists that we would like to combine and then iterate through them.
Instead of doing two for loops, we could use the zip() function to do something like this:

.. code-block:: python

    for (value1, value2) in zip(list1, list2):
        print(value1, value2)

On the contrary, if you have a list of tuples, you can unzip them by doing:

.. code-block:: python

    zipped_list = [(1, 2), (3, 4), (5, 6)]
    unzipped_lists = list(zip(*zipped_list))  # -> [(1, 3, 5), (2, 4, 6)]

Be careful again, the output of *zip()* in an *iterator*. You will need to cast it as a list or iterate trough it. No need to understand much about *iterators*, we will leave that for another tip ;)

