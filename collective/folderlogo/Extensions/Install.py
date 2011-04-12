from StringIO import StringIO
from zope.annotation.interfaces import IAnnotations
from zope.component import getSiteManager
from Products.CMFCore.utils import getToolByName

def uninstall(self):
    out = StringIO()
    print >> out, "Removing Folder Logo"

    controlpanel = getToolByName(self, 'portal_controlpanel')
    actids= [o.id for o in controlpanel.listActions()]
    controlpanel.deleteActions([actids.index('folder_logo')])

    p_properties = getToolByName(self, 'portal_properties')
    if hasattr(p_properties, 'folder_logo_properties'):
        p_properties.manage_delObjects('folder_logo_properties')

    return out.getvalue()
