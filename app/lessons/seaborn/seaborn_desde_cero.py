from __future__ import annotations

from app.lesson_base import Lesson


class SeabornDesdeCeroLesson(Lesson):
    TITLE = "Seaborn desde cero"
    CATEGORY = "Seaborn"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["🧠"]
    TAGS = ["seaborn", "visualización", "gráficas", "pandas"]

    def summary(self) -> str:
        return (
            "Aprende a crear gráficas estadísticos con seaborn, usar DataFrames de pandas "
            "y evitar errores típicos al mapear columnas."
        )

    def guide(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Qué es seaborn?
Seaborn es una librería de visualización estadística basada en matplotlib. Brilla cuando
trabajas con `DataFrame` de pandas porque permite mapear columnas a ejes y estilos con poco
código.

Micro-ejemplo correcto:
```py
import seaborn as sns
```

Micro-ejemplo incorrecto:
```py
sns.scatterplot(x=[1, 2, 3], y=[2, 4, 6])
```

Error real:
```py
NameError: name 'sns' is not defined
```

Cómo se arregla: importa seaborn con `import seaborn as sns`.

## Paso 1: tema visual consistente con sns.set_theme
**Aprende esto:** un tema unifica colores y estilos antes de crear gráficas.

Micro-ejemplo correcto:
```py
import seaborn as sns

sns.set_theme(style="whitegrid")
```

Micro-ejemplo incorrecto:
```py
import seaborn as sns

sns.set_theme()
sns.set_theme(styley="whitegrid")
```

Error real:
```py
TypeError: set_theme() got an unexpected keyword argument 'styley'
```

Cómo se arregla: usa el argumento correcto `style`.

## Paso 2: scatterplot con columnas de un DataFrame
**Aprende esto:** seaborn interpreta columnas cuando pasas `data=`.

Micro-ejemplo correcto:
```py
import pandas as pd
import seaborn as sns

ventas = pd.DataFrame({
    "mes": [1, 2, 3, 4],
    "unidades": [120, 90, 150, 130],
})

sns.scatterplot(data=ventas, x="mes", y="unidades")
```

Micro-ejemplo incorrecto:
```py
import pandas as pd
import seaborn as sns

ventas = pd.DataFrame({
    "mes": [1, 2, 3, 4],
    "unidades": [120, 90, 150, 130],
})

sns.scatterplot(data=ventas, x="mes", y="ventas")
```

Error real:
```py
ValueError: Could not interpret value `ventas` for `y`
```

Cómo se arregla: asegúrate de que el nombre de la columna exista en el DataFrame.

## Paso 3: histplot para entender la distribución
**Aprende esto:** `histplot` muestra frecuencias y te ayuda a detectar sesgos.

Micro-ejemplo correcto:
```py
import seaborn as sns

sns.histplot(data=[12, 15, 18, 20, 22], bins=5)
```

Micro-ejemplo incorrecto:
```py
import seaborn as sns

sns.histplot(data=[12, 15, 18], bin=5)
```

Error real:
```py
TypeError: histplot() got an unexpected keyword argument 'bin'
```

Cómo se arregla: usa `bins` en plural para controlar la cantidad de barras.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** construir un DataFrame, graficar tendencias y añadir contexto.

**Haz esto (código con contexto):**
```py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

clientes = pd.DataFrame({
    "mes": [1, 2, 3, 4, 5, 6],
    "visitas": [120, 150, 130, 180, 200, 210],
    "ticket": [18, 20, 17, 22, 24, 23],
})

sns.lineplot(data=clientes, x="mes", y="visitas", marker="o", label="Visitas")
plt.title("Visitas mensuales")
plt.xlabel("Mes")
plt.ylabel("Visitas")
plt.show()
```

**Verás esto (salida real):**
```
Se abre una ventana con una línea de tendencia y marcadores por mes.
```

**Por qué funciona:** seaborn toma columnas del DataFrame, `lineplot` conecta puntos por
orden de `mes` y matplotlib agrega título y etiquetas.

**Lo típico que sale mal (error real):**
```py
sns.lineplot(data=clientes, x="mes", y="visitas", marker="o")
plt.title("Visitas")
plt.show
```
```
<function show at 0x...>
```

Solución: llama `plt.show()` con paréntesis para renderizar la figura.

## Errores típicos rápidos
- Omitir `data=` y pasar columnas como strings sin DataFrame.
- Confundir nombres de columna y recibir `ValueError`.
- Olvidar `plt.show()` en entornos no interactivos.

## Ejercicios
1) Crea un `DataFrame` con columnas `dia` y `ventas`, y usa `sns.scatterplot`.
2) Cambia el tema a `style="dark"` y compara la legibilidad.
3) Usa `sns.histplot` para ver la distribución de una lista de 20 números.

## Checklist final
- [ ] Sé importar seaborn como `sns`.
- [ ] Uso `sns.set_theme` para estilos consistentes.
- [ ] Mapeo columnas de `DataFrame` con `data=`, `x` y `y`.
- [ ] Distingo `scatterplot`, `lineplot` e `histplot`.
"""
