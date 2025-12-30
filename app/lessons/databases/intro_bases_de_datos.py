from __future__ import annotations

from app.lesson_base import Lesson


class IntroBasesDeDatosLesson(Lesson):
    TITLE = "¿Qué es una base de datos?"
    CATEGORY = "Bases de datos"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = [
        "bases-de-datos",
        "sql",
        "nosql",
        "persistencia",
        "conceptos",
    ]

    def summary(self) -> str:
        return (
            "Entiende desde cero qué es una base de datos, cómo se organiza la información "
            "y por qué la persistencia es clave en aplicaciones reales."
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

## Idea central
Una **base de datos** es un sistema diseñado para **guardar, organizar y recuperar información** de forma confiable.
Piensa en ella como una biblioteca: si los libros no están ordenados, encontrarlos sería lento o imposible.

## ¿Qué significa persistencia?
**Persistencia** es la capacidad de que los datos **no se pierdan** al cerrar la app o apagar el equipo.
Si guardas un contacto, lo quieres ver mañana: eso es persistencia.

## Tablas, filas y columnas (con analogías)
- **Tabla**: una hoja de cálculo o una ficha de archivo físico.
- **Fila**: un registro completo (por ejemplo, un cliente).
- **Columna**: un atributo del registro (por ejemplo, nombre o email).

Ejemplo conceptual: una tabla de clientes tendría columnas como *id*, *nombre* y *email*, y cada fila sería una persona. Puedes pensar cada fila como un **objeto** con atributos.

## ¿Qué es una consulta?
Una **consulta** es una pregunta que haces a la base de datos.
Por ejemplo: “dame los clientes que viven en Lima”.
No necesitas saber SQL aún, solo entender que **consultar = pedir información**.

## ¿Qué es una conexión?
Una **conexión** es el canal por el cual tu programa habla con la base de datos.
Sin conexión, la base de datos no sabe que existes.

## ¿Qué es una transacción?
Una **transacción** es un conjunto de cambios que se aplican **todos o ninguno**.
Si algo falla en medio, se hace *rollback* y nada se guarda.

### Buenas prácticas (CalloutBox: best_practice)
Define desde el inicio **qué datos realmente necesitas**. Guardar “todo por si acaso” complica la app y la hace más lenta.

## SQL vs NoSQL (cuándo usar cada uno)
- **SQL** (relacional): ideal cuando necesitas relaciones claras, reportes y reglas estrictas.
- **NoSQL**: útil para documentos flexibles, datos cambiantes o escalado horizontal.

### Regla simple
Si necesitas **consistencia y relaciones**, empieza con SQL. Si tus datos son muy flexibles, evalúa NoSQL.

## Errores comunes de principiantes
- Crear tablas sin pensar en el futuro.
- Guardar datos duplicados porque “es más rápido”.
- No respaldar la información.
- Confiar en que la app nunca fallará.

### Buenas prácticas básicas (CalloutBox: best_practice)
- Escribe nombres claros para tablas y columnas.
- Mantén datos consistentes (por ejemplo, mismos formatos de fecha).
- Guarda claves únicas para identificar registros.

## Más allá (nivel pro)
- Modela datos con **normalización** para reducir duplicados.
- Aprende sobre **índices** para acelerar consultas.
- Considera **migraciones** cuando el esquema cambia.
- Diseña pensando en **seguridad** y acceso mínimo.


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
                "Creer que una base de datos es solo un archivo",
                "Aunque pueda verse como archivo, también incluye reglas, índices y seguridad.",
            ),
            (
                "Confundir tabla con hoja de cálculo",
                "Las tablas tienen reglas estrictas: tipos, claves y relaciones.",
            ),
            (
                "No pensar en la persistencia",
                "Si no guardas de forma persistente, perderás datos al cerrar la app.",
            ),
            (
                "Usar NoSQL sin necesidad",
                "Si necesitas relaciones fuertes, SQL suele ser más simple y seguro.",
            ),
            (
                "Ignorar las copias de seguridad",
                "Los backups no son opcionales: fallos ocurren.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Ejemplo conceptual: tabla de clientes",
                """# Tabla: clientes (concepto)
# Columnas: id, nombre, email
# Fila 1: id=1, nombre="Ana", email="ana@correo.com"
# Fila 2: id=2, nombre="Luis", email="luis@correo.com""",
            ),
            (
                "Ejemplo conceptual: consulta",
                """# Consulta (concepto): "dame clientes de Lima"
# Resultado: filas que cumplen la condición""",
            ),
            (
                "Ejemplo conceptual: transacción",
                """# Transacción (concepto)
# Paso 1: guardar compra
# Paso 2: reducir stock
# Si falla el paso 2, se revierte el paso 1""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Describe con tus palabras qué es persistencia y da un ejemplo.",
                "hints": ["Piensa en guardar y recuperar mañana"],
                "solution": "Persistencia es conservar datos aunque la app se cierre. Ejemplo: guardar un contacto.",
            },
            {
                "question": "Explica la diferencia entre tabla, fila y columna con una analogía.",
                "hints": ["Hoja de cálculo o biblioteca"],
                "solution": "Tabla es la hoja, fila es un registro, columna es un atributo como nombre.",
            },
            {
                "question": "¿Qué es una consulta en una base de datos?",
                "hints": ["Es una pregunta"],
                "solution": "Es una pregunta para recuperar o filtrar datos.",
            },
            {
                "question": "Menciona dos casos donde prefieras SQL en lugar de NoSQL.",
                "hints": ["Relaciones y consistencia"],
                "solution": "Cuando hay relaciones fuertes entre tablas o se necesita consistencia estricta.",
            },
            {
                "question": "Lista tres errores comunes de principiantes.",
                "hints": ["Duplicar datos, sin backups"],
                "solution": "Duplicar datos, no hacer backups, no planear el esquema.",
            },
        ]
