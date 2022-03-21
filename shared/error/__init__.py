"""Errors classes"""


class Error(Exception):
    pass


class ReadonlyError(Error):
    pass


class AlreadyDeletedError(Error):
    pass
