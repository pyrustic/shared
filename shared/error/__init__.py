"""Errors classes"""


class Error(Exception):
    pass


class ReadonlyError(Error):
    pass


class AlreadyClosedError(Error):
    pass


class AlreadyDeletedError(Error):
    pass
