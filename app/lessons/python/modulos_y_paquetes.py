from __future__ import annotations

from app.lesson_base import Lesson


class ModulosPaquetesLesson(Lesson):
    TITLE = "Módulos y paquetes"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    BADGES = ["⭐"]
    TAGS = ["import", "módulos", "paquetes", "__init__", "organización"]

    def summary(self) -> str:
        return (
            "Aprende a organizar tu código con módulos y paquetes, usar importaciones "
            "claras y evitar errores típicos al reutilizar lógica."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## Por qué módulos y paquetes importan
Un proyecto real crece rápido. Si metes todo en un archivo, se vuelve inmanejable.
Los módulos y paquetes te permiten separar responsabilidades, reutilizar código y
mantener el proyecto claro.

## Paso 1: qué es un módulo
Un módulo es un archivo `.py` con funciones, clases o constantes reutilizables.

**Micro-ejemplo correcto**
```py
import math

resultado = math.sqrt(9)
```

**Micro-ejemplo incorrecto**
```py
resultado = math.sqrt(9)
```

**Error real**
```py
NameError: name 'math' is not defined
```

**Cómo se arregla**
Importa el módulo antes de usarlo: `import math`.

## Paso 2: qué es un paquete y por qué existe `__init__.py`
Un paquete es una carpeta que agrupa módulos. El archivo `__init__.py` define qué expone
el paquete y permite importaciones más limpias.

**Micro-ejemplo correcto**
```py
# mi_paquete/__init__.py
from .utilidades import limpiar_texto
```

**Micro-ejemplo incorrecto**
```py
from mi_paquete import limpiar_texto
```

**Error real**
```py
ModuleNotFoundError: No module named 'mi_paquete'
```

**Cómo se arregla**
Asegúrate de que la carpeta exista, tenga `__init__.py` y se ejecute desde la raíz del proyecto.

## Paso 3: importar solo lo que necesitas
`from ... import ...` trae nombres específicos para escribir menos prefijos.

**Micro-ejemplo correcto**
```py
from math import sqrt

print(sqrt(16))
```

**Micro-ejemplo incorrecto**
```py
from math import squareroot
```

**Error real**
```py
ImportError: cannot import name 'squareroot' from 'math'
```

**Cómo se arregla**
Revisa el nombre exacto exportado por el módulo.

## Paso 4: usa alias para evitar conflictos
Los alias te ayudan cuando hay nombres largos o duplicados.

**Micro-ejemplo correcto**
```py
import math as m

print(m.sqrt(9))
```

**Micro-ejemplo incorrecto**
```py
import math as m

print(math.pi)
```

**Error real**
```py
NameError: name 'math' is not defined
```

**Cómo se arregla**
Usa siempre el alias (`m`) una vez definido.

## Paso 4.5: importaciones relativas dentro de un paquete
Cuando un módulo está dentro de un paquete, lo más estable es usar imports relativos con `.`.
Esto evita errores cuando ejecutas el proyecto desde la raíz.

**Micro-ejemplo correcto**
```py
# mi_app/ventas.py
from .calculos import total_con_impuesto
```

**Micro-ejemplo incorrecto**
```py
# mi_app/ventas.py
from calculos import total_con_impuesto
```

**Error real**
```py
ModuleNotFoundError: No module named 'calculos'
```

**Cómo se arregla**
Usa `from .calculos import total_con_impuesto` y ejecuta el paquete desde la raíz.

## Ejemplo principal: un mini-paquete bien organizado
### 1) Aprende esto
Separar lógica en módulos y exponer una API simple desde el paquete.

### 2) Haz esto
```py
# mi_app/calculos.py
def total_con_impuesto(precio, tasa):
    return precio * (1 + tasa)

# mi_app/__init__.py
from .calculos import total_con_impuesto

# main.py
from mi_app import total_con_impuesto

precio = 100
print(total_con_impuesto(precio, 0.19))
```

### 3) Verás esto
```text
119.0
```

### 4) Por qué funciona
`mi_app` es el paquete, `calculos.py` es el módulo y `__init__.py` expone una función
principal. Así `main.py` importa desde el paquete sin conocer la estructura interna.

### 5) Lo típico que sale mal
1) Ejecutar desde una carpeta distinta:
```py
from mi_app import total_con_impuesto
```
```py
ModuleNotFoundError: No module named 'mi_app'
```

Solución: ejecuta `python main.py` desde la raíz del proyecto o ajusta `sys.path`.

## Checklist final
- [ ] Cada archivo `.py` es un módulo con una responsabilidad clara.
- [ ] Los paquetes tienen `__init__.py` y exportan una API sencilla.
- [ ] Usas `import` o `from ... import ...` según lo que necesites.
- [ ] Evitas errores de import revisando el entorno y la ruta del proyecto.
"""
