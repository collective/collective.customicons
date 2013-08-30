from plone.indexer.decorator import indexer
from .utils import get_relative_url_to_scale
from .dx.behavior import IDXCustomIcon
from .interfaces import ICustomIcon

@indexer(ICustomIcon)
def get_icon_index(ob, **kw):
    icon = get_relative_url_to_scale(ob)
    if icon is not None:
        return icon
    try:
        icon = ob.aq_inner.getIcon(True)
    except Exception:
        return ''
    if icon:
        return icon
    return ''

@indexer(ICustomIcon)
def get_tile_index(ob, **kw):
    icon = get_relative_url_to_scale(ob, scale='tile')
    if icon is None:
        raise AttributeError('Indexing')
    return icon

