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
## Operaciones y métodos más útiles
### Conexión y cursor (DB-API)
1) `connect()` ⭐  
Qué hace: abre una conexión a la base de datos.  
Así se escribe:
```py
import sqlite3
conn = sqlite3.connect("datos.db")
```
Error típico:
```py
conn = sqlite3.connect
```
Verás esto: una conexión abierta.  
Por qué funciona: crea el canal de comunicación.  
Lo típico que sale mal: olvidar paréntesis; usar una ruta/credencial inválida.

2) `cursor()`  
Qué hace: crea un cursor para ejecutar SQL.  
Así se escribe:
```py
cur = conn.cursor()
```
Error típico:
```py
cur = conn.cursor
```
Verás esto: cursor listo para consultas.  
Por qué funciona: el cursor gestiona la ejecución.  
Lo típico que sale mal: olvidar paréntesis; usar cursor tras cerrar la conexión.

3) `execute()` ⭐  
Qué hace: ejecuta una consulta SQL.  
Así se escribe:
```py
cur.execute("SELECT * FROM usuarios")
```
Error típico:
```py
cur.execute
```
Verás esto: consulta ejecutada.  
Por qué funciona: envía SQL al motor.  
Lo típico que sale mal: SQL mal formado; usar parámetros sin placeholders.

4) `executemany()`  
Qué hace: ejecuta muchas inserciones.  
Así se escribe:
```py
cur.executemany("INSERT INTO usuarios(nombre) VALUES (?)", [("Ana",), ("Luis",)])
```
Error típico:
```py
cur.executemany("INSERT INTO usuarios(nombre) VALUES (?)", ("Ana", "Luis"))
```
Verás esto: múltiples filas insertadas.  
Por qué funciona: repite la consulta por cada tupla.  
Lo típico que sale mal: pasar tuplas mal formadas; mismatch de placeholders.

5) `fetchone()`  
Qué hace: obtiene una fila.  
Así se escribe:
```py
fila = cur.fetchone()
```
Error típico:
```py
fila = cur.fetchone
```
Verás esto: una tupla o `None`.  
Por qué funciona: avanza el cursor una fila.  
Lo típico que sale mal: llamar antes de `execute`; asumir que siempre hay datos.

6) `fetchall()`  
Qué hace: obtiene todas las filas.  
Así se escribe:
```py
filas = cur.fetchall()
```
Error típico:
```py
filas = cur.fetchall
```
Verás esto: lista de tuplas.  
Por qué funciona: lee todo el resultado.  
Lo típico que sale mal: usar en consultas enormes; consumir memoria innecesaria.

7) `commit()` ⭐  
Qué hace: confirma cambios.  
Así se escribe:
```py
conn.commit()
```
Error típico:
```py
conn.commit
```
Verás esto: cambios persistidos.  
Por qué funciona: cierra la transacción.  
Lo típico que sale mal: olvidar commit; asumir auto-commit.

8) `rollback()`  
Qué hace: revierte cambios no confirmados.  
Así se escribe:
```py
conn.rollback()
```
Error típico:
```py
conn.rollback
```
Verás esto: cambios descartados.  
Por qué funciona: anula la transacción actual.  
Lo típico que sale mal: llamar tras commit; no manejar excepciones.

9) `close()` ⭐  
Qué hace: cierra la conexión.  
Así se escribe:
```py
conn.close()
```
Error típico:
```py
conn.close
```
Verás esto: conexión cerrada.  
Por qué funciona: libera recursos.  
Lo típico que sale mal: olvidar cerrar; reusar conexión cerrada.

### SQLAlchemy (Engine / Session)
1) `create_engine()` ⭐  
Qué hace: crea el engine de conexión.  
Así se escribe:
```py
from sqlalchemy import create_engine
engine = create_engine("sqlite:///datos.db")
```
Error típico:
```py
engine = create_engine
```
Verás esto: engine listo.  
Por qué funciona: configura el pool y dialecto.  
Lo típico que sale mal: URL inválida; olvidar importar.

2) `connect()`  
Qué hace: abre una conexión del engine.  
Así se escribe:
```py
conn = engine.connect()
```
Error típico:
```py
conn = engine.connect
```
Verás esto: conexión activa.  
Por qué funciona: toma una conexión del pool.  
Lo típico que sale mal: olvidar cerrar; usar fuera de contexto.

3) `execute()` ⭐  
Qué hace: ejecuta SQL o expresiones.  
Así se escribe:
```py
conn.execute(text("SELECT 1"))
```
Error típico:
```py
conn.execute
```
Verás esto: resultado ejecutado.  
Por qué funciona: envía la consulta al motor.  
Lo típico que sale mal: olvidar `text()`; no parametrizar.

4) `begin()`  
Qué hace: inicia una transacción.  
Así se escribe:
```py
with engine.begin() as conn:
    conn.execute(text("DELETE FROM usuarios"))
```
Error típico:
```py
engine.begin()
```
Verás esto: transacción gestionada.  
Por qué funciona: commit/rollback automáticos.  
Lo típico que sale mal: no usar contexto; olvidar importar `text`.

5) `session.add()` ⭐  
Qué hace: agrega un objeto a la sesión.  
Así se escribe:
```py
session.add(usuario)
```
Error típico:
```py
session.add
```
Verás esto: objeto en la sesión.  
Por qué funciona: marca para insert/update.  
Lo típico que sale mal: olvidar commit; agregar objetos sin relaciones completas.

6) `session.commit()` ⭐  
Qué hace: confirma cambios de la sesión.  
Así se escribe:
```py
session.commit()
```
Error típico:
```py
session.commit
```
Verás esto: cambios persistidos.  
Por qué funciona: guarda en la BD.  
Lo típico que sale mal: olvidar commit; no manejar errores.

7) `session.rollback()`  
Qué hace: revierte la sesión.  
Así se escribe:
```py
session.rollback()
```
Error típico:
```py
session.rollback
```
Verás esto: cambios descartados.  
Por qué funciona: restaura estado previo.  
Lo típico que sale mal: olvidar rollback en excepciones; continuar con sesión sucia.

8) `session.query()` ⭐  
Qué hace: consulta registros (ORM).  
Así se escribe:
```py
usuarios = session.query(Usuario).all()
```
Error típico:
```py
usuarios = session.query
```
Verás esto: lista de objetos.  
Por qué funciona: construye una consulta ORM.  
Lo típico que sale mal: olvidar `all()`; usar filtros sin índices.

9) `session.close()`  
Qué hace: cierra la sesión.  
Así se escribe:
```py
session.close()
```
Error típico:
```py
session.close
```
Verás esto: sesión cerrada.  
Por qué funciona: libera recursos.  
Lo típico que sale mal: olvidar cerrar; reusar sesión cerrada.

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
