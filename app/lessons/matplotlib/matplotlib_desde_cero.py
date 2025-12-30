from __future__ import annotations

from app.lesson_base import Lesson


class MatplotlibDesdeCeroLesson(Lesson):
    TITLE = "Matplotlib desde cero"
    CATEGORY = "Matplotlib"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐"]
    TAGS = ["matplotlib", "pyplot", "gráficas", "visualización"]

    def summary(self) -> str:
        return (
            "Aprende a crear gráficas básicas con matplotlib, configurar títulos y "
            "etiquetas, y evitar errores comunes al trazar datos."
        )

    def guide(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## ¿Qué es matplotlib?
`matplotlib` es la librería estándar de visualización en Python. Su submódulo `pyplot`
ofrece una API simple para crear gráficas rápido sin perder control.

Micro-ejemplo correcto:
```py
import matplotlib.pyplot as plt
```

Micro-ejemplo incorrecto:
```py
plt.plot([1, 2, 3], [2, 4, 6])
```

Error real:
```py
NameError: name 'plt' is not defined
```

Cómo se arregla: importa `matplotlib.pyplot as plt` antes de usarlo.

## Paso 1: trazar una serie con plt.plot
`plt.plot` dibuja una línea (o puntos) con pares x/y. Luego `plt.show` muestra la figura.

Micro-ejemplo correcto:
```py
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
plt.show()
```

Micro-ejemplo incorrecto:
```py
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4]
plt.plot(x, y)
```

Error real:
```py
ValueError: x and y must have same first dimension, but have shapes (3,) and (2,)
```

Cómo se arregla: asegúrate de que `x` e `y` tengan la misma cantidad de datos.

## Paso 2: títulos y etiquetas para dar contexto
`plt.title`, `plt.xlabel` y `plt.ylabel` hacen que la gráfica sea legible.

Micro-ejemplo correcto:
```py
import matplotlib.pyplot as plt

plt.title("Ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Unidades")
```

Micro-ejemplo incorrecto:
```py
import matplotlib.pyplot as plt

plt.title()
```

Error real:
```py
TypeError: title() missing 1 required positional argument: 'label'
```

Cómo se arregla: pasa el texto del título como argumento.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** crear una gráfica con etiquetas claras para comunicar un resultado.

**Haz esto (código con contexto):**
```py
import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May"]
ventas = [120, 90, 150, 130, 170]

plt.plot(meses, ventas, marker="o")
plt.title("Ventas 2024")
plt.xlabel("Mes")
plt.ylabel("Unidades")
plt.show()
```

**Verás esto (salida real):**
```
Se abre una ventana con una línea de tendencia y puntos para cada mes.
```

**Por qué funciona:** `plt.plot` conecta los puntos con la misma longitud en `meses` y
`ventas`, y las etiquetas ayudan a interpretar el eje x/y.

**Lo típico que sale mal (error real):**
```py
meses = ["Ene", "Feb", "Mar"]
ventas = [120, 90]
plt.plot(meses, ventas)
```
```
ValueError: x and y must have same first dimension, but have shapes (3,) and (2,)
```

Solución: completa los datos o recorta ambas listas para que tengan la misma longitud.

## Errores típicos rápidos
- Olvidar `plt.show()` y pensar que la gráfica “no salió”.
- Pasar listas con longitudes distintas y obtener errores de dimensiones.

## Ejercicios
1) Grafica el doble de una lista `[1, 2, 3, 4]` usando `plt.plot`.
2) Cambia el título a “Producción semanal” y agrega etiquetas de ejes.
3) Prueba un marcador distinto con `marker="x"` y observa el cambio.

## Checklist final
- [ ] Sé importar `matplotlib.pyplot` correctamente.
- [ ] Uso `plt.plot` y `plt.show` para visualizar datos.
- [ ] Etiqueto la gráfica con título y ejes.
"""
