from io import BytesIO

from PKPIL import Image

from .helper import PKPillowLeakTestCase, skip_unless_feature

test_file = "Tests/images/hopper.webp"


@skip_unless_feature("webp")
class TestWebPLeaks(PKPillowLeakTestCase):
    mem_limit = 3 * 1024  # kb
    iterations = 100

    def test_leak_load(self):
        with open(test_file, "rb") as f:
            im_data = f.read()

        def core():
            with Image.open(BytesIO(im_data)) as im:
                im.load()

        self._test_leak(core)
