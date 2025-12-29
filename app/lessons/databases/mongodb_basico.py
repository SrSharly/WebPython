from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class MongoDBBasicoLesson(Lesson):
    TITLE = "NoSQL: MongoDB"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "NoSQL"
    LEVEL = "Intermedio"
    TAGS = ["mongodb", "nosql", "documentos", "pymongo", "colecciones"]

    def summary(self) -> str:
        return (
            "Introducción a MongoDB desde cero: documentos, colecciones y operaciones básicas "
            "con pymongo, más cuándo NO usarlo."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es NoSQL?
NoSQL agrupa bases de datos que no usan tablas tradicionales.
MongoDB almacena **documentos** (parecidos a dicts de Python).

## Documentos vs tablas
- **Documento**: conjunto flexible de campos, como un objeto.
- **Colección**: grupo de documentos (similar a una tabla, pero flexible).
Un documento es un **objeto** JSON con campos opcionales.

## Conceptos base
- **Conexión**: canal con el servidor MongoDB.
- **Consulta**: filtro para obtener documentos.
- **Transacción**: cambios agrupados (en MongoDB se usan en escenarios específicos).

### Buenas prácticas (CalloutBox: best_practice)
Diseña tus documentos pensando en cómo los vas a consultar.

## Conexión con pymongo
```
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["tienda"]
coleccion = db["clientes"]
```

## Insertar documentos
```
coleccion.insert_one({"nombre": "Ana", "activo": True})
```

## Buscar documentos
```
for doc in coleccion.find({"activo": True}):
    print(doc)
```

## Actualizar documentos
```
coleccion.update_one({"nombre": "Ana"}, {"$set": {"activo": False}})
```

## ¿Cuándo NO usar MongoDB?
- Si necesitas **relaciones complejas** con joins frecuentes.
- Si necesitas **consistencia estricta** tipo SQL.

### Buenas prácticas (CalloutBox: best_practice)
No uses MongoDB solo “porque es moderno”. Úsalo cuando el modelo de documentos encaje.

## Más allá (nivel pro)
- Aprende a usar **índices** para acelerar búsquedas.
- Evalúa transacciones en replica sets cuando sea necesario.
- Diseña un esquema flexible, pero con reglas claras.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Guardar todo en un solo documento gigante",
                "Dificulta actualizaciones y puede impactar rendimiento.",
            ),
            (
                "No crear índices",
                "Las búsquedas se vuelven lentas con muchos documentos.",
            ),
            (
                "Ignorar validaciones",
                "MongoDB es flexible, pero debes mantener consistencia.",
            ),
            (
                "Usar MongoDB para relaciones complejas",
                "No es su punto fuerte; SQL puede ser mejor.",
            ),
            (
                "No cerrar conexiones",
                "Los clientes deben cerrarse al terminar.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Conectar y seleccionar colección",
                """from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  # Conexión
bd = client["tienda"]  # Base de datos
coleccion = bd["clientes"]  # Colección""",
            ),
            (
                "Insertar y buscar",
                """coleccion.insert_one({"nombre": "Ana", "activo": True})  # Insertar
for doc in coleccion.find({"activo": True}):  # Buscar
    print(doc)  # Mostrar documento""",
            ),
            (
                "Actualizar documento",
                """coleccion.update_one(
    {"nombre": "Ana"},
    {"$set": {"activo": False}},
)  # Actualizamos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Define qué es un documento en MongoDB.",
                "hints": ["Objeto flexible"],
                "solution": "Es un conjunto flexible de campos, similar a un dict.",
            },
            {
                "question": "Conecta a MongoDB en localhost.",
                "hints": ["MongoClient"],
                "solution": "client = MongoClient('mongodb://localhost:27017')",
            },
            {
                "question": "Inserta un documento con nombre 'Luis'.",
                "hints": ["insert_one"],
                "solution": "coleccion.insert_one({'nombre': 'Luis'})",
            },
            {
                "question": "Busca documentos activos.",
                "hints": ["find"],
                "solution": "coleccion.find({'activo': True})",
            },
            {
                "question": "Menciona un caso donde NO usar MongoDB.",
                "hints": ["Relaciones complejas"],
                "solution": "Cuando se necesitan joins complejos o consistencia estricta.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["pymongo"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("pymongo")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "pymongo no disponible."))
            layout.addWidget(QLabel("Instala pymongo con: pip install pymongo"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("pymongo disponible. Revisa los ejemplos en la guía."))
        return widget
