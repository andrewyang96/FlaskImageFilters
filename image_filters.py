"""Functions to process an image."""

from io import BytesIO  # python 3 specific
from PIL import Image
from PIL import ImageEnhance


def parse_tint(tint):
    """Parse tint string, returns tuple."""
    if len(tint) == 0:
        return None
    return tuple(int(n) for n in tint.split(','))


def blend_components(original_component, tint_component, tint_strength):
    """Blend the two color components with the given tint strength.

    original_color and tint_color are integers in [0, 255].
    Formula: http://stackoverflow.com/a/29321264
    """
    return 0  # TODO: implement formula


def apply_brightness(im, brightness):
    """Apply brightness to image and returns it."""
    return im  # TODO: implement brightness filter


def apply_contrast(im, contrast):
    """Apply contrast to image and returns it."""
    return im  # TODO: implement contrast filter


def apply_sharpen(im, sharpen):
    """Apply sharpen to image and returns it.

    If sharpen is negative, the image will be blurred.
    """
    return im  # TODO: implement sharpen filter


def apply_tint(im, tint_color, tint_strength):
    """Apply tint color to image and returns it.

    tint_color is an RGB tuple.
    Quick Pixel Iteration: http://stackoverflow.com/a/2181473
    """
    return im  # TODO: implement tint color filter
    # HINT: Check out these methods below
    # Image.split: https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.split
    # Image.point: https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.point
    # PIL.Image.merge: https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.merge


def apply_filters(input_file, **kwargs):
    """Process an image with given filters.

    Returns a BytesIO object representing the processed image as a JPG.
    """
    return input_file  # TODO: implement
