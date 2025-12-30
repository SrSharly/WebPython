from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class RedshiftConSQLAlchemyLesson(Lesson):
    TITLE = "Redshift con SQLAlchemy"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Redshift"
    LEVEL = "Intermedio"
    TAGS = ["redshift", "sqlalchemy", "warehouse", "dsn", "analytics"]

    def summary(self) -> str:
        return (
            "Conecta Redshift con SQLAlchemy paso a paso: URL de conexión, "
            "credenciales seguras, consultas analíticas y buenas prácticas."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es Amazon Redshift? (5 líneas)
Redshift es un **warehouse** (almacén de datos) en la nube de AWS. Está optimizado para
consultas analíticas grandes, no para transacciones pequeñas. Se usa cuando necesitas
agrupar millones de filas, generar reportes o alimentar dashboards.

## Cuándo usarlo
- Analítica y reporting.
- Grandes volúmenes de datos históricos.
- Consultas agregadas complejas.

## Conceptos desde cero
- **DSN / URL de conexión**: cadena que describe cómo conectarte (host, puerto, dbname).
- **Credenciales**: usuario y contraseña necesarios para autenticarse.
- **Pool**: conjunto de conexiones reutilizables para evitar abrir una nueva cada vez.

### Buenas prácticas (CalloutBox: best_practice)
- Usa variables de entorno para credenciales.
- Aplica mínimo privilegio.
- Configura timeouts y reintentos.

## Opción A (preferida): redshift-connector + SQLAlchemy
```
pip install sqlalchemy redshift-connector
```

### URL de conexión paso a paso
Partes básicas:
- **host**: endpoint del cluster.
- **puerto**: normalmente 5439.
- **dbname**: base de datos dentro de Redshift.
- **user** y **password**: credenciales.

Ejemplo (no real, solo formato):
```
redshift+redshift_connector://usuario:password@host:5439/analytics
```

### Usar variables de entorno (seguro)
```
import os

usuario = os.environ.get("REDSHIFT_USER")
password = os.environ.get("REDSHIFT_PASSWORD")
host = os.environ.get("REDSHIFT_HOST")
puerto = os.environ.get("REDSHIFT_PORT", "5439")
dbname = os.environ.get("REDSHIFT_DBNAME")

url = f"redshift+redshift_connector://{usuario}:{password}@{host}:{puerto}/{dbname}"
```

## Opción B: psycopg / psycopg2 (si ya la usas)
Puedes usar el dialecto de SQLAlchemy con psycopg si tu stack ya lo incluye.

## Consultas analíticas típicas
```
SELECT region, SUM(ventas) AS total
FROM ventas_diarias
GROUP BY region
ORDER BY total DESC
LIMIT 10;
```

## Paginación básica
```
SELECT * FROM ventas_diarias
ORDER BY fecha DESC
LIMIT 100 OFFSET 0;
```

## Más allá (nivel pro)
- Usa IAM o Secrets Manager para gestionar credenciales.
- Añade `statement_timeout` para evitar consultas eternas.
- Ajusta pooling y retries según la carga.


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
                "Hardcodear credenciales",
                "Riesgo de seguridad. Usa variables de entorno.",
            ),
            (
                "No usar SSL",
                "Puede exponer datos en tránsito.",
            ),
            (
                "Omitir LIMIT",
                "Consultas sin límite pueden ser costosas.",
            ),
            (
                "No configurar timeouts",
                "Consultas largas bloquean recursos.",
            ),
            (
                "Olvidar permisos mínimos",
                "Aumenta el impacto de errores o fugas.",
            ),
            (
                "Pool mal dimensionado",
                "Demasiadas conexiones pueden saturar el cluster.",
            ),
            (
                "No manejar retries",
                "Fallos temporales dejan procesos incompletos.",
            ),
            (
                "Confundir Redshift con OLTP",
                "No está pensado para transacciones rápidas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Construir URL con variables",
                """import os  # Importamos os\nusuario = os.environ.get(\"REDSHIFT_USER\")  # Usuario\npassword = os.environ.get(\"REDSHIFT_PASSWORD\")  # Password\nhost = os.environ.get(\"REDSHIFT_HOST\")  # Host\npuerto = os.environ.get(\"REDSHIFT_PORT\", \"5439\")  # Puerto\ndbname = os.environ.get(\"REDSHIFT_DBNAME\")  # DB\nurl = f\"redshift+redshift_connector://{usuario}:{password}@{host}:{puerto}/{dbname}\"  # URL""",
            ),
            (
                "Crear engine",
                """from sqlalchemy import create_engine  # Importamos create_engine\nengine = create_engine(url, pool_size=5, max_overflow=2)  # Creamos engine""",
            ),
            (
                "Consulta analítica",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Abrimos conexión\n    result = conn.execute(text(\"SELECT region, SUM(ventas) AS total FROM ventas_diarias GROUP BY region\"))  # Ejecutamos\n    for fila in result:  # Iteramos\n        print(fila)  # Mostramos""",
            ),
            (
                "Consulta con LIMIT",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Conexión\n    result = conn.execute(text(\"SELECT * FROM ventas_diarias ORDER BY fecha DESC LIMIT 100\"))  # Ejecutamos\n    print(result.fetchall())  # Leemos filas""",
            ),
            (
                "Paginación con OFFSET",
                """from sqlalchemy import text  # Importamos text\nwith engine.connect() as conn:  # Conexión\n    result = conn.execute(text(\"SELECT * FROM ventas_diarias ORDER BY fecha DESC LIMIT 100 OFFSET 100\"))  # Ejecutamos\n    print(result.fetchall())  # Leemos""",
            ),
            (
                "Timeout en la conexión",
                """from sqlalchemy import create_engine  # Importamos create_engine\nengine = create_engine(url, connect_args={\"connect_timeout\": 10})  # Timeout""",
            ),
            (
                "Retry simple",
                """from sqlalchemy import text  # Importamos text\nintentos = 3  # Número de intentos\nwhile intentos > 0:  # Bucle\n    try:  # Intentamos\n        with engine.connect() as conn:  # Conectamos\n            conn.execute(text(\"SELECT 1\"))  # Consulta simple\n        break  # Salimos si ok\n    except Exception:  # Si falla\n        intentos -= 1  # Reducimos""",
            ),
            (
                "URL con psycopg",
                """url = \"redshift+psycopg://usuario:password@host:5439/analytics\"  # URL con psycopg""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Construye una URL de Redshift usando variables de entorno.",
                "hints": ["REDSHIFT_USER", "REDSHIFT_HOST"],
                "solution": "url = f'redshift+redshift_connector://{usuario}:{password}@{host}:{puerto}/{dbname}'",
            },
            {
                "question": "Crea un engine con pool_size=3.",
                "hints": ["create_engine"],
                "solution": "engine = create_engine(url, pool_size=3)",
            },
            {
                "question": "Escribe una consulta con LIMIT 50.",
                "hints": ["LIMIT"],
                "solution": "SELECT * FROM tabla LIMIT 50",
            },
            {
                "question": "¿Qué práctica evita hardcodear credenciales?",
                "hints": ["variables de entorno"],
                "solution": "Usar variables de entorno o Secrets Manager.",
            },
            {
                "question": "Menciona una razón para usar Redshift.",
                "hints": ["analítica", "reporting"],
                "solution": "Para consultas analíticas grandes y reportes.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["sqlalchemy", "redshift-connector"]

    def build_demo(self) -> QWidget | None:
        ok_sqlalchemy, _, msg_sqlalchemy = optional_import("sqlalchemy")
        ok_redshift, _, msg_redshift = optional_import("redshift_connector")
        if not ok_sqlalchemy:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(msg_sqlalchemy or "SQLAlchemy no disponible."))
            layout.addWidget(QLabel("Instala dependencias con: pip install sqlalchemy redshift-connector"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        if not ok_redshift:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(msg_redshift or "redshift-connector no disponible."))
            layout.addWidget(QLabel("Si usas psycopg/psycopg2 puedes ignorar este aviso."))
            layout.addWidget(QLabel("Instala con: pip install redshift-connector"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo simulada: construye una URL segura (no conecta)."))

        form = QFormLayout()
        host_input = QLineEdit()
        port_input = QLineEdit("5439")
        dbname_input = QLineEdit()
        user_input = QLineEdit()
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        form.addRow("Host:", host_input)
        form.addRow("Puerto:", port_input)
        form.addRow("DB name:", dbname_input)
        form.addRow("Usuario:", user_input)
        form.addRow("Password:", password_input)
        layout.addLayout(form)

        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output)

        build_button = QPushButton("Construir URL")
        layout.addWidget(build_button)

        def _build_url() -> None:
            host = host_input.text().strip()
            port = port_input.text().strip()
            dbname = dbname_input.text().strip()
            user = user_input.text().strip()
            password = password_input.text().strip()
            output.clear()
            if not all([host, port, dbname, user, password]):
                output.append("Completa todos los campos para construir la URL.")
                output.append("Ejemplo seguro:")
                output.append("redshift+redshift_connector://usuario:********@host:5439/analytics")
                return
            masked_password = "*" * len(password)
            url = f"redshift+redshift_connector://{user}:{masked_password}@{host}:{port}/{dbname}"
            output.append("URL construida (password oculto):")
            output.append(url)

        build_button.clicked.connect(_build_url)
        return widget
