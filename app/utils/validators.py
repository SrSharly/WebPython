from __future__ import annotations

import logging
import os

LOGGER = logging.getLogger(__name__)


def warn_if_short_example(code: str, context: str) -> None:
    if not _is_dev_mode():
        return
    code_lines = [
        line
        for line in code.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if len(code_lines) < 3:
        LOGGER.warning(
            "Ejemplo demasiado corto: debe seguir el patrón Aprende/Haz/Verás/Por qué/Pitfalls (%s)",
            context,
        )


def _is_dev_mode() -> bool:
    env_value = os.getenv("PYTHONPEDIA_ENV", "").lower()
    explicit_flag = os.getenv("PYTHONPEDIA_DEV", "").lower()
    return env_value in {"dev", "development", "local"} or explicit_flag in {"1", "true", "yes"}
