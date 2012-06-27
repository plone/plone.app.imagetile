from zope.schema import URI
from zope.schema import Text
from zope.schema import TextLine
from zope.interface import invariant
from zope.interface import Invalid
from zope.i18nmessageid import MessageFactory
from plone.directives import form
from plone.tiles.tile import Tile
from Products.CMFCore.utils import getToolByName


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

    @invariant
    def url_or_uid(data):
        if getattr(data, 'url', None) and getattr(data, 'uid', None):
            raise Invalid(_('Url and Uid field can not be filled ' + \
                            'at the same time.'))

        elif not getattr(data, 'url', None) and not getattr(data, 'uid', None):
            raise Invalid(_('No image specified.'))

        return True


class ImageTile(Tile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """

    @property
    def image_src(self):
        if self.data.get('uid', None):
            catalog = getToolByName(self.context, 'portal_catalog')
            result = catalog(UID=self.data['uid'])
            if len(result) == 1:
                return result[0].getURL()
            return False

        if self.data.get('url', None):
            return self.data['url']

        return False
