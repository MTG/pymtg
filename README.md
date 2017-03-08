# pymtg
Python research utils that some of us use at the MTG and eventually everyone will use :)

You can install this package using `pip` using the following line:
```
pip install git+https://github.com/MTG/pymtg
```

## Documentation

Docs are hosted using Github Pages and can be found here [https://mtg.github.io/pymtg/](https://mtg.github.io/pymtg/).

Docs are built using [Sphinx](http://www.sphinx-doc.org/en/stable/).
Use the following commands:
```
pip install sphinx sphinx_bootstrap_theme sphinxcontrib-napoleon
make html
```

To update the documentation hosted in [https://mtg.github.io/pymtg/](https://mtg.github.io/pymtg/), docs need to be rebuild locally and newly generated files (under `docs/`) pushed to the `master` branch.

Documentation is mainly built by reading docstrings. To have better
consistency we recommend to follow the [Google Style Python Docstrings]
(http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html),
which read well on console and also render well using Sphinx.
