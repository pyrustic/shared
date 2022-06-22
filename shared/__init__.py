"""The Shared Data Interface"""
from shared.document import Document, create, write, readonly, autosave
from shared.dossier import Dossier
from shared.database import Database
from shared.constant import DEFAULT_DIRECTORY
from jesth.util import get_key_value


__all__ = ["Document", "Dossier", "Database",
           "create", "readonly", "write", "autosave",
           "get_key_value", "DEFAULT_DIRECTORY"]
