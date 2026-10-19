import unittest
from PIL import Image
from studio.engine import enhance
class EngineTests(unittest.TestCase):
    def test_dimensions_unchanged(self):
        im=Image.new('RGB',(77,53),(70,110,160))
        result=enhance(im)
        self.assertEqual(result.size,im.size)
    def test_zero_strength_preserves_pixels(self):
        im=Image.new('RGB',(40,40),(70,110,160))
        self.assertEqual(list(enhance(im,0).getdata()),list(im.getdata()))
    def test_invalid_strength(self):
        with self.assertRaises(ValueError): enhance(Image.new('RGB',(4,4)),2)
if __name__=='__main__': unittest.main()
