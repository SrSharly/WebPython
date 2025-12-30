from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class AsyncAwaitLesson(Lesson):
    TITLE = "Async / await"
    CATEGORY = "Python"
    SUBCATEGORY = "Avanzado"
    LEVEL = "Avanzado"
    BADGES = ["🧠"]
    TAGS = ["async", "await", "asyncio", "corutinas"]

    def summary(self) -> str:
        return (
            "Aprende a usar async/await para tareas concurrentes, entender el event loop y evitar "
            "errores típicos al mezclar funciones síncronas con corutinas."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: concurrencia sin hilos
`async` y `await` te permiten pausar y reanudar tareas sin bloquear el programa. Esto es ideal para operaciones lentas
como esperar respuestas o temporizadores. En Python, la concurrencia se coordina con el **event loop** de `asyncio`.

## Conceptos clave (micro-ejemplos)
**Corutina**: función declarada con `async def` que puede pausarse.

**Así se escribe**
```py
async def cargar_datos():
    return "ok"
```

**Error típico (❌)**
```py
async def cargar_datos()
    return "ok"
```

**Qué significa el error**
`SyntaxError` porque falta el `:` al final de la definición.

**Cómo se arregla**
Agrega el `:` y mantén la indentación del bloque.

**Event loop**: motor que programa la ejecución de corutinas.

**Así se escribe**
```py
import asyncio

async def main():
    return "listo"

resultado = asyncio.run(main())
```

**Error típico (❌)**
```py
import asyncio

async def main():
    return "listo"

resultado = asyncio.run(main)
```

**Qué significa el error**
`TypeError` porque `asyncio.run` espera una corutina, no la función sin llamar.

**Cómo se arregla**
Llama a la función: `asyncio.run(main())`.

## Paso 1: usar await dentro de async
`await` solo funciona dentro de una corutina. Sirve para pausar mientras otra tarea termina.

**Así se escribe**
```py
import asyncio

async def esperar():
    await asyncio.sleep(1)
    return "hecho"
```

**Error típico (❌)**
```py
import asyncio

def esperar():
    await asyncio.sleep(1)
```

**Qué significa el error**
`SyntaxError: 'await' outside async function` porque `await` requiere `async def`.

**Cómo se arregla**
Convierte la función en corutina con `async def`.

## Paso 2: ejemplo grande con contexto
**Aprende esto:** ejecutar dos tareas de forma concurrente y recoger resultados sin bloquear.

**Haz esto (ejemplo completo con contexto):**
```py
import asyncio

async def descargar(nombre, demora):
    print(f"Inicio {nombre}")
    await asyncio.sleep(demora)
    print(f"Fin {nombre}")
    return f"{nombre} listo"

async def main():
    tarea_a = asyncio.create_task(descargar("A", 1))
    tarea_b = asyncio.create_task(descargar("B", 2))
    resultados = await asyncio.gather(tarea_a, tarea_b)
    print("Resultados:", resultados)

asyncio.run(main())
```

**Verás esto (salida real):**
```
Inicio A
Inicio B
Fin A
Fin B
Resultados: ['A listo', 'B listo']
```

**Por qué funciona:** `create_task` registra corutinas en el event loop, `await asyncio.gather` espera a que terminen y
`asyncio.run` ejecuta el loop principal.

**Lo típico que sale mal (con error real):**
```py
import asyncio

def descargar():
    return "listo"

async def main():
    await descargar()

asyncio.run(main())
```

```
TypeError: object str can't be used in 'await' expression
```

Solución: `await` solo acepta corutinas o awaitables. Convierte `descargar` en `async def` o no uses `await`.

## Resumen rápido
- Declara corutinas con `async def`.
- Usa `await` solo dentro de corutinas.
- Ejecuta el flujo con `asyncio.run`.
- El event loop coordina la concurrencia sin bloquear el programa.
"""

    def practice(self) -> str:
        return """
1) Crea una corutina que espere 0.5 segundos con `asyncio.sleep` y devuelva un mensaje.
2) Lanza dos corutinas con `asyncio.gather` y observa el orden de salida.
3) Provoca el error de `await` fuera de `async` y corrígelo.
"""

    def get_widget(self) -> QWidget:
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Aprende async/await con ejemplos claros y errores típicos."))
        container = QWidget()
        container.setLayout(layout)
        return container
