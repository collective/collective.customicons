from zope.interface import Interface, Attribute
from z3c.form import interfaces
from zope import schema
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.customicons')


class ICustomIcon(Interface):
    """
    Marker for icon extensible classes.
    """


class ICustomIconLayer(Interface):
    """
    Browser Layer
    """


class ICustomIconSettings(Interface):
    """Global custom icons settings. This describes where the custom icons -
       imagepool will be stored.
    """

    imagepool_path = schema.TextLine(
        title=_(u"Path to Image-pool"),
        description=_(u"Set the Custom Icons image-pool",
        default=u"Enter the path to your Imagepool-folder. "
                 "For example, when you created a folder "
                 "at the plone-siteroot, "
                 "it would be: imagepool "
                 "You can exclude the folder from the navigation, so it won't "
                 "disturb your project."),
        required=False,
        default=u'',)
