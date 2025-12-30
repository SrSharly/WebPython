from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class PostgreSQLPythonLesson(Lesson):
    TITLE = "PostgreSQL con Python (psycopg / asyncpg)"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Relacionales"
    LEVEL = "Intermedio"
    TAGS = ["postgresql", "psycopg", "asyncpg", "sql", "seguridad"]

    def summary(self) -> str:
        return (
            "Conoce PostgreSQL, cuándo usarlo y cómo conectarte desde Python con psycopg. "
            "Incluye consultas básicas y seguridad contra SQL injection."
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

## ¿Qué es PostgreSQL y cuándo usarlo?
PostgreSQL es una base de datos **robusta y escalable**. Es ideal para aplicaciones con muchos usuarios,
consultas complejas y necesidad de consistencia.

## Conceptos base
- **Conexión**: canal con el servidor PostgreSQL.
- **Consulta**: instrucción SQL para leer o escribir datos.
- **Transacción**: bloque de cambios que se confirman juntos.

### Buenas prácticas (CalloutBox: best_practice)
Usa un usuario con permisos mínimos para cada aplicación.

## Conexión con psycopg
```
import psycopg

conn = psycopg.connect(
    "host=localhost dbname=tienda user=app password=secreto"
)
```

## Consultas básicas
```
with conn.cursor() as cur:
    cur.execute("SELECT id, nombre FROM clientes WHERE activo = %s", (True,))
    filas = cur.fetchall()
    print(filas)
```

## ¿Qué es un pool de conexiones?
Un **pool** mantiene conexiones abiertas para reutilizarlas.
Esto reduce el tiempo de espera cuando hay muchas peticiones.

## Seguridad: SQL injection
Nunca concatenes strings con datos del usuario.
Usa parámetros (`%s`) para separar SQL y datos.
Un **parámetro** mantiene la consulta segura.

### Buenas prácticas (CalloutBox: best_practice)
- Valida entradas del usuario.
- Usa parámetros siempre.
- Registra errores sin exponer datos sensibles.

## ¿Y asyncpg?
`asyncpg` es una opción asíncrona ideal para APIs modernas. El concepto es el mismo:
conectar, consultar y confirmar transacciones.

## Más allá (nivel pro)
- Aprende a crear **índices** compuestos.
- Usa `EXPLAIN ANALYZE` para medir rendimiento.
- Considera particionar tablas grandes.


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
                "Conectar con credenciales en texto plano",
                "Usa variables de entorno o un gestor de secretos.",
            ),
            (
                "No cerrar la conexión",
                "Las conexiones abiertas consumen recursos en el servidor.",
            ),
            (
                "Concatenar SQL",
                "Esto abre la puerta a SQL injection.",
            ),
            (
                "No usar transacciones",
                "Puedes dejar datos a medias si algo falla.",
            ),
            (
                "Ignorar el pool",
                "Sin pool, cada request abre conexión y se vuelve lento.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Conexión y consulta segura",
                """import psycopg

conn = psycopg.connect("host=localhost dbname=tienda user=app password=secreto")
with conn.cursor() as cur:
    cur.execute("SELECT id, nombre FROM clientes WHERE activo = %s", (True,))  # Parámetro seguro
    print(cur.fetchall())  # Resultado""",
            ),
            (
                "Transacción explícita",
                """import psycopg

conn = psycopg.connect("host=localhost dbname=tienda user=app password=secreto")
with conn.cursor() as cur:
    cur.execute("BEGIN")  # Inicia transacción
    cur.execute("UPDATE cuentas SET saldo = saldo - %s WHERE id = %s", (50, 1))
    cur.execute("UPDATE cuentas SET saldo = saldo + %s WHERE id = %s", (50, 2))
    cur.execute("COMMIT")  # Confirma""",
            ),
            (
                "Pool de conexiones (concepto)",
                """# En proyectos reales, configura un pool para reutilizar conexiones.
# Un pool evita abrir/cerrar conexiones por cada request.""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Explica cuándo preferirías PostgreSQL sobre SQLite.",
                "hints": ["Usuarios concurrentes", "Escalabilidad"],
                "solution": "Cuando hay muchos usuarios, consultas complejas o necesidad de escalado.",
            },
            {
                "question": "Escribe un SELECT con parámetros para filtrar por email.",
                "hints": ["WHERE email = %s"],
                "solution": "cur.execute('SELECT * FROM usuarios WHERE email = %s', (correo,))",
            },
            {
                "question": "¿Qué es un pool de conexiones?",
                "hints": ["Reutilizar conexiones"],
                "solution": "Es un conjunto de conexiones abiertas que se reutilizan para mejorar rendimiento.",
            },
            {
                "question": "Da un ejemplo de SQL injection que evitarías con parámetros.",
                "hints": ["' OR 1=1"],
                "solution": "Ejemplo: email = 'x' OR 1=1. Con parámetros se evita.",
            },
            {
                "question": "Menciona dos buenas prácticas de seguridad en PostgreSQL.",
                "hints": ["Usuarios mínimos", "No exponer errores"],
                "solution": "Usar usuarios con permisos mínimos y no exponer datos sensibles en logs.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["psycopg"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("psycopg")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "psycopg no disponible."))
            layout.addWidget(QLabel("Instala psycopg con: pip install psycopg"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("psycopg disponible. Revisa los ejemplos en la guía."))
        return widget
