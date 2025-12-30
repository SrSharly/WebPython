from __future__ import annotations

from app.lesson_base import Lesson


class SeabornDesdeCeroLesson(Lesson):
    TITLE = "Seaborn desde cero"
    CATEGORY = "Seaborn"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐"]
    TAGS = ["seaborn", "visualización", "estadística", "gráficas"]

    def summary(self) -> str:
        return (
            "Aprende a crear gráficas estadísticas con Seaborn, configurar temas "
            "visuales y evitar errores típicos al mapear columnas."
        )

    def guide(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## ¿Qué es Seaborn?
`seaborn` es una librería de visualización estadística basada en matplotlib. Su ventaja
es que **simplifica** la creación de gráficos con datos tabulares (como DataFrames) y
aplica estilos consistentes por defecto.

Micro-ejemplo correcto:
```py
import seaborn
```

Micro-ejemplo incorrecto:
```py
seaborn.scatterplot(data=df, x="edad", y="altura")
```

Error real:
```py
NameError: name 'seaborn' is not defined
```

Cómo se arregla: importa `seaborn` antes de usarlo.

## Paso 1: tema visual con set_theme
`set_theme` define el estilo global (rejilla, colores, tamaños) para toda la sesión.

Micro-ejemplo correcto:
```py
import seaborn

seaborn.set_theme(style="whitegrid")
```

Micro-ejemplo incorrecto:
```py
import seaborn

seaborn.set_theme(styl="whitegrid")
```

Error real:
```py
TypeError: set_theme() got an unexpected keyword argument 'styl'
```

Cómo se arregla: usa el parámetro correcto `style`.

## Paso 2: scatterplot para relaciones numéricas
`scatterplot` muestra relación entre dos variables numéricas, ideal para detectar tendencias.

Micro-ejemplo correcto:
```py
import pandas as pd
import seaborn

df = pd.DataFrame({"edad": [20, 25, 30], "altura": [1.70, 1.75, 1.80]})
seaborn.scatterplot(data=df, x="edad", y="altura")
```

Micro-ejemplo incorrecto:
```py
import pandas as pd
import seaborn

df = pd.DataFrame({"edad": [20, 25, 30], "altura": [1.70, 1.75, 1.80]})
seaborn.scatterplot(data=df, x="años", y="altura")
```

Error real:
```py
ValueError: Could not interpret value `años` for `x`
```

Cómo se arregla: usa nombres de columnas que existan en el DataFrame.

## Paso 3: relplot para comparaciones con categorías
`relplot` permite comparar relaciones separando por color o paneles.

Micro-ejemplo correcto:
```py
import pandas as pd
import seaborn

df = pd.DataFrame(
    {"mes": [1, 2, 3, 1, 2, 3], "ventas": [10, 12, 9, 14, 15, 13], "region": ["N", "N", "N", "S", "S", "S"]}
)
seaborn.relplot(data=df, x="mes", y="ventas", hue="region", kind="scatter")
```

Micro-ejemplo incorrecto:
```py
import pandas as pd
import seaborn

df = pd.DataFrame({"mes": [1, 2, 3], "ventas": [10, 12, 9]})
seaborn.relplot(data=df, x="mes", y="ventas", hue="region")
```

Error real:
```py
ValueError: Could not interpret value `region` for `hue`
```

Cómo se arregla: usa una columna categórica real para `hue`.

## Ejemplo principal: comparar ventas por región con contexto real
### 1) Aprende esto
Crear una gráfica clara para comparar ventas por región sin escribir código extra.

### 2) Haz esto
```py
import pandas as pd
import seaborn
import matplotlib.pyplot as plt

seaborn.set_theme(style="whitegrid")

df = pd.DataFrame(
    {"mes": [1, 2, 3, 4, 1, 2, 3, 4], "ventas": [10, 14, 9, 16, 8, 11, 12, 15], "region": ["N", "N", "N", "N", "S", "S", "S", "S"]}
)

seaborn.relplot(data=df, x="mes", y="ventas", hue="region", kind="line")
plt.show()
```

### 3) Verás esto
Una gráfica con dos líneas (N y S) mostrando la evolución mensual de ventas.

### 4) Por qué funciona
`relplot` crea una figura completa y `hue="region"` separa los datos por categoría.
El tema `whitegrid` mejora la lectura y `plt.show()` muestra la gráfica.

### 5) Lo típico que sale mal
1) Olvidar matplotlib cuando se quiere mostrar la figura:
```py
seaborn.relplot(data=df, x="mes", y="ventas", hue="region", kind="line")
plt.show()
```
```py
NameError: name 'plt' is not defined
```

2) Mezclar longitudes distintas:
```py
df = pd.DataFrame({"mes": [1, 2, 3], "ventas": [10, 12]})
seaborn.scatterplot(data=df, x="mes", y="ventas")
```
```py
ValueError: All arrays must be of the same length
```

## Checklist final (rápido)
- ¿Configuraste `set_theme` si quieres estilo consistente?
- ¿Usas columnas reales en `x`, `y` y `hue`?
- ¿Mostraste la figura con `plt.show()` cuando lo necesitas?
"""
