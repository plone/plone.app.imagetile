from zope.schema import TextLine
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from plone.tiles.tile import PersistentTile


_ = MessageFactory('plone')


class IImageTile(Interface):

    external_url = TextLine(title=_('External Image URL'))


class ImageTile(PersistentTile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """
