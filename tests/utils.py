import os

def get_test_path():
    """
    Returns the path to the ``tests`` dir that this module resides in.

    :rtype: str
    :returns: The full path to the ``tests/`` dir.
    """
    return os.path.dirname(__file__)

def get_test_images_path(image_filename=None):
    """
    Returns the path to the ``tests/test_images`` dir. Optionally, you may
    also pass an image filename that resides under ``test_images``, getting
    a full path back to said image in return.

    :keyword str image_filename: Filename of a test image to
        return the full path to.
    :rtype: str
    :returns: The full path to the ``test_images`` dir, or the full path to
        the requested image (via ``image_filename``).
    """
    test_images_path = os.path.join(get_test_path(), 'test_images')

    if image_filename:
        return os.path.join(test_images_path, image_filename)
    else:
        return test_images_path