from rearrange import rearrange_name
import unittest
class rearrangetest(unittest.TestCase):
    def test_rearrange(self):
        tt="Lovelace, Ada"
        ex="Ada Lovelace"
        self.assertEqual(rearrange_name(tt),ex)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double(self):
        testing="Keerthi, vasan A."
        Expected="vasan A. Keerthi"
        self.assertEqual(rearrange_name(testing),Expected)
    def test_singel(Self):
        tia="Keerthi"
        expected="Keerthi"
        Self.assertEqual(rearrange_name(tia),expected)
    def test_sample(self):
        self.assertEqual("foo".upper(), "FOO")
        self.assertTrue("foo".islower())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            s.split(2)
unittest.main()