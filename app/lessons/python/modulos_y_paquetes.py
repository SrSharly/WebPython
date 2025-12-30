from __future__ import annotations

from app.lesson_base import Lesson


class ModulosPaquetesLesson(Lesson):
    TITLE = "Módulos y paquetes"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    BADGES = ["⭐"]
    TAGS = ["modulos", "paquetes", "import", "from", "alias"]

    def summary(self) -> str:
        return (
            "Aprende a organizar código con módulos y paquetes, importar correctamente "
            "y evitar los errores clásicos de importación."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## ¿Qué es un módulo y qué es un paquete?
- **Módulo**: un archivo `.py` con funciones, clases o constantes reutilizables.
- **Paquete**: una carpeta con módulos relacionados (normalmente con `__init__.py`).

Micro-ejemplo correcto:
```py
import logging
print("Módulo importado")
```

Micro-ejemplo incorrecto:
```py
import loggin
```

Error real:
```py
ModuleNotFoundError: No module named 'loggin'
```

Cómo se arregla: revisa el nombre real del módulo (`logging`).

## Import básico con `import`
Cuando importas un módulo, accedes a sus miembros con el nombre del módulo.

Micro-ejemplo correcto:
```py
import logging
logger = logging.getLogger("app")
print(logger)
```

Micro-ejemplo incorrecto:
```py
import logging
logger = getLogger("app")
```

Error real:
```py
NameError: name 'getLogger' is not defined
```

Cómo se arregla: usa el prefijo `logging.` o importa el símbolo explícitamente.

## Importar símbolos con `from ... import ...`
Sirve para traer funciones o constantes sin el prefijo del módulo.

Micro-ejemplo correcto:
```py
from logging import getLogger
logger = getLogger("app")
print(logger)
```

Micro-ejemplo incorrecto:
```py
from logging import getLoger
```

Error real:
```py
ImportError: cannot import name 'getLoger' from 'logging'
```

Cómo se arregla: importa el nombre correcto (`getLogger`).

## Alias con `as`
Usa alias para nombres largos o para evitar colisiones.

Micro-ejemplo correcto:
```py
import logging as log
logger = log.getLogger("app")
print(logger)
```

Micro-ejemplo incorrecto:
```py
import logging as log
logger = logging.getLogger("app")
```

Error real:
```py
NameError: name 'logging' is not defined
```

Cómo se arregla: usa el alias (`log`) después de `as`.

## Paquetes: organización por carpetas
Un paquete agrupa módulos relacionados. Un `__init__.py` deja claro que la carpeta es un paquete.

Micro-ejemplo correcto:
```py
from utilidades import saludos
```

Micro-ejemplo incorrecto:
```py
from utilidad import saludos
```

Error real:
```py
ModuleNotFoundError: No module named 'utilidad'
```

Cómo se arregla: usa el nombre real del paquete (`utilidades`).

## Ejemplo principal: mini paquete con un módulo reutilizable
### 1) Aprende esto
Separar tu lógica en módulos te permite reutilizarla y mantener el código limpio.

### 2) Haz esto
```py
# utilidades/saludos.py
MENSAJE_BASE = "Hola"

def construir_saludo(nombre):
    return f"{MENSAJE_BASE}, {nombre}"

# main.py
from utilidades.saludos import construir_saludo

print(construir_saludo("Ana"))
```

### 3) Verás esto
```text
Hola, Ana
```

### 4) Por qué funciona
`main.py` importa la función desde el módulo `saludos` dentro del paquete `utilidades`.
Eso mantiene la lógica reutilizable en un solo lugar.

### 5) Lo típico que sale mal
1) Importar el módulo con el nombre equivocado:
```py
from utilidades.saludo import construir_saludo
```
```py
ModuleNotFoundError: No module named 'utilidades.saludo'
```

2) Escribir mal el símbolo importado:
```py
from utilidades.saludos import construir_saludos
```
```py
ImportError: cannot import name 'construir_saludos' from 'utilidades.saludos'
```

Cómo se arregla: revisa el nombre exacto del módulo y del símbolo.

## Nota preventiva: evita colisiones de nombres
Si llamas a tu archivo `logging.py`, ocultas el módulo estándar `logging` y tus imports fallarán.

Micro-ejemplo incorrecto:
```py
import logging
```

Error real:
```py
AttributeError: module 'logging' has no attribute 'basicConfig'
```

Cómo se arregla: renombra tu archivo local para no ocultar módulos estándar.

## Ejercicios
1) Crea un paquete `utils` con un módulo `texto.py` que tenga una constante y úsala.
2) Importa un símbolo con `from ... import ...` y muéstralo con `print`.
3) Prueba un alias con `as` y úsalo en una llamada.

## Checklist final
- [ ] Sé cuándo usar `import` y cuándo `from ... import ...`.
- [ ] Puedo crear un paquete con `__init__.py`.
- [ ] Evito colisiones de nombres con módulos estándar.
""".strip()
