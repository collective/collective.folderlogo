from StringIO import StringIO
from zope.annotation.interfaces import IAnnotations
from zope.component import getSiteManager
from Products.CMFCore.utils import getToolByName

def uninstall(self):
    out = StringIO()
    print >> out, "Removing Folder Logo"

    annotations = IAnnotations(self)
    del annotations['collective.folderlogo.imageid']

    controlpanel = getToolByName(self, 'portal_controlpanel')
    actids= [o.id for o in controlpanel.listActions()]
    controlpanel.deleteActions([actids.index('folder_logo')])

    return out.getvalue()
