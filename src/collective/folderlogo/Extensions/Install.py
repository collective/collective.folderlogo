from Products.CMFCore.utils import getToolByName


def uninstall(self):

    setup = getToolByName(self, 'portal_setup')
    setup.runAllImportStepsFromProfile(
        'profile-collective.folderlogo:uninstall'
    )
    setup.setBaselineContext('profile-Products.CMFPlone:plone')
    return "Ran all uninstall steps."
