from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.customicons.interfaces import ICustomIconSettings


def get_icon_folder(context):
    #siteroot hohlen
    portal = context.portal_url.getPortalObject()
    #wert ausm zmi hohlen
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ICustomIconSettings)
    #pfad in path schreiben
    #import ipdb;ipdb.set_trace()
    path = settings.imagepool_path
    if path is not None:
        #strip the slashes, if the user has entered the path incorrectly
        path = path.strip('/')
        try:
            full_path = portal.unrestrictedTraverse(str(path))
            if full_path.contentIds() is not None:
                return full_path
        except: 
            """Error you have no images in the Folder, 
               or inserted a wrong lookup place"""
    return None

#schoenerer fehlerabfang zb wenn im folder koane images drin sin, schoen ansagen.
# und wenn at und dx dann is bei at di edit view weg???
