from zope.annotation.interfaces import IAnnotations

def setupImageId(portal):
    annotations = IAnnotations(portal)
    if annotations.get('collective.folderlogo.imageid', None) is None:
        annotations['collective.folderlogo.imageid'] = 'logo'

def setupVarious(context):

    if context.readDataFile('collective.folderlogo_various.txt') is None:
        return

    portal = context.getSite()
    setupImageId(portal)
