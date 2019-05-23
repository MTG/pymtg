Python tip of the week 7, Paths and Files
=========================================

You may wish to load files in your python code. Sometimes you might want to pass a directory for input or output as a program argument or function parameter. Image that you have an output directory and want to write some files to it. You may be tempted to do something like this:

.. code-block:: python

    >>> filename = output_dir + "data.json"

but this requires that ``output_dir`` ends in a ``/`` , otherwise you'll just write a file "resultsdata.json" instead of "results/data.json". You could ask people to ensure that it ends with a /, or check it yourself, but this can get messy.
Instead, use ``os.path.join``:

.. code-block:: python

    >>> filename = os.path.join(output_dir, "data.json")

This will automatically join arguments with a directory separator if needed (\\ in windows!), and can take any number of arguments, which it will join.

In python 3, you can also use the ``pathlib`` module which is pretty cool: https://docs.python.org/3/library/pathlib.html

.. code-block:: python

    >>> output_dir = pathlib.Path(dirname)
    >>> filename = output_dir / "data.json"

This overrides the division operator to allow you to join paths together. As long as one of the items is a Path object, you can perform this operation.

The os.path and os modules have many other useful methods:

 - https://docs.python.org/3/library/os.path.html
 - https://docs.python.org/3/library/os.html

Take a look at the documentation, but here are a few methods which I use often:

Splitting a filename into parts

.. code-block:: python

    # Takes care of multiple . in the filename, some extensions are longer than 3 characters
    >>> os.path.splitext("myfile.data.json")
    ('myfile.data', '.json')

    # Get the filename from a full path
    >>> os.path.basename("/path/to/myfile.json")
    myfile.json

    # Get the directory name from a full path
    >>> os.path.dirname("/path/to/myfile.json")
    /path/to

Making directories

.. code-block:: python

    # os.mkdir can only make one directory at a time. If you want to make a tree, use:
    >>> os.makedirs("all/of/my/directories")
    # This will raise an exception if the final directory already exists. In python 3 use
    >>> os.makedirs("all/of/my/directories", exists_ok=True)
    # or
    import errno, os
    try:
        os.makedirs("all/of/my/directories")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

Why shouldn't you use ``os.path.exists()`` instead of catching ``OSError``? Because it's theoretically possible that between the time that you check if a directory exists, and you make it, some other process could create this directory. It's better to check the exception instead.

Getting file lists from directories
-----------------------------------

Often you might want to scan a directory and get files in it:

Single directory:

.. code-block:: python

    >>> os.listdir("/my/directory")
    >>> glob.glob("/my/directory/*.txt")

Recursive:

.. code-block:: python

    >>> all_files = []
    >>> for root, dirs, files in os.walk("/my/directory"):
    ...     for f in files:
    ...         all_files.append(os.path.join(root, f)) if f.endswith(".txt")
    
    >>> glob.glob("/my/directory/*/*.txt", recursive=True)

Other file operations
---------------------

Also check out the shutil module for functions to copy and move files: https://docs.python.org/3/library/shutil.html