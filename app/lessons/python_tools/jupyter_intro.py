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
