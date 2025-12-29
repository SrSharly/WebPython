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
