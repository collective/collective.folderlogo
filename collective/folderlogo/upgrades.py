from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-collective.folderlogo:default'


def upgrade_0_to_1(context, logger=None):
    """Move configuration from properties to registry records."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    logger.info('Remove folder_logo configlet.')
    controlpanel = getToolByName(context, 'portal_controlpanel')
    actids= [o.id for o in controlpanel.listActions()]
    controlpanel.deleteActions([actids.index('folder_logo')])
    logger.info('Removed folder_logo configlet.')

    properties = getToolByName(context, 'portal_properties')
    if hasattr(properties, 'folder_logo_properties'):
        logger.info('Move properties to registry records.')
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        flp = getattr(properties,'folder_logo_properties')
        registry['collective.folderlogo.logo_id'] = unicode(flp.getProperty('logo_id', 'logo'))
        registry['collective.folderlogo.background_color'] = unicode(flp.getProperty('background_color', 'transparent'))
        registry['collective.folderlogo.background_image_id'] = unicode(flp.getProperty('background_image_id', 'background'))
        logger.info('Moved properties to registry records.')

    logger.info('Remove folder_logo_properties.')
    properties.manage_delObjects('folder_logo_properties')
    logger.info('Removed folder_logo_properties.')
