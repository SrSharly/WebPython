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
