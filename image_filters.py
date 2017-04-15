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
    tint_factor = tint_strength / 100.
    return round((
        (1 - tint_factor) * original_component ** 2 +
        tint_factor * tint_component ** 2) ** 0.5)


def apply_brightness(im, brightness):
    """Apply brightness to image and returns it."""
    if brightness == 0:
        return im
    factor = 1. + brightness / 100.
    enh = ImageEnhance.Brightness(im)
    return enh.enhance(factor)


def apply_contrast(im, contrast):
    """Apply contrast to image and returns it."""
    if contrast == 0:
        return im
    factor = 1. + contrast / 100.
    enh = ImageEnhance.Contrast(im)
    return enh.enhance(factor)


def apply_sharpen(im, sharpen):
    """Apply sharpen to image and returns it.

    If sharpen is negative, the image will be blurred.
    """
    if sharpen == 0:
        return im
    factor = 1. + sharpen / 100.
    enh = ImageEnhance.Sharpness(im)
    return enh.enhance(factor)


def apply_tint(im, tint_color, tint_strength):
    """Apply tint color to image and returns it.

    tint_color is an RGB tuple.
    Quick Pixel Iteration: http://stackoverflow.com/a/2181473
    """
    if tint_color is None:
        return im
    source = im.split()
    reds = source[0].point(
        lambda original_component: blend_components(
            original_component, tint_color[0], tint_strength))
    greens = source[1].point(
        lambda original_component: blend_components(
            original_component, tint_color[1], tint_strength))
    blues = source[2].point(
        lambda original_component: blend_components(
            original_component, tint_color[2], tint_strength))
    return Image.merge(im.mode, (reds, greens, blues))


def apply_filters(input_file, **kwargs):
    """Process an image with given filters.

    Returns a BytesIO object representing the processed image as a JPG.
    """
    brightness = kwargs.get('brightness', 0)
    contrast = kwargs.get('contrast', 0)
    sharpen = kwargs.get('sharpen', 0)
    tint_color = parse_tint(kwargs.get('tint'))
    tint_strength = kwargs.get('tint_strength', 0)

    im = Image.open(input_file).convert('RGB')
    im = apply_brightness(im, brightness)
    im = apply_contrast(im, contrast)
    im = apply_sharpen(im, sharpen)
    im = apply_tint(im, tint_color, tint_strength)

    output_file = BytesIO()
    im.save(output_file, format='JPEG')
    output_file.seek(0)  # important!
    return output_file
