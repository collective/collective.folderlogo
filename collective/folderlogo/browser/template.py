from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope import interface, schema
#from z3c.form import form, field, button
#from plone.z3cform.layout import wrap_form, FormWrapper
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from collective.folderlogo import FolderLogoMessageFactory as _
try:
    from z3c.form import form, field, button
    from plone.z3cform.layout import wrap_form, FormWrapper

    class IFolderLogo(interface.Interface):
        logo_id = schema.TextLine(title=_(u"Logo ID"))

    class FolderLogoForm(form.Form):
        fields = field.Fields(IFolderLogo)
        ignoreContext = True # don't use context to get widget data
        label = _(u"Update Logo ID")

        @button.buttonAndHandler(_(u'Update'))
        def handleApply(self, action):
            data, errors = self.extractData()
            if data.has_key('logo_id'):
                portal = getToolByName(self.context, 'portal_url').getPortalObject()
                annotations = IAnnotations(portal)
                logo_id = str(data['logo_id'])
                if annotations['collective.folderlogo.imageid'] != logo_id:
                    annotations['collective.folderlogo.imageid'] = logo_id

        def update(self):
            ## Hide the editable-object border
            request = self.request
            request.set('disable_border', True)
            super(FolderLogoForm, self).update()

        def updateWidgets(self):
            super(FolderLogoForm, self).updateWidgets()
            portal = getToolByName(self.context, 'portal_url').getPortalObject()
            annotations = IAnnotations(portal)
            logo_id_widget = self.widgets.get('logo_id')
            logo_id_widget.value = annotations['collective.folderlogo.imageid']
            self.widgets.update()


    class FolderLogoView(FormWrapper):
        index = ViewPageTemplateFile('templates/folder_logo.pt')
        form = FolderLogoForm

except ImportError:
    class FolderLogoView(BrowserView):
        template = ViewPageTemplateFile('templates/folder_logo_for_plone3.pt')

        def __call__(self):
            self.request.set('disable_border', True)
            form = self.request.form
            if form.get("form.buttons.update", None) is not None:
                logo_id = form.get("form.widgets.logo_id")
                if logo_id != '':
                    portal = getToolByName(self.context, 'portal_url').getPortalObject()
                    annotations = IAnnotations(portal)
                    if annotations['collective.folderlogo.imageid'] != logo_id:
                        annotations['collective.folderlogo.imageid'] = logo_id
            return self.template()

        def label(self):
            return _(u"Update Logo ID")

        def logo_id(self):
            portal = getToolByName(self.context, 'portal_url').getPortalObject()
            annotations = IAnnotations(portal)
            return annotations['collective.folderlogo.imageid']

        def current_url(self):
            """Returns current url"""
            context_state = getMultiAdapter((self.context, self.request),
                                                name=u'plone_context_state')
            return context_state.current_page_url()
