from zope.schema import Text
from zope.schema import TextLine
from zope.interface import invariant
from zope.interface import Invalid
from zope.i18nmessageid import MessageFactory
from plone.tiles.tile import PersistentTile
from plone.app.tiles.interfaces import ITileBaseSchema

from plone.namedfile.field import NamedImage

_ = MessageFactory('plone')


class IImageTile(ITileBaseSchema):

    picture = NamedImage(
        title=_('Select an image'),
        required=True,
        )

    # -- rest --

    title = TextLine(
        title=_('Image title.'),
        required=False,
        )

    description = Text(
        title=_('Image description.'),
        required=False,
        )


class ImageTile(PersistentTile):
    """A tile which displays an image.

    This is a persistent tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """
