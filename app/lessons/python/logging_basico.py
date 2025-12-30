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
