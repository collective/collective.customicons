from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.customicons.interfaces import ICustomIconSettings
import logging


logger = logging.getLogger(__name__)


def get_icon_folder(context):
    portal = context.portal_url.getPortalObject()
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ICustomIconSettings)
    path = settings.imagepool_path
    if path is not None:
        # strip the slashes, if the user has entered the path incorrectly
        path = path.strip('/')
        try:
            full_path = portal.restrictedTraverse(path.encode('utf-8'))
            if full_path.contentIds() is not None:
                return full_path
        except:
            logger.warn('Error you have no images in the Folder, '
                        'or inserted a wrong lookup place')
    return None
