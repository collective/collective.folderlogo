from collective.folderlogo.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_folderlogo_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.folderlogo'))

    ## controlpanel.xml
    def test_controlpanel(self):
        controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        ids = [action.id for action in controlpanel.listActions()]
        self.failUnless('folder_logo' in ids)

    ## propertiestool.xm
    def test_propertiestool(self):
        properties = getToolByName(self.portal, 'portal_properties')
        lfp = getattr(properties, 'folder_logo_properties')
        self.assertEqual('Folder Logo Properties', lfp.getProperty('title'))
        self.assertEqual('logo', lfp.getProperty('logo_id'))
        self.assertEqual('transparent', lfp.getProperty('background_color'))
        self.assertEqual('background', lfp.getProperty('background_image_id'))

    ## browserlayer.xml
    def test_browserlayer(self):
        from collective.folderlogo.interfaces import IFolderLogoLayer
        from plone.browserlayer import utils
        self.failUnless(IFolderLogoLayer in utils.registered_layers())

    ## Uninstalling
    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.failIf(installer.isProductInstalled('collective.folderlogo'))
        properties = getToolByName(self.portal, 'portal_properties')
        self.failIf(hasattr(properties, 'folder_logo_properties'))
        controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        ids = [action.id for action in controlpanel.listActions()]
        self.failUnless('folder_logo' not in ids)
