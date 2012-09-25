from plone.formwidget.namedfile.widget import NamedImageWidget
from plone.app.imagetile.interfaces import IImageWidget
from zope.component import adapter
from zope.interface import implementer, implements
from plone.namedfile.interfaces import INamedImageField
from plone.app.tiles.interfaces import ITilesFormLayer
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget


class ImageWidget(NamedImageWidget):

    implements(IImageWidget)

    klass = u'named-image-widget allowDefault'

    @property
    def tileView(self):
        return self.form.context.restrictedTraverse('@@%s/%s' % (self.form.tileType.__name__, self.form.tileId))


@implementer(IFieldWidget)
@adapter(INamedImageField, ITilesFormLayer)
def ImageFieldWidget(field, request):
    return FieldWidget(field, ImageWidget(request))
