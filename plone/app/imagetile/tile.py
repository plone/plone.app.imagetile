from zope.schema import Text
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
from plone.autoform import directives as form
from plone.tiles.tile import PersistentTile
from plone.app.tiles.interfaces import ITileBaseSchema

from plone.namedfile.field import NamedImage

_ = MessageFactory('plone')


class IImageTile(ITileBaseSchema):

    form.widget(picture='plone.app.imagetile.widget.ImageTileNamedImageFieldWidget')
    picture = NamedImage(
        title=_('Select an image'),
        required=True,
        )

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
