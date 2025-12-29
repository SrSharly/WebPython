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
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
        """
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
