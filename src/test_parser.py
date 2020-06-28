import unittest
from .parser import Parser


class TestParserInit(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Parser.parse("- abc"), ["abc"])
        self.assertEqual(Parser.parse("[abc, sdf]"), ["abc", "sdf"])
        self.assertEqual(Parser.parse("cat: dog"), {"cat": "dog"})
        self.assertEqual(Parser.parse("cat: [dog,goose]"),
                         {"cat": ["dog", "goose"]})


if __name__ == "__main__":
    unittest.main()
