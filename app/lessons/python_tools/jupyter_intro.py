from __future__ import annotations

from app.lesson_base import Lesson


class JupyterIntroLesson(Lesson):
    TITLE = "Jupyter (Notebook): cuándo y por qué usarlo"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas"
    LEVEL = "Básico"
    TAGS = ["jupyter", "notebook", "herramientas", "eda", "reproducibilidad"]

    def summary(self) -> str:
        return (
            "Entiende qué es Jupyter Notebook, por qué existe y cuándo usarlo frente a un IDE, "
            "con reglas prácticas, advertencias reales y buenas prácticas para no perder el control."
        )

    def guide(self) -> str:
        return """
## 1) Qué es Jupyter (en palabras simples)
Un **Notebook** es un documento interactivo con **celdas**. Cada celda puede ser:
- **Código** (Python que se ejecuta y muestra resultados).
- **Texto** (Markdown para explicar lo que haces).
- **Resultados** (salidas y gráficos).

El **Kernel** es el “Python vivo” que ejecuta las celdas y **guarda el estado**.
Si defines `x = 10` en una celda, el kernel lo recuerda hasta que lo reinicies.

## 2) Por qué existe (el motivo real)
Jupyter existe para **explorar, analizar y comunicar** ideas rápidamente:
- Ver resultados al instante.
- Iterar con datos sin crear una app completa.
- Explicar el razonamiento con texto + resultados.

**No intenta sustituir un IDE**, es otra herramienta para otro momento del trabajo.

## 3) Cuándo ES mejor que PyCharm/Spyder (casos reales)
Jupyter es ideal cuando:
- Haces **data science** o **EDA** (análisis exploratorio).
- Quieres **probar ideas** y ver resultados rápido.
- Necesitas **enseñar** o documentar un análisis paso a paso.
- Comparas modelos en **ML** (métricas y gráficos).
- Quieres generar un **reporte reproducible** para otros.

## 4) Cuándo NO conviene (honestidad)
No es la mejor herramienta para:
- Proyectos grandes con arquitectura, tests y paquetes.
- Apps GUI (PySide), APIs complejas o producción.
- Situaciones donde el **estado oculto** te confunde.
- Trabajo donde la repetibilidad y el control de versiones son críticos sin disciplina.

## 5) “Lo feo e incómodo” explicado + cómo solucionarlo
Si te parece feo o incómodo, suele ser por falta de costumbre:
- **Atajos básicos**:
  - Ejecutar celda: `Shift + Enter`.
  - Crear celda abajo: `Esc` luego `B`.
  - Cambiar tipo de celda a Markdown: `Esc` luego `M`.
  - Subir/bajar celdas: `Esc` luego `A` (arriba) o `B` (abajo).
- **Markdown** hace el notebook claro y bonito (títulos, listas, tablas).
- **Extensiones opcionales** pueden mejorar la experiencia (sin ser obligatorias).
- Ajustes: **tema oscuro**, **tamaño de fuente**, **ancho de celda**.
- Truco útil: usa Jupyter como **laboratorio** y pasa el código a `.py` cuando madure.

## 6) Notebook vs .py vs IDE: regla práctica (muy clara)
Usa esta regla simple:

```
IDEA -> NOTEBOOK -> CÓDIGO REUTILIZABLE -> .py (módulo) -> APP COMPLETA -> IDE
```

- **Idea**: notebook para experimentar.
- **Código reutilizable**: pásalo a `.py` como funciones limpias.
- **App completa**: un IDE para estructura, tests y despliegue.

## 7) Estados y reproducibilidad (la gran trampa)
Lo peligroso del notebook es el **estado oculto**:
- El orden de ejecución importa.
- Las variables siguen vivas aunque borres celdas.

Soluciones concretas:
- Usa **"Restart kernel and run all"**.
- Escribe **funciones** para limpiar dependencias.
- Evita variables globales “mágicas”.
- Limpia el notebook antes de compartir.

## 8) Buenas prácticas PRO (explicadas)
- **Una idea por notebook**: evita mezclas confusas.
- **Nombres claros** para celdas y variables.
- **Secciones Markdown**: Título, Objetivo, Datos, Proceso, Conclusiones.
- **Rutas portables**: evita rutas absolutas duras.
- **Exportar** a HTML/PDF cuando quieras compartir.
- Convertir a script con `jupyter nbconvert` (como concepto, no obligatorio).

## Cierre
Jupyter no es “peor que un IDE”: es un **laboratorio rápido** para pensar y mostrar.
Si lo usas con disciplina, te ahorra tiempo y mejora cómo explicas tus análisis.


## Operaciones y métodos más útiles
### Strings (`str`)
1) `upper()` ⭐  
Qué hace: convierte a mayúsculas.  
Así se escribe:
```py
texto = "hola"
resultado = texto.upper()
```
Error típico:
```py
resultado = texto.upper
```
Verás esto: `"HOLA"`.  
Por qué funciona: `upper()` crea un texto nuevo con mayúsculas.  
Lo típico que sale mal: olvidar paréntesis; creer que cambia el string original.

2) `lower()` ⭐  
Qué hace: convierte a minúsculas.  
Así se escribe:
```py
texto = "HoLa"
resultado = texto.lower()
```
Error típico:
```py
resultado = texto.lower
```
Verás esto: `"hola"`.  
Por qué funciona: normaliza el texto para comparar.  
Lo típico que sale mal: no normalizar ambos lados; asumir mutación in-place.

3) `strip()` ⭐  
Qué hace: quita espacios al inicio y final.  
Así se escribe:
```py
texto = "  hola  "
resultado = texto.strip()
```
Error típico:
```py
resultado = texto.strip
```
Verás esto: `"hola"`.  
Por qué funciona: recorta whitespace en bordes.  
Lo típico que sale mal: esperar que quite espacios internos; no guardar el resultado.

4) `replace()` ⭐  
Qué hace: reemplaza un fragmento por otro.  
Así se escribe:
```py
texto = "hola mundo"
resultado = texto.replace("mundo", "Python")
```
Error típico:
```py
resultado = texto.replace("mundo")
```
Verás esto: `"hola Python"`.  
Por qué funciona: genera un string nuevo con reemplazo.  
Lo típico que sale mal: olvidar el segundo argumento; creer que modifica en sitio.

5) `split()` ⭐  
Qué hace: separa el texto en una lista.  
Así se escribe:
```py
texto = "a,b,c"
partes = texto.split(",")
```
Error típico:
```py
partes = texto.split
```
Verás esto: `['a', 'b', 'c']`.  
Por qué funciona: corta según el separador.  
Lo típico que sale mal: confundir split con slicing; usar separador incorrecto.

6) `join()`  
Qué hace: une textos con un separador.  
Así se escribe:
```py
partes = ["a", "b", "c"]
resultado = ",".join(partes)
```
Error típico:
```py
resultado = partes.join(",")
```
Verás esto: `"a,b,c"`.  
Por qué funciona: `join()` es método del separador.  
Lo típico que sale mal: pasar elementos no string; invertir el orden.

### Números (`int` / `float`)
1) `round()` ⭐  
Qué hace: redondea a n decimales.  
Así se escribe:
```py
precio = 3.1416
aprox = round(precio, 2)
```
Error típico:
```py
aprox = round("3.1416", 2)
```
Verás esto: `3.14`.  
Por qué funciona: `round` opera sobre números.  
Lo típico que sale mal: pasar strings; esperar más decimales sin indicar n.

2) `abs()` ⭐  
Qué hace: devuelve el valor absoluto.  
Así se escribe:
```py
delta = abs(-5)
```
Error típico:
```py
delta = abs[-5]
```
Verás esto: `5`.  
Por qué funciona: elimina el signo negativo.  
Lo típico que sale mal: olvidar paréntesis; pasar texto no numérico.

3) `int()` ⭐  
Qué hace: convierte a entero (trunca decimales).  
Así se escribe:
```py
cantidad = int("12")
```
Error típico:
```py
cantidad = int("12.5")
```
Verás esto: `12`.  
Por qué funciona: `int` convierte strings numéricos enteros.  
Lo típico que sale mal: usar strings con punto; asumir redondeo en vez de truncado.

4) `float()` ⭐  
Qué hace: convierte a flotante.  
Así se escribe:
```py
valor = float("3.5")
```
Error típico:
```py
valor = float("tres")
```
Verás esto: `3.5`.  
Por qué funciona: `float` interpreta strings numéricos.  
Lo típico que sale mal: usar textos no numéricos; confundir coma con punto.

5) `//` (división entera)  
Qué hace: divide y descarta decimales.  
Así se escribe:
```py
resultado = 7 // 2
```
Error típico:
```py
resultado = 7 // 0
```
Verás esto: `3`.  
Por qué funciona: aplica división entera.  
Lo típico que sale mal: división por cero; asumir que redondea (en realidad trunca).

6) `%` (módulo)  
Qué hace: devuelve el resto de una división.  
Así se escribe:
```py
resto = 7 % 2
```
Error típico:
```py
resto = 7 % 0
```
Verás esto: `1`.  
Por qué funciona: calcula el residuo.  
Lo típico que sale mal: división por cero; usarlo con floats y esperar enteros.

### Booleanos (`bool`)
1) `bool()` ⭐  
Qué hace: convierte un valor a True/False.  
Así se escribe:
```py
activo = bool(1)
```
Error típico:
```py
activo = bool("0")
```
Verás esto: `True`.  
Por qué funciona: cualquier string no vacío es True.  
Lo típico que sale mal: asumir que "0" es False; no validar entradas.

2) `not` ⭐  
Qué hace: niega una condición.  
Así se escribe:
```py
es_vacio = not True
```
Error típico:
```py
es_vacio = not
```
Verás esto: `False`.  
Por qué funciona: invierte el valor booleano.  
Lo típico que sale mal: usarlo sin operando; encadenar sin paréntesis.

3) `and` ⭐  
Qué hace: True solo si ambas condiciones son True.  
Así se escribe:
```py
permitido = True and False
```
Error típico:
```py
permitido = True and
```
Verás esto: `False`.  
Por qué funciona: evalúa ambas condiciones.  
Lo típico que sale mal: olvidar el segundo operando; confiar en el orden sin paréntesis.

4) `or` ⭐  
Qué hace: True si alguna condición es True.  
Así se escribe:
```py
permitido = False or True
```
Error típico:
```py
permitido = False or
```
Verás esto: `True`.  
Por qué funciona: basta un True para pasar.  
Lo típico que sale mal: olvidar el segundo operando; asumir que evalúa siempre ambas partes.

5) `==` (comparación)  
Qué hace: compara igualdad.  
Así se escribe:
```py
es_cero = (0 == 0)
```
Error típico:
```py
es_cero = (0 = 0)
```
Verás esto: `True`.  
Por qué funciona: `==` compara valores.  
Lo típico que sale mal: usar `=` por accidente; comparar tipos incompatibles.

6) `is` (identidad)  
Qué hace: comprueba identidad, útil con `None`.  
Así se escribe:
```py
valor = None
es_nulo = valor is None
```
Error típico:
```py
es_nulo = valor == None
```
Verás esto: `True`.  
Por qué funciona: `is` compara identidad exacta.  
Lo típico que sale mal: usar `==` en lugar de `is`; comparar objetos mutables.

### Listas (`list`)
1) `append()` ⭐  
Qué hace: agrega un elemento al final.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.append("pera")
```
Error típico:
```py
frutas.append
```
Verás esto: `['manzana', 'pera']`.  
Por qué funciona: muta la lista en sitio.  
Lo típico que sale mal: olvidar paréntesis; asumir que devuelve una lista nueva.

2) `extend()` ⭐  
Qué hace: agrega varios elementos.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.extend(["pera", "uva"])
```
Error típico:
```py
frutas.extend("uva")
```
Verás esto: `['manzana', 'pera', 'uva']`.  
Por qué funciona: recorre el iterable y añade cada elemento.  
Lo típico que sale mal: pasar un string y separar por caracteres; confundir con `append`.

3) `insert()`  
Qué hace: inserta en una posición.  
Así se escribe:
```py
frutas = ["manzana", "uva"]
frutas.insert(1, "pera")
```
Error típico:
```py
frutas.insert("1", "pera")
```
Verás esto: `['manzana', 'pera', 'uva']`.  
Por qué funciona: usa un índice entero.  
Lo típico que sale mal: índice fuera de rango; pasar índice como string.

4) `pop()` ⭐  
Qué hace: quita y devuelve el último (o por índice).  
Así se escribe:
```py
frutas = ["manzana", "pera"]
ultima = frutas.pop()
```
Error típico:
```py
frutas.pop(5)
```
Verás esto: `ultima = 'pera'`.  
Por qué funciona: elimina el elemento y lo retorna.  
Lo típico que sale mal: `IndexError` por índice inválido; mutar lista mientras iteras.

5) `remove()`  
Qué hace: elimina el primer valor encontrado.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
frutas.remove("pera")
```
Error típico:
```py
frutas.remove("uva")
```
Verás esto: `['manzana']`.  
Por qué funciona: busca el valor y lo elimina.  
Lo típico que sale mal: `ValueError` si no existe; confundir valor con índice.

6) `sort()` ⭐  
Qué hace: ordena la lista.  
Así se escribe:
```py
numeros = [3, 1, 2]
numeros.sort()
```
Error típico:
```py
ordenados = numeros.sort()
```
Verás esto: `[1, 2, 3]`.  
Por qué funciona: ordena en sitio y devuelve `None`.  
Lo típico que sale mal: esperar una lista nueva; mezclar tipos incompatibles.

7) `reverse()`  
Qué hace: invierte el orden.  
Así se escribe:
```py
numeros = [1, 2, 3]
numeros.reverse()
```
Error típico:
```py
numeros = numeros.reverse()
```
Verás esto: `[3, 2, 1]`.  
Por qué funciona: invierte en sitio.  
Lo típico que sale mal: esperar retorno; confundir con `sorted(..., reverse=True)`.

8) `len()` ⭐  
Qué hace: cuenta elementos.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
total = len(frutas)
```
Error típico:
```py
total = frutas.len()
```
Verás esto: `2`.  
Por qué funciona: `len()` es función global.  
Lo típico que sale mal: usar `.len()`; olvidar que algunas operaciones dependen del tamaño.

9) `sum()` ⭐  
Qué hace: suma los valores de la lista.  
Así se escribe:
```py
numeros = [1, 2, 3]
total = sum(numeros)
```
Error típico:
```py
total = sum([1, "2", 3])
```
Verás esto: `6`.  
Por qué funciona: suma elementos numéricos.  
Lo típico que sale mal: mezclar tipos; pasar lista vacía y esperar un promedio.

10) `max()`  
Qué hace: devuelve el mayor valor.  
Así se escribe:
```py
numeros = [4, 8, 15]
mayor = max(numeros)
```
Error típico:
```py
mayor = max([])
```
Verás esto: `15`.  
Por qué funciona: compara valores y retorna el más alto.  
Lo típico que sale mal: lista vacía (`ValueError`); mezclar tipos no comparables.

11) `min()`  
Qué hace: devuelve el menor valor.  
Así se escribe:
```py
numeros = [4, 8, 15]
menor = min(numeros)
```
Error típico:
```py
menor = min([])
```
Verás esto: `4`.  
Por qué funciona: compara valores y retorna el más bajo.  
Lo típico que sale mal: lista vacía (`ValueError`); comparar tipos incompatibles.

### DataFrame / Series (pandas)
1) `head()` ⭐  
Qué hace: muestra las primeras filas.  
Así se escribe:
```py
df.head(3)
```
Error típico:
```py
df.head
```
Verás esto: 3 filas iniciales.  
Por qué funciona: `head()` crea una vista rápida.  
Lo típico que sale mal: olvidar paréntesis; asumir que modifica el DataFrame.

2) `info()` ⭐  
Qué hace: resumen de columnas y tipos.  
Así se escribe:
```py
df.info()
```
Error típico:
```py
info = df.info
```
Verás esto: tipos, nulos y memoria.  
Por qué funciona: inspecciona la estructura.  
Lo típico que sale mal: confundir con `describe`; olvidar paréntesis.

3) `describe()` ⭐  
Qué hace: estadísticos descriptivos.  
Así se escribe:
```py
df.describe()
```
Error típico:
```py
df.describe
```
Verás esto: media, percentiles, etc.  
Por qué funciona: calcula estadísticas numéricas.  
Lo típico que sale mal: esperar columnas no numéricas; olvidar paréntesis.

4) `loc` ⭐  
Qué hace: selección por etiquetas.  
Así se escribe:
```py
df.loc[df["edad"] > 25, "edad"]
```
Error típico:
```py
df.loc[df["edad"] > 25]["edad"] = 99
```
Verás esto: columna filtrada.  
Por qué funciona: `loc` selecciona y asigna seguro.  
Lo típico que sale mal: asignación encadenada; confundir filas/columnas.

5) `iloc` ⭐  
Qué hace: selección por posición.  
Así se escribe:
```py
df.iloc[0, 1]
```
Error típico:
```py
df.iloc["0", "1"]
```
Verás esto: un valor puntual.  
Por qué funciona: usa índices enteros.  
Lo típico que sale mal: usar strings; salir de rango.

6) `groupby()` ⭐  
Qué hace: agrupa para agregaciones.  
Así se escribe:
```py
df.groupby("nombre")["edad"].mean()
```
Error típico:
```py
df.groupby("nombre").mean["edad"]
```
Verás esto: promedio por grupo.  
Por qué funciona: crea grupos y aplica agregaciones.  
Lo típico que sale mal: olvidar `()` en `mean`; agrupar por columna inexistente.

7) `merge()` ⭐  
Qué hace: une tablas por claves.  
Así se escribe:
```py
df.merge(otros, on="id")
```
Error típico:
```py
df.merge(otros)
```
Verás esto: DataFrame combinado.  
Por qué funciona: alinea por clave.  
Lo típico que sale mal: duplicar columnas; claves con tipos distintos.

8) `concat()`  
Qué hace: concatena filas o columnas.  
Así se escribe:
```py
pd.concat([df1, df2], axis=0)
```
Error típico:
```py
df1.concat(df2)
```
Verás esto: DataFrame unido.  
Por qué funciona: `concat` es función de pandas.  
Lo típico que sale mal: usar método inexistente; índices desalineados.

9) `dropna()` ⭐  
Qué hace: elimina filas/columnas con NaN.  
Así se escribe:
```py
df.dropna()
```
Error típico:
```py
df.dropna(axis="filas")
```
Verás esto: DataFrame sin nulos.  
Por qué funciona: descarta NaN según el eje.  
Lo típico que sale mal: usar axis inválido; borrar datos sin copia.

10) `fillna()` ⭐  
Qué hace: rellena NaN con un valor.  
Así se escribe:
```py
df.fillna(0)
```
Error típico:
```py
df.fillna()
```
Verás esto: NaN reemplazados por 0.  
Por qué funciona: sustituye valores faltantes.  
Lo típico que sale mal: olvidar el valor; no guardar el resultado.

11) `astype()`  
Qué hace: cambia el tipo de una columna.  
Así se escribe:
```py
df["edad"] = df["edad"].astype(int)
```
Error típico:
```py
df["edad"].astype("numero")
```
Verás esto: columna en tipo `int`.  
Por qué funciona: `astype` convierte dtype.  
Lo típico que sale mal: usar dtype inválido; convertir con valores no compatibles.

## Micro-ejemplo: orden de ejecución de celdas

### Así se escribe
```py
total = 10
resultado = total + 5
```

### Error típico: usar una variable antes de definirla
```py
resultado = total + 5
```

```py
NameError: name 'total' is not defined
```

Explicación breve: en Jupyter el orden de ejecución importa; corre la celda donde defines `total`.

## Micro-ejemplo incremental: celdas y comandos en Jupyter

### Así se escribe
```py
resultado = 3 + 4
resultado
```

### Error típico: ejecutar comandos de shell sin !
```py
pip install pandas
```

```py
SyntaxError: invalid syntax
```

Explicación breve: en Jupyter, los comandos de shell requieren `!`.

### Error típico: olvidar ejecutar la celda de import
```py
df = pd.DataFrame({"x": [1, 2]})
```

```py
NameError: name 'pd' is not defined
```

Explicación breve: asegúrate de ejecutar la celda con `import pandas as pd` antes.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Ejecutar celdas fuera de orden",
                "El resultado puede depender del orden; usa 'Restart & Run All'.",
            ),
            (
                "Confiar en variables que ya existían",
                "El kernel guarda estado; reinicia para validar la reproducibilidad.",
            ),
            (
                "Notebooks gigantes sin estructura",
                "Divide por temas y usa secciones Markdown claras.",
            ),
            (
                "Mezclar exploración con producción",
                "Pasa a .py las partes maduras y reutilizables.",
            ),
            (
                "No fijar seed en experimentos",
                "Define semillas para resultados consistentes.",
            ),
            (
                "Hardcodear rutas locales",
                "Usa rutas relativas o configuración portable.",
            ),
            (
                "No reiniciar el kernel antes de compartir",
                "Otros no reproducirán los mismos resultados.",
            ),
            (
                "Depender de variables globales",
                "Encapsula en funciones para evitar estado oculto.",
            ),
            (
                "Dejar celdas con resultados viejos",
                "Borra salidas y vuelve a ejecutar todo antes de enviar.",
            ),
            (
                "No documentar el objetivo",
                "Agrega una sección de objetivo para guiar al lector.",
            ),
            (
                "No separar datos, proceso y conclusiones",
                "Ordena el flujo para que sea legible y verificable.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Simular celdas con comentarios",
                """# Celda 1: variables
numeros = [10, 20, 30]  # Lista con datos
factor = 2  # Factor de multiplicación

# Celda 2: transformación
numeros_doblados = [n * factor for n in numeros]  # Multiplicamos cada número

# Celda 3: conclusión
promedio = sum(numeros_doblados) / len(numeros_doblados)  # Calculamos promedio
print(promedio)  # Mostramos el resultado""",
            ),
            (
                "Estado oculto: fallo típico",
                """# Celda 1
resultado = 10  # Guardamos un valor

# Celda 2
resultado = resultado + 5  # Sumamos 5

# Celda 3 (ejecutada sin la Celda 1)
print(resultado)  # Falla si resultado no existe""",
            ),
            (
                "Reset mental con función",
                """def calcular_total(base):  # Encapsulamos la lógica
    return base + 5  # Sumamos 5 de forma explícita

print(calcular_total(10))  # Resultado reproducible
print(calcular_total(0))  # Resultado reproducible""",
            ),
            (
                "Mini análisis con lista de números",
                """numeros = [4, 8, 15, 16, 23, 42]  # Datos de ejemplo

media = sum(numeros) / len(numeros)  # Calculamos la media
maximo = max(numeros)  # Calculamos el máximo
minimo = min(numeros)  # Calculamos el mínimo

print("Media:", media)  # Mostramos la media
print("Máximo:", maximo)  # Mostramos el máximo
print("Mínimo:", minimo)  # Mostramos el mínimo""",
            ),
            (
                "Markdown explicado como texto",
                """# Título del notebook  # Encabezado principal
## Objetivo  # Subtítulo
Queremos explorar datos y explicar hallazgos.  # Texto descriptivo

- Paso 1: cargar datos  # Lista de pasos
- Paso 2: limpiar datos  # Lista de pasos
- Paso 3: analizar resultados  # Lista de pasos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea la estructura de un notebook con títulos en Markdown (Título, Objetivo, Datos, Proceso, Conclusiones).",
                "hints": ["Usa # para el título y ## para secciones."],
                "solution": (
                    "# Análisis de ventas\n"
                    "## Objetivo\n"
                    "Explicar qué queremos aprender.\n"
                    "## Datos\n"
                    "Origen y descripción de los datos.\n"
                    "## Proceso\n"
                    "Pasos de limpieza y análisis.\n"
                    "## Conclusiones\n"
                    "Resultados principales y próximos pasos."
                ),
            },
            {
                "question": "Detecta el error por ejecución fuera de orden y explica por qué ocurre.",
                "hints": ["Piensa en una variable definida en otra celda."],
                "solution": (
                    "Si ejecutas una celda que usa 'total' sin haber ejecutado la celda donde se define, "
                    "el kernel no conoce la variable y aparece NameError."
                ),
            },
            {
                "question": "Convierte un bloque de notebook en una función reutilizable.",
                "hints": ["Recibe datos como parámetro y retorna el resultado."],
                "solution": (
                    "def calcular_media(valores):\n"
                    "    return sum(valores) / len(valores)\n"
                    "\n"
                    "print(calcular_media([1, 2, 3]))"
                ),
            },
            {
                "question": "Haz un 'restart & run all' mental y explica qué cambia.",
                "hints": ["Piensa en variables creadas fuera de orden."],
                "solution": (
                    "Al reiniciar y ejecutar todo en orden, solo sobreviven las variables definidas en el notebook. "
                    "Si dependías de estado oculto, el error aparecerá inmediatamente."
                ),
            },
            {
                "question": "Aplica la regla Notebook vs .py para 6 casos (idea rápida, módulo reutilizable, app completa, EDA, reporte, tests).",
                "hints": ["Usa la regla IDEA->Notebook->.py->IDE."],
                "solution": (
                    "Idea rápida: Notebook\n"
                    "EDA con datos: Notebook\n"
                    "Reporte reproducible: Notebook\n"
                    "Módulo reutilizable: .py\n"
                    "Tests y arquitectura: IDE\n"
                    "App completa: IDE"
                ),
            },
        ]
