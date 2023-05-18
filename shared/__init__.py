"""The Shared Data Interface"""
from shared.document import Document
from shared.dossier import Dossier
from shared.database import Database
from shared.document.json import JsonDoc, json_create,\
    json_readonly, json_write, json_autosave
from shared.constant import DEFAULT_DIRECTORY


__all__ = ["Document", "Dossier", "Database",
           "JsonDoc", "json_create", "json_readonly",
           "json_write", "json_autosave", "DEFAULT_DIRECTORY"]
