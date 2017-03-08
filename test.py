import doctest
import unittest
import pkgutil
import pymtg

# Create a unit test suite and add all pymtg modules' doctests
suite = unittest.TestSuite()
for _, modname, _ in pkgutil.iter_modules(pymtg.__path__, prefix='pymtg.'):
    suite.addTest(doctest.DocTestSuite(modname))
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
