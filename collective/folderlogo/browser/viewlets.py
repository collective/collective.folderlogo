from Acquisition import aq_chain, aq_inner, aq_parent
from zope.annotation.interfaces import IAnnotations
#from Products.ATContentTypes.interfaces.image import IATImage
from Products.ATContentTypes.interface.image import IATImage
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import LogoViewlet

class LogoViewlet(LogoViewlet):

    def update(self):
        super(LogoViewlet, self).update()
        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse('base_properties', None)
        logo_id = IAnnotations(portal).get('collective.folderlogo.imageid')
        title = None
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
