import unittest
import doctest
import function

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(function))
    return tests

	
