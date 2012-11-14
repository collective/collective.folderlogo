from Products.CMFCore.utils import getToolByName
from collective.folderlogo.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_upgrade_0_to_1(self):
        controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        controlpanel.addAction('folder_logo', 'Folder Logo', 'action')
        ids = [action.id for action in controlpanel.listActions()]
        self.assertIn('folder_logo', ids)

        properties = getToolByName(self.portal, 'portal_properties')
        properties.addPropertySheet('folder_logo_properties')
        flp = getattr(properties, 'folder_logo_properties')
        flp.manage_addProperty('logo_id', 'LOGO', 'string')
        flp.manage_addProperty('background_color', 'TRANSPARENT', 'string')
        flp.manage_addProperty('background_image_id', 'BACKGROUND', 'string')
        self.assertEqual(flp.getProperty('logo_id'), 'LOGO')
        self.assertEqual(flp.getProperty('background_color'), 'TRANSPARENT')
        self.assertEqual(flp.getProperty('background_image_id'), 'BACKGROUND')

        from collective.folderlogo.upgrades import upgrade_0_to_1
        upgrade_0_to_1(self.portal)

        ids = [action.id for action in controlpanel.listActions()]
        self.assertNotIn('folder_logo', ids)

        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        self.assertEqual(registry['collective.folderlogo.logo_id'], u'LOGO')
        self.assertEqual(registry['collective.folderlogo.background_color'], u'TRANSPARENT')
        self.assertEqual(registry['collective.folderlogo.background_image_id'], u'BACKGROUND')

        self.assertFalse(hasattr(properties, 'folder_logo_properties'))
