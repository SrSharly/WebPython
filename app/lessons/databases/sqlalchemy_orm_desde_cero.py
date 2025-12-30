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
