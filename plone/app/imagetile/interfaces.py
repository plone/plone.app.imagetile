from zope.interface import Interface
from zope import schema
from plone.app.imagetile import PloneMessageFactory as _

class IImageSettings(Interface):
    """Settings for image tile."""

    images_repo_path = schema.TextLine(title=_(u"Images repository path"),
                                       description=_(u"The relative path to "
                                                      "the folder containing "
                                                      "the images available "
                                                      "to select in the image "
                                                      "tile, starting from "
                                                      "the root of the site."),
                                       default=_(u"images"))
