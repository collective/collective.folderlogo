from zope.i18nmessageid import MessageFactory

PROJECTNAME = 'collective.folderlogo'
FolderLogoMessageFactory = MessageFactory(PROJECTNAME)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
