from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set


class ModelBase:
    def __init__(self, id: int, status: int, is_deleted: bool, created_by: str, last_updated_by: str, created_on: Optional[date], last_updated_on: Optional[date]):
        #super().__init__(**kwargs)
        self._id = id
        self._status = status
        self._created_on = created_on
        self._created_by = created_by
        self._last_updated_on = last_updated_on
        self._last_updated_by = last_updated_by
        self._is_deleted = is_deleted