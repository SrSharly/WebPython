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
