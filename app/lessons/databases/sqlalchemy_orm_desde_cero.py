from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class SQLAlchemyORMDesdeCeroLesson(Lesson):
    TITLE = "SQLAlchemy ORM desde cero"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "SQLAlchemy"
    LEVEL = "Intermedio"
    TAGS = ["sqlalchemy", "orm", "session", "modelos", "relaciones"]

    def summary(self) -> str:
        return (
            "Aprende ORM desde cero con SQLAlchemy: modelos, sesiones, relaciones "
            "y transacciones con SQLite como base de práctica."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es un ORM?
Un **ORM** (Object-Relational Mapping) traduce clases de Python a tablas SQL y objetos a filas.
Te permite trabajar con objetos sin escribir SQL en cada consulta.

## Conceptos clave desde cero
- **Declarative Base**: clase base para definir modelos.
- **Session**: unidad de trabajo que gestiona objetos y transacciones.
- **Commit/Rollback**: guardar o revertir cambios.

### Buenas prácticas (CalloutBox: best_practice)
- Crea una sesión por unidad de trabajo.
- Usa `commit()` cuando quieras guardar cambios.
- Cierra la sesión cuando termines.

## Paso 1: Instalar SQLAlchemy
```
pip install sqlalchemy
```

## Paso 2: Crear el engine y la base declarativa
```
from sqlalchemy import create_engine  # Importamos engine
from sqlalchemy.orm import declarative_base  # Importamos base

engine = create_engine("sqlite+pysqlite:///:memory:")  # Engine en memoria
Base = declarative_base()  # Base de modelos
```

## Paso 3: Definir un modelo
```
from sqlalchemy import Column, Integer, String  # Importamos columnas

class Cliente(Base):  # Creamos modelo
    __tablename__ = "clientes"  # Nombre de tabla
    id = Column(Integer, primary_key=True)  # PK
    nombre = Column(String, nullable=False)  # Columna texto
```

## Paso 4: Crear tablas
```
Base.metadata.create_all(engine)  # Creamos tablas
```

## Paso 5: Crear una sesión
```
from sqlalchemy.orm import sessionmaker  # Importamos sessionmaker

Session = sessionmaker(bind=engine)  # Configuramos fábrica
session = Session()  # Creamos sesión
```

## Paso 6: Insertar y consultar
```
cliente = Cliente(nombre="Ana")  # Creamos objeto
session.add(cliente)  # Agregamos a la sesión
session.commit()  # Guardamos

clientes = session.query(Cliente).all()  # Consultamos
for c in clientes:
    print(c.nombre)
```

## Relaciones básicas (muy simple)
Una relación enlaza tablas. Ejemplo: Cliente tiene muchos pedidos.
```
from sqlalchemy import ForeignKey  # Importamos ForeignKey
from sqlalchemy.orm import relationship  # Importamos relationship

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", backref="pedidos")
```

## Errores comunes y su causa
- **Sesión mal gestionada**: olvidar cerrarla deja conexiones abiertas.
- **Objetos detached**: usar objetos fuera de la sesión sin recargar.
- **Autocommit mental model**: creer que los cambios se guardan solos.

## Más allá (nivel pro)
- Usa patrones de repositorio para organizar consultas.
- Configura `expire_on_commit=False` si quieres evitar recargas.
- Optimiza relaciones con `selectinload`.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No cerrar la sesión",
                "Deja conexiones abiertas y consume recursos.",
            ),
            (
                "Olvidar commit",
                "Los cambios se pierden si no confirmas.",
            ),
            (
                "Modificar objetos detached",
                "No se sincronizan con la base si la sesión ya cerró.",
            ),
            (
                "Abusar de consultas N+1",
                "Lanzas demasiadas consultas al cargar relaciones.",
            ),
            (
                "Confundir Base con engine",
                "Base define modelos; engine conecta.",
            ),
            (
                "Usar una sesión global",
                "Dificulta manejo de errores y transacciones.",
            ),
            (
                "No manejar rollback",
                "Una excepción deja la sesión en estado inválido.",
            ),
            (
                "Pensar que ORM evita SQL",
                "A veces necesitas SQL explícito para rendimiento.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Base declarativa",
                """from sqlalchemy.orm import declarative_base  # Importamos base\nBase = declarative_base()  # Creamos base""",
            ),
            (
                "Engine y sesión",
                """from sqlalchemy import create_engine  # Importamos engine\nfrom sqlalchemy.orm import sessionmaker  # Importamos sessionmaker\nengine = create_engine(\"sqlite+pysqlite:///:memory:\")  # Engine\nSession = sessionmaker(bind=engine)  # Fábrica de sesiones\nsession = Session()  # Creamos sesión""",
            ),
            (
                "Definir un modelo",
                """from sqlalchemy import Column, Integer, String  # Importamos columnas\nclass Cliente(Base):  # Modelo\n    __tablename__ = \"clientes\"  # Nombre tabla\n    id = Column(Integer, primary_key=True)  # PK\n    nombre = Column(String, nullable=False)  # Campo""",
            ),
            (
                "Crear tablas",
                """Base.metadata.create_all(engine)  # Creamos tablas""",
            ),
            (
                "Insertar un registro",
                """cliente = Cliente(nombre=\"Ana\")  # Creamos objeto\nsession.add(cliente)  # Agregamos\nsession.commit()  # Confirmamos""",
            ),
            (
                "Consultar registros",
                """clientes = session.query(Cliente).all()  # Consultamos\nfor cliente in clientes:  # Iteramos\n    print(cliente.nombre)  # Mostramos""",
            ),
            (
                "Relacion simple",
                """from sqlalchemy import ForeignKey  # Importamos ForeignKey\nfrom sqlalchemy.orm import relationship  # Importamos relationship\nclass Pedido(Base):  # Modelo\n    __tablename__ = \"pedidos\"  # Tabla\n    id = Column(Integer, primary_key=True)  # PK\n    cliente_id = Column(Integer, ForeignKey(\"clientes.id\"))  # FK\n    cliente = relationship(\"Cliente\", backref=\"pedidos\")  # Relación""",
            ),
            (
                "Rollback tras error",
                """try:  # Bloque seguro\n    session.add(Cliente(nombre=\"Luis\"))  # Agregamos\n    session.commit()  # Confirmamos\nexcept Exception:  # Capturamos error\n    session.rollback()  # Revertimos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Define un modelo Producto con id y nombre.",
                "hints": ["Column", "Integer", "String"],
                "solution": "class Producto(Base): __tablename__='productos'; id=Column(Integer, primary_key=True); nombre=Column(String)",
            },
            {
                "question": "Crea las tablas con metadata.",
                "hints": ["create_all"],
                "solution": "Base.metadata.create_all(engine)",
            },
            {
                "question": "Crea una sesión y agrega un Producto.",
                "hints": ["sessionmaker", "add"],
                "solution": "session = Session(); session.add(Producto(nombre='Mesa')); session.commit()",
            },
            {
                "question": "Consulta todos los productos.",
                "hints": ["query", "all"],
                "solution": "productos = session.query(Producto).all()",
            },
            {
                "question": "Define una relación simple Cliente-Pedido.",
                "hints": ["ForeignKey", "relationship"],
                "solution": "cliente_id = Column(Integer, ForeignKey('clientes.id')); cliente = relationship('Cliente')",
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

        from sqlalchemy import Column, Integer, String, create_engine
        from sqlalchemy.orm import declarative_base, sessionmaker

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo ORM con SQLite en memoria."))

        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output)

        run_button = QPushButton("Crear y consultar datos")
        layout.addWidget(run_button)

        def _run_demo() -> None:
            engine = create_engine("sqlite+pysqlite:///:memory:")
            Base = declarative_base()

            class Persona(Base):
                __tablename__ = "personas"
                id = Column(Integer, primary_key=True)
                nombre = Column(String, nullable=False)

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(Persona(nombre="Ada"))
            session.add(Persona(nombre="Linus"))
            session.commit()
            personas = session.query(Persona).all()
            session.close()

            output.clear()
            output.append("Personas:")
            for persona in personas:
                output.append(f"- {persona.nombre}")

        run_button.clicked.connect(_run_demo)
        return widget
