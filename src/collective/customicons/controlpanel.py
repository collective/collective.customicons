from plone.app.registry.browser import controlpanel
from .interfaces import ICustomIconSettings, _


class CustomIconSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICustomIconSettings
    label = _(u"Customicons Settings")
    description = _(u"""""")

    def updateFields(self):
        super(CustomIconSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(CustomIconSettingsEditForm, self).updateWidgets()

class CustomIconSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CustomIconSettingsEditForm
