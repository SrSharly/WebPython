from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class VariablesTiposLesson(Lesson):
    TITLE = "Variables y tipos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["variables", "tipos", "mutabilidad", "tipado-dinámico"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es una variable, cómo funcionan los tipos, y por qué "
            "la mutabilidad, las copias y las conversiones importan en tu día a día."
        )

    def guide(self) -> str:
        return """
## ¿Qué es una variable?
Una **variable** es un nombre que apunta a un valor. No es una caja física: es una etiqueta que señala un dato en memoria.

Ejemplo inmediato (explicación + ejemplo):
```
mensaje = "Hola"  # La variable apunta a un texto (str)
```

## ¿Cuándo se usan las variables?
Las usas siempre que quieras **guardar** un resultado, **reutilizar** un dato o **darle un nombre** a algo para que el código sea legible.

Ejemplo inmediato:
```
precio = 19.99  # Guardamos un número con decimales (float)
```

## Conceptos previos (definidos sin asumir nada)
- **tipo**: categoría del dato (int, float, str, bool, lista, tupla, etc.).
- **objeto**: el dato real en memoria al que la variable apunta.
- **mutable**: se puede cambiar el contenido sin crear un objeto nuevo.
- **inmutable**: no se puede cambiar el contenido; se crea uno nuevo.
- **método**: función asociada a un objeto (por ejemplo, `append` en listas).

### Nota (CalloutBox: best_practice)
Usa nombres que expliquen el dato: `total_ventas` es más claro que `tv`.

## Paso 1: Asignar un valor con claridad
Asignar es dar un valor a una variable con `=`.
```
edad = 20  # int: número entero
```

## Paso 2: Reconocer tipos básicos
Tipos básicos que verás todos los días:
- **int**: 10, -3
- **float**: 3.14, -0.5
- **str**: "hola"
- **bool**: True/False

Ejemplo inmediato:
```
usuario = "Ana"  # str: texto
activo = True  # bool: verdadero o falso
```

## Paso 3: Entender el tipado dinámico
Python es de **tipado dinámico**: una misma variable puede apuntar a otro tipo después.
```
edad = 20  # int
edad = "veinte"  # str
```

### Advertencia (CalloutBox: best_practice)
No abuses del cambio de tipo: mantiene el código predecible.

## Paso 4: Mutabilidad con ejemplos inmediatos
Una **lista** es mutable: puedes modificarla en el mismo objeto.
```
compras = ["pan", "leche"]  # lista mutable
compras.append("café")  # append agrega un elemento al final de la lista
```

Un **str** es inmutable: `upper` devuelve un nuevo texto en mayúsculas.
```
texto = "hola"  # str inmutable
texto_mayus = texto.upper()  # upper crea un nuevo texto en mayúsculas
```

### Best practice (CalloutBox: best_practice)
Si necesitas cambiar texto, crea una nueva variable como `texto_mayus` para mantener claridad.

## Paso 5: Referencias vs copias
Cuando haces `b = a`, no copias el objeto: solo creas otro nombre para lo mismo.
```
original = [1, 2]  # lista original
alias = original  # alias apunta al mismo objeto
alias.append(3)  # modifica la misma lista
```

Para copiar de verdad, usa `copy()`:
```
original = [1, 2]  # lista original
copia = original.copy()  # copia independiente
copia.append(3)  # solo cambia la copia
```

### Nota (CalloutBox: best_practice)
Si vas a modificar una lista sin afectar el original, crea una copia primero.

## Paso 6: Conversión explícita de tipos
Convertir es transformar un tipo a otro con funciones como `int()` o `float()`.
```
texto = "42"  # str con un número
numero = int(texto)  # int: conversión explícita
```

## Paso 7: El valor especial None
`None` significa “aún no tengo valor”. No es 0 ni "".
```
resultado = None  # ausencia de valor
if resultado is None:  # comparación correcta
    print("Falta calcular")  # print muestra texto en pantalla
```

## Paso 8: Buenas prácticas de naming
- Usa **snake_case** en variables y funciones.
- Evita nombres que oculten funciones internas como `list` o `str`.

### Best practice (CalloutBox: best_practice)
Mantén nombres consistentes en todo el archivo: mejora la lectura en equipo.

## Más allá (nivel pro)
- **Copia superficial vs copia profunda (deep copy = copia total)**: una copia superficial
  duplica la lista principal pero mantiene referencias internas; la profunda copia todo.
  ```
  import copy  # importamos el módulo de copias
  matriz = [[1], [2]]  # lista con listas internas
  copia_superficial = matriz.copy()  # copia solo la lista externa
  copia_profunda = copy.deepcopy(matriz)  # copia todo el contenido
  copia_superficial[0].append(9)  # modifica también la matriz original
  ```
  Úsalo cuando tengas estructuras anidadas y necesites independencia real.
  Evítalo cuando la estructura sea plana: una copia superficial suele ser suficiente.
- **`is` para identidad, `==` para valores**: `is` comprueba si son el mismo objeto,
  `==` compara el contenido.
  ```
  valor = None  # ausencia de valor
  print(valor is None)  # True: identidad con None
  print([1, 2] == [1, 2])  # True: mismos valores
  ```
  Úsalo cuando compares con `None` o quieras saber si es el mismo objeto.
  Evítalo para comparar números o textos: ahí debe ir `==`.
- **`dataclass` (clase de datos simple)**: agrupa datos relacionados con menos código.
  ```
  from dataclasses import dataclass  # importamos dataclass
  @dataclass  # decorador para clases de datos
  class Producto:  # clase con datos
      nombre: str  # nombre del producto
      precio: float  # precio del producto
  cafe = Producto("Café", 2.5)  # creamos una instancia
  ```
  Úsalo cuando necesites agrupar campos con nombres claros.
  Evítalo si solo necesitas una variable simple o un dict temporal.
- **Constantes con nombres claros**: usar mayúsculas indica “no cambiar”.
  ```
  IVA = 0.21  # constante fiscal
  precio_base = 100  # variable normal
  precio_final = precio_base * (1 + IVA)  # cálculo
  ```
  Úsalo para valores estables que se repiten en el proyecto.
  Evítalo si el valor cambia durante la ejecución.
- **Evitar efectos secundarios con mutables**: modifica una copia si no quieres
  afectar al valor original.
  ```
  def agregar_item(lista, item):  # función de ejemplo
      nueva_lista = lista.copy()  # copiamos antes de modificar
      nueva_lista.append(item)  # cambiamos la copia
      return nueva_lista  # devolvemos nueva lista
  ```
  Úsalo cuando una función no debe alterar los datos que recibe.
  Evítalo cuando quieras modificar “en sitio” por rendimiento o claridad explícita.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar b = a en listas no copia, solo crea un alias. Usa a.copy() si quieres independencia.",
            ),
            (
                "Mezclar tipos en operaciones",
                "\"3\" + 4 falla porque str e int no se combinan sin convertir.",
            ),
            (
                "Cambiar de tipo sin avisar",
                "Reusar la misma variable con tipos distintos vuelve confuso el código.",
            ),
            (
                "Usar == en vez de is con None",
                "Para comprobar ausencia de valor usa `is None`.",
            ),
            (
                "Mutables como default en funciones",
                "Listas o dicts como valores por defecto se comparten entre llamadas.",
            ),
            (
                "Crear listas con *",
                "[[0]] * 3 repite referencias: modificar un elemento afecta a todos.",
            ),
            (
                "Olvidar que str es inmutable",
                "Métodos como upper devuelven un nuevo texto; no modifican el original.",
            ),
            (
                "Nombrar variables como list o dict",
                "Sobrescribes funciones útiles del lenguaje y pierdes acceso a ellas.",
            ),
            (
                "Confundir 0 con None",
                "0 puede ser un valor válido; None indica ausencia de valor.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Asignación básica",
                """nombre = "Ana"  # Guardamos un texto en una variable
print(nombre)  # print muestra el contenido en pantalla""",
            ),
            (
                "Reasignación con otro tipo",
                """edad = 20  # Guardamos un int
edad = "veinte"  # Ahora la misma variable guarda un str
print(edad)  # Mostramos el nuevo valor""",
            ),
            (
                "Lista mutable con append",
                """compras = ["pan", "leche"]  # Creamos una lista
compras.append("café")  # append agrega un elemento al final
print(compras)  # Mostramos la lista actualizada""",
            ),
            (
                "String inmutable con upper",
                """texto = "hola"  # Creamos un string
texto_mayus = texto.upper()  # upper devuelve un nuevo texto en mayúsculas
print(texto)  # Mostramos el original sin cambios
print(texto_mayus)  # Mostramos el nuevo texto""",
            ),
            (
                "Alias vs copia",
                """original = [1, 2]  # Lista original
alias = original  # Alias al mismo objeto
alias.append(3)  # Modificamos el mismo objeto
print(original)  # Se ve el cambio""",
            ),
            (
                "Copia independiente",
                """original = [1, 2]  # Lista original
copia = original.copy()  # Copia real
copia.append(99)  # Modificamos la copia
print(original)  # Original intacta""",
            ),
            (
                "Conversión de tipos",
                """texto = "42"  # Texto numérico
numero = int(texto)  # Convertimos a int
print(numero + 1)  # Sumamos uno""",
            ),
            (
                "Uso de None",
                """valor = None  # Sin valor aún
if valor is None:  # Comprobamos ausencia de valor
    print("Sin valor")  # Mensaje informativo""",
            ),
            (
                "Longitud con len",
                """datos = ["a", "b", "c"]  # Lista con tres elementos
cantidad = len(datos)  # len devuelve la cantidad de elementos
print(cantidad)  # Mostramos la longitud""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una variable llamada ciudad con el valor 'Lima' y muéstrala.",
                "hints": ["Usa print"],
                "solution": "ciudad = 'Lima'\nprint(ciudad)",
            },
            {
                "question": "Convierte la cadena '3.14' a float y súmale 1.",
                "hints": ["Usa float()"],
                "solution": "valor = float('3.14')\nprint(valor + 1)",
            },
            {
                "question": "Crea una lista con tres frutas y agrega una cuarta con append.",
                "hints": ["Lista con []", "append agrega al final"],
                "solution": "frutas = ['manzana', 'pera', 'uva']\nfrutas.append('naranja')\nprint(frutas)",
            },
            {
                "question": "Demuestra que una copia de lista no cambia al modificar la copia.",
                "hints": ["Usa copy()"],
                "solution": "original = [1, 2]\ncopia = original.copy()\ncopia.append(3)\nprint(original)",
            },
            {
                "question": "Guarda None en una variable llamada resultado y compruébalo con is.",
                "hints": ["Usa if"],
                "solution": "resultado = None\nif resultado is None:\n    print('Sin resultado')",
            },
            {
                "question": "Crea un texto en minúsculas y una versión en mayúsculas usando upper.",
                "hints": ["upper devuelve un nuevo string"],
                "solution": "texto = 'hola'\ntexto_mayus = texto.upper()\nprint(texto_mayus)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
