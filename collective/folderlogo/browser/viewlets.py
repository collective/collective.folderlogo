from Acquisition import aq_chain, aq_inner, aq_parent
#from zope.annotation.interfaces import IAnnotations
from Products.ATContentTypes.interface.image import IATImage
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase, LogoViewlet
from collective.folderlogo.interfaces import IFolderLogoProperties


class PortalHeaderViewlet(ViewletBase):

    index = render = ViewPageTemplateFile('templates/portal_header.pt')

    def background(self):
        context = aq_inner(self.context)
        p_properties = getToolByName(context, 'portal_properties')
        if hasattr(p_properties, 'folder_logo_properties'):
            catalog = getToolByName(context, 'portal_catalog')
            folder_logo_properties = getattr(p_properties, 'folder_logo_properties')
            flp = IFolderLogoProperties(folder_logo_properties)
            color = flp.background_color
            image_id = flp.background_image_id

            folders = [folder for folder in aq_chain(context) if IFolderish.providedBy(folder)]
            images = []
            for folder in folders:
                path = '/'.join(folder.getPhysicalPath())
                brains = catalog(
                    path=dict(query=path, depth=1),
                    id = image_id,
                    object_provides = IATImage.__identifier__,
                )
                if len(brains) != 0:
                    images.append(brains[0])
            if len(images) != 0:
                image_path = images[0].getPath()
                style = "background: %s url(%s) no-repeat;" % (color, image_path)
            else:
                style = "background: %s no-repeat;" % (color)
            return style


class LogoViewlet(LogoViewlet):

    def update(self):
        super(LogoViewlet, self).update()
        context = aq_inner(self.context)
        p_properties = getToolByName(context, 'portal_properties')
        if hasattr(p_properties, 'folder_logo_properties'):
            portal = self.portal_state.portal()
            bprops = portal.restrictedTraverse('base_properties', None)
            title = None
            folder_logo_properties = getattr(p_properties, 'folder_logo_properties')
            logo_id = IFolderLogoProperties(folder_logo_properties).logo_id
            context = aq_inner(self.context)
            catalog = getToolByName(context, 'portal_catalog')
            folders = [folder for folder in aq_chain(context) if IFolderish.providedBy(folder)]
            logos = []
            for folder in folders:
                path = '/'.join(folder.getPhysicalPath())
                brains = catalog(
                    path=dict(query=path, depth=1),
                    id = logo_id,
                    object_provides = IATImage.__identifier__,
                )
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
            self.logo_tag = portal.restrictedTraverse(logoName).tag()

            self.portal_title = title or self.portal_state.portal_title()
