from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class SQLAlchemyORMLesson(Lesson):
    TITLE = "ORMs: SQLAlchemy"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "ORM"
    LEVEL = "Intermedio"
    TAGS = ["sqlalchemy", "orm", "modelos", "sesiones", "sql"]

    def summary(self) -> str:
        return (
            "Comprende qué es un ORM, cómo funciona SQLAlchemy y cómo modelar datos "
            "con sesiones, commits y buenas prácticas profesionales."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es un ORM?
Un **ORM** (Object-Relational Mapper) traduce objetos de Python a tablas SQL.
Te permite trabajar con clases en lugar de escribir SQL manual.
Cada fila se representa como un **objeto** con atributos.

## Ventajas y desventajas
**Ventajas**:
- Código más legible y mantenible.
- Menos SQL repetitivo.
- Migraciones y modelos centralizados.

**Desventajas**:
- Curva de aprendizaje.
- Puede ocultar detalles de rendimiento.

## SQLAlchemy Core vs ORM
- **Core**: SQL expresivo, más cercano a la base.
- **ORM**: trabaja con clases, ideal para lógica de negocio.

## Conceptos base
- **Conexión**: canal hacia la base.
- **Consulta**: instrucción para leer/escribir datos.
- **Transacción**: cambios confirmados juntos con `commit()`.

### Buenas prácticas (CalloutBox: best_practice)
Aísla la capa de datos en un módulo separado para mantener el código limpio.

## Modelos, sesiones y commits
```
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///tienda.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
```

```
session = Session()
cliente = Cliente(nombre="Ana")
session.add(cliente)
session.commit()  # Confirma la transacción
```

## Relación con SQLite y PostgreSQL
SQLAlchemy permite usar el mismo código con SQLite o PostgreSQL.
Solo cambia la URL de conexión.

### Buenas prácticas (CalloutBox: best_practice)
Usa `session.rollback()` si algo falla para evitar datos inconsistentes.

## Más allá (nivel pro)
- Aprende **lazy loading** y **eager loading** para evitar N+1.
- Usa **Alembic** para migraciones de esquema.
- Mide el rendimiento de tus consultas reales.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir ORM con base de datos",
                "El ORM no reemplaza la base, solo la abstrae.",
            ),
            (
                "Olvidar commit",
                "Sin commit, los cambios no se guardan.",
            ),
            (
                "No cerrar la sesión",
                "La sesión debe cerrarse para liberar recursos.",
            ),
            (
                "Cargar todo en memoria",
                "Usa paginación o filtros para grandes volúmenes.",
            ),
            (
                "Ignorar rendimiento",
                "Algunas consultas generadas pueden ser lentas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Definir un modelo",
                """from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"  # Nombre de la tabla
    id = Column(Integer, primary_key=True)  # Clave primaria
    nombre = Column(String, nullable=False)  # Columna requerida""",
            ),
            (
                "Crear sesión y guardar",
                """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tienda.db")  # Conexión
Session = sessionmaker(bind=engine)
session = Session()  # Sesión activa

session.add(Cliente(nombre="Ana"))  # Agregamos un objeto
session.commit()  # Confirmamos transacción""",
            ),
            (
                "Consultar datos",
                """# Consulta simple con ORM
clientes = session.query(Cliente).filter_by(nombre="Ana").all()  # Lista de resultados""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Explica con tus palabras qué es un ORM.",
                "hints": ["Objetos a tablas"],
                "solution": "Un ORM traduce clases/objetos de Python a tablas y filas en SQL.",
            },
            {
                "question": "Define un modelo Producto con id y nombre.",
                "hints": ["Column", "Integer", "String"],
                "solution": "class Producto(Base): __tablename__='productos'; id=Column(Integer, primary_key=True); nombre=Column(String)",
            },
            {
                "question": "¿Qué hace session.commit()?",
                "hints": ["Confirma transacción"],
                "solution": "Guarda de forma permanente los cambios pendientes.",
            },
            {
                "question": "Menciona una desventaja de usar ORM.",
                "hints": ["Rendimiento"],
                "solution": "Puede ocultar detalles de rendimiento o generar consultas subóptimas.",
            },
            {
                "question": "¿Qué es SQLAlchemy Core?",
                "hints": ["SQL expresivo"],
                "solution": "Es la capa de SQL explícito de SQLAlchemy, más cercana a la base.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["sqlalchemy"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("sqlalchemy")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "SQLAlchemy no disponible."))
            layout.addWidget(QLabel("Instala SQLAlchemy con: pip install sqlalchemy"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("SQLAlchemy disponible. Revisa los ejemplos en la guía."))
        return widget
