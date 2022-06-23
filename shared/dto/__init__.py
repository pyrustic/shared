"""Classes for Data Transfer Objects"""
from collections import namedtuple


Target = namedtuple("Target", ["name", "directory", "pathname", "tempdir"])

DossierEntryInfo = namedtuple("DossierEntryInfo", ["name", "container", "filename"])

ColumnInfo = namedtuple("ColumnInfo", ["index", "name", "type", "not_null", "default", "primary_key"])

QueryResult = namedtuple("QueryResult", ["columns", "data"])
