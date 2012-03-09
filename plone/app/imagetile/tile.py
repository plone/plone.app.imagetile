from plone.tiles import PersistentTile


class ImageTile(PersistentTile):
    """A tile which displays an image.

    This is a transient tile which stores a reference to an image and
    optionally alt text. When rendered, the tile will look-up the image
    url and output an <img /> tag.
    """
