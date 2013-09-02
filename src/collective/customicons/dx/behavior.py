from zope import schema
from zope.interface import provider
from plone.supermodel import model
from plone.namedfile import field as namedfile
from plone.autoform.interfaces import IFormFieldProvider
from collective.customicons import _
from zope.interface import implementer
from plone.directives import form
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from collective.customicons.lookup import get_icon_folder
from collective.customicons.interfaces import ICustomIcon


@implementer(IVocabularyFactory)
class CustomIconVocabulary(object):

    def __call__(self, instance):
        iconfolder = get_icon_folder(instance)
        terms = []
        if iconfolder is None:
            return SimpleVocabulary(terms)
        for value, obj in iconfolder.items():
            terms.append(SimpleVocabulary.createTerm(value, str(value), obj.title))
        return SimpleVocabulary(terms)


@provider(IFormFieldProvider)
class IDXCustomIcon(model.Schema, ICustomIcon):
    """Dexterity behavior for custom icons
    """

    iconimage = namedfile.NamedBlobImage(
        title=_(u"Icon Image"),

        description=_(u"You can upload an icon image. This image will be"
                    u" used as the icon for the content."),

        required=False,
    )

    iconpool = schema.Choice(
        title=_(u"Icon Pool"),

        description=_(u"You can select an icon from the pool. This image"
                    u" will be used as the icon for the content."),

        vocabulary=u"customicons.vocabulary",

        required=False,

    )
    form.fieldset('settings', fields=['iconimage', 'iconpool'])
