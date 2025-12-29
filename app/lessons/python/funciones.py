from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class FuncionesLesson(Lesson):
    TITLE = "Funciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["funciones", "parametros", "retorno", "scope"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es una función, cuándo usarla, cómo recibir argumentos y "
            "devolver resultados con buenas prácticas claras."
        )

    def guide(self) -> str:
        return """
## ¿Qué es una función?
Una **función** es un bloque de código con nombre que realiza una tarea. Puedes llamarla muchas veces y evita repetir pasos.

Ejemplo inmediato (explicación + ejemplo):
```
def saludar(nombre):  # Definimos una función con un parámetro
    return f"Hola {nombre}"  # return devuelve un resultado
```

## ¿Cuándo se usan las funciones?
- Cuando una acción se repite.
- Cuando quieres separar pasos en partes pequeñas.
- Cuando necesitas claridad y reutilización.

Ejemplo inmediato:
```
mensaje = saludar("Ana")  # Reutilizamos la función
```

## Conceptos previos (definidos sin asumir nada)
- **parámetro**: nombre dentro de la definición que recibe datos.
- **argumento**: valor real que pasas al llamar a la función.
- **return**: instrucción que devuelve un resultado (si no hay, se devuelve `None`).
- **scope**: alcance de una variable (dónde existe y es visible).

### Nota (CalloutBox: best_practice)
Da nombres que describan acciones: `calcular_total` es más claro que `calc`.

## Paso 1: Definir una función
Usa `def`, un nombre claro y paréntesis para los parámetros.
```
def sumar(a, b):  # Definimos la función con dos parámetros
    return a + b  # Devolvemos la suma
```

## Paso 2: Llamar a una función con argumentos
Los argumentos son los valores reales que envías.
```
resultado = sumar(3, 5)  # 3 y 5 son argumentos
```

## Paso 3: Valores por defecto
Un parámetro puede tener un valor por defecto si no envías el argumento.
```
def potencia(base, exponente=2):  # exponente tiene default
    return base ** exponente  # Calcula la potencia
```

### Advertencia (CalloutBox: best_practice)
Evita usar listas o diccionarios como default: se comparten entre llamadas.

## Paso 4: Variables locales y scope
Las variables dentro de la función son locales y no cambian las de afuera.
```
contador = 0  # Variable global

def sumar_uno():  # Definimos función
    contador_local = contador + 1  # Variable local
    return contador_local  # Devolvemos el resultado
```

## Paso 5: *args y **kwargs (recibir muchos datos)
- `*args` guarda varios argumentos posicionales en una **tupla**.
- `**kwargs` guarda argumentos con nombre en un **dict**.
```
def resumen(*args, **kwargs):  # Recibe muchos datos
    return args, kwargs  # Devuelve tupla y diccionario
```

## Paso 6: Métodos dentro de funciones
Si usas un método, explícalo: `append` agrega un elemento a una lista.
```
def agregar_item(lista, item):  # Función que modifica una lista
    lista.append(item)  # append agrega el item al final
    return lista  # Devuelve la lista actualizada
```

### Best practice (CalloutBox: best_practice)
Si una función modifica una lista, indícalo en el nombre o en la docstring.

## Paso 7: Docstrings simples
Una docstring es un texto dentro de la función que explica lo que hace.
```
def promedio(valores):  # Función de ejemplo
    '''Calcula el promedio de una lista de números.'''  # Docstring
    return sum(valores) / len(valores)  # Calcula y devuelve
```

## Paso 8: Type hints sin miedo
Los hints no cambian la ejecución, pero ayudan a leer y evitar errores.
```
def area_cuadrado(lado: float) -> float:  # Hint de entrada y salida
    return lado * lado  # Devuelve el área
```

## Paso 9: Buenas prácticas clave
- Usa **snake_case** para nombres.
- Mantén funciones cortas y con un solo objetivo.
- Evita efectos secundarios si no son necesarios.

### Best practice (CalloutBox: best_practice)
Escribe pruebas simples con ejemplos reales para validar tu función.

## Más allá (nivel pro)
- Aprende sobre funciones de orden superior (`map`, `filter`, `sorted`).
- Estudia closures y cómo capturan variables del scope externo.
- Explora decoradores para añadir comportamiento sin repetir código.
- Usa `typing` avanzado (`Iterable`, `Callable`) para proyectos grandes.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Mutable como default",
                "`def f(x=[]):` comparte la misma lista en cada llamada. Usa None y crea la lista dentro.",
            ),
            (
                "Olvidar return",
                "Si no usas return, la función devuelve None y puede romper cálculos.",
            ),
            (
                "Confundir parámetros y argumentos",
                "Parámetro es el nombre en la definición; argumento es el valor real.",
            ),
            (
                "Orden incorrecto de parámetros",
                "Los parámetros con default deben ir después de los que no tienen default.",
            ),
            (
                "Modificar datos sin avisar",
                "Si una función modifica una lista, puede sorprender; documenta el efecto.",
            ),
            (
                "Reusar nombres",
                "Si llamas a una variable igual que una función, sobrescribes la función.",
            ),
            (
                "Scope global confuso",
                "Modificar variables globales dentro de funciones hace el código difícil de seguir.",
            ),
            (
                "Usar print en lugar de return",
                "print solo muestra; return permite reutilizar el resultado.",
            ),
            (
                "Args y kwargs mal usados",
                "*args es tupla de posicionales y **kwargs es dict de nombrados.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Función básica",
                """def saludar(nombre):  # Definimos la función
    mensaje = f"Hola {nombre}"  # Creamos el saludo
    return mensaje  # Devolvemos el resultado
print(saludar("Ana"))  # Llamamos a la función""",
            ),
            (
                "Parámetros y argumentos",
                """def sumar(a, b):  # Dos parámetros
    return a + b  # Retorna la suma
resultado = sumar(2, 5)  # Enviamos argumentos
print(resultado)  # Mostramos el resultado""",
            ),
            (
                "Valores por defecto",
                """def potencia(base, exponente=2):  # Default en exponente
    return base ** exponente  # Calcula potencia
print(potencia(3))  # Usa el default
print(potencia(3, 3))  # Usa el argumento""",
            ),
            (
                "*args en acción",
                """def suma_todos(*nums):  # Recibe muchos números
    total = sum(nums)  # sum calcula la suma
    return total  # Devuelve el total
print(suma_todos(1, 2, 3))  # Probamos la función""",
            ),
            (
                "**kwargs en acción",
                """def perfil(**datos):  # Recibe datos con nombre
    return datos  # Devuelve un dict
print(perfil(nombre="Luis", edad=30))  # Enviamos argumentos con nombre""",
            ),
            (
                "Scope local",
                """x = 10  # Variable global
def mostrar():  # Función
    x = 5  # Variable local
    print(x)  # Imprime 5
mostrar()  # Ejecutamos
print(x)  # Imprime 10""",
            ),
            (
                "Docstring",
                """def promedio(valores):  # Definimos función
    '''Calcula el promedio de números.'''  # Docstring
    return sum(valores) / len(valores)  # Calculamos
print(promedio([1, 2, 3]))  # Probamos""",
            ),
            (
                "Modificar listas con append",
                """def agregar(lista, item):  # Recibe una lista
    lista.append(item)  # append agrega al final
    return lista  # Devuelve la lista
print(agregar(["a"], "b"))  # Probamos la función""",
            ),
            (
                "Type hints",
                """def area_cuadrado(lado: float) -> float:  # Hint de tipos
    return lado * lado  # Calculamos el área
print(area_cuadrado(4))  # Ejecutamos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función que reciba una lista de números y devuelva el mayor.",
                "hints": ["Puedes usar max()", "Valida que la lista no esté vacía."],
                "solution": "def mayor(nums):\n    if not nums:\n        return None\n    return max(nums)",
            },
            {
                "question": "Escribe una función que acepte *args y devuelva la suma de pares.",
                "hints": ["Filtra con n % 2 == 0"],
                "solution": "def suma_pares(*nums):\n    return sum(n for n in nums if n % 2 == 0)",
            },
            {
                "question": "Crea una función que reciba nombre y apellido y devuelva 'Apellido, Nombre'.",
                "hints": ["Usa f-strings"],
                "solution": "def formato(nombre, apellido):\n    return f\"{apellido}, {nombre}\"",
            },
            {
                "question": "Define una función con un parámetro por defecto que salude en español.",
                "hints": ["El default puede ser 'es'"],
                "solution": "def saludar(nombre, idioma='es'):\n    return f\"Hola {nombre}\" if idioma == 'es' else f\"Hello {nombre}\"",
            },
            {
                "question": "Crea una función que reciba una lista y un item, y lo agregue con append.",
                "hints": ["Retorna la lista"],
                "solution": "def agregar(lista, item):\n    lista.append(item)\n    return lista",
            },
            {
                "question": "Crea una función que devuelva el cuadrado de un número con type hints.",
                "hints": ["Usa -> int o -> float"],
                "solution": "def cuadrado(n: int) -> int:\n    return n * n",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo simple: prueba las funciones en los ejemplos."))
        return widget
