import unittest2
from PIL import Image, ImageFile, ImageDraw
from pial.engines.pil_engine import Engine
from tests.utils import get_test_images_path

class SimpleTestCase(unittest2.TestCase):
    def setUp(self):
        self.engine = Engine()
        self.trololo_path = get_test_images_path(image_filename='trololo.jpg')

    def tearDown(self):
        del self.engine

    def test_create_thumb(self):
        im = Image.open(self.trololo_path)
        options = {
            'crop': 'center',
            'quality': 99,
            'colorspace': 'RGB',
            'upscale': False,
        }

        thumb_path = get_test_images_path(image_filename='trololo_100x100.jpg')
        result = self.engine.create(im, (100, 100), options)
        result.save(thumb_path)