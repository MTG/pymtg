import os
import errno
import json
import fnmatch


def json_dump(path, data, indent=4, verbose=False):
    """
    Save python dictionary ``data`` to JSON file at ``path``.
    Set ``verbose=True`` to print additional information on screen.
    """
    with open(path, 'w') as f:
        if verbose:
            print('Saving data to {0}'.format(path))
        json.dump(data, f, indent=indent)


def json_load(path, verbose=False):
    """
    Load python dictionary stored in JSON file at ``path``.
    Set ``verbose=True`` to print additional information on screen.
    """
    with open(path, 'r') as f:
        if verbose:
            print('Loading data from {0}'.format(path))
        return json.load(f)


def save_to_file(path, data, verbose=False):
    """
    Save arbitrary data to file at ``path``.
    Set ``verbose=True`` to print additional information on screen.
    """
    with open(path, 'w') as f:
        if verbose:
            print('Saving data to {0}'.format(path))
        f.write(data)


def mkdir_p(path):
    """
    TODO: document this function
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def get_filenames_in_dir(dir_name, keyword='*', skip_foldername='', match_case=True, verbose=False):
    """
    Inputs
    ``dir_name``          : the foldername
    ``keyword``           : the keyword to search (defaults to '*')
    ``skip_foldername``   : an optional foldername to skip searching
    ``match_case``        : flag for case matching
    ``verbose``           : verbose flag

    Outputs:
    ``fullnames``         : list of the fullpaths of the files found
    ``folder``            : list of the folders of the files
    ``names``             : list of the filenames without the foldername

    TODO: better document this function?
    TODO: does a python 3 version of this function exist
    """
    names = []
    folders = []
    fullnames = []

    if verbose:
        print dir_name

    # check if the folder exists
    if not os.path.isdir(dir_name):
        if verbose:
            print("Directory doesn't exist!")
        return [], [], []

    # if the dir_name finishes with the file separator,
    # remove it so os.walk works properly
    dir_name = dir_name[:-1] if dir_name[-1] == os.sep else dir_name

    # walk all the subdirectories
    for (path, dirs, files) in os.walk(dir_name):
        for f in files:
            hasKey = (fnmatch.fnmatch(f, keyword) if match_case else
                      fnmatch.fnmatch(f.lower(), keyword.lower()))
            if hasKey and skip_foldername not in path.split(os.sep)[1:]:
                try:
                    folders.append(unicode(path, 'utf-8'))
                except TypeError:  # already unicode
                    folders.append(path)
                try:
                    names.append(unicode(f, 'utf-8'))
                except TypeError:  # already unicode
                    names.append(path)
                fullnames.append(os.path.join(path, f))

    if verbose:
        print("> Found " + str(len(names)) + " files.")
    return fullnames, folders, names
