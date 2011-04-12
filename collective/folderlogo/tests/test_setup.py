import unittest
from zope.annotation.interfaces import IAnnotations
from Products.CMFCore.utils import getToolByName
from collective.folderlogo.tests.base import FolderLogoTestCase

class TestSetup(FolderLogoTestCase):

    def afterSetUp(self):
        self.catalog = getToolByName(self.portal, 'portal_catalog')
        self.controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        self.portal_annotations = IAnnotations(self.portal)
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.properties = getToolByName(self.portal, 'portal_properties')
        self.lfp = getattr(self.properties, 'folder_logo_properties')

    def test_is_folderlogo_installed(self):
        self.failUnless(self.installer.isProductInstalled('collective.folderlogo'))

#    ## Annotations
#    def test_portal_annotations(self):
#        self.failUnless('collective.folderlogo.imageid' in self.portal_annotations.keys())

    ## controlpanel.xml
    def test_controlpanel(self):
        ids = [action.id for action in self.controlpanel.listActions()]
        self.failUnless('folder_logo' in ids)

    ## propertiestool.xm
    def test_propertiestool(self):
        self.assertEqual('Folder Logo Properties', self.lfp.getProperty('title'))
        self.assertEqual('logo', self.lfp.getProperty('logo_id'))
        self.assertEqual('transparent', self.lfp.getProperty('background_color'))
        self.assertEqual('background', self.lfp.getProperty('background_image_id'))

    ## Uninstalling
    def test_uninstall(self):
        self.installer.uninstallProducts(['collective.folderlogo'])
        self.failIf(self.installer.isProductInstalled('collective.folderlogo'))
        self.failIf(hasattr(self.properties, 'folder_logo_properties'))
#        self.failUnless('collective.folderlogo.imageid' not in self.portal_annotations.keys())
        ids = [action.id for action in self.controlpanel.listActions()]
        self.failUnless('folder_logo' not in ids)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
