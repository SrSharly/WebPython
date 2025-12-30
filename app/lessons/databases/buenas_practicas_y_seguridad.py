from __future__ import annotations

from app.lesson_base import Lesson


class BuenasPracticasSeguridadLesson(Lesson):
    TITLE = "Buenas prácticas y seguridad"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Profesional"
    LEVEL = "Intermedio"
    TAGS = ["seguridad", "sql-injection", "logging", "backups", "patrones"]

    def summary(self) -> str:
        return (
            "Aprende a proteger tus bases de datos: SQL injection, variables de entorno, "
            "errores, logging, backups y separación de capas."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Por qué la seguridad importa?
Una base de datos contiene información crítica. Un error de seguridad puede exponer datos personales.

## Conceptos base
- **Conexión**: canal seguro con la base.
- **Consulta**: instrucción SQL para leer o escribir.
- **Transacción**: conjunto de cambios confirmados juntos.

## SQL Injection explicado desde cero
SQL injection ocurre cuando un atacante logra **alterar tu consulta**.
Ejemplo inseguro:
```
consulta = f"SELECT * FROM usuarios WHERE email = '{email}'"  # Inseguro
```
Ejemplo seguro:
```
consulta = "SELECT * FROM usuarios WHERE email = ?"
```

### Buenas prácticas (CalloutBox: best_practice)
Nunca construyas SQL con strings. Usa parámetros siempre.

## Variables de entorno
Las credenciales no deben estar en el código.
Usa una **variable** de entorno para `DB_USER`, `DB_PASSWORD`, etc.

### Buenas prácticas (CalloutBox: best_practice)
Si compartes el proyecto, entrega un archivo `.env.example` sin credenciales reales.

## Gestión de errores
No expongas errores crudos al usuario.
Registra el error completo solo en el servidor.

## Logging
El logging te ayuda a detectar fallas y patrones sospechosos.
Registra: hora, acción, usuario y error.

## Backups
Sin backups, un error puede ser fatal.
Define un calendario: diario, semanal o según el negocio.

## Separación de capas (repo pattern)
Separa la lógica de datos en un **repositorio**.
Así cambias la base sin tocar la lógica del negocio.

### Buenas prácticas (CalloutBox: best_practice)
Crea una interfaz única para consultas; evita SQL repartido por todo el proyecto.

## Buenas prácticas “nivel pro”
- Rotación de credenciales.
- Encriptación en reposo y en tránsito.
- Auditoría de accesos.

## Más allá (nivel pro)
- Usa herramientas de migración (Alembic, Flyway).
- Implementa tests de integración para la capa de datos.
- Monitorea tiempos de respuesta y consultas lentas.


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
                "Guardar contraseñas en el código",
                "Usa variables de entorno o gestores de secretos.",
            ),
            (
                "Mostrar errores internos al usuario",
                "Puede revelar estructura de la base o credenciales.",
            ),
            (
                "No tener backups",
                "Los datos se pueden perder por error humano o fallos.",
            ),
            (
                "No validar inputs",
                "Inputs sin validación facilitan ataques.",
            ),
            (
                "SQL en todas partes",
                "Es difícil de mantener y aumenta el riesgo de errores.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Consulta insegura vs segura",
                """# Inseguro: concatena strings
consulta = f"SELECT * FROM usuarios WHERE email = '{email}'"  # Riesgo

# Seguro: usa parámetros
consulta = "SELECT * FROM usuarios WHERE email = ?"  # Parámetro""",
            ),
            (
                "Variables de entorno",
                """import os

usuario = os.getenv("DB_USER")  # Usuario desde entorno
password = os.getenv("DB_PASSWORD")  # Password desde entorno""",
            ),
            (
                "Separación de capas",
                """class UsuarioRepository:
    def __init__(self, conn):
        self.conn = conn  # Guardamos conexión

    def obtener_por_email(self, email):
        return self.conn.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,),
        )""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Explica qué es SQL injection.",
                "hints": ["Alterar consultas"],
                "solution": "Es cuando un atacante modifica una consulta SQL para acceder o cambiar datos.",
            },
            {
                "question": "Da un ejemplo de consulta segura con parámetros.",
                "hints": ["WHERE email = ?"],
                "solution": "conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,))",
            },
            {
                "question": "¿Por qué no debes hardcodear credenciales?",
                "hints": ["Seguridad"],
                "solution": "Porque se pueden filtrar en repositorios o logs.",
            },
            {
                "question": "Menciona dos elementos clave de un plan de backups.",
                "hints": ["Frecuencia", "Restauración"],
                "solution": "Definir frecuencia de copias y probar restauraciones.",
            },
            {
                "question": "¿Qué es el patrón repositorio?",
                "hints": ["Separar lógica"],
                "solution": "Una capa que centraliza el acceso a datos y separa la lógica de negocio.",
            },
        ]
