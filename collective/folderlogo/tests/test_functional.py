import unittest
import doctest
from Testing import ZopeTestCase as ztc
from collective.folderlogo.tests import base

class TestSetup(base.FolderLogoFunctionalTestCase):

    def afterSetUp( self ):
        """After SetUp"""

def test_suite():
    return unittest.TestSuite([

        # Functional tests for adapters.
        ztc.FunctionalDocFileSuite(
            'tests/functional/functional.txt', package='collective.folderlogo',
            test_class=TestSetup,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

            ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
