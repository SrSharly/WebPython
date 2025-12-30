from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class NumpyDesdeCeroLesson(Lesson):
    TITLE = "NumPy desde cero"
    CATEGORY = "NumPy"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐", "🧠"]
    TAGS = ["numpy", "arrays", "ndarray", "vectorizacion", "cálculo-numérico"]

    def summary(self) -> str:
        return (
            "Aprende a crear arrays con NumPy, operar de forma vectorizada, "
            "inspeccionar shape y dtype, y evitar errores típicos de índices."
        )

    def guide(self) -> str:
        return """
## Introducción: por qué NumPy es la base del cálculo científico
NumPy aporta arrays n-dimensionales eficientes (ndarray) y operaciones vectorizadas. Es la base
de pandas, scikit-learn y muchas librerías científicas, así que dominarlo te ahorra tiempo y errores.

### Micro-ejemplo correcto: importar NumPy
```py
import numpy as np
```

### Micro-ejemplo incorrecto: usar np sin importar
```py
datos = np.array([1, 2, 3])
```

```py
NameError: name 'np' is not defined
```

Corrección: importa con `import numpy as np` antes de usarlo.

## Paso 1: crear arrays con np.array
Un array de NumPy se crea a partir de listas o tuplas.

**Así se escribe**
```py
import numpy as np
valores = np.array([1, 2, 3])
```

**Error típico (❌)**
```py
import numpy as np
valores = np.array(1, 2, 3)
```

```py
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
```

**Cómo se arregla**
Pasa una sola lista o tupla: `np.array([1, 2, 3])`.

## Paso 2: vectorización (operar sin bucles)
Los arrays permiten operar elemento a elemento de forma directa.

**Así se escribe**
```py
import numpy as np
precios = np.array([10, 20, 30])
con_iva = precios * 1.21
```

**Error típico (❌)**
```py
precios = [10, 20, 30]
con_iva = precios * 1.21
```

```py
TypeError: can't multiply sequence by non-int of type 'float'
```

**Cómo se arregla**
Convierte la lista a `np.array` para operar con floats.

## Paso 3: índices, slicing y shape
Puedes leer posiciones con índices y revisar la forma con `shape`.

**Así se escribe**
```py
import numpy as np
datos = np.array([5, 10, 15, 20])
primero = datos[0]
ultimos = datos[2:]
forma = datos.shape
```

**Error típico (❌)**
```py
datos = np.array([5, 10, 15, 20])
valor = datos[10]
```

```py
IndexError: index 10 is out of bounds for axis 0 with size 4
```

**Cómo se arregla**
Verifica el tamaño con `shape` antes de indexar.

## Paso 4: dtype y creación rápida
`dtype` describe el tipo real del array. Para crear arrays rápidos usa helpers.

**Así se escribe**
```py
import numpy as np
ceros = np.zeros(4)
secuencia = np.arange(1, 6)
tipo = secuencia.dtype
```

**Error típico (❌)**
```py
import numpy as np
ceros = np.zeros("4")
```

```py
TypeError: 'str' object cannot be interpreted as an integer
```

**Cómo se arregla**
Pasa enteros a `np.zeros` y `np.arange`.

## Ejemplo ampliado con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** aplicar descuentos y obtener métricas sin bucles.

**Haz esto**
```py
import numpy as np

ventas = np.array([120, 80, 100, 90], dtype=float)
descuento = 0.10
ventas_desc = ventas * (1 - descuento)
total = ventas_desc.sum()
promedio = ventas_desc.mean()

print(ventas_desc)
print(total)
print(promedio)
```

**Verás esto**
```py
[108.  72.  90.  81.]
351.0
87.75
```

**Por qué funciona**
NumPy aplica la multiplicación a cada elemento del array y luego calcula métricas agregadas.

**Lo típico que sale mal**
Usar una lista en lugar de un array y obtener errores al multiplicar por decimales.

## Operaciones y métodos más útiles
1) `np.array()` ⭐  
Qué hace: crea un array desde listas o tuplas.  
Así se escribe:
```py
np.array([1, 2, 3])
```
Error típico:
```py
np.array(1, 2, 3)
```
Verás esto: un `ndarray`.  
Por qué funciona: convierte la estructura en un array contiguo.  
Lo típico que sale mal: pasar argumentos separados.

2) `np.zeros()` ⭐  
Qué hace: crea un array de ceros.  
Así se escribe:
```py
np.zeros(3)
```
Error típico:
```py
np.zeros("3")
```
Verás esto: `[0. 0. 0.]`.  
Por qué funciona: reserva memoria inicializada en 0.  
Lo típico que sale mal: pasar strings en lugar de enteros.

3) `np.arange()` ⭐  
Qué hace: crea una secuencia numérica.  
Así se escribe:
```py
np.arange(1, 5)
```
Error típico:
```py
np.arange(1, "5")
```
Verás esto: `[1 2 3 4]`.  
Por qué funciona: genera un rango eficiente.  
Lo típico que sale mal: pasar límites no numéricos.

4) `np.sum()` ⭐  
Qué hace: suma todos los elementos.  
Así se escribe:
```py
np.sum(np.array([1, 2, 3]))
```
Error típico:
```py
np.sum("123")
```
Verás esto: `6`.  
Por qué funciona: reduce el array a un escalar.  
Lo típico que sale mal: pasar texto en lugar de array.

5) `np.mean()` ⭐  
Qué hace: calcula la media.  
Así se escribe:
```py
np.mean(np.array([10, 20, 30]))
```
Error típico:
```py
np.mean(["10", "20"])
```
Verás esto: `20.0`.  
Por qué funciona: convierte a float y promedia.  
Lo típico que sale mal: mezclar strings y números.

## Checklist final
- Sé crear arrays y revisar `shape` y `dtype`.
- Uso vectorización en lugar de bucles cuando aplica.
- Sé generar secuencias con `np.arange` y ceros con `np.zeros`.
- Identifico errores de índice y de tipos en NumPy.
"""

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Usar listas donde necesitas arrays",
                "Las listas no soportan operaciones con floats. Convierte con np.array.",
            ),
            (
                "Indexar fuera de rango",
                "Comprueba el tamaño con shape antes de acceder a un índice.",
            ),
            (
                "Confundir dtype y tipo Python",
                "dtype describe el tipo interno del array, no la clase del objeto.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear arrays básicos",
                """import numpy as np

enteros = np.array([1, 2, 3])
flotantes = np.array([1.5, 2.5, 3.5])
print(enteros)
print(flotantes)""",
            ),
            (
                "Vectorización rápida",
                """import numpy as np

pesos = np.array([70, 80, 65])
pesos_kg = pesos * 1.0
print(pesos_kg)""",
            ),
            (
                "Crear secuencias",
                """import numpy as np

secuencia = np.arange(0, 10, 2)
ceros = np.zeros(5)
print(secuencia)
print(ceros)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un array con 5 números del 1 al 5.",
                "hints": ["Usa np.arange."],
                "solution": "numeros = np.arange(1, 6)",
            },
            {
                "question": "Calcula el total de un array de precios.",
                "hints": ["Usa np.sum."],
                "solution": "total = np.sum(np.array([10, 20, 30]))",
            },
            {
                "question": "Crea un array de 4 ceros.",
                "hints": ["Usa np.zeros."],
                "solution": "ceros = np.zeros(4)",
            },
        ]

    def requirements(self) -> list[str]:
        return ["numpy"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("numpy")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "NumPy no disponible."))
            layout.addWidget(QLabel("Instala numpy con: pip install numpy"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("NumPy disponible. Revisa los ejemplos para explorar."))
        return widget
