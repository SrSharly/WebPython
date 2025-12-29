from __future__ import annotations

import html
import re

TERMS = {
    "snake_case": "Convención de nombres con palabras en minúsculas separadas por guiones bajos.",
    "pascalcase": "Convención de nombres con cada palabra iniciando en mayúscula, sin separadores.",
    "variable": "Espacio de memoria con un nombre que guarda un valor.",
    "función": "Bloque reutilizable de código que realiza una tarea específica.",
    "parámetro": "Nombre definido en la función para recibir valores.",
    "argumento": "Valor real que se envía a una función al llamarla.",
    "tupla": "Colección ordenada e inmutable de elementos.",
    "lista": "Colección ordenada y mutable de elementos.",
    "mutable": "Se puede modificar después de ser creado.",
    "inmutable": "No se puede modificar después de ser creado.",
    "método": "Función asociada a un objeto o clase.",
    "objeto": "Instancia de una clase con estado y comportamiento.",
    "scope": "Alcance donde una variable es visible y válida.",
    "append": "Método de listas que agrega un elemento al final.",
    "upper": "Método de strings que convierte a mayúsculas.",
    "len": "Función que devuelve la longitud de una colección.",
    "print": "Función que muestra texto en la salida estándar.",
}

_TERM_PATTERN = re.compile(
    r"(?<!\w)(" + "|".join(re.escape(term) for term in sorted(TERMS, key=len, reverse=True)) + r")(?!\w)",
    flags=re.IGNORECASE,
)


def _apply_tooltips_to_text(text: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        original = match.group(0)
        definition = TERMS.get(original.lower())
        if definition is None:
            return original
        safe_definition = html.escape(definition, quote=True)
        return f'<span title="{safe_definition}">{original}</span>'

    return _TERM_PATTERN.sub(_replace, text)


def apply_glossary_tooltips(html_or_text: str) -> str:
    parts = re.split(r"(<[^>]+>)", html_or_text)
    output: list[str] = []
    in_code = False
    for part in parts:
        if part.startswith("<"):
            tag = part.lower()
            if tag.startswith("<code") or tag.startswith("<pre"):
                in_code = True
            if tag.startswith("</code") or tag.startswith("</pre"):
                in_code = False
            output.append(part)
        else:
            output.append(part if in_code else _apply_tooltips_to_text(part))
    return "".join(output)
