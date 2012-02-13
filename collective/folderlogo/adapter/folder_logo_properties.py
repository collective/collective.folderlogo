from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.properties import ISimpleItemWithProperties
from collective.folderlogo.interfaces import IFolderLogoProperties
from zope.component import adapts
from zope.interface import implements


class FolderLogoProperties(object):

    adapts(ISimpleItemWithProperties)
    implements(IFolderLogoProperties)

    def __init__(self, context):
        self.context = context

    def __getattr__(self, attr):
        if attr == 'context':
            return self.context
        else:
            return self.context.getProperty(attr)

    def __setattr__(self, attr, value):
        if attr == 'context':
            self.__dict__[attr] = value
        else:
            self.context._updateProperty(attr, value)
