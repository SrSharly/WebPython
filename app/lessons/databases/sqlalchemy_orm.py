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
