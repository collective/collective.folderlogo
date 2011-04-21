try:
    from Zope2.App import zcml
except ImportError:
    from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_collective_folderlogo():

    fiveconfigure.debug_mode = True

    import collective.folderlogo
    zcml.load_config('configure.zcml', collective.folderlogo)
    fiveconfigure.debug_mode = False

    ztc.installPackage('collective.folderlogo')

setup_collective_folderlogo()
ptc.setupPloneSite(products=['collective.folderlogo'])
class FolderLogoTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """

class FolderLogoFunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests
    """
