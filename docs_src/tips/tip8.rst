Python tip of the week 8, Generators
====================================

This tip is about the use of generators for optimizing your code. To understand generators, 
we will also quickly talk about iterators, iterables and iterations.

Iterables, iterators and iterations
-----------------------------------

An iterable is just an object that has a ``__iter__`` method which returns an iterable, or 
a ``__getitem__`` method that can take sequential indexes starting from zero.

An iterator is an object that implements ``__next__``, which is expected to return the next 
element of the iterable object that returned it, and raise a StopIteration exception when 
no more elements are available.

An iteration is the process of taking an item from something. When we use a loop to 
iterate over something it is called an iteration.

You can define your own custom iterables in python like this:

.. code-block:: python

    class MusicCollection:
        def __init__(self, tracks=[]):
            self.tracks = tracks
            # keep track of the current index of the iteration
            self.current = 0

        def __iter__(self):    # iterable
            return self

        def __next__(self):    # iterator
            if self.current < len(self.tracks):
                track = self.tracks[self.current]
                self.current += 1
                return track
            else:
                self.current = 0
                raise StopIteration()

    music_collection = MusicCollection(['track1.wav', 'track2.wav', 'track3.wav'])

    for track in music_collection:
        print(track)

Generators
----------
In the example above, we can iterate several times on the tracks of a music collection. The names of the tracks are just kept in memory (stored in a list). But what if we have a million tracks or feature vectors, but we still want to iterate through them and input them to our processing pipeline? That is where generators become interesting. generators are iterators, but you can iterate over them only once, because they do not store all the values in memory, they generate them on the fly. 


The way to declare a generator is quite different from the iterables. Basically you can create a function and use yield instead of the return statement. Let’s consider another example that might be more relevant for you. When we train artificial neural networks, we often have a lot of pre-computed features stored in a file that allows fast I/O processing, such as hdf5 files. Let’s see how we can create batches of shuffled training examples for each epoch, without requiring a huge amount of memory:

.. code-block:: python

    def load_batches(hdf5_file, batch_size):
        num_data, num_frames, num_bands = hdf5_file["train_X"].shape
        nb_batches = int(math.ceil(float(num_data) / batch_size))
        ids = list(range(num_data))
        shuffle(ids)
        for i, idx_batch in enumerate(range(nb_batches)):
                i_start = i * batch_size
            i_end = min([(i + 1) * batch_size, num_data])
                batch_indexes = ids[i_start:i_end]
                batch_indexes.sort()
                examples = hdf5_file["train_X"][batch_indexes]
                yield examples


Generator expressions
---------------------

Generator expressions are just a shortcut to declare generators. It might remind you
about a previous tip where we talked about list comprehensions...

The code:

.. code-block:: python

    def repeater(value, max_repeats):
        for i in range(max_repeats):
            yield value

    iterator = repeater('Hello', 3)

Is equivalent to:

.. code-block:: python

    iterator = ('Hello' for i in range(3))


Generator expression provide a very concise way for supporting iterator protocols and avoiding 
the verbosity of defining functions with the yield operator. The nice thing is that you can 
create processing chains in a very succinct way while keeping a good code readability.
Let’s see a simplified example of a natural language processing pipeline where we want to 
extract processable terms from a list of sentences:

.. code-block:: python

    import re

    stop_words = ['a', 'is', 'in', 'he', 'also']
    text = ['A dog is barking in a street.', 'He also growls!']

    lemmas = (lemma for phrase in text for lemma in re.findall('\w+', phrase))
    lower_case = (term.lower() for term in lemmas)
    terms = (term for term in lower_case if term not in stop_words)

    list(terms)
    -> ['dog', 'barking', 'street', 'growls']