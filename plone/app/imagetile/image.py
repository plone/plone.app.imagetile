from zope.interface import directlyProvides, implementsOnly, \
    implementer, Interface
from zope import schema
from zope.component import adapter
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory, IChoice
from zope.app.component.hooks import getSite
from plone.app.imagetile import PloneMessageFactory as _
from plone.app.mediarepository.source import MediaRepoSourceBinder
from plone.app.imaging.utils import getAllowedSizes
from plone.app.uuid.utils import uuidToCatalogBrain
from plone.directives import form as directivesform
from plone.tiles import PersistentTile

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from z3c.form.browser.select import SelectWidget
from z3c.form.interfaces import IFormLayer, IFieldWidget, ISelectWidget
from z3c.form.widget import FieldWidget


class IImagePreviewSelectWidget(ISelectWidget):
    """Marker interface for the image preview select widget."""
    pass


class ImagePreviewSelectWidget(SelectWidget):
    """A select widget for images that shows a preview of the selected
    image next to it.
    """

    implementsOnly(IImagePreviewSelectWidget)

    klass = u'image-preview-select-widget'

    def method(self):
        return self.request.get("%s.method" % self.name, "existing")

    def renderMediaRepository(self):
        site = getSite()
        view = site.restrictedTraverse("@@mediarepo-picker")
        return view.__of__(site)()

    def js(self):
        return  """\
        (function($) {
          $().ready(function() {

            // Clicking an image updates selected value
            $('ul.mediaRepository a').click(function(e) {
              e.preventDefault();
              $('#%(id)s').attr('value',$(this).attr('href'));
              //TODO: Set altText default too
              $(this).parent().siblings('.mediaRepositoryEntry').removeClass('selected');
              $(this).parent().addClass('selected');
            });

            // If there is an initial value, try and find a matching checkbox
            var input_value = $('#%(id)s').attr('value');
            if(input_value) {
              if(input_value.indexOf('"') != -1) { return; }
              $('ul.mediaRepository a[href="'+input_value+'"]').trigger('click');
              //TODO: Should put up a warning message if not found
            }

          })
        })(jQuery);
        """ % {'id': self.id}


@adapter(IChoice,
         Interface,
         IFormLayer)
@implementer(IFieldWidget)
def ImagePreviewSelectFieldWidget(field, source, request=None):
    """IFieldWidget factory for ImagePreviewSelectWidget."""
    # BBB: emulate our pre-2.0 signature (field, request)
    if request is None:
        real_request = source
    else:
        real_request = request
    fieldwidget = FieldWidget(field, ImagePreviewSelectWidget(real_request))
    return fieldwidget


def availablePloneAppImagingScalesVocabulary(context):
    terms = []
    terms.append(SimpleTerm('original', 'original', "original"))

    for scale, (width, height) in getAllowedSizes().iteritems():
        terms.append(SimpleTerm(scale, scale, \
                                "%s (%dx%d)" % (scale, width, height)))

    return SimpleVocabulary(terms)
directlyProvides(availablePloneAppImagingScalesVocabulary, IVocabularyFactory)


class IImageTile(directivesform.Schema):

    directivesform.widget(image_id=ImagePreviewSelectFieldWidget)
    image_id = schema.Choice(title=_(u"Select an Image"), required=True,
                            source=MediaRepoSourceBinder())

    alt_text = schema.TextLine(title=_(u"Alternative text"), required=False,
                            missing_value=u'')

    image_size = schema.Choice(title=_(u"Image Size"),
                            vocabulary=u"Available Images Scales",
                            required=True)


class ImageTile(PersistentTile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """
    display_template = ViewPageTemplateFile('image.pt')

    def __call__(self):
        image = uuidToCatalogBrain(self.data.get('image_id'))
        if image is None:
            return self.display_template()

        image_size = self.data.get('image_size', 'original')
        if image_size=='original':
            image_url = image.getURL()
        else:
            image_url = '%s/@@images/image/%s' % (image.getURL(), image_size)
        return self.display_template(image_url=image_url,
                                     alt_text=self.data.get('alt_text'))
