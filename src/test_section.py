import unittest
from .section import Section


class TestSectionInit(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Section("- abc").content, ["abc"])
        self.assertEqual(Section("[abc, sdf]").content, ["abc", "sdf"])
        self.assertEqual(Section("cat: dog").content, {"cat": "dog"})
        self.assertEqual(
            Section("cat: [dog,goose]").content, {"cat": ["dog", "goose"]})


if __name__ == "__main__":
    unittest.main()
