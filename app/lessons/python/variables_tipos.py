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
            "Aprende cómo Python guarda datos en variables, cómo funcionan los tipos, "
            "y por qué la mutabilidad y las copias importan desde el primer día."
        )

    def guide(self) -> str:
        return """
## Empezamos desde cero: ¿qué es una variable?
Una **variable** es un nombre que apunta a un valor en memoria. No es una caja física, es una *etiqueta*.

Imagina un post-it pegado a un objeto: el post-it es el nombre, el objeto es el valor.
```
mensaje = "Hola"  # La variable 'mensaje' apunta a un texto
```

### Tipado dinámico en palabras simples
Python es de **tipado dinámico**: el nombre puede apuntar a valores de distinto tipo en distintos momentos.
```
edad = 20  # Ahora edad apunta a un int
edad = "veinte"  # Ahora apunta a un str
```

### Tipos básicos que usarás todo el tiempo
- **int**: números enteros (10, -3)
- **float**: números con decimales (3.14)
- **str**: texto ("hola")
- **bool**: verdadero o falso (True/False)
- **list, tuple, dict, set**: estructuras para guardar varios datos

Ejemplo inmediato:
```
precio = 19.99  # float
nombre = "Ana"  # str
activo = True  # bool
```

## Mutabilidad: ¿qué puede cambiar y qué no?
**Mutable** significa que el valor se puede modificar sin crear uno nuevo.
- Listas y diccionarios: mutables.
- Strings y tuplas: inmutables.

Ejemplo con lista (mutable):
```
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # Cambia la misma lista
```

Ejemplo con string (inmutable):
```
texto = "hola"  # String inicial
texto = texto.upper()  # Crea un nuevo string
```

## Referencia vs copia (muy importante)
Cuando haces `b = a`, **no copias** el objeto, solo creas otra referencia.
```
original = [1, 2]  # Lista original
alias = original  # alias apunta al mismo objeto
alias.append(3)  # Cambiamos el mismo objeto
```
Para copiar de verdad:
```
original = [1, 2]  # Lista original
copia = original.copy()  # Copia real
copia.append(3)  # Solo cambia la copia
```

## Conversión explícita: no adivines, convierte
No mezcles tipos sin convertir. Es más claro y seguro.
```
texto = "42"  # str
numero = int(texto)  # convertimos a int
```

## None: “aún no tengo valor”
`None` indica ausencia de valor, no es 0 ni "".
```
resultado = None  # No hay valor todavía
if resultado is None:  # Comparación correcta
    print("Falta calcular")
```

## Buenas prácticas desde el inicio
- **PEP8**: usa `snake_case` para variables y funciones, `PascalCase` para clases.
- **Indentación**: 4 espacios, evita tabs.
- **Nombres claros**: mejor `total_ventas` que `tv`.
- **Evita magic numbers**: usa constantes con nombre.
- **Claridad > trucos**: el código se lee más veces de las que se escribe.

Ejemplo con constantes y nombres claros:
```
IVA = 0.21  # Constante con nombre
precio_base = 100  # Nombre claro
precio_final = precio_base * (1 + IVA)  # Cálculo legible
```

### Tip (pequeña ayuda)
Si dudas del tipo, usa `type(valor)` o imprime el valor para entenderlo.

## Resumen de ejemplos
```
usuario = "Marta"  # Variable tipo str
edad = 31  # Variable tipo int
```
```
lista = [1, 2]  # Lista mutable
lista.append(3)  # Modificamos en sitio
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar b = a en listas no copia, solo crea un alias. Usa list(a) o a.copy().",
            ),
            (
                "Mezclar tipos en operaciones",
                '"3" + 4 produce error: str e int no se concatenan sin conversión.',
            ),
            (
                "Mutabilidad en argumentos",
                "Listas o dicts mutables como valores por defecto en funciones se comparten.",
            ),
            (
                "Comparar con == en lugar de is",
                "Para comparar con None usa `is None`, no `== None`.",
            ),
            (
                "Shadowing de builtins",
                "Nombrar variables como list, dict o str sobrescribe funciones útiles.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Asignación y reasignación",
                """nombre = "Ana"  # Creamos un string
nombre = 3.14  # Reasignamos a float
print(nombre)  # Mostramos el valor""",
            ),
            (
                "Mutabilidad y alias",
                """nums = [1, 2]  # Lista mutable
alias = nums  # Alias a la misma lista
alias.append(3)  # Modificamos la lista
print(nums)  # Se ve el cambio""",
            ),
            (
                "Copia segura",
                """original = [1, 2]  # Lista original
copia = original.copy()  # Copia independiente
copia.append(99)  # Cambiamos la copia
print(original)  # Original intacta""",
            ),
            (
                "Conversión explícita",
                """texto = "42"  # Texto numérico
numero = int(texto)  # Convertimos a int
print(numero + 1)  # Sumamos uno""",
            ),
            (
                "Uso de None",
                """valor = None  # Sin valor
if valor is None:  # Comparación correcta
    print("Sin valor")  # Mensaje""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Explica la diferencia entre una copia superficial y un alias.",
                "hints": ["Piensa en listas", "¿Qué pasa si modificas uno?"],
                "solution": "Un alias apunta al mismo objeto; una copia crea un objeto distinto.",
            },
            {
                "question": "Crea una tupla con un solo elemento 'python'.",
                "hints": ["La coma es obligatoria"],
                "solution": "tupla = (\"python\",)",
            },
            {
                "question": "Convierte la cadena '3.14' en float y súmale 1.",
                "hints": ["Usa float()"],
                "solution": "valor = float('3.14')\nprint(valor + 1)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
