from __future__ import annotations

from app.lesson_base import Lesson


class SeabornDesdeCeroLesson(Lesson):
    TITLE = "Seaborn desde cero"
    CATEGORY = "Seaborn"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["🧠"]
    TAGS = ["seaborn", "visualizacion", "estadistica", "scatterplot", "histplot"]

    def summary(self) -> str:
        return (
            "Aprende a usar Seaborn para crear gráficos estadísticos claros, "
            "aplicar temas, y evitar errores típicos al visualizar datos."
        )

    def guide(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Qué es Seaborn?
Seaborn es una librería de visualización estadística construida sobre Matplotlib.
Aporta estilos listos y funciones de alto nivel para explorar datos rápidamente.

Micro-ejemplo correcto:
```py
import seaborn
```

Micro-ejemplo incorrecto:
```py
seaborn.scatterplot(x=[1, 2], y=[2, 4])
```

Error real:
```py
NameError: name 'seaborn' is not defined
```

Cómo se arregla: importa `seaborn` antes de usar sus funciones.

## Paso 1: aplicar un tema con seaborn.set_theme
Un tema ajusta colores, tamaños y estilo general para que los gráficos sean legibles.

Micro-ejemplo correcto:
```py
import seaborn

seaborn.set_theme(style="whitegrid")
```

Micro-ejemplo incorrecto:
```py
import seaborn

seaborn.set_theme("whitegrid", "extra")
```

Error real:
```py
TypeError: set_theme() takes from 0 to 1 positional arguments but 2 were given
```

Cómo se arregla: pasa solo el estilo (o usa parámetros con nombre).

## Paso 2: scatterplot para ver relación entre variables
`seaborn.scatterplot` dibuja puntos y permite detectar tendencias visuales.

Micro-ejemplo correcto:
```py
import seaborn

seaborn.scatterplot(x=[1, 2, 3], y=[2, 4, 5])
```

Micro-ejemplo incorrecto:
```py
import seaborn

seaborn.scatterplot(x=[1, 2, 3], y=5)
```

Error real:
```py
TypeError: 'int' object is not iterable
```

Cómo se arregla: entrega listas del mismo tamaño para `x` y `y`.

## Paso 3: histplot para distribución
`seaborn.histplot` muestra cómo se distribuyen los valores.

Micro-ejemplo correcto:
```py
import seaborn

seaborn.histplot(data=[10, 12, 13, 15, 18])
```

Micro-ejemplo incorrecto:
```py
import seaborn

seaborn.histplot()
```

Error real:
```py
TypeError: histplot() missing 1 required positional argument: 'data'
```

Cómo se arregla: pasa el dataset con `data=[...]`.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** crear un gráfico claro con tema y puntos para comparar dos variables.

**Haz esto (código con contexto):**
```py
import seaborn
import matplotlib.pyplot as plt

seaborn.set_theme(style="whitegrid")

horas = [1, 2, 3, 4, 5, 6]
progreso = [10, 18, 30, 35, 48, 60]

seaborn.scatterplot(x=horas, y=progreso)
plt.title("Horas de estudio vs progreso")
plt.xlabel("Horas")
plt.ylabel("Puntos")
plt.show()
```

**Verás esto (salida real):**
```
Se abre una ventana con puntos marcando la relación entre horas y progreso.
```

**Por qué funciona:** Seaborn usa el tema definido y Matplotlib muestra la figura.

**Lo típico que sale mal (con error real):**
```py
import seaborn

seaborn.scatterplot(x=[1, 2], y=[3])
```
```
ValueError: All arrays must be of the same length
```
Solución: asegúrate de que `x` e `y` tengan la misma longitud.

## Ejemplo ampliado con contexto: comparar distribuciones
**Aprende esto:** usar `histplot` para comparar el comportamiento de grupos.

**Haz esto (8–25 líneas con contexto):**
```py
import seaborn
import matplotlib.pyplot as plt

seaborn.set_theme(style="darkgrid")

ventas_a = [10, 12, 14, 18, 22, 25]
ventas_b = [8, 9, 11, 13, 15, 17]

seaborn.histplot(data=ventas_a, color="steelblue", label="Equipo A", kde=False)
seaborn.histplot(data=ventas_b, color="salmon", label="Equipo B", kde=False)
plt.legend()
plt.title("Distribución de ventas")
plt.show()
```

**Verás esto (salida real):**
```
Dos histogramas superpuestos para comparar equipos.
```

**Por qué funciona:** cada `histplot` agrega una serie y Matplotlib compone la figura.

**Lo típico que sale mal (con error real):**
```py
import seaborn

seaborn.histplot(data="ventas")
```
```
TypeError: Neither the `x` nor `y` variable appears to be numeric.
```
Solución: pasa una lista de números, no un string literal.

## Errores típicos rápidos
- Olvidar `plt.show()` y creer que el gráfico no funciona.
- Pasar listas de tamaños distintos en `scatterplot`.
- Usar strings en `histplot` en lugar de números.

## Ejercicios
1) Cambia el `style` de `set_theme` y describe qué cambió.
2) Ajusta los datos y observa cómo cambia la nube de puntos.
3) Agrega un tercer histograma con otro grupo de ventas.

## Checklist final
- [ ] Importo `seaborn` antes de usar sus funciones.
- [ ] Uso `set_theme` para estilos coherentes.
- [ ] Verifico que `x` e `y` tengan la misma longitud.
- [ ] Llamo a `plt.show()` al final.
"""
