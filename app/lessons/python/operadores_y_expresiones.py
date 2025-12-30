from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class OperadoresExpresionesLesson(Lesson):
    TITLE = "Operadores y expresiones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["operadores", "expresiones", "aritmetica", "comparacion"]

    def summary(self) -> str:
        return (
            "Conoce los operadores de Python (aritméticos, comparación y lógicos) "
            "y cómo combinarlos en expresiones claras desde cero."
        )

    def guide(self) -> str:
        return """
## ¿Qué es una expresión?
Una **expresión** es un fragmento de código que produce un valor.
```
resultado = 2 + 3  # Expresión que devuelve 5
```

## Operadores aritméticos
Los más comunes:
- `+` suma
- `-` resta
- `*` multiplicación
- `/` división (siempre float)
- `//` división entera
- `%` módulo (resto)
- `**` potencia

Ejemplo inmediato:
```
precio = 100
iva = 0.21
total = precio + (precio * iva)
```

### Así se escribe: operaciones básicas con tipos
```py
subtotal = 80
impuesto = 0.2
total = subtotal + (subtotal * impuesto)
division = subtotal / 2  # float
entero = subtotal // 3  # int
```

### Error típico: dividir esperando int
```py
mitad = 5 / 2
mensaje = "Mitad: " + mitad
```

```py
TypeError: can only concatenate str (not "float") to str
```

Explicación breve: `/` devuelve `float`. Convierte con `str()` o usa `//` si quieres entero.

### Así se escribe: usar input y print con operadores
```py
base = int(input("Base: "))
altura = int(input("Altura: "))
area = (base * altura) / 2
print("Área:", area)
```

### Error típico: no convertir input antes de operar
```py
base = input("Base: ")
altura = input("Altura: ")
area = (base * altura) / 2
```

```py
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Explicación breve: convierte a `int` o `float` antes de multiplicar o dividir.

## Operadores de comparación
Devuelven `True` o `False`:
- `==` igual
- `!=` distinto
- `>` mayor
- `<` menor
- `>=` mayor o igual
- `<=` menor o igual

Ejemplo:
```
edad = 20
es_adulto = edad >= 18
```

### Así se escribe: comparar y guardar booleanos
```py
precio = 120
es_caro = precio > 100
resultado = "caro" if es_caro else "barato"
```

### Error típico: usar = en lugar de ==
```py
precio = 120
es_caro = precio = 100
```

```py
SyntaxError: cannot assign to expression
```

Explicación breve: `=` asigna y `==` compara. Para comparaciones usa `==`.

## Operadores lógicos
Se usan para combinar condiciones:
- `and` (y)
- `or` (o)
- `not` (no)

Ejemplo:
```
tiene_credencial = True
es_mayor = True
puede_entrar = tiene_credencial and es_mayor
```

### Así se escribe: combinar condiciones
```py
tiene_ticket = True
es_mayor = False
puede_pasar = tiene_ticket and es_mayor
```

### Error típico: confundir operadores lógicos y bitwise
```py
tiene_ticket = True
es_mayor = False
puede_pasar = tiene_ticket & es_mayor
```

```py
TypeError: unsupported operand type(s) for &: 'bool' and 'bool'
```

Explicación breve: usa `and`/`or` para lógica booleana. `&` es bitwise.

## Prioridad de operadores (orden de evaluación)
Si dudas del orden, usa paréntesis para claridad.
```
resultado = (2 + 3) * 4
```

## Ejemplo principal guiado
Aprende / Haz / Verás / Por qué / Pitfalls con una expresión real.

Aprende: verás cómo combinar operadores aritméticos y comparaciones en una sola expresión.

Haz esto:
```py
subtotal = 50
descuento = 0.1
total = subtotal - (subtotal * descuento)
es_oferta = total < 45
print(total, es_oferta)
```

Verás esto:
```py
45.0 True
```

Por qué funciona: la multiplicación se evalúa antes que la resta y la comparación devuelve `bool`.

Pitfalls: olvidar paréntesis o asumir que `/` devuelve `int`.

## Buenas prácticas
- **PEP8**: espacios alrededor de operadores (`a + b`).
- **Evita magic numbers**: usa constantes.
- **Claridad primero**: paréntesis cuando haya duda.

## Resumen de ejemplos
```
numero = 10
es_par = (numero % 2) == 0
```
```
valor = 5
mensaje = "alto" if valor > 3 else "bajo"
```


## Micro-ejemplo incremental: sintaxis y errores reales

### Así se escribe
```py
numero = 6
resultado = numero * 2
mensaje = "Doble: " + str(resultado)
print(mensaje)

estado = True
valor = None
if valor is None and estado:
    valor = 0
```

### Error típico: concatenar texto y número
```py
numero = 6
mensaje = "Doble: " + numero
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: convierte el número con `str()` o usa f-strings.

### Error típico: operar con texto como número
```py
numero = "6"
resultado = numero / 2
```

```py
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Explicación breve: convierte el texto a `int` o `float` antes de dividir.

### Error típico: operar con None
```py
valor = None
resultado = valor + 1
```

```py
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Explicación breve: valida `None` con `is None` antes de usarlo.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir = con ==",
                "= asigna, == compara.",
            ),
            (
                "Olvidar paréntesis",
                "Puede cambiar el resultado en expresiones largas.",
            ),
            (
                "Usar / esperando int",
                "La división / siempre devuelve float; usa // si quieres entero.",
            ),
            (
                "Comparar floats sin tolerancia",
                "Los floats tienen redondeos; usa round si necesitas precisión.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Aritmética básica",
                """a = 8  # Valor A
b = 3  # Valor B
suma = a + b  # Suma
resta = a - b  # Resta
print(suma, resta)  # Mostramos""",
            ),
            (
                "Comparaciones",
                """edad = 20  # Edad
es_adulto = edad >= 18  # Comparación
print(es_adulto)  # Resultado""",
            ),
            (
                "Lógicos",
                """tiene_ticket = True  # Condición 1
es_mayor = False  # Condición 2
puede_pasar = tiene_ticket and es_mayor  # AND lógico
print(puede_pasar)  # Resultado""",
            ),
            (
                "División entera y módulo",
                """total = 17  # Total
cajas = total // 5  # División entera
sobran = total % 5  # Resto
print(cajas, sobran)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Calcula el precio final con IVA usando una constante.",
                "hints": ["Define IVA = 0.21"],
                "solution": "IVA = 0.21\nprecio = 100\nfinal = precio * (1 + IVA)",
            },
            {
                "question": "Comprueba si un número es múltiplo de 3.",
                "hints": ["Usa el operador %"],
                "solution": "numero = 9\nes_multiplo = (numero % 3) == 0",
            },
            {
                "question": "Crea una expresión que diga si una persona puede entrar: mayor de edad y con ticket.",
                "hints": ["Usa and"],
                "solution": "es_mayor = True\ntiene_ticket = True\npuede_entrar = es_mayor and tiene_ticket",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Practica los operadores en los ejemplos."))
        return widget
