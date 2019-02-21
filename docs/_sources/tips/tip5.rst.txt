Python tip of the week 5, Sets
===============================

The last major datatype of python (after lists and dictionaries the last few weeks)

Sets are "unordered collections of unique elements" - https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset

We mentioned sets for speed of membership tests in tip #2, but they are also useful for quickly calculating mathematical set operations.

This is especially useful when you want to calculate the intersection or difference of two collections of items. You can quickly convert a list into a set to perform this operation:

.. code-block:: python

	>>> a = ['a', 'b', 'c', 1, 2, 3]
	>>> b = [1, 2, 3, 'x', 'y', 'z']
	>>> aset = set(a)
	>>> bset = set(b)
	>>> aset & bset  # intersection, or aset.intersection(bset)
	set([1, 2, 3])
	>>> aset - bset # difference, or aset.difference(bset)
	set(['a', 'c', 'b'])
	>>> bset - aset
	set(['y', 'x', 'z'])

Note that sets are unordered, you can't guarantee that converting a list to a set and back to a list again will result in the items remaining in the same order.

