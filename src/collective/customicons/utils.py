from Products.Archetypes.interfaces import IBaseObject as IATBaseObject
from .dx.behavior import IDXCustomIcon
from .lookup import get_icon_folder


def _get_imagepath(imgob, fieldname, scale):
    portal_path_length = len(imgob.portal_url.getPortalObject().getPhysicalPath())
    relativepath = list(imgob.getPhysicalPath()[portal_path_length:])
    if IATBaseObject.providedBy(imgob):
        relativepath += ['%s_%s' % (fieldname, scale)]
    else:
        relativepath += ['@@images/%s/%s' % (fieldname, scale)]
    return '/'.join(relativepath)


def _get_pool_image(ob, img_id):
    iconfolder = get_icon_folder(ob)
    if not img_id or iconfolder is None or img_id not in iconfolder.contentIds():
        return None, None
    return  iconfolder[img_id], 'image'


def get_relative_url_to_scale(ob, scale='icon'):
    if IATBaseObject.providedBy(ob):
        field = ob.Schema().get('iconimage', None)
        if field and field.get_size(ob) != 0:
            return _get_imagepath(ob, 'iconimage', scale)

        field = ob.Schema().get('iconpool', None)
        if not field:
            return None
        img_id = field.get(ob)
        pool_image, fieldname = _get_pool_image(ob, img_id)
        if pool_image:
            return _get_imagepath(pool_image, fieldname, scale)
        return None

    if IDXCustomIcon.providedBy(ob):
        if ob.iconimage:
            return _get_imagepath(ob, 'iconimage', scale)
        if ob.iconpool:
            pool_image, fieldname = _get_pool_image(ob, ob.iconpool)
            if pool_image:
                return _get_imagepath(pool_image, fieldname, scale)
        return None
