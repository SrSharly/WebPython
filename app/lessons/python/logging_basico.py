from __future__ import annotations

from app.lesson_base import Lesson


class LoggingBasicoLesson(Lesson):
    TITLE = "Logging básico"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas estándar"
    LEVEL = "Intermedio"
    TAGS = ["logging", "logger", "debug", "info", "error"]

    def summary(self) -> str:
        return (
            "Aprende a usar logging para registrar eventos reales, evitar prints perdidos "
            "y diagnosticar problemas con mensajes claros."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## ¿Por qué usar logging?
`logging` es la librería estándar para registrar eventos (información, advertencias y errores).
Te da control sobre el nivel de detalle y sobre el formato de los mensajes.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")
logger.info("Arrancó el proceso")
```

Micro-ejemplo incorrecto:
```py
logger = logging.getLogger("app")
```

Error real:
```py
NameError: name 'logging' is not defined
```

Cómo se arregla: importa `logging` antes de usarlo.

## Niveles de logging (qué se muestra y cuándo)
Cada logger filtra mensajes según su nivel. De menor a mayor severidad:
`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("app")
logger.debug("Detalle útil para depuración")
```

Micro-ejemplo incorrecto:
```py
logger.debig("detalle")
```

Error real:
```py
AttributeError: 'Logger' object has no attribute 'debig'
```

Cómo se arregla: usa el método correcto `logger.debug(...)`.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("app")
logger.info("No se verá")
logger.error("Sí se verá")
```

Micro-ejemplo incorrecto:
```py
logger.warning("texto")
```

Error real:
```py
NameError: name 'logger' is not defined
```

Cómo se arregla: crea el logger con `logging.getLogger(...)` antes de usarlo.

## WARNING vs ERROR (no todo es un fallo crítico)
`WARNING` alerta sobre algo raro pero recuperable. `ERROR` indica fallo real.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")
logger.warning("Respuesta lenta del servicio")
logger.error("No se pudo guardar el pedido")
```

Micro-ejemplo incorrecto:
```py
logger.warn("respuesta lenta")
```

Error real:
```py
AttributeError: 'Logger' object has no attribute 'warn'
```

Cómo se arregla: usa `logger.warning(...)`, no `logger.warn(...)`.

## Formateo perezoso para no gastar CPU de más
Cuando usas `%s` en logging, el formateo se evalúa solo si el mensaje se va a emitir.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")
usuario = "Nora"
logger.info("Usuario activo: %s", usuario)
```

Micro-ejemplo incorrecto:
```py
logger.info("Usuario activo: " + usuario)
```

Error real:
```py
NameError: name 'logger' is not defined
```

Cómo se arregla: define el logger y usa el formato perezoso con `%s`.

## Registrar logs en archivo sin perderlos
Guardar logs en un archivo te permite auditar errores después de que el programa termina.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(levelname)s:%(name)s:%(message)s",
)
logger = logging.getLogger("app")
logger.info("Registro persistente en archivo")
```

Micro-ejemplo incorrecto:
```py
import logging

logging.basicConfig(filename=123)
```

Error real:
```py
TypeError: expected str, bytes or os.PathLike object, not int
```

Cómo se arregla: usa una ruta válida en `filename`, por ejemplo `"app.log"`.

## Ejemplo principal: configurar y registrar eventos reales
### 1) Aprende esto
Registrar eventos útiles y coherentes para entender qué pasó sin leer el código.

### 2) Haz esto
```py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)

logger = logging.getLogger("ventas")
logger.info("Inicio de cálculo")

try:
    total = 120 / 3
    logger.info("Total calculado: %s", total)
except ZeroDivisionError:
    logger.exception("División inválida en cálculo de ventas")
```

### 3) Verás esto
```text
INFO:ventas:Inicio de cálculo
INFO:ventas:Total calculado: 40.0
```

### 4) Por qué funciona
`logging.basicConfig(...)` define nivel y formato. El logger "ventas" hereda esa
configuración y registra mensajes con `info` y `exception`. Cuando ocurre una
excepción, `logger.exception(...)` incluye el traceback automáticamente.

### 5) Lo típico que sale mal
1) Olvidar el import:
```py
logger = logging.getLogger("ventas")
```
```py
NameError: name 'logging' is not defined
```

2) Usar un método mal escrito:
```py
logger.inf("mensaje")
```
```py
AttributeError: 'Logger' object has no attribute 'inf'
```

## logger.exception: úsalo dentro de except
`logger.exception` incluye el traceback **solo** cuando hay una excepción activa.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("app")
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Falló la división")
```

Micro-ejemplo incorrecto:
```py
logger.exception("fallo")
```

Error real:
```py
NameError: name 'logger' is not defined
```

Cómo se arregla: crea el logger y úsalo dentro de un bloque `except`.

## Nota preventiva: basicConfig solo aplica una vez
Si llamas `logging.basicConfig(...)` varias veces, solo la primera tiene efecto.
Si necesitas reconfigurar, hazlo en un punto central del programa.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")
logger.info("Configuración aplicada una vez")
```

Micro-ejemplo incorrecto:
```py
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
```

Error real (no hay excepción, pero hay comportamiento inesperado):
```text
Los mensajes DEBUG no aparecen porque el primer basicConfig ya fijó el nivel.
```

Cómo se arregla: define la configuración una sola vez.

## Evita logs duplicados al añadir handlers repetidos
Si agregas un handler en una función que se llama muchas veces, acabarás con
mensajes repetidos.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("app")
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())
```

Micro-ejemplo incorrecto:
```py
import logging

logger = logging.getLogger("app")
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.StreamHandler())
```

Error real (no hay excepción, pero verás mensajes duplicados):
```text
INFO:app:Mensaje
INFO:app:Mensaje
```

Cómo se arregla: agrega handlers una sola vez o verifica `logger.handlers`.

## Usa un logger por módulo (y evita prints en librerías)
En módulos reutilizables, crea un logger con nombre y deja que la app principal
decida el nivel y el formato.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("ventas.reporte")
logger.info("Se generó el reporte")
```

Micro-ejemplo incorrecto:
```py
def generar_reporte():
    print("Se generó el reporte")
```

Error real:
```py
No hay error de Python, pero el mensaje se pierde si nadie ve la consola.
```

Cómo se arregla: usa `logging.getLogger(...)` y deja que el consumidor configure
`basicConfig` o handlers en un punto único.

## Registrar logs en archivo (sin perderlos en consola)
Si quieres que los mensajes queden guardados, configura un archivo de salida.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8",
)
logger = logging.getLogger("app")
logger.info("Este mensaje queda en app.log")
```

Micro-ejemplo incorrecto:
```py
import logging

logging.basicConfig(filename="logs/app.log", level=logging.INFO)
logger = logging.getLogger("app")
logger.info("Mensaje")
```

Error real:
```py
FileNotFoundError: [Errno 2] No such file or directory: 'logs/app.log'
```

Cómo se arregla: crea la carpeta antes o usa una ruta existente.

## Handlers: consola vs archivo (y por qué importa)
Un handler decide **a dónde** se envía el log. Lo típico es consola + archivo.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("app")
archivo = logging.FileHandler("app.log", encoding="utf-8")
logger.addHandler(archivo)
logger.warning("Esto queda en el archivo")
```

Micro-ejemplo incorrecto:
```py
archivo = logging.FileHandler("app.log")
logger.addHandler(archivo)
```

Error real:
```py
NameError: name 'logger' is not defined
```

Cómo se arregla: crea el logger antes de añadir handlers.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("app")
consola = logging.StreamHandler()
logger.addHandler(consola)
logger.info("También se ve en consola")
```

Micro-ejemplo incorrecto:
```py
logger.addHandler("consola")
```

Error real:
```py
TypeError: Handler expected, got str
```

Cómo se arregla: añade un handler real como `logging.StreamHandler()`.

## Formato detallado con Formatter
Un `Formatter` define **cómo** se ve cada línea de log.

Micro-ejemplo correcto:
```py
import logging

logger = logging.getLogger("app")
consola = logging.StreamHandler()
formato = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
consola.setFormatter(formato)
logger.addHandler(consola)
logger.error("Mensaje formateado")
```

Micro-ejemplo incorrecto:
```py
formato = logging.Formatter
consola.setFormatter(formato)
```

Error real:
```py
TypeError: expected Formatter instance, got type
```

Cómo se arregla: instancia `logging.Formatter(...)`.

## Jerarquía de loggers y propagate
Los loggers heredan configuración por nombre. `app.db` hereda de `app`.
Si `logger.propagate = True`, el mensaje sube al logger padre.

Micro-ejemplo correcto:
```py
import logging

logging.basicConfig(level=logging.INFO)
root = logging.getLogger("app")
child = logging.getLogger("app.db")
child.info("Usa la configuración del padre")
```

Micro-ejemplo incorrecto:
```py
child = logging.getLogger("app.db")
child.propagate("no")
```

Error real:
```py
TypeError: 'bool' object is not callable
```

Cómo se arregla: `child.propagate = False` (es una propiedad booleana).

## Ejemplo ampliado: consola + archivo + niveles distintos
### 1) Aprende esto
Separar logs en consola y archivo te permite revisar errores reales sin perder detalles.

### 2) Haz esto
```py
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

consola = logging.StreamHandler()
consola.setLevel(logging.INFO)

archivo = logging.FileHandler("app.log", encoding="utf-8")
archivo.setLevel(logging.DEBUG)

formato = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
consola.setFormatter(formato)
archivo.setFormatter(formato)

logger.addHandler(consola)
logger.addHandler(archivo)

logger.debug("Detalle solo en archivo")
logger.info("Mensaje visible en consola y archivo")
```

### 3) Verás esto
```text
INFO:app:Mensaje visible en consola y archivo
```

### 4) Por qué funciona
Cada handler filtra por nivel y usa su formato. El logger principal controla
qué mensajes pueden pasar, y los handlers deciden dónde se imprimen.

### 5) Lo típico que sale mal
1) Olvidar el nivel del logger:
```py
logger = logging.getLogger("app")
logger.addHandler(logging.StreamHandler())
logger.debug("No aparece")
```
```text
El DEBUG no aparece porque el logger por defecto filtra por WARNING.
```

2) Añadir handlers duplicados:
```py
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.StreamHandler())
logger.info("Se duplica")
```
```text
El mensaje aparece dos veces porque tienes dos handlers iguales.
```

Cómo se arregla: define niveles y añade handlers una sola vez.

## Errores típicos rápidos
- Configurar `basicConfig` después de crear loggers y pensar que afecta el formato.
- Usar `logger.error` para todo y perder la diferencia entre advertencias y errores.

## Ejercicios
1) Cambia el nivel a `DEBUG` y agrega un `logger.debug(...)`.
2) Prueba `logger.error(...)` con un texto distinto y observa el formato.
3) Intenta provocar una excepción y captura el traceback con `logger.exception(...)`.

## Checklist final
- [ ] Sé cuándo usar `DEBUG` vs `INFO` vs `ERROR`.
- [ ] Configuro el formato una sola vez con `basicConfig`.
- [ ] Tengo un logger con nombre (no uso solo el root logger).
"""
