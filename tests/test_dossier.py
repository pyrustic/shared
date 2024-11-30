import os.path
import unittest
import tempfile
import paradict
from shared import Dossier


DATA = r"""
# strings
string = "Hello "World" ! \\ \n \\n \\u000A ˫"
raw_string = 'Hello 'World' ! \n \\n \u000A ˫'
empty_string = ""
empty_raw_string = ''

# scalars
int = -4_200_000
hex_int = 0xAE1F
oct_int = 0o3427
bin_int = 0b101_0011_1010_1010
float = 3.141
decimal_float = 3.141_592_653_589_793_238_46E-10
complex = -4.2+6.9i
bool_1 = true
bool_2 = false

# null value
empty_value = null

# date and time (ISO 8601)
datetime = 2020-10-20T15:35:57Z
date = 2020-10-20
time = 15:35:57

# text
text = (text)
    Stand a little less \\n
    between me and the sun. ˫
    ---
empty_text = (text)
    ---

# raw text
raw = (raw)
    The foundation of every state
    is the education of its youth. ˫
    \u000A - WYSIWYG - C:\home\alex
    ---
empty_raw = (raw)
    ---

# bin data (standard base64 - RFC 4648)
bin = (bin)
    68 65 6C 6C 6F 20 77 6F 72 6C 64 20 68 65 6C 6C
    6F 20 77 6F 72 6C 64 20 68 65 6C 6C 6F 20 77 6F
    72 6C 64 20 68 65 6C 6C 6F 20 77 6F 72 6C 64 20
    68 65 6C 6C 6F 20 77 6F 72 6C 64 20 68 65 6C 6C
    6F 20 77 6F 72 6C 64 20 68 65 6C 6C 6F 20 77 6F
    72 6C 64
empty_bin = (bin)

# list collection
list = (list)
    "Item 1"
    "Item 2"
    "Item 3"
    # nested list
    (list)
        "item i"
        "item ii"
        "item iii"
empty_list = (list)

# dict collection
dict = (dict)
    key_1 = "value"
    key_2 = (list)
        "item i"
        "item ii"
        # nested dict
        (dict)
            project = "Jesth: Just Extract Sections Then Hack !"
            description = "Next level human-readable data serialization format"
            repository = 'https://github.com/pyrustic/jesth'
            author = "alex rustic"
empty_dict = (dict)
"""


class TestDossier(unittest.TestCase):

    def setUp(self):
        self._tempdir = tempfile.TemporaryDirectory()
        self._dossier = Dossier(self._tempdir.name)

    def tearDown(self):
        # the Try/Except is needed here because I can only
        # benefit from the constructor's "ignore_cleanup_errors=True"
        # in Python 3.10
        try:
            self._tempdir.cleanup()
        except Exception as e:
            pass

    def test_keys(self):
        r = self._dossier.keys()
        expected = tuple()
        self.assertEqual(expected, r)
        self._dossier.set("key1", {"id": 42, "name": "alex"})
        self._dossier.set("key2", {"id": 42, "name": "alex"})
        r = self._dossier.keys()
        expected = ("key1", "key2")
        self.assertEqual(expected, r)

    def test_exists_method(self):
        self.assertTrue(self._dossier.exists())
        self.assertFalse(self._dossier.exists("nonexistent-key"))
        self._dossier.set("key1", {"id": 42, "name": "alex"})
        self.assertTrue(self._dossier.exists("key1"))

    def test_locate_method(self):
        r = self._dossier.locate("nonexistent-key")
        self.assertIsNone(r)
        self._dossier.set("key1", {"id": 42, "name": "alex"})
        r = self._dossier.locate("key1")
        self.assertTrue(os.path.isfile(r))
        self.assertTrue(os.path.isabs(r))

    def test_get_set_methods(self):
        my_dict = paradict.decode(DATA)
        self._dossier.set("my-key", my_dict)
        r = self._dossier.get("my-key")
        expected = my_dict
        self.assertEqual(expected, r)

    def test_delete_method(self):
        self.assertFalse(self._dossier.delete("nonexistent-key"))
        self._dossier.set("key1", {"id": 42, "name": "alex"})
        self._dossier.set("key2", {"id": 42, "name": "alex"})
        self._dossier.delete("key1")
        self.assertFalse(self._dossier.exists("key1"))
        self.assertTrue(self._dossier.exists("key2"))


if __name__ == "__main__":
    unittest.main()
