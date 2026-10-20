import unittest
from PIL import Image
from studio.engine import enhance, PRESETS
class PresetTests(unittest.TestCase):
    def test_all_presets_dimensions(self):
        im=Image.new('RGB',(64,48),(50,90,130))
        for preset in PRESETS:
            self.assertEqual(enhance(im,.8,preset).size,im.size)
    def test_invalid_preset(self):
        with self.assertRaises(ValueError): enhance(Image.new('RGB',(32,32)),.6,'invalid')
    def test_zero_strength(self):
        im=Image.new('RGB',(32,32),(55,101,140))
        for preset in PRESETS:
            self.assertEqual(enhance(im,0,preset).tobytes(),im.tobytes())
if __name__=='__main__': unittest.main()
