try:
    import unittest2 as unittest
except ImportError:
    import unittest

from doctest import (
    DocFileSuite,
    ELLIPSIS,
    NORMALIZE_WHITESPACE,
    REPORT_ONLY_FIRST_FAILURE,
)

from zope.component import testing

OF = REPORT_ONLY_FIRST_FAILURE | NORMALIZE_WHITESPACE | ELLIPSIS

def test_suite():
    return unittest.TestSuite([

        # Unit tests to test utilities.
        DocFileSuite(
            'tests/unittest/adapter.txt', package='collective.folderlogo',
            setUp=testing.setUp, tearDown=testing.tearDown,
            optionflags=OF),

    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
