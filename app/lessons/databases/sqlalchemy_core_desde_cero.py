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


class SQLAlchemyCoreDesdeCeroLesson(Lesson):
    TITLE = "SQLAlchemy Core desde cero"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "SQLAlchemy"
    LEVEL = "Básico"
    TAGS = ["sqlalchemy", "core", "engine", "connection", "sql", "pool"]

    def summary(self) -> str:
        return (
            "Aprende SQLAlchemy Core desde cero: qué es, cómo crear un engine, "
            "ejecutar consultas seguras y leer resultados usando SQLite."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es SQLAlchemy?
SQLAlchemy es una librería que te permite trabajar con SQL en Python de forma segura y portátil.
Su capa **Core** es SQL explícito, sin magia, pero con herramientas útiles.

## Conceptos clave desde cero
- **Engine**: objeto que sabe cómo conectar a la base de datos.
- **Connection**: conexión activa para ejecutar SQL.
- **Pool**: grupo de conexiones reutilizables para no abrir una nueva cada vez.

### Buenas prácticas (CalloutBox: best_practice)
- Usa `text()` y parámetros con nombre para evitar SQL injection.
- Mantén el engine como singleton en apps reales.
- Cierra conexiones con `with`.

## Paso 1: Instalar (si no está)
```
pip install sqlalchemy
```

## Paso 2: Crear un engine con SQLite
SQLite siempre está disponible y es ideal para aprender.
```
from sqlalchemy import create_engine  # Importamos create_engine

engine = create_engine("sqlite+pysqlite:///:memory:")  # Engine en memoria
```

## Paso 3: Ejecutar SQL seguro con text()
`text()` permite **bind params** (parámetros enlazados), que son valores separados del SQL
para evitar errores y ataques de SQL injection. SQL injection es cuando alguien intenta
inyectar SQL dentro de un dato de entrada.
```
from sqlalchemy import text  # Importamos text

with engine.connect() as conn:
    conn.execute(
        text("SELECT :numero AS valor"),
        {"numero": 42},
    )
```

## Paso 4: Crear tabla e insertar datos
```
from sqlalchemy import text

with engine.begin() as conn:  # begin abre transacción
    conn.execute(
        text("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)"),
    )
    conn.execute(
        text("INSERT INTO productos (nombre, precio) VALUES (:nombre, :precio)"),
        {"nombre": "Café", "precio": 3.5},
    )
```

## Paso 5: Consultar resultados
```
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT nombre, precio FROM productos"))
    for fila in result:
        print(fila)
```

## ¿Qué es una transacción aquí?
Una **transacción** agrupa cambios. `engine.begin()` hace commit automático si todo va bien, y
rollback si ocurre un error.

## Más allá (nivel pro)
- Usa `pool_pre_ping=True` para detectar conexiones muertas.
- Agrega logs de SQL cuando estés depurando.
- Configura timeouts para consultas largas.


## Micro-ejemplo incremental: conexión y consulta segura

### Así se escribe
```py
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE demo (id INTEGER)")
cursor.execute("INSERT INTO demo (id) VALUES (?)", (1,))
conn.commit()
```

### Error típico: pasar el placeholder incorrecto
```py
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("INSERT INTO demo (id) VALUES (?)", 1)
```

```py
ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 0 supplied.
```

Explicación breve: los parámetros van en tuplas, por ejemplo `(1,)`.

### Error típico: usar conexión cerrada
```py
import sqlite3

conn = sqlite3.connect(":memory:")
conn.close()
conn.execute("SELECT 1")
```

```py
ProgrammingError: Cannot operate on a closed database.
```

Explicación breve: la conexión debe estar abierta antes de ejecutar consultas.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear engines en cada consulta",
                "Pierdes el beneficio del pool y creas sobrecarga.",
            ),
            (
                "No usar text()",
                "Sin text() pierdes parámetros seguros.",
            ),
            (
                "Olvidar cerrar conexiones",
                "Se agotan conexiones y la app se ralentiza.",
            ),
            (
                "Confundir Connection con Engine",
                "El engine es la fábrica, la connection es temporal.",
            ),
            (
                "Usar SQL concatenado",
                "Vuelve a aparecer SQL injection.",
            ),
            (
                "No manejar transacciones",
                "Puedes dejar datos a medias sin rollback.",
            ),
            (
                "Asumir autocommit",
                "En Core debes decidir cuándo commit.",
            ),
            (
                "Ignorar el pool",
                "Un pool mal configurado puede causar bloqueos.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear un engine",
                """from sqlalchemy import create_engine  # Importamos create_engine\nengine = create_engine(\"sqlite+pysqlite:///:memory:\")  # Creamos engine""",
            ),
            (
                "Consulta simple con text",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Abrimos conexión\n    result = conn.execute(text(\"SELECT 1 AS valor\"))  # Ejecutamos SQL\n    print(result.fetchone())  # Leemos una fila""",
            ),
            (
                "Parámetros con nombre",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Abrimos conexión\n    result = conn.execute(text(\"SELECT :x + :y AS suma\"), {\"x\": 2, \"y\": 3})  # Ejecutamos\n    print(result.scalar())  # Mostramos resultado""",
            ),
            (
                "Crear tabla",
                """from sqlalchemy import text  # Importamos text\nwith engine.begin() as conn:  # Transacción automática\n    conn.execute(text(\"CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT)\"))  # Creamos""",
            ),
            (
                "Insertar datos",
                """from sqlalchemy import text  # Importamos text\nwith engine.begin() as conn:  # Transacción\n    conn.execute(text(\"INSERT INTO productos (nombre) VALUES (:nombre)\"), {\"nombre\": \"Té\"})  # Insertamos""",
            ),
            (
                "Consultar datos",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Conexión\n    result = conn.execute(text(\"SELECT nombre FROM productos\"))  # Consultamos\n    for fila in result:  # Iteramos\n        print(fila.nombre)  # Mostramos""",
            ),
            (
                "Actualizar datos",
                """from sqlalchemy import text  # Importamos text\nwith engine.begin() as conn:  # Transacción\n    conn.execute(text(\"UPDATE productos SET nombre = :nuevo WHERE nombre = :viejo\"), {\"nuevo\": \"Té verde\", \"viejo\": \"Té\"})  # Actualizamos""",
            ),
            (
                "Borrar datos",
                """from sqlalchemy import text  # Importamos text\nwith engine.begin() as conn:  # Transacción\n    conn.execute(text(\"DELETE FROM productos WHERE nombre = :nombre\"), {\"nombre\": \"Té verde\"})  # Borramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un engine para SQLite en memoria.",
                "hints": ["create_engine", ":memory:"],
                "solution": "engine = create_engine('sqlite+pysqlite:///:memory:')",
            },
            {
                "question": "Ejecuta un SELECT con text() que devuelva 10.",
                "hints": ["text", "SELECT"],
                "solution": "conn.execute(text('SELECT 10 AS valor'))",
            },
            {
                "question": "Crea una tabla clientes con id y nombre.",
                "hints": ["CREATE TABLE"],
                "solution": "conn.execute(text('CREATE TABLE clientes (id INTEGER PRIMARY KEY, nombre TEXT)'))",
            },
            {
                "question": "Inserta un cliente llamado 'Lia'.",
                "hints": ["INSERT", ":nombre"],
                "solution": "conn.execute(text('INSERT INTO clientes (nombre) VALUES (:nombre)'), {'nombre': 'Lia'})",
            },
            {
                "question": "Consulta todos los clientes.",
                "hints": ["SELECT", "result"],
                "solution": "result = conn.execute(text('SELECT * FROM clientes'))",
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

        from sqlalchemy import create_engine, text

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo SQLAlchemy Core (SQLite en memoria)."))

        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output)

        run_button = QPushButton("Ejecutar consulta demo")
        layout.addWidget(run_button)

        def _run_demo() -> None:
            engine = create_engine("sqlite+pysqlite:///:memory:")
            with engine.begin() as conn:
                conn.execute(text("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT)"))
                conn.execute(text("INSERT INTO productos (nombre) VALUES (:nombre)"), {"nombre": "Café"})
                result = conn.execute(text("SELECT id, nombre FROM productos"))
                filas = result.fetchall()
            output.clear()
            output.append("Resultados:")
            for fila in filas:
                output.append(f"- {fila.id}: {fila.nombre}")

        run_button.clicked.connect(_run_demo)
        return widget
