from Products.CMFCore.utils import getToolByName
from collective.folderlogo.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed_folderlogo(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.folderlogo'))

    def test_browserlayer(self):
        from collective.folderlogo.interfaces import IFolderLogoLayer
        from plone.browserlayer import utils
        self.assertIn(IFolderLogoLayer, utils.registered_layers())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-collective.folderlogo:default'),
            u'1')

    def get_record(self, name):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        return registry.records.get(name)

    def test_registry_record__logo_id__field__instance(self):
        record = self.get_record('collective.folderlogo.logo_id')
        from plone.registry.field import TextLine
        self.assertIsInstance(record.field, TextLine)

    def test_registry_record__logo_id__field__title(self):
        record = self.get_record('collective.folderlogo.logo_id')
        self.assertEqual(record.field.title, u'Logo ID')

    def test_registry_record__logo_id__field__description(self):
        record = self.get_record('collective.folderlogo.logo_id')
        self.assertIsNone(record.field.description)

    def test_registry_record__logo_id__value(self):
        record = self.get_record('collective.folderlogo.logo_id')
        self.assertEqual(record.value, u'logo')

    def test_registry_record__background_color__field__instance(self):
        record = self.get_record('collective.folderlogo.background_color')
        from plone.registry.field import TextLine
        self.assertIsInstance(record.field, TextLine)

    def test_registry_record__background_color__field__title(self):
        record = self.get_record('collective.folderlogo.background_color')
        self.assertEqual(record.field.title, u'Background Color')

    def test_registry_record__background_color__field__description(self):
        record = self.get_record('collective.folderlogo.background_color')
        self.assertIsNone(record.field.description)

    def test_registry_record__background_color__value(self):
        record = self.get_record('collective.folderlogo.background_color')
        self.assertEqual(record.value, u'transparent')

    def test_registry_record__background_image_id__field__instance(self):
        record = self.get_record('collective.folderlogo.background_image_id')
        from plone.registry.field import TextLine
        self.assertIsInstance(record.field, TextLine)

    def test_registry_record__background_image_id__field__title(self):
        record = self.get_record('collective.folderlogo.background_image_id')
        self.assertEqual(record.field.title, u'Background Image ID')

    def test_registry_record__background_image_id__field__description(self):
        record = self.get_record('collective.folderlogo.background_image_id')
        self.assertIsNone(record.field.description)

    def test_registry_record__background_image_id__value(self):
        record = self.get_record('collective.folderlogo.background_image_id')
        self.assertEqual(record.value, u'background')

    def test_uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.assertFalse(installer.isProductInstalled('collective.folderlogo'))

    def test_uninstall_browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        from collective.folderlogo.interfaces import IFolderLogoLayer
        from plone.browserlayer import utils
        self.assertNotIn(IFolderLogoLayer, utils.registered_layers())

    def test_uninstall__registry_record__logo_id(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.assertIsNone(self.get_record('collective.folderlogo.logo_id'))

    def test_uninstall__registry_record__background_color(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.assertIsNone(self.get_record('collective.folderlogo.background_color'))

    def test_uninstall__registry_record__background_image_id(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.assertIsNone(self.get_record('collective.folderlogo.background_image_id'))
