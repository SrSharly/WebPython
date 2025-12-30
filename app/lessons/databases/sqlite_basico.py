from __future__ import annotations

from app.lesson_base import Lesson


class SQLiteBasicoLesson(Lesson):
    TITLE = "SQLite con Python (sqlite3)"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["sqlite", "sql", "sqlite3", "consultas", "transacciones"]

    def summary(self) -> str:
        return (
            "Aprende a usar SQLite desde cero: conexión, tablas, CRUD, cursores y "
            "transacciones con ejemplos paso a paso."
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

## ¿Qué es SQLite?
SQLite es una base de datos **ligera** que vive en un archivo local. No necesitas servidor.
Es ideal para apps pequeñas, prototipos y aprendizaje.

## ¿Qué es una conexión?
Una **conexión** es el canal con el archivo de la base de datos. Sin conexión no hay datos.
En SQLite, la conexión crea el archivo si no existe.

## ¿Qué es una consulta?
Una **consulta** es una instrucción para leer o modificar datos, como `SELECT` o `INSERT`.

## ¿Qué es una transacción?
Una **transacción** agrupa varios cambios. Si algo falla, se revierte todo.

### Buenas prácticas (CalloutBox: best_practice)
Usa `with sqlite3.connect(...)` para asegurar cierre automático de la conexión.

## Paso 1: Conectar a SQLite
```
import sqlite3

with sqlite3.connect("tienda.db") as conn:  # Abrimos conexión
    print("Conexión lista")  # Mensaje simple
```

## Paso 2: Crear una tabla
```
with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
        '''
    )
```

## Paso 3: Insertar datos (INSERT)
```
with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
        ("Café", 3.5),
    )
```
Cada `?` representa un **parámetro** que se envía por separado y evita errores.

## Paso 4: Consultar datos (SELECT)
```
with sqlite3.connect("tienda.db") as conn:
    cursor = conn.execute("SELECT id, nombre, precio FROM productos")
    for fila in cursor:
        print(fila)
```

## Paso 5: Actualizar datos (UPDATE)
```
with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        "UPDATE productos SET precio = ? WHERE nombre = ?",
        (4.0, "Café"),
    )
```

## Paso 6: Borrar datos (DELETE)
```
with sqlite3.connect("tienda.db") as conn:
    conn.execute("DELETE FROM productos WHERE nombre = ?", ("Café",))
```

## ¿Qué es un cursor?
Un **cursor** es el objeto que recorre los resultados de una consulta.
En sqlite3, `conn.execute()` devuelve un cursor listo para iterar.

## Transacciones: BEGIN / COMMIT / ROLLBACK
SQLite maneja transacciones automáticamente con `with`, pero puedes controlarlas:
- `BEGIN`: inicia la transacción.
- `COMMIT`: confirma cambios.
- `ROLLBACK`: revierte si hay error.

### Buenas prácticas (CalloutBox: best_practice)
- No concatenes SQL con datos: usa parámetros `?`.
- Cierra conexiones y cursores para liberar recursos.
- Separa la lógica de acceso a datos de la interfaz.

## Más allá (nivel pro)
- Usa **índices** cuando las consultas sean lentas.
- Agrega tests para tu capa de datos.
- Aprende a migrar el esquema sin perder datos.

## Micro-ejemplo: placeholders y parámetros

### Así se escribe
```py
import sqlite3

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE productos (id INTEGER, nombre TEXT)")
cursor.execute("INSERT INTO productos VALUES (?, ?)", (1, "Teclado"))
```

### Error típico: número de parámetros incorrecto
```py
import sqlite3

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE productos (id INTEGER, nombre TEXT)")
cursor.execute("INSERT INTO productos VALUES (?, ?)", (1,))
```

```py
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 2, and there are 1 supplied.
```

Explicación breve: cada `?` necesita un valor en la tupla de parámetros.


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
                "Concatenar SQL con strings",
                "Puede causar SQL injection y errores. Usa parámetros.",
            ),
            (
                "Olvidar cerrar la conexión",
                "Deja recursos abiertos y puede bloquear el archivo.",
            ),
            (
                "No usar COMMIT",
                "Sin commit, los cambios pueden perderse.",
            ),
            (
                "Crear tablas sin restricciones",
                "Sin NOT NULL o PRIMARY KEY es fácil tener datos inconsistentes.",
            ),
            (
                "Confundir cursor con conexión",
                "La conexión gestiona la base, el cursor recorre resultados.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Conexión segura con with",
                """import sqlite3  # Importamos el módulo estándar

with sqlite3.connect("tienda.db") as conn:  # Abrimos y cerramos automáticamente
    print("Conectado")  # Mensaje de prueba""",
            ),
            (
                "Crear tabla y usar cursor",
                """import sqlite3

with sqlite3.connect("tienda.db") as conn:
    cursor = conn.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nombre TEXT)"
    )  # cursor representa el resultado
    print("Tabla creada", cursor)  # Mostramos el cursor""",
            ),
            (
                "CRUD básico",
                """import sqlite3

with sqlite3.connect("tienda.db") as conn:
    conn.execute("INSERT INTO clientes (nombre) VALUES (?)", ("Ana",))  # Create
    conn.execute("UPDATE clientes SET nombre = ? WHERE id = ?", ("Ana Pérez", 1))  # Update
    conn.execute("DELETE FROM clientes WHERE id = ?", (1,))  # Delete
    cursor = conn.execute("SELECT id, nombre FROM clientes")  # Read
    for fila in cursor:
        print(fila)  # Mostramos cada fila""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una tabla llamada pedidos con id y total.",
                "hints": ["Usa INTEGER PRIMARY KEY", "total REAL"],
                "solution": "CREATE TABLE pedidos (id INTEGER PRIMARY KEY, total REAL)",
            },
            {
                "question": "Inserta un pedido con total 19.99.",
                "hints": ["Usa INSERT con parámetros"],
                "solution": "conn.execute('INSERT INTO pedidos (total) VALUES (?)', (19.99,))",
            },
            {
                "question": "Consulta todos los pedidos.",
                "hints": ["SELECT * FROM pedidos"],
                "solution": "cursor = conn.execute('SELECT * FROM pedidos')",
            },
            {
                "question": "Actualiza el total del pedido con id=1 a 25.0.",
                "hints": ["UPDATE con WHERE"],
                "solution": "conn.execute('UPDATE pedidos SET total = ? WHERE id = ?', (25.0, 1))",
            },
            {
                "question": "Elimina el pedido con id=1.",
                "hints": ["DELETE con WHERE"],
                "solution": "conn.execute('DELETE FROM pedidos WHERE id = ?', (1,))",
            },
        ]
