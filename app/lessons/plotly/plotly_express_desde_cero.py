from __future__ import annotations

from app.lesson_base import Lesson


class PlotlyExpressDesdeCeroLesson(Lesson):
    TITLE = "Plotly Express desde cero"
    CATEGORY = "Plotly"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["plotly", "plotly-express", "graficas", "visualizacion"]

    def summary(self) -> str:
        return (
            "Aprende a crear gráficas interactivas con Plotly Express, ajustar títulos "
            "y evitar errores comunes al construir visualizaciones."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Qué es Plotly Express y cuándo usarlo?
Plotly Express (`plotly.express`) es la API rápida de Plotly para crear gráficas interactivas
con pocas líneas. Es ideal cuando quieres explorar datos y compartir visualizaciones
interactivas sin escribir mucho código.

Micro-ejemplo correcto:
```py
import plotly.express as px
```

Micro-ejemplo incorrecto:
```py
import plotly as px
fig = px.line(x=[1, 2], y=[3, 4])
```

Error real:
```py
AttributeError: module 'plotly' has no attribute 'line'
```

Cómo se arregla: importa `plotly.express` como `px` para usar `px.line`, `px.bar`, etc.

## Paso 1: tu primera línea con px.line
`px.line` dibuja una serie conectando puntos. Puedes pasar listas simples para empezar rápido.

Micro-ejemplo correcto:
```py
import plotly.express as px

fig = px.line(x=[1, 2, 3], y=[2, 4, 6])
fig.show()
```

Micro-ejemplo incorrecto:
```py
import plotly.express as px

fig = px.line(x=[1, 2, 3], y=[2, 4])
```

Error real:
```py
ValueError: All arguments should have the same length.
```

Cómo se arregla: asegúrate de que `x` e `y` tengan la misma cantidad de elementos.

## Paso 2: barras rápidas con px.bar
`px.bar` sirve para comparar categorías. Usa etiquetas claras para que se entiendan rápido.

Micro-ejemplo correcto:
```py
import plotly.express as px

fig = px.bar(x=["A", "B"], y=[10, 20], labels={"x": "Categoría", "y": "Ventas"})
fig.show()
```

Micro-ejemplo incorrecto:
```py
import plotly.express as px

fig = px.bar()
```

Error real:
```py
TypeError: bar() missing 1 required positional argument: 'data_frame'
```

Cómo se arregla: pasa datos en `data_frame` o al menos `x`/`y` para construir la gráfica.

## Paso 3: ajustar títulos con fig.update_layout
`fig.update_layout` modifica el diseño general: título, márgenes y ejes.

Micro-ejemplo correcto:
```py
import plotly.express as px

fig = px.scatter(x=[1, 2, 3], y=[2, 3, 5])
fig.update_layout(title="Relación entre X e Y")
fig.show()
```

Micro-ejemplo incorrecto:
```py
fig.update_layout["title"] = "Ventas"
```

Error real:
```py
TypeError: 'method' object is not subscriptable
```

Cómo se arregla: llama al método `fig.update_layout(...)` con argumentos nombrados.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
### 1) Aprende esto
Crear una gráfica de barras interactiva con título y ejes claros para reportes rápidos.

### 2) Haz esto
```py
import plotly.express as px

meses = ["Ene", "Feb", "Mar", "Abr", "May"]
ventas = [120, 90, 150, 130, 170]

fig = px.bar(
    x=meses,
    y=ventas,
    labels={"x": "Mes", "y": "Unidades"},
    title="Ventas 2024",
)
fig.update_layout(yaxis_title="Unidades vendidas")
fig.show()
```

### 3) Verás esto
```text
Se abre una ventana del navegador con una gráfica interactiva de barras.
```

### 4) Por qué funciona
`px.bar` genera una figura Plotly con datos y etiquetas, y `fig.update_layout`
ajusta el título y los ejes. `fig.show()` renderiza la visualización interactiva.

### 5) Lo típico que sale mal
1) Olvidar mostrar la figura:
```py
fig = px.bar(x=[1, 2], y=[3, 4])
```
```text
No aparece ninguna ventana porque faltó fig.show().
```

2) Pasar listas con longitudes distintas:
```py
fig = px.bar(x=["A", "B"], y=[10])
```
```py
ValueError: All arguments should have the same length.
```

Cómo se arregla: llama `fig.show()` y valida que `x` e `y` tengan el mismo tamaño.

## Errores típicos rápidos
- Importar `plotly` en lugar de `plotly.express` y no encontrar `px.line`.
- Olvidar llamar `fig.show()` y pensar que no se generó nada.

## Ejercicios
1) Crea una gráfica de línea con 6 puntos y un título claro.
2) Convierte la gráfica anterior a barras con `px.bar`.
3) Añade `fig.update_layout(title=...)` con un título distinto.

## Checklist final
- [ ] Sé importar `plotly.express` como `px`.
- [ ] Puedo crear una línea con `px.line` o barras con `px.bar`.
- [ ] Ajusto títulos con `fig.update_layout`.
"""
