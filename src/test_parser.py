import unittest
from .parser import Parser


class TestParserInit(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Parser("- abc").content, ["abc"])
        self.assertEqual(Parser("[abc, sdf]").content, ["abc", "sdf"])
        self.assertEqual(Parser("cat: dog").content, {"cat": "dog"})
        self.assertEqual(
            Parser("cat: [dog,goose]").content, {"cat": ["dog", "goose"]})


if __name__ == "__main__":
    unittest.main()
