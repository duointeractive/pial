import unittest2
import PIL
from pial.engines.pil_engine import PILEngine
from tests.utils import get_test_images_path

class SimpleTestCase(unittest2.TestCase):
    def setUp(self):
        """
        Instantiates the PILEngine, loads up a basic source image in an
        instance of PIL.Image.
        """
        self.engine = PILEngine()
        self.trololo_path = get_test_images_path(image_filename='trololo.jpg')
        self.trololo_image = PIL.Image.open(self.trololo_path)

    def tearDown(self):
        """
        Explicitly clean up everything we made to prevent contamination.
        """
        del self.engine
        del self.trololo_path
        del self.trololo_image

    def test_get_image(self):
        """
        Tests the loading of a file-like object into an Engine's representation
        of an Image. In this case, ``PIL.Image``.
        """
        trolo_fobj = open(self.trololo_path, 'rb')
        self.assertIsInstance(self.engine.get_image(trolo_fobj),
                              PIL.JpegImagePlugin.JpegImageFile)

    def test_thumb_center_crop(self):
        """
        Tests the creation of a thumbnail with center cropping.
        """
        # Running this gives us a thumbnailed PIL.Image instance.
        thumb_img = self.engine.create_thumbnail(
            image=self.trololo_image,
            geometry=(100, 100),
            crop='center'
        )
        # Now let's save it somewhere.
        thumb_path = get_test_images_path(
            image_filename='trololo_ccrop_100x100.jpg')
        thumb_fobj = open(thumb_path, 'wb')
        # This does the actual saving. Transfers the data from the PIL.Image
        # instance in ``thumb_img`` to the ``thumb_fobj`` file-like object.
        self.engine.write(thumb_img, thumb_fobj, format='jpeg')

    def test_ccrop_image_with_weird_dimensions1(self):
        """
        Tests center-cropping on an image with weird dimensions.
        """
        cho_path = get_test_images_path(image_filename='cho.jpg')
        cho_image = PIL.Image.open(cho_path)

        thumb_img = self.engine.create_thumbnail(
            image=cho_image,
            geometry=(100, 100),
            crop='center center'
        )
        thumb_path = get_test_images_path(
            image_filename='cho_ccrop_100x100.jpg')
        thumb_fobj = open(thumb_path, 'wb')
        self.engine.write(thumb_img, thumb_fobj, format='jpeg')

    def test_ccrop_image_with_weird_dimensions2(self):
        """
        More weird image dimension center cropping tests.
        """
        hol_path = get_test_images_path(image_filename='hol.jpg')
        hol_image = PIL.Image.open(hol_path)

        thumb_img = self.engine.create_thumbnail(
            image=hol_image,
            geometry=(100, 100),
            crop='center center'
        )
        thumb_path = get_test_images_path(
            image_filename='hol_ccrop_100x100.jpg')
        thumb_fobj = open(thumb_path, 'wb')
        self.engine.write(thumb_img, thumb_fobj, format='jpeg')

    def test_thumb_no_center_crop(self):
        """
        Tests the creation of a thumbnail without center cropping.
        """
        thumb_img = self.engine.create_thumbnail(
            image=self.trololo_image,
            geometry=(100, 100),
        )
        thumb_path = get_test_images_path(
            image_filename='trololo_nocrop_100x100.jpg')
        thumb_fobj = open(thumb_path, 'wb')
        self.engine.write(thumb_img, thumb_fobj, format='jpeg')