# try:
#     from Zope2.App import zcml
# except ImportError:
#     from Products.Five import zcml
# from Products.Five import fiveconfigure
# from Testing import ZopeTestCase as ztc
# from Products.PloneTestCase import PloneTestCase as ptc
# from Products.PloneTestCase.layer import onsetup

# @onsetup
# def setup_collective_folderlogo():

#     fiveconfigure.debug_mode = True

#     import collective.folderlogo
#     zcml.load_config('configure.zcml', collective.folderlogo)
#     fiveconfigure.debug_mode = False

#     ztc.installPackage('collective.folderlogo')

# setup_collective_folderlogo()
# ptc.setupPloneSite(products=['collective.folderlogo'])
# class FolderLogoTestCase(ptc.PloneTestCase):
#     """We use this base class for all the tests in this package.
#     If necessary, we can put common utility or setup code in here.
#     """

# class FolderLogoFunctionalTestCase(ptc.FunctionalTestCase):
#     """Test case class used for functional (doc-)tests
#     """

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest2 as unittest


class CollectiveFolderlogoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        # Required by Products.CMFPlone:plone-content to setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')

        # Load ZCML
        import collective.folderlogo
        self.loadZCML(package=collective.folderlogo)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup

        # Installs all the Plone stuff. Workflows etc. to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install portal content. Including the Members folder! to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')

        self.applyProfile(portal, 'collective.folderlogo:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'collective.folderlogo')


FIXTURE = CollectiveFolderlogoLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="CollectiveFolderlogoLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="CollectiveFolderlogoLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
