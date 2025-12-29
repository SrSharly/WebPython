from __future__ import annotations

import importlib
from types import ModuleType
from typing import Tuple


def optional_import(name: str) -> Tuple[bool, ModuleType | None, str | None]:
    try:
        module = importlib.import_module(name)
    except Exception as exc:  # pragma: no cover - used for optional deps
        return False, None, f"No se pudo importar {name}: {exc}"
    return True, module, None
