"""Functions to process an image."""

from cStringIO import StringIO
from PIL import Image


def apply_filters(input_file):
    """Process an image with given filters.

    Returns a StringIO object representing the processed image as a JPG.
    """
    im = Image.open(input_file)
    output_file = StringIO()
    im.save(output_file, format='JPEG')
    output_file.seek(0)  # important!
    return output_file
