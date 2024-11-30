import unittest
import shared


class TestRootImports(unittest.TestCase):

    def test_wrong_import(self):
        with self.assertRaises(AttributeError):
            shared.abracadabra

    def test(self):
        shared.Dossier
        shared.HOME
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()