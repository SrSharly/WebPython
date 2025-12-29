from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class TypingPracticoLesson(Lesson):
    TITLE = "Typing práctico"
    CATEGORY = "Python"
    SUBCATEGORY = "Buenas prácticas"
    LEVEL = "Intermedio"
    TAGS = ["typing", "Optional", "Protocol", "TypeVar", "hints"]

    def summary(self) -> str:
        return (
            "El tipado gradual ayuda a comunicar intención, detectar errores y "
            "documentar APIs con hints como Optional, Union y Protocol."
        )

    def guide(self) -> str:
        return """
TL;DR: Usa typing para describir contratos y detectar problemas antes de ejecutar.
- Optional[T] es lo mismo que Union[T, None].
- Literal restringe valores válidos (p. ej., Literal["A", "B"]).
- TypedDict describe dicts con claves y tipos esperados.
- Protocol define interfaces estructurales (duck typing tipado).
- Sequence es más general que list; Mapping más general que dict.
- Callable[[args], retorno] describe funciones invocables.
- TypeVar permite funciones genéricas reutilizables.
- Evita Any si quieres validación; se propaga y desactiva chequeos.
- Preferir tipos inmutables para defaults (None + asignación interna).
- Usa comentarios de tipo para casos complejos.
- type checkers detectan incompatibilidades de forma estática.
- Mantén hints simples y consistentes en toda la API.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Optional mal usado",
                "Si un valor nunca es None, no lo marques como Optional.",
            ),
            (
                "Any contagioso",
                "Una función que acepta Any propaga el tipo dinámico a todo.",
            ),
            (
                "Default mutable",
                "list/dict como default rompe el tipado y el comportamiento.",
            ),
            (
                "TypeVar sin restricciones",
                "Puede generar resultados demasiado genéricos o inútiles.",
            ),
            (
                "Union excesivo",
                "Unión grande dificulta la lectura y el mantenimiento.",
            ),
            (
                "Usar list en APIs genéricas",
                "Sequence permite pasar tuplas o rangos sin copiar.",
            ),
            (
                "TypedDict incompleto",
                "Si falta una clave obligatoria, el checker no puede validar.",
            ),
            (
                "Protocol no importado",
                "Necesitas typing.Protocol para interfaces estructurales.",
            ),
            (
                "Callable sin firma",
                "Callable sin args ni retorno pierde información útil.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Optional vs Union",
                """from typing import Optional\n\ndef buscar(nombre: str) -> Optional[int]:\n    return 1 if nombre else None""",
            ),
            (
                "Literal",
                """from typing import Literal\n\ndef modo(color: Literal["rojo", "azul"]) -> str:\n    return color""",
            ),
            (
                "TypedDict",
                """from typing import TypedDict\n\nclass Usuario(TypedDict):\n    nombre: str\n    edad: int\n\nu: Usuario = {"nombre": "Ana", "edad": 30}""",
            ),
            (
                "Protocol",
                """from typing import Protocol\n\nclass Escribible(Protocol):\n    def escribir(self, texto: str) -> None: ...""",
            ),
            (
                "Sequence vs list",
                """from typing import Sequence\n\ndef total(valores: Sequence[int]) -> int:\n    return sum(valores)""",
            ),
            (
                "Mapping vs dict",
                """from typing import Mapping\n\ndef leer(cfg: Mapping[str, str]) -> str:\n    return cfg.get("host", "")""",
            ),
            (
                "Callable",
                """from typing import Callable\n\ndef aplicar(x: int, fn: Callable[[int], int]) -> int:\n    return fn(x)""",
            ),
            (
                "TypeVar",
                """from typing import TypeVar\n\nT = TypeVar("T")\n\ndef primero(valores: list[T]) -> T:\n    return valores[0]""",
            ),
            (
                "Default seguro",
                """from typing import Optional\n\ndef agregar(item: int, datos: Optional[list[int]] = None) -> list[int]:\n    if datos is None:\n        datos = []\n    datos.append(item)\n    return datos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Define una función que reciba Sequence[str] y devuelva su longitud.",
                "hints": ["Sequence", "len"],
                "solution": "from typing import Sequence\n\ndef contar(textos: Sequence[str]) -> int:\n    return len(textos)",
            },
            {
                "question": "Crea un TypedDict para un producto con nombre y precio.",
                "hints": ["TypedDict"],
                "solution": "from typing import TypedDict\n\nclass Producto(TypedDict):\n    nombre: str\n    precio: float",
            },
            {
                "question": "Escribe un Protocol llamado Exportable con método exportar().",
                "hints": ["Protocol"],
                "solution": "from typing import Protocol\n\nclass Exportable(Protocol):\n    def exportar(self) -> str: ...",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo textual: ejemplos de firmas buenas y malas."))
        layout.addWidget(
            QLabel(
                "Buen hint: def total(valores: Sequence[int]) -> int\n"
                "Mal hint: def total(valores) -> Any\n"
                "Buen hint: def cargar(cfg: Mapping[str, str]) -> str"
            )
        )
        return widget
