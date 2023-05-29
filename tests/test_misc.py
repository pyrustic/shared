import unittest
import os.path
import pathlib
from shared import misc


class TestEntryValidation(unittest.TestCase):
    def test_legal_entry(self):
        r = misc.validate_entry("my_entry.jesth")
        expected = True
        self.assertEqual(expected, r)

    def test_illegal_entry(self):
        r = misc.validate_entry("my entry.jesth")
        expected = False
        self.assertEqual(expected, r)


class TestPathComputation(unittest.TestCase):
    def test(self):
        directory = os.path.join("home", "alex")
        r = misc.compute_path(directory, "entry")
        expected = str(pathlib.Path(directory, "entry").resolve())
        self.assertEqual(expected, r)


if __name__ == '__main__':
    unittest.main()
