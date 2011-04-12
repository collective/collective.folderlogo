import unittest
import doctest
from doctest import DocFileSuite
from zope.component import testing
from Products.PloneTestCase.version import PLONE40

def test_suite():
    if PLONE40:
        return unittest.TestSuite([

            # Unit tests to test utilities.
            DocFileSuite(
                'tests/unittest/unittest.txt', package='collective.folderlogo',
                setUp=testing.setUp, tearDown=testing.tearDown,
                optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

                ])

    else:
        return unittest.TestSuite([
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
