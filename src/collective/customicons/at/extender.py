from zope.interface import implementer
from archetypes.schemaextender.interfaces import (
    IOrderableSchemaExtender,
    IBrowserLayerAwareExtender,
)
from plone.indexer.decorator import indexer
from archetypes.schemaextender.field import ExtensionField
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from Products.Archetypes.utils import OrderedDict
from Products.Archetypes.interfaces import IVocabulary
from Products.validation import V_REQUIRED
from plone.app.blob.field import ImageField 
from collective.customicons.utils import get_icon_folder
from collective.customicons.interfaces import (
    ICustomIcon,
    ICustomIconLayer
)


class ImageExtensionField(ExtensionField, ImageField):
    """ImageField for use within schemaextender."""


class StringExtensionField(ExtensionField, atapi.StringField):
    """StringField for use within schemaextender."""


@implementer(IVocabulary)
class IconVocabulary(object):
    security = ClassSecurityInfo()
    security.declarePublic('getDisplayList')

    def getDisplayList(self, instance):
        iconfolder = get_icon_folder(instance)
        if iconfolder is None:
            return atapi.DisplayList()
        values = [(_, iconfolder[_].Title()) for _ in iconfolder.contentIds()]
        return atapi.DisplayList([('__empty__', '---')] + values)


@implementer(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
class IconExtender(object):
    """Schema extender for Icons.
    """

    fields = [
        ImageExtensionField('iconimage',
            schemata='settings',
            mode="w",
            write_permission="Manage portal",
            required=False,
            validators=(('isNonEmptyFile', V_REQUIRED),
                        ('checkNewsImageMaxSize', V_REQUIRED)),
            widget=atapi.ImageWidget(
                label=u"Icon Image",
                description=u"You can upload an icon image. This image will be"
                            u" used as the icon for the content.",
                show_content_type=False,
            ),
        ),
        StringExtensionField('iconpool',
            schemata='settings',
            mode="w",
            write_permission="Manage portal",
            default='__empty__',
            required=False,
            vocabulary=IconVocabulary(),
            widget=atapi.SelectionWidget(
                label=u"Icon Pool",
                description=u"You can select an icon from the pool. This image"
                            u" will be used as the icon for the content.",

            )
        ),
    ]

    layer = ICustomIconLayer

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        neworder = OrderedDict()
        for schemata in original.keys():
            neworder[schemata] = original[schemata]
        return neworder
