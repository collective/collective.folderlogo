from Acquisition import aq_chain
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interface.image import IATImage
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class PortalHeaderViewlet(ViewletBase):

    index = ViewPageTemplateFile('templates/portal_header.pt')

    def background(self):
        context = aq_inner(self.context)
        registry = getUtility(IRegistry)
        color = registry.get('collective.folderlogo.background_color', u'transparent')
        image_id = registry.get('collective.folderlogo.background_image_id', u'background')
        catalog = getToolByName(context, 'portal_catalog')
        folders = [folder for folder in aq_chain(context) if IFolderish.providedBy(folder)]
        images = []
        for folder in folders:
            path = '/'.join(folder.getPhysicalPath())
            brains = catalog(
                path=dict(query=path, depth=1),
                id=image_id,
                object_provides=IATImage.__identifier__)
            if len(brains) != 0:
                images.append(brains[0])
        if len(images) != 0:
            image_path = images[0].getPath()
            style = "background: {} url({}) no-repeat;".format(color, image_path)
        else:
            style = "background: {} no-repeat;".format(color)
        return style


class LogoViewlet(LogoViewlet):

    def update(self):
        super(LogoViewlet, self).update()
        context = aq_inner(self.context)
        registry = getUtility(IRegistry)
        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse('base_properties', None)
        title = None
        logo_id = registry.get('collective.folderlogo.logo_id', u'logo')
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        folders = [folder for folder in aq_chain(context) if IFolderish.providedBy(folder)]
        logos = []
        for folder in folders:
            path = '/'.join(folder.getPhysicalPath())
            brains = catalog(
                path=dict(query=path, depth=1),
                id=logo_id,
                object_provides=IATImage.__identifier__)
            if len(brains) != 0:
                logos.append(brains[0])
        if len(logos) != 0:
            logoName = logo_id
            title = logos[0].Title
            portal = aq_parent(logos[0].getObject())
        elif bprops is not None:
            logoName = bprops.logoName
        else:
            logoName = 'logo.jpg'
        self.logo_tag = portal.restrictedTraverse(str(logoName)).tag()

        self.portal_title = title or self.portal_state.portal_title()
