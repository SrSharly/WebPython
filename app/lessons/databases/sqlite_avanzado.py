from __future__ import annotations

from app.lesson_base import Lesson


class SQLiteAvanzadoLesson(Lesson):
    TITLE = "Rendimiento y patrones reales"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Avanzado"
    LEVEL = "Intermedio"
    TAGS = ["sqlite", "indices", "relaciones", "migraciones", "rendimiento"]

    def summary(self) -> str:
        return (
            "Profundiza en SQLite con parámetros seguros, índices, relaciones simples, "
            "manejo de errores y migraciones básicas."
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

## Enfoque de esta lección
Vamos a mejorar tus bases con **prácticas reales**: seguridad, rendimiento y estructura.
Usaremos SQLite, pero los conceptos aplican a otras bases de datos.

## Recordatorio rápido
- **Conexión**: canal entre tu app y la base de datos.
- **Consulta**: instrucción para leer o modificar datos.
- **Transacción**: cambios que se confirman todos o ninguno.

### Buenas prácticas (CalloutBox: best_practice)
Siempre usa parámetros en las consultas. Evitan errores y ataques.

## Parámetros seguros con `?`
Los parámetros separan los datos del SQL:
```
import sqlite3

with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
        ("Té", 2.5),
    )
```
Un **parámetro** evita que el usuario altere la consulta.

## Índices: acelerar consultas
Un **índice** es una estructura que hace más rápido buscar por una columna.
```
CREATE INDEX IF NOT EXISTS idx_productos_nombre ON productos(nombre);
```

### Buenas prácticas (CalloutBox: best_practice)
Crea índices solo en columnas que realmente filtras o ordenas con frecuencia.

## Relaciones simples entre tablas
Cuando tienes clientes y pedidos, una tabla puede referenciar a otra.
```
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

## Manejo de errores
Si algo falla, debes poder reaccionar sin romper la app.
```
import sqlite3

try:
    with sqlite3.connect("tienda.db") as conn:
        conn.execute("INSERT INTO clientes (nombre) VALUES (?)", ("Ana",))
except sqlite3.Error as exc:
    print(f"Error de base de datos: {exc}")
```

## Migraciones simples (concepto)
Una **migración** es un cambio controlado en el esquema.
Ejemplo conceptual: agregar una columna nueva sin perder datos.

### Buenas prácticas (CalloutBox: best_practice)
Guarda un historial de cambios del esquema, aunque sea en un archivo de texto.

## Patrones reales de rendimiento
- Evita hacer una consulta por cada fila (problema N+1).
- Usa transacciones para agrupar muchos INSERT.
- Mantén consultas pequeñas y específicas.

## Más allá (nivel pro)
- Aprende a **analizar planes de consulta** con `EXPLAIN`.
- Considera particionar datos cuando crezcan demasiado.
- Usa pruebas de carga para validar tiempos reales.


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
                "No usar índices",
                "Sin índices, las búsquedas pueden volverse muy lentas.",
            ),
            (
                "Olvidar habilitar claves foráneas",
                "SQLite requiere activar `PRAGMA foreign_keys = ON` en cada conexión.",
            ),
            (
                "Usar una consulta por elemento",
                "El patrón N+1 degrada mucho el rendimiento.",
            ),
            (
                "No capturar errores",
                "Los errores sin manejo pueden romper la app completa.",
            ),
            (
                "Migrar manualmente sin registro",
                "Sin historial, es difícil reproducir cambios en producción.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Parámetros seguros",
                """import sqlite3

with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        "UPDATE productos SET precio = ? WHERE nombre = ?",  # SQL con placeholders
        (3.0, "Té"),  # Valores separados
    )""",
            ),
            (
                "Crear índices",
                """import sqlite3

with sqlite3.connect("tienda.db") as conn:
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_pedidos_total ON pedidos(total)"  # Índice
    )""",
            ),
            (
                "Transacción para múltiples INSERT",
                """import sqlite3

with sqlite3.connect("tienda.db") as conn:
    conn.execute("BEGIN")  # Iniciamos transacción
    conn.execute("INSERT INTO pedidos (cliente_id, total) VALUES (?, ?)", (1, 10.0))
    conn.execute("INSERT INTO pedidos (cliente_id, total) VALUES (?, ?)", (1, 15.0))
    conn.execute("COMMIT")  # Confirmamos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un índice en la columna email de una tabla usuarios.",
                "hints": ["CREATE INDEX", "IF NOT EXISTS"],
                "solution": "CREATE INDEX IF NOT EXISTS idx_usuarios_email ON usuarios(email)",
            },
            {
                "question": "Escribe una consulta segura que actualice un precio por id.",
                "hints": ["Usa ?"],
                "solution": "conn.execute('UPDATE productos SET precio = ? WHERE id = ?', (9.99, 1))",
            },
            {
                "question": "Define una relación simple entre pedidos y clientes.",
                "hints": ["FOREIGN KEY"],
                "solution": "FOREIGN KEY (cliente_id) REFERENCES clientes(id)",
            },
            {
                "question": "Menciona dos ventajas de usar transacciones en lotes.",
                "hints": ["Consistencia", "Rendimiento"],
                "solution": "Evitan datos parciales y son más rápidas al agrupar operaciones.",
            },
            {
                "question": "¿Qué es una migración y por qué es útil?",
                "hints": ["Cambio de esquema controlado"],
                "solution": "Es un cambio versionado del esquema que permite evolucionar la base sin perder datos.",
            },
        ]
