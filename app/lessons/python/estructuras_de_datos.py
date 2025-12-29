from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class EstructurasDatosLesson(Lesson):
    TITLE = "Estructuras de datos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["listas", "tuplas", "diccionarios", "sets"]

    def summary(self) -> str:
        return (
            "Aprende las estructuras de datos básicas de Python: listas, tuplas, "
            "diccionarios y conjuntos, con ejemplos claros y buenas prácticas."
        )

    def guide(self) -> str:
        return """
## ¿Por qué necesitas estructuras de datos?
Sirven para guardar **varios valores** juntos y trabajar con ellos de forma organizada.

## Listas (mutables y ordenadas)
```
frutas = ["manzana", "pera", "uva"]
frutas.append("mango")
```

## Tuplas (inmutables y ordenadas)
```
coordenadas = (10, 20)
```

## Diccionarios (clave → valor)
```
usuario = {"nombre": "Ana", "edad": 30}
```

## Sets (sin duplicados, sin orden)
```
colores = {"rojo", "azul", "rojo"}  # Dupes se eliminan
```

## Acceder y modificar
- Lista: `frutas[0]`
- Diccionario: `usuario["nombre"]`

Ejemplo inmediato:
```
usuario = {"nombre": "Ana", "edad": 30}
usuario["edad"] = 31
```

## Buenas prácticas
- **PEP8**: nombres en `snake_case`.
- **Claridad**: elige la estructura correcta.
- **Evita magic numbers**: usa constantes para índices importantes.
- **No modifiques mientras iteras**: crea copias si es necesario.

## Resumen de ejemplos
```
lista = [1, 2, 3]
lista.append(4)
```
```
config = {"debug": True}
config["debug"] = False
```

## Más allá (nivel pro)
- **List comprehension (listas por comprensión)**: generan listas de forma clara.
  ```
  numeros = [1, 2, 3, 4]  # lista base
  pares = [n for n in numeros if n % 2 == 0]  # filtramos pares
  print(pares)  # muestra [2, 4]
  ```
  Úsalo cuando una transformación sea corta y legible.
  Evítalo si la lógica es compleja: usa un for con nombre claro.
- **`dict.get` con valor por defecto**: evita errores al pedir claves.
  ```
  usuario = {"nombre": "Ana"}  # dict sin edad
  edad = usuario.get("edad", 0)  # 0 si falta la clave
  print(edad)  # muestra 0
  ```
  Úsalo cuando la clave puede faltar y tengas un valor razonable.
  Evítalo si la ausencia es un error que debe reportarse.
- **Sets para pertenencia rápida**: `in` en sets es más eficiente.
  ```
  permisos = {"leer", "escribir"}  # set de permisos
  puede_editar = "escribir" in permisos  # comprobamos pertenencia
  print(puede_editar)  # True
  ```
  Úsalo para listas grandes donde necesitas búsquedas frecuentes.
  Evítalo si el orden de los elementos es importante.
- **Tuplas para datos fijos**: una tupla comunica “no modificar”.
  ```
  punto = (10, 20)  # coordenadas fijas
  x, y = punto  # desempaquetamos
  print(x, y)  # mostramos
  ```
  Úsalo cuando los datos sean inmutables por diseño.
  Evítalo si necesitas añadir o quitar elementos.
- **`defaultdict` (dict con valor automático)**: simplifica conteos.
  ```
  from collections import defaultdict  # importamos
  conteos = defaultdict(int)  # valor inicial 0
  for letra in "banana":  # recorremos texto
      conteos[letra] += 1  # sumamos por letra
  print(conteos["a"])  # muestra 3
  ```
  Úsalo para contadores o agrupaciones sencillas.
  Evítalo si necesitas controlar manualmente cada clave.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Usar lista cuando necesitas diccionario",
                "Si necesitas buscar por clave, usa dict.",
            ),
            (
                "Olvidar que las tuplas son inmutables",
                "No puedes cambiar elementos de una tupla.",
            ),
            (
                "Acceso a clave inexistente",
                "Usa dict.get() si la clave puede faltar.",
            ),
            (
                "Esperar orden en sets",
                "Los sets no mantienen orden.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Lista",
                """frutas = ["manzana", "pera"]  # Lista
frutas.append("uva")  # Agregamos
print(frutas)  # Mostramos""",
            ),
            (
                "Tupla",
                """coordenadas = (10, 20)  # Tupla
x = coordenadas[0]  # Accedemos
print(x)  # Mostramos""",
            ),
            (
                "Diccionario",
                """usuario = {"nombre": "Ana", "edad": 30}  # Dict
usuario["edad"] = 31  # Actualizamos
print(usuario)  # Mostramos""",
            ),
            (
                "Set",
                """colores = {"rojo", "azul", "rojo"}  # Set
colores.add("verde")  # Añadimos
print(colores)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una lista con tres ciudades y agrega una cuarta.",
                "hints": ["Usa append()"],
                "solution": "ciudades = ['Madrid', 'Lima', 'Bogotá']\nciudades.append('Quito')",
            },
            {
                "question": "Crea un diccionario con nombre y edad, y cambia la edad.",
                "hints": ["Usa dict[clave] = valor"],
                "solution": "persona = {'nombre': 'Ana', 'edad': 20}\npersona['edad'] = 21",
            },
            {
                "question": "Crea un set con números y verifica que no haya duplicados.",
                "hints": ["Los sets eliminan duplicados"],
                "solution": "numeros = {1, 2, 2, 3}\nprint(numeros)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Explora estructuras básicas en los ejemplos."))
        return widget
