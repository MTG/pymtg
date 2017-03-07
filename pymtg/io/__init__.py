import os
import errno
import json


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
