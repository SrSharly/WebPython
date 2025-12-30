from __future__ import annotations

from app.lesson_base import Lesson


class PlotlyDesdeCeroLesson(Lesson):
    TITLE = "Plotly desde cero"
    CATEGORY = "Plotly"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["🧠"]
    TAGS = ["plotly", "plotly express", "visualización", "gráficas", "html"]

    def summary(self) -> str:
        return (
            "Aprende a crear gráficos interactivos con Plotly, exportarlos a HTML "
            "y evitar errores típicos al preparar datos y columnas."
        )

    def guide(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Qué es Plotly y cuándo usarlo?
Plotly es una librería de visualización interactiva. Sus gráficos permiten zoom,
hover y exportación a HTML, lo cual es ideal para dashboards y reportes compartibles.

Micro-ejemplo correcto:
```py
import plotly.express as px
```

Micro-ejemplo incorrecto:
```py
px.bar(x=[1, 2, 3], y=[2, 4, 6])
```

Error real:
```py
NameError: name 'px' is not defined
```

Cómo se arregla: importa `plotly.express as px` antes de usarlo.

## Paso 1: estructura de datos simple con Plotly Express
Plotly Express trabaja bien con diccionarios y DataFrames.

Micro-ejemplo correcto:
```py
import plotly.express as px

ventas = {
    "mes": ["Ene", "Feb", "Mar"],
    "unidades": [120, 90, 150],
}
fig = px.bar(ventas, x="mes", y="unidades")
```

Micro-ejemplo incorrecto:
```py
fig = px.bar(ventas, x="mes", y="monto")
```

Error real:
```py
ValueError: Value of 'y' is not the name of a column in 'data_frame'. Expected one of ['mes', 'unidades']
```

Cómo se arregla: usa columnas reales del diccionario o DataFrame.

## Paso 2: mostrar el gráfico
`fig.show()` abre el visor interactivo (en notebook o en navegador).

Micro-ejemplo correcto:
```py
fig.show()
```

Micro-ejemplo incorrecto:
```py
fig.show
```

Error real:
```py
No hay error, pero el gráfico no se muestra porque no se llamó al método.
```

Cómo se arregla: ejecuta `fig.show()` con paréntesis.

## Paso 3: exportar a HTML para compartir
Guardar el gráfico como HTML permite enviarlo por correo o abrirlo en navegador.

Micro-ejemplo correcto:
```py
fig.write_html("reporte_ventas.html")
```

Micro-ejemplo incorrecto:
```py
fig.write_html("reportes/reporte_ventas.html")
```

Error real:
```py
FileNotFoundError: [Errno 2] No such file or directory: 'reportes/reporte_ventas.html'
```

Cómo se arregla: crea la carpeta antes o usa una ruta existente.

## Ejemplo principal: gráfico interactivo con etiquetas claras
### 1) Aprende esto
Crear un gráfico de barras interactivo para comunicar ventas mensuales y exportarlo.

### 2) Haz esto
```py
import plotly.express as px

ventas = {
    "mes": ["Ene", "Feb", "Mar", "Abr", "May"],
    "unidades": [120, 90, 150, 130, 170],
}

fig = px.bar(
    ventas,
    x="mes",
    y="unidades",
    title="Ventas 2024",
    labels={"mes": "Mes", "unidades": "Unidades"},
)
fig.update_traces(marker_color="#2E86AB")
fig.show()
fig.write_html("ventas_2024.html")
```

### 3) Verás esto
```text
Se abre un gráfico interactivo con barras, tooltip al pasar el cursor y título.
Además se genera ventas_2024.html para compartir.
```

### 4) Por qué funciona
Plotly Express interpreta `ventas` como tabla, genera ejes con `x` e `y`, y
`update_traces` ajusta el estilo sin reescribir el gráfico completo.

### 5) Lo típico que sale mal
1) Usar columnas inexistentes:
```py
fig = px.bar(ventas, x="mes", y="total")
```
```py
ValueError: Value of 'y' is not the name of a column in 'data_frame'. Expected one of ['mes', 'unidades']
```

2) Olvidar exportar antes de compartir:
```py
fig.write_html("ventas_2024.html")
```
```text
Si no ejecutas write_html, no tendrás un archivo para enviar.
```

Cómo se arregla: revisa las columnas y genera el HTML como último paso.

## Plotly Express vs Graph Objects (cuándo usar cada uno)
Plotly Express es rápido para gráficos estándar. `plotly.graph_objects` da control
fino cuando necesitas múltiples ejes o combinaciones avanzadas.

Micro-ejemplo correcto:
```py
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[2, 1, 3]))
fig.show()
```

Micro-ejemplo incorrecto:
```py
go.scatter(x=[1, 2, 3], y=[2, 1, 3])
```

Error real:
```py
AttributeError: module 'plotly.graph_objects' has no attribute 'scatter'
```

Cómo se arregla: usa `go.Scatter` con mayúscula.

## Errores típicos rápidos
- Olvidar instalar la librería y ver `ModuleNotFoundError: No module named 'plotly'`.
- Pasar listas con longitudes distintas en `x` e `y` al usar `go.Scatter`.

## Ejercicios
1) Crea un gráfico de línea con `px.line` usando meses y temperatura.
2) Cambia el color de las barras con `update_traces`.
3) Guarda el resultado en un archivo HTML con otro nombre.

## Checklist final
- [ ] Sé crear gráficos con Plotly Express.
- [ ] Sé mostrar y exportar gráficos interactivos.
- [ ] Entiendo cuándo usar Plotly Express vs Graph Objects.
"""
