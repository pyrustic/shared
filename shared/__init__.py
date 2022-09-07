"""The Shared Data Interface"""
from shared.document import Document
from shared.dossier import Dossier
from shared.database import Database
from shared.document.json import JsonDocument, json_create,\
    json_readonly, json_write, json_autosave
from shared.document.jesth import JesthDocument, jesth_create,\
    jesth_readonly, jesth_write, jesth_autosave
from jesth.util import get_key_value
from shared.constant import DEFAULT_DIRECTORY


__all__ = ["Document", "Dossier", "Database",
           "JsonDocument", "json_create", "json_readonly",
           "json_write", "json_autosave",
           "JesthDocument", "jesth_create", "jesth_readonly",
           "jesth_write", "jesth_autosave",
           "get_key_value", "DEFAULT_DIRECTORY"]
