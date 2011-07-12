#coding=utf-8
from pial.helpers import toint
from pial.parsers import parse_crop

class EngineBase(object):
    """
    A base class whose public methods define the public-facing API for all
    EngineBase sub-classes. Do not use this class directly, but instantiate
    and use one of the sub-classes.

    If you're writing a new backend, implement all of the methods seen after
    the comment header 'Methods which engines need to implement'.

    .. note:: Do not instantiate and use this class directly, use one of the
        sub-classes.
    """
    def create_thumbnail(self, image, geometry,
                         upscale=True, crop=None, colorspace='RGB'):
        """
        Processing conductor, returns the thumbnail as an image engine instance

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :param tuple geometry: Geometry of the image in the format of (x,y).
        :keyword str crop: A cropping offset string. This is either one or two
            space-separated values. If only one value is specified, the cropping
            amount (pixels or percentage) for both X and Y dimensions is the
            amount given. If two values are specified, X and Y dimension cropping
            may be set independently. Some examples: '50% 50%', '50px 20px',
            '50%', '50px'.
        :keyword str colorspace: The colorspace to set/convert the image to.
            This is typically 'RGB' or 'GRAY'.
        """
        image = self.colorspace(image, colorspace)
        image = self.scale(image, geometry, upscale, crop)
        image = self.crop(image, geometry, crop)
        return image

    def colorspace(self, image, colorspace):
        """
        Sets the image's colorspace. This is typical 'RGB' or 'GRAY', but
        may be other things, depending on your choice of Engine.

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :param str colorspace: The colorspace to set/convert the image to.
            This is typically 'RGB' or 'GRAY'.
        :returns: The scaled image. The returned type depends on your
            choice of Engine.
        """
        return self._colorspace(image, colorspace)

    def scale(self, image, geometry, upscale, crop):
        """
        Wrapper for ``_scale``

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :param tuple geometry: Geometry of the image in the format of (x,y).
        :returns: The scaled image. The returned type depends on your
            choice of Engine.
        """
        x_image, y_image = map(float, self.get_image_size(image))
        # calculate scaling factor
        factors = (geometry[0] / x_image, geometry[1] / y_image)
        factor = max(factors) if crop else min(factors)
        if factor < 1 or upscale:
            width = toint(x_image * factor)
            height = toint(y_image * factor)
            image = self._scale(image, width, height)
        return image

    def crop(self, image, geometry, crop):
        """
        Crops the given ``image``, with dimensions specified in ``geometry``,
        according to the value(s) in ``crop``. Returns the cropped image.

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :param tuple geometry: Geometry of the image in the format of (x,y).
        :param str crop: A cropping offset string. This is either one or two
            space-separated values. If only one value is specified, the cropping
            amount (pixels or percentage) for both X and Y dimensions is the
            amount given. If two values are specified, X and Y dimension cropping
            may be set independently. Some examples: '50% 50%', '50px 20px',
            '50%', '50px'.
        :returns: The cropped image. The returned type depends on your
            choice of Engine.
        """
        if not crop:
            return image

        x_image, y_image = self.get_image_size(image)
        x_offset, y_offset = parse_crop(crop, (x_image, y_image), geometry)
        return self._crop(image, geometry[0], geometry[1], x_offset, y_offset)

    def write(self, image, dest_fobj, quality=95, format=None):
        """
        Wrapper for ``_write``

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :keyword int quality: A quality level as a percent. The lower, the
            higher the compression, the worse the artifacts.
        :keyword str format: The format to save to. If omitted, guess based
            on the extension. We recommend specifying this. Typical values
            are 'JPEG', 'GIF', 'PNG'. Other formats largely depend on your
            choice of Engine.
        """
        raw_data = self._get_raw_data(image, format, quality)
        dest_fobj.write(raw_data)

    def get_image_ratio(self, image):
        """
        Calculates the image ratio (X to Y).

        :param Image image: This is your engine's ``Image`` object. For
            PIL it's PIL.Image.
        :rtype: float
        :returns: The X to Y ratio of your image's dimensions.
        """
        x, y = self.get_image_size(image)
        return float(x) / y

    #
    # Methods which engines need to implement
    # The ``image`` argument refers to a backend image object
    #
    def get_image(self, source):
        """
        Returns the backend image objects from a ImageFile instance
        """
        raise NotImplemented()

    def get_image_size(self, image):
        """
        Returns the image width and height as a tuple
        """
        raise NotImplemented()

    def is_valid_image(self, raw_data):
        """
        Checks if the supplied raw data is valid image data
        """
        raise NotImplemented()

    def _colorspace(self, image, colorspace):
        """
        `Valid colorspaces
        <http://www.graphicsmagick.org/GraphicsMagick.html#details-colorspace>`_.
        Backends need to implement the following::

            RGB, GRAY
        """
        raise NotImplemented()

    def _scale(self, image, width, height):
        """
        Does the resizing of the image
        """
        raise NotImplemented()

    def _crop(self, image, width, height, x_offset, y_offset):
        """
        Crops the image
        """
        raise NotImplemented()

    def _get_raw_data(self, image, format_, quality):
        """
        Gets raw data given the image, format and quality. This method is
        called from :meth:`write`
        """
        raise NotImplemented()

