from __future__ import annotations

from app.lesson_base import Lesson


class AsyncAwaitLesson(Lesson):
    TITLE = "Async y await"
    CATEGORY = "Python"
    SUBCATEGORY = "Concurrencia"
    LEVEL = "Avanzado"
    BADGES = ["🧠"]
    TAGS = ["async", "await", "asyncio", "corutinas", "event loop"]

    def summary(self) -> str:
        return (
            "Aprende a escribir corutinas con async/await, ejecutar el event loop con "
            "asyncio.run y evitar los errores típicos al olvidar await."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
🧠 LECCIÓN PRO

## Introducción: qué resuelve async/await
`async` y `await` permiten escribir tareas que **ceden el control** mientras esperan. En lugar de
bloquear el programa, cooperan con el **event loop** para ejecutar otras tareas mientras tanto.

## Paso 1: declarar una corutina con async def
Una corutina es una función que se puede pausar y reanudar. Se declara con `async def`.

**Micro-ejemplo correcto**
```py
import asyncio

async def obtener_estado():
    await asyncio.sleep(0.1)
    return "ok"
```

**Micro-ejemplo incorrecto**
```py
def obtener_estado():
    await asyncio.sleep(0.1)
```

**Error real**
```py
SyntaxError: 'await' outside async function
```

**Cómo se arregla**
Declara la función con `async def` cuando uses `await` dentro.

## Paso 2: usar await para ceder el control
`await` suspende la corutina hasta que termina la operación async.

**Micro-ejemplo correcto**
```py
import asyncio

async def esperar():
    await asyncio.sleep(1)
```

**Micro-ejemplo incorrecto**
```py
import asyncio

async def esperar():
    asyncio.sleep(1)
```

**Error real**
```py
RuntimeWarning: coroutine 'sleep' was never awaited
```

**Cómo se arregla**
Agrega `await` para ejecutar la corutina.

## Paso 3: ejecutar corutinas con asyncio.run
Las corutinas no se ejecutan solas. Se lanzan con `asyncio.run(...)`.

**Micro-ejemplo correcto**
```py
import asyncio

async def main():
    await asyncio.sleep(0.1)

asyncio.run(main())
```

**Micro-ejemplo incorrecto**
```py
async def main():
    return 1

main()
```

**Error real**
```py
RuntimeWarning: coroutine 'main' was never awaited
```

**Cómo se arregla**
Usa `asyncio.run(main())` desde código síncrono.

## Ejemplo principal: una tarea async con espera real
### 1) Aprende esto
Modelar tareas que esperan sin bloquear el programa.

### 2) Haz esto
```py
import asyncio

async def preparar_pedido(nombre):
    print(f"Preparando {nombre}")
    await asyncio.sleep(1)
    print(f"Listo {nombre}")
    return nombre

async def main():
    resultado = await preparar_pedido("café")
    print(f"Entregado: {resultado}")

asyncio.run(main())
```

### 3) Verás esto
```text
Preparando café
Listo café
Entregado: café
```

### 4) Por qué funciona
`asyncio.run` crea el event loop, ejecuta `main` y espera a que la corutina termine.
`await asyncio.sleep(1)` libera el loop durante la espera.

### 5) Lo típico que sale mal
1) Olvidar `await`:
```py
async def main():
    preparar_pedido("café")
```
```py
RuntimeWarning: coroutine 'preparar_pedido' was never awaited
```

2) Llamar `asyncio.run` dentro de un loop ya activo (por ejemplo, un notebook):
```py
asyncio.run(main())
```
```py
RuntimeError: asyncio.run() cannot be called from a running event loop
```

Solución: en un notebook usa `await main()` directamente.

## Errores típicos rápidos
- Mezclar `time.sleep` dentro de corutinas y bloquear el event loop.
- Asumir que `async` crea paralelismo real: solo coopera, no usa hilos por defecto.

## Ejercicios
1) Crea una corutina `saludar_async` que espere 0.2 segundos y devuelva un saludo.
2) Ejecuta la corutina con `asyncio.run` y muestra el resultado.
3) Provoca el error de "coroutine was never awaited" y corrígelo.

## Checklist final
- [ ] Declaro corutinas con `async def`.
- [ ] Uso `await` al llamar corutinas.
- [ ] Ejecuto desde código síncrono con `asyncio.run`.
"""
