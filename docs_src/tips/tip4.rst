Python tip of the week 4, Dictionaries
=======================================

Dictionaries in python are cool. They provide a mapping from some key (which can be any hashable object) to some value (which can be any object)

https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries

https://docs.python.org/3.7/library/stdtypes.html#typesmapping

You can make a dictionary with the dict literal syntax:

.. code-block:: python

	>>> d = {'key': 'value', 'second': 1}
	>>> d
	{'key': 'value', 'second': 1}

And add to it by assigning to a new key:

.. code-block:: python

	>>> d['another'] = ['one', 'two']
	>>> d
	{'key': 'value', 'second': 1, 'another': ['one', 'two']}

You can also make one from a list of 2-tuples:

.. code-block:: python

	>>> items = [('key1', 1), ('key2', 2)]
	>>> dict(items)
	{'key1': 1, 'key2': 2}

Or with a dictionary comprehension:

.. code-block:: python

	>>> {k: 'a'*v for k, v in items}
	{'key1': 'a', 'key2': 'aa'}

You can combine two dictionaries with ``.update()``

.. code-block:: python

	>>> d = {'key': 'value', 'second': 1}
	>>> e = {'upf': 'cool', 'year': 2019}
	>>> d.update(e)
	>>> d
	{'key': 'value', 'second': 1, 'upf': 'cool', 'year': 2019}

You can see if a key exists in a dictionary by using the in keyword:

.. code-block:: python

	>>> 'upf' in d
	True
	>>> 'test' in d
	False

Note that this is fast (like a set in python)

Get a value from a dictionary by accessing it with ``[]``

.. code-block:: python

	>>> d['upf']
	'cool'

If the item doesn't exist, an exception will be raised. If you don't catch this exception your program will exit. Keep this in mind especially if you're reading data from an external file or webservice and you don't know if it will exist or not. You don't want the script to quit 80% through a 3 hour execution...

.. code-block:: python

	>>> d['not_here']
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'not_here'

You can check if the key exists first (if 'not here' in d), but you can also use ``.get()``. By default, this will return ``None`` if the key doesn't exist, but you can set it to something else if you want.

.. code-block:: python

	>>> print(d.get('not_here'))
	None

	>>> d.get('not_here', 'default_value')
	'default_value'

Delete an item from a dictionary by using ``del``

.. code-block:: python

	>>> del d['upf']
	>>> 'upf' in d
	False

You can get all of the keys of a dictionary with ``.keys()``, and the values with ``.values()``

.. code-block:: python

	>>> d.keys()
	dict_keys(['key', 'second', 'year'])

	>>> d.values()
	dict_values(['value', 1, 2019])

In python 3, ``.keys()`` and ``.values()`` return iterators. This means that you can use them in a for loop, but if you want to get the first or second element, for example, you need to cast it to a list:

.. code-block:: python

	>>> d.keys()[0]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'dict_keys' object does not support indexing

	>>> list(d.keys())[0]
	'key'

These values are also views into the dictionary, which means that if you change the dictionary, the view also changes:

.. code-block:: python

	>>> keys = d.keys()
	>>> keys
	dict_keys(['key', 'second', 'year'])
	>>> del d['year']
	>>> keys
	dict_keys(['key', 'second'])

Be careful when combining views and loops that modify a dictionary:

.. code-block:: python

	>>> for k in d.keys():
	...     if k == 'second':
	...         del d[k]
	...
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	RuntimeError: dictionary changed size during iteration

If you want to iterate through all of the keys and values in the dictionary at the same time, use ``.items()``:

.. code-block:: python

	>>> d = {'key': 'value', 'second': 1, 'upf': 'cool', 'year': 2019}
	>>> for k, v in d.items():
	...     print('> %s: %s' % (k, v))
	...
	> key: value
	> second: 1
	> upf: cool
	> year: 2019

In Python 2 and Python 3 up to 3.5, if you remove and add items from a dictionary then there is no guarantee that the dictionary is ordered. That is, the value of ``.keys()`` might not loop the same twice in a row, and might not be the same as the order which you added items to the dictionary.

You can use ``collections.OrderedDict`` to create a dictionary which is guaranteed to keep its keys and values in the same order that they were added.
From Python 3.7 this behaviour is part of the language definition and you don't have to use OrderedDict.

https://docs.python.org/3/library/collections.html#collections.OrderedDict

One common pattern that you might have to do with a dictionary is add a default value the first time that you encounter a key, and then modify it the next time that you see it. e.g.

.. code-block:: python

	>>> data = ['one', 'one', 'two', 'three', 'three', 'three']
	>>> d = {}
	>>> for item in data:
	...     if item not in d:
	...         d[item] = 1
	...     else:
	...         d[item] += 1
	...
	>>> d
	{'one': 2, 'two': 1, 'three': 3}

You can use collections.defaultdict to set a default value if the key doesn't exist. This means that you don't need to include a check for the key in each loop

https://docs.python.org/3/library/collections.html#collections.defaultdict

.. code-block:: python

	>>> import collections
	>>> d = collections.defaultdict(int)
	>>> for item in data:
	...     d[item] += 1
	...
	>>> d
	defaultdict(<class 'int'>, {'one': 2, 'two': 1, 'three': 3})

Common types to use with defaultdict could be int (for counters), list (for a dictionary of lists), or dict (for a nested dictionary)

If you simply want a counter, consider using ``collections.Counter``:

https://docs.python.org/3/library/collections.html#collections.Counter

.. code-block:: python

	>>> d = collections.Counter(data)
	>>> d
	Counter({'three': 3, 'one': 2, 'two': 1})
	>>> d.most_common()
	[('three', 3), ('one', 2), ('two', 1)]
	>>> d.most_common(1)
	[('three', 3)]

the ``.most_common()`` method will order items by their count, or you can choose to select only the top n most common items.

