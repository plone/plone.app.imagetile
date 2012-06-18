from zope.schema import URI
from zope.schema import Text
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
from plone.directives import form
from plone.tiles.tile import Tile


_ = MessageFactory('plone')


class IImageTile(form.Schema):

    url = URI(
        title=_('External Image URL'),
        required=False,
        )

    # -- or --

    uid = TextLine(
        title=_(u"Please select image from Image Repository"),
        required=False,
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


class ImageTile(Tile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """
