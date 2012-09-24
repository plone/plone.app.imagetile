from plone.formwidget.namedfile.widget import NamedImageWidget
from plone.app.imagetile.interfaces import IImageTileNamedImageWidget
from zope.component import adapter
from zope.interface import implementer, implements
from plone.namedfile.interfaces import INamedImageField
from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.widget import FieldWidget


class ImageTileNamedImageWidget(NamedImageWidget):

    implements(IImageTileNamedImageWidget)

    klass = u'named-image-widget allowDefault'

    @property
    def tileView(self):
        return self.form.context.restrictedTraverse('@@%s/%s' % (self.form.tileType.__name__, self.form.tileId))


@implementer(IFieldWidget)
@adapter(INamedImageField, IFormLayer)
def ImageTileNamedImageFieldWidget(field, request):
    return FieldWidget(field, ImageTileNamedImageWidget(request))
