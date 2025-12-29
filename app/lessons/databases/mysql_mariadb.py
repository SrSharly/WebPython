from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class MySQLMariaDBLesson(Lesson):
    TITLE = "MySQL / MariaDB con Python"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Relacionales"
    LEVEL = "Intermedio"
    TAGS = ["mysql", "mariadb", "sql", "conexiones", "crud"]

    def summary(self) -> str:
        return (
            "Aprende a conectar MySQL o MariaDB desde Python, ejecutar consultas básicas "
            "y entender sus diferencias con PostgreSQL."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Diferencias clave con PostgreSQL
- MySQL/MariaDB suele ser más común en hosting tradicional.
- PostgreSQL destaca en funciones avanzadas y consistencia estricta.
Ambas son excelentes opciones, elige según el proyecto.

## Conceptos base
- **Conexión**: canal hacia el servidor.
- **Consulta**: instrucción SQL para leer o escribir.
- **Transacción**: conjunto de cambios confirmados juntos.

### Buenas prácticas (CalloutBox: best_practice)
Nunca guardes credenciales en el código. Usa variables de entorno.

## Conexión con mysql-connector-python
```
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="app",
    password="secreto",
    database="tienda",
)
```

## Consultas básicas
```
cursor = conn.cursor()
cursor.execute("SELECT id, nombre FROM clientes WHERE activo = %s", (1,))
for fila in cursor.fetchall():
    print(fila)
```
Aquí `%s` representa un **parámetro** seguro.

## Inserciones
```
cursor.execute(
    "INSERT INTO clientes (nombre, activo) VALUES (%s, %s)",
    ("Ana", 1),
)
conn.commit()
```

### Buenas prácticas (CalloutBox: best_practice)
Cierra siempre el cursor y la conexión para liberar recursos.

## Más allá (nivel pro)
- Usa pools de conexiones para APIs con alto tráfico.
- Revisa el motor (InnoDB es el estándar recomendado).
- Diseña índices para las consultas más frecuentes.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No llamar a commit",
                "Sin commit, los cambios no se guardan.",
            ),
            (
                "Concatenar SQL",
                "Esto abre la puerta a SQL injection.",
            ),
            (
                "Usar root en producción",
                "Debes usar usuarios con permisos mínimos.",
            ),
            (
                "No cerrar cursores",
                "Deja recursos abiertos y afecta el rendimiento.",
            ),
            (
                "Olvidar configurar el motor",
                "InnoDB es mejor para transacciones y relaciones.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Conectar y consultar",
                """import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="app",
    password="secreto",
    database="tienda",
)
cursor = conn.cursor()  # Creamos cursor
cursor.execute("SELECT id, nombre FROM clientes WHERE activo = %s", (1,))  # Consulta segura
print(cursor.fetchall())  # Mostramos resultados""",
            ),
            (
                "Insertar con commit",
                """import mysql.connector

conn = mysql.connector.connect(host="localhost", user="app", password="secreto", database="tienda")
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO clientes (nombre, activo) VALUES (%s, %s)",
    ("Ana", 1),
)
conn.commit()  # Confirmamos cambios""",
            ),
            (
                "Cerrar recursos",
                """# Después de trabajar
cursor.close()  # Cerramos cursor
conn.close()  # Cerramos conexión""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Conecta a una base llamada tienda usando mysql-connector-python.",
                "hints": ["mysql.connector.connect"],
                "solution": "conn = mysql.connector.connect(host='localhost', user='app', password='secreto', database='tienda')",
            },
            {
                "question": "Escribe un SELECT que filtre por id.",
                "hints": ["WHERE id = %s"],
                "solution": "cursor.execute('SELECT * FROM clientes WHERE id = %s', (1,))",
            },
            {
                "question": "Inserta un cliente llamado 'Luis'.",
                "hints": ["INSERT INTO"],
                "solution": "cursor.execute('INSERT INTO clientes (nombre) VALUES (%s)', ('Luis',))",
            },
            {
                "question": "¿Por qué es importante cerrar conexiones?",
                "hints": ["Recursos"],
                "solution": "Para liberar recursos del servidor y evitar fugas de conexiones.",
            },
            {
                "question": "Menciona una diferencia entre MySQL y PostgreSQL.",
                "hints": ["Funciones avanzadas", "hosting"],
                "solution": "PostgreSQL ofrece funciones avanzadas y consistencia; MySQL es común en hosting tradicional.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["mysql-connector-python"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("mysql.connector")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "mysql-connector-python no disponible."))
            layout.addWidget(QLabel("Instala mysql-connector-python con: pip install mysql-connector-python"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("mysql-connector-python disponible. Revisa los ejemplos en la guía."))
        return widget
