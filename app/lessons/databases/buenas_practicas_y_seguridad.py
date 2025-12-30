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
