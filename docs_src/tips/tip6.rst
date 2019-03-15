Python tip of the week 6, String formatting
============================================

This week's tip is about ways to format strings in Python.

An 'intuitive' way for string formatting can be using '+' operator for concatenating strings. To use this formatting style, we have to cast the integers or other data types into strings manually. An example can be as following:

.. code-block:: python

	>>> num_of_items = 42
	>>> type_of_items = 'songs'
	>>> print('Here, we have ' + str(num_of_items) + ' ' + type_of_items)

	Output: Here, we have 42 songs

While using '+' operator seems easy to use, it comes with a bunch of problems (e.g. manual type casting, difficulty in reading code). Instead, you should consider using one of these recommended methods:

- Old Style: (https://docs.python.org/3/library/stdtypes.html#old-string-formatting) This way of string formatting uses format specifiers to indicate what to substitute. 
- New Style: (https://docs.python.org/3/library/stdtypes.html#str.format) This method is used with calling the ".format()" function.
- F-strings: (https://www.python.org/dev/peps/pep-0498/) The F-strings style is supported in Python 3.6+, and it is a simple yet powerful way for string formatting. Unlike in 'New Style', you don't have to call a specific function such as '.format()' or use format specifiers as in 'Old Style'.
- Template Strings: (https://docs.python.org/3/library/string.html#template-strings) This simpler and less powerful method of formatting strings can be useful in terms of privacy of variables. For this method, Template class for Python string module should be imported.


Below, you can find some examples of use:

Basic formatting
----------------

.. code-block:: python

	>>> num_of_items = 42
	>>> type_of_items = 'songs'

	# Old style
	>>> print('Here, we have %d %s' % (num_of_items, type_of_items))

	# New style
	>>> print('Here, we have {} {}'.format(num_of_items, type_of_items))

	# F-strings
	>>> print(f'Here, we have {num_of_items} {type_of_items}')

	Output: Here, we have 42 songs

Named placeholders
------------------

.. code-block:: python

	>>> params = {'hop_size': 512, 'frame_size': 1024}

	# Old style
	>>> print('The parameters for hop size is %(hop_size)d, and frame size is %(frame_size)s.' % params)

	# New style
	>>> print('The parameters for hop size is {hop_size}, and frame size is {frame_size}.'.format(**params))

	# F-strings
	>>> print(f'The parameters for hop size is {params["hop_size"]}, and frame size is {params["frame_size"]}.')

	Output: The parameters for hop size is 512, and frame size is 1024.

Number formatting
-----------------

.. code-block:: python

	>>> def get_duration():
	>>>     return 331.1932148

	# Old Style
	>>> print('Duration of this track is %.2f seconds.' % get_duration())

	# New Style
	>>> print('Duration of this track is {:.2f} seconds'.format(get_duration()))

	# F-strings
	>>> print(f'Duration of this track is {get_duration():.2f} seconds.')

	Output: Duration of this track is 331.19 seconds.

Padding and alignment
---------------------

.. code-block:: python

	>>> songs = ['Yesterday', 'All You Need Is Love', 'Hey Jude']
	>>> albums = ['Help!', 'Magical Mystery Tour', 'The Beatles']
	>>> song_ids = [483, 65448, 98]

	# Old Style
	>>> for i in range(3):
	>>>     print('%20s - %-20s - %6d ' % (songs[i], albums[i], song_ids[i]))

	# New Style
	>>> for i in range(3):
	>>>     print('{:>20} - {:<20} - {:>6}'.format(songs[i], albums[i], song_ids[i]))
	    
	# F-strings
	>>> for i in range(3):
	>>>    print(f'{songs[i]:>20} - {albums[i]:<20} - {song_ids[i]:>6}')

	Output:            Yesterday - Help!                -    483 
	        All You Need Is Love - Magical Mystery Tour -  65448 
	                    Hey Jude - The Beatles          -     98 

Example for Template strings
-----------------------------

In most of the cases, one of the methods shown above would be appropriated. However, these methods might introduce security vulnerabilities to your programs. For instance, a user of a web application could retrieve some variables with a designed input. Let's have a look at a simple example where an hypothetical attacker would be able to access some global variables:

.. code-block:: python

	# This is a variable we don't want to show
	>>> SECRET_VARIABLE = "don't tell anyone"

	>>> class Music:
	>>>     def __init__(self):
	>>>         pass
	    
	>>> song = Music()

	# New Style
	>>> user_provided_string = '{track.__init__.__globals__[SECRET_VARIABLE]}'
	>>> print(user_provided_string.format(track=song))

	Output: don't tell anyone

Here is where the Template strings method becomes useful:

.. code-block:: python

	>>> from string import Template

	>>> user_provided_string = '${track.__init__.__globals__[SECRET_VARIABLE]}'
	>>> print(Template(user_provided_string).substitute(track=song))

	Raises: ValueError: Invalid placeholder in string: line 1, col 1

Bonus tip: join function
------------------------
For joining all the items in a tuple or a list into a single string,  you might be tented to use a for loop and concatenate elements one by one. However, the '.join()' function provides a better way to do it:

.. code-block:: python

	>>> songs = ['Yesterday', 'Come Together', 'Hey Jude', 'Blackbird', '...']
	>>> message = 'Processing the songs: '
	>>> message += ', '.join(songs)
	>>> print(message)

	Output: Processing the songs: Yesterday, Come Together, Hey Jude, Blackbird, ...