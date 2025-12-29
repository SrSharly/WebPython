from __future__ import annotations

import sqlite3

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class SQLiteDesdeCeroLesson(Lesson):
    TITLE = "SQLite desde cero"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "SQLite"
    LEVEL = "Básico"
    TAGS = ["sqlite", "sqlite3", "sql", "crud", "transacciones", "cursor"]

    def summary(self) -> str:
        return (
            "Crea tu primera base de datos SQLite desde cero: conexión, tablas, "
            "CRUD, parámetros seguros y transacciones con ejemplos guiados."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Objetivo
Vamos a construir una mini base de datos con SQLite desde cero: conectar, crear una tabla, insertar,
consultar, actualizar y borrar datos con seguridad.

## ¿Qué es SQLite?
SQLite es una base de datos ligera que vive en un archivo local (o en memoria). No necesitas
servidor y es perfecta para aprender.

## Conceptos base (definidos desde cero)
- **Conexión**: canal abierto hacia la base de datos.
- **Cursor**: objeto que recorre los resultados de una consulta.
- **Transacción**: grupo de cambios que se confirman juntos con `commit` o se revierten con `rollback`.

### Buenas prácticas (CalloutBox: best_practice)
- Usa parámetros `?` para evitar **SQL injection**.
- Abre conexiones con `with` para cerrar automáticamente.
- Haz commits explícitos cuando quieras guardar cambios.

## Paso 1: Conectar a SQLite
```
import sqlite3  # Importamos sqlite3

with sqlite3.connect("agenda.db") as conn:  # Abrimos la conexión
    print("Conexión lista")  # Confirmamos
```

## Paso 2: Crear una tabla
```
import sqlite3  # Módulo estándar

with sqlite3.connect("agenda.db") as conn:  # Conexión
    conn.execute(  # Ejecutamos SQL
        '''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL
        )
        '''
    )
```

## Paso 3: Insertar datos con parámetros seguros
Los **parámetros** evitan que un texto malicioso se convierta en SQL. **SQL injection** es un
ataque donde alguien intenta inyectar código SQL dentro de un campo de entrada.
```
import sqlite3

with sqlite3.connect("agenda.db") as conn:
    conn.execute(
        "INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",
        ("Ana", "555-123"),
    )
```

## Paso 4: Leer datos con cursor
Un **cursor** recorre las filas resultado.
```
import sqlite3

with sqlite3.connect("agenda.db") as conn:
    cursor = conn.execute("SELECT id, nombre, telefono FROM contactos")
    for fila in cursor:
        print(fila)
```

## Paso 5: Actualizar datos
```
import sqlite3

with sqlite3.connect("agenda.db") as conn:
    conn.execute(
        "UPDATE contactos SET telefono = ? WHERE nombre = ?",
        ("555-999", "Ana"),
    )
```

## Paso 6: Borrar datos
```
import sqlite3

with sqlite3.connect("agenda.db") as conn:
    conn.execute("DELETE FROM contactos WHERE nombre = ?", ("Ana",))
```

## Transacciones desde cero
Una **transacción** junta varios cambios. Si algo falla, puedes revertir con `rollback`.
```
import sqlite3

conn = sqlite3.connect("agenda.db")  # Conexión manual
try:
    conn.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", ("Luis", "111"))
    conn.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", ("Marta", "222"))
    conn.commit()  # Confirmamos
except Exception:
    conn.rollback()  # Revertimos
finally:
    conn.close()  # Cerramos
```

## Context manager con `with`
`with` cierra la conexión incluso si ocurre un error.
```
import sqlite3

with sqlite3.connect("agenda.db") as conn:
    conn.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", ("Nora", "333"))
```

## Más allá (nivel pro)
- Crea índices para acelerar búsquedas.
- Separa la capa de datos en un módulo propio.
- Agrega validaciones antes de insertar datos.
- Usa backups automáticos del archivo SQLite.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenar SQL con strings",
                "Abre la puerta a SQL injection. Usa parámetros ?.",
            ),
            (
                "Olvidar commit",
                "Sin commit los cambios pueden no guardarse.",
            ),
            (
                "No cerrar la conexión",
                "Deja recursos abiertos y bloquea el archivo.",
            ),
            (
                "Usar tipos incorrectos",
                "Guardas texto donde debía ir un número.",
            ),
            (
                "No manejar errores",
                "Un fallo puede dejar datos a medias sin rollback.",
            ),
            (
                "Crear tablas sin claves",
                "Sin PRIMARY KEY será difícil identificar filas.",
            ),
            (
                "Confundir cursor y conexión",
                "La conexión gestiona la base; el cursor recorre resultados.",
            ),
            (
                "Reutilizar la misma conexión en hilos",
                "SQLite no es seguro para hilos sin configuración.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Conectar con with",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    print(\"Conectado\")  # Mostramos mensaje""",
            ),
            (
                "Crear tabla contactos",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    conn.execute(  # Ejecutamos SQL\n        \"CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT)\"  # Definimos tabla\n    )  # Cerramos ejecución""",
            ),
            (
                "Insertar con parámetros",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    conn.execute(\"INSERT INTO contactos (nombre, telefono) VALUES (?, ?)\", (\"Ana\", \"555-123\"))  # Insertamos""",
            ),
            (
                "Consultar con cursor",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    cursor = conn.execute(\"SELECT nombre, telefono FROM contactos\")  # Ejecutamos SELECT\n    for fila in cursor:  # Iteramos filas\n        print(fila)  # Mostramos cada fila""",
            ),
            (
                "Actualizar un registro",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    conn.execute(\"UPDATE contactos SET telefono = ? WHERE nombre = ?\", (\"555-999\", \"Ana\"))  # Actualizamos""",
            ),
            (
                "Eliminar un registro",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    conn.execute(\"DELETE FROM contactos WHERE nombre = ?\", (\"Ana\",))  # Eliminamos""",
            ),
            (
                "Transacción manual",
                """import sqlite3  # Importamos sqlite3\nconn = sqlite3.connect(\"agenda.db\")  # Abrimos conexión\ntry:  # Iniciamos bloque seguro\n    conn.execute(\"INSERT INTO contactos (nombre, telefono) VALUES (?, ?)\", (\"Luis\", \"111\"))  # Insertamos\n    conn.commit()  # Confirmamos\nexcept Exception:  # Capturamos error\n    conn.rollback()  # Revertimos\nfinally:  # Cerramos siempre\n    conn.close()  # Cerramos conexión""",
            ),
            (
                "Contar filas",
                """import sqlite3  # Importamos sqlite3\nwith sqlite3.connect(\"agenda.db\") as conn:  # Abrimos conexión\n    cursor = conn.execute(\"SELECT COUNT(*) FROM contactos\")  # Contamos filas\n    total = cursor.fetchone()[0]  # Leemos resultado\n    print(total)  # Mostramos total""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una tabla tareas con id y descripcion.",
                "hints": ["INTEGER PRIMARY KEY", "TEXT"],
                "solution": "CREATE TABLE tareas (id INTEGER PRIMARY KEY, descripcion TEXT)",
            },
            {
                "question": "Inserta una tarea llamada 'Comprar pan'.",
                "hints": ["INSERT", "parámetros"],
                "solution": "conn.execute('INSERT INTO tareas (descripcion) VALUES (?)', ('Comprar pan',))",
            },
            {
                "question": "Consulta todas las tareas.",
                "hints": ["SELECT *"],
                "solution": "cursor = conn.execute('SELECT * FROM tareas')",
            },
            {
                "question": "Actualiza la tarea con id=1 a 'Comprar café'.",
                "hints": ["UPDATE", "WHERE"],
                "solution": "conn.execute('UPDATE tareas SET descripcion = ? WHERE id = ?', ('Comprar café', 1))",
            },
            {
                "question": "Elimina la tarea con id=1.",
                "hints": ["DELETE", "WHERE"],
                "solution": "conn.execute('DELETE FROM tareas WHERE id = ?', (1,))",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Agenda en memoria (SQLite :memory:)."))

        form_layout = QHBoxLayout()
        name_input = QLineEdit()
        name_input.setPlaceholderText("Nombre")
        phone_input = QLineEdit()
        phone_input.setPlaceholderText("Teléfono")
        form_layout.addWidget(name_input)
        form_layout.addWidget(phone_input)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        add_button = QPushButton("Agregar")
        list_button = QPushButton("Listar")
        clear_button = QPushButton("Limpiar salida")
        button_layout.addWidget(add_button)
        button_layout.addWidget(list_button)
        button_layout.addWidget(clear_button)
        layout.addLayout(button_layout)

        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output)

        conn = sqlite3.connect(":memory:")
        conn.execute(
            "CREATE TABLE contactos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, telefono TEXT NOT NULL)"
        )

        def _append(text: str) -> None:
            output.append(text)

        def _add_contact() -> None:
            nombre = name_input.text().strip()
            telefono = phone_input.text().strip()
            if not nombre or not telefono:
                _append("Completa nombre y teléfono antes de agregar.")
                return
            try:
                conn.execute(
                    "INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",
                    (nombre, telefono),
                )
                conn.commit()
            except Exception:
                conn.rollback()
                _append("Error al insertar. Intenta de nuevo.")
                return
            _append(f"Agregado: {nombre} - {telefono}")
            name_input.clear()
            phone_input.clear()

        def _list_contacts() -> None:
            cursor = conn.execute("SELECT nombre, telefono FROM contactos ORDER BY nombre")
            filas = cursor.fetchall()
            if not filas:
                _append("Agenda vacía.")
                return
            _append("Contactos:")
            for nombre, telefono in filas:
                _append(f"- {nombre}: {telefono}")

        add_button.clicked.connect(_add_contact)
        list_button.clicked.connect(_list_contacts)
        clear_button.clicked.connect(output.clear)

        return widget
