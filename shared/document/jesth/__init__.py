import jesth
from shared.document import Document
from shared.constant import DEFAULT_DIRECTORY


def jesth_create(target, *, default=None, directory=DEFAULT_DIRECTORY):
    """Convenience function to create a document"""
    document = JesthDocument(target, default=default, autosave=False,
                             readonly=False, caching=False,
                             directory=directory, temporary=False)
    document.close()


def jesth_readonly(target, *, default=None, directory=DEFAULT_DIRECTORY,
                   compact=False, split_body=True):
    """Convenience function to open a document in readonly mode. It returns the data"""
    document = JesthDocument(target, default=default, autosave=False,
                             readonly=True, caching=False,
                             directory=directory, temporary=False,
                             compact=compact, split_body=split_body)
    data = document.read()
    document.close()
    return data


def jesth_write(target, data, *, directory=DEFAULT_DIRECTORY):
    """Convenience function to open a document then write data inside"""
    document = JesthDocument(target, default=None, autosave=False,
                             readonly=False, caching=False,
                             directory=directory, temporary=False)
    document.write(data)
    document.close()


def jesth_autosave(target, *, default=None, directory=DEFAULT_DIRECTORY,
                   compact=False, split_body=True):
    """Convenience function to open a document in autosave mode. It returns data"""
    document = JesthDocument(target, default=default, autosave=True,
                             readonly=False, caching=True,
                             directory=directory, temporary=False,
                             compact=compact, split_body=split_body)
    return document.read()


class JesthDocument(Document):
    def __init__(self, target, *, default=None,
                 autosave=False, readonly=False,
                 caching=True, directory=DEFAULT_DIRECTORY,
                 temporary=False, compact=False, split_body=True):
        """
        Init.

        [parameters]
        - target: target is either the absolute pathname or the basename of a file.
        Its datatype is either a string or a pathlib.Path instance.
        - default: default value for this document file.
        If the document is newly created, the default value will populate it. If you don't set a default value, a dict will be the default value.
        - autosave: boolean to say if you want to activate the autosave feature or not
        - readonly: boolean to say if you want to open this document in readonly mode or not
        - caching: boolean to set if whether data should be cached or not
        - directory: the directory where you want to store the document.
        By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory,
        the document will be created in a temporary directory
        - temporary: boolean to tell if either you want this document to be temporary or not
        """
        super().__init__(target, default=default, autosave=autosave,
                         readonly=readonly, caching=caching, directory=directory,
                         temporary=temporary)
        self.__compact = compact
        self.__split_body = split_body

    def _read(self):
        return jesth.read(self._pathname, compact=self.__compact,
                          split_body=self.__split_body)

    def _write(self, data):
        return jesth.write(data, self._pathname)
