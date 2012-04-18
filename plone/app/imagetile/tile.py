from zope.schema import URI
from zope.schema import Text
from zope.schema import TextLine
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from zope.publisher.browser import BrowserView
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces import NotFound
from plone.directives import form
from plone.namedfile.field import NamedImage
from plone.namedfile.utils import set_headers, stream_data
from plone.app.tiles.browser.traversal import TileTraverser
from plone.tiles.tile import PersistentTile


_ = MessageFactory('plone')


class IImageTile(form.Schema):

    external_url = URI(
        title=_('External Image URL'),
        required=False,
        )

    # -- or --

    file = NamedImage (
        title=_(u"Please upload an image"),
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


class ImageTile(PersistentTile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """

    @property
    def image_url(self):
        if self.data['external_url']:
            return self.data['external_url']
        elif self.data['file']:
            return '%s/@@downloadimage-tile/%s/%s' % (
                self.context.absolute_url(),
                self.__name__,
                self.id
                )
        else:
            return None


class IDownloadImageTileView(IBrowserView):
    """ """


class DownloadImageTile(TileTraverser):

    targetInterface = IDownloadImageTileView


class DownloadImageTileView(BrowserView):

    def __init__(self, context, request, tileType):
        super(DownloadImageTileView, self).__init__(context, request)
        self.tileType = tileType

    def __call__(self):
        tile = self.context.restrictedTraverse(
                '@@%s/%s' % (self.tileType.__name__, self.tileId,))

        file = tile.data['file']
        if file == None:
            raise NotFound(self.context, '', self.request)

        # Try determine blob name and default to "context_id_download"
        # This is only visible if the user tried to save the file to local computer
        filename = getattr(file, 'filename', '%s_%s_%s_download' % (
                self.context.id, self.tileType.__name__, self.tileId))

        set_headers(file, self.request.response)

        # Set headers for Flash 10
        # http://www.littled.net/new/2008/10/17/plone-and-flash-player-10/
        cd = 'inline; filename=%s' % filename
        self.request.response.setHeader("Content-Disposition", cd)

        return stream_data(file)
