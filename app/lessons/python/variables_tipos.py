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
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: variables y tipos como base de todo
Una variable es el nombre que le damos a un dato para reutilizarlo. Los tipos nos dicen **qué clase de dato es** y cómo
se comporta: no es lo mismo sumar enteros, concatenar textos o modificar una lista. Si entiendes esto, evitas errores
clásicos como mezclar números con texto, perder cambios en listas o confundir `None` con un valor real. La idea aquí es
ir paso a paso, con un patrón repetible, para que puedas explicar y depurar tu propio código sin adivinar.

## Paso 1: Nombrar datos con intención
Nombrar bien las variables es la primera práctica de claridad: el nombre explica el propósito antes de leer el código.

**Aprende esto**
- Aprenderás a crear variables con significado y a reutilizarlas en mensajes.
- Verás que una variable es una etiqueta, no un contenedor mágico.

**Haz esto**
print("ok")  # Confirmamos
```
nombre = "Ana"  # Guardamos un nombre en texto
apellido = "López"  # Guardamos el apellido en texto
separador = " "  # Definimos un espacio para unir textos
nombre_completo = nombre + separador + apellido  # Construimos el nombre completo
rol = "Cliente"  # Definimos el rol que queremos mostrar
mensaje = rol + ": " + nombre_completo  # Creamos el mensaje final
longitud = len(mensaje)  # Medimos cuántos caracteres tiene
print(mensaje)  # Mostramos el mensaje
print(longitud)  # Mostramos la longitud
print("ok")  # Confirmamos
```

**Verás esto**
Verás un texto como `Cliente: Ana López` y un número con la longitud del mensaje.

**Por qué funciona**
Cada variable apunta a un texto distinto y el operador `+` concatena esos textos en orden. `len()` cuenta caracteres y
confirma que tu mensaje no es vacío.

**Lo típico que sale mal**
- Usar nombres genéricos como `x` o `tmp` y perder el significado del dato.
- Olvidar espacios al concatenar y obtener textos pegados.

## Paso 2: Reconocer tipos básicos
Python tiene tipos básicos como `int`, `float`, `str` y `bool`. Saberlos evita operaciones inválidas.

**Aprende esto**
- Aprenderás a identificar el tipo con `type()` y a decidir qué operaciones son válidas.
- Verás cómo convertir un número a texto para mostrarlo con claridad.

**Haz esto**
print("ok")  # Confirmamos
```
edad = 20  # int: número entero
altura = 1.72  # float: número decimal
activo = True  # bool: estado lógico
texto_edad = str(edad)  # Convertimos int a str para unir con texto
resumen = "Edad: " + texto_edad  # Construimos un resumen
print(resumen)  # Mostramos el resumen
print(type(altura))  # Mostramos el tipo de altura
print(activo)  # Mostramos el booleano
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Edad: 20`, el tipo `<class 'float'>` y el valor `True`.

**Por qué funciona**
`str()` convierte el entero en texto y `type()` revela el tipo real. Con eso puedes decidir si sumar, concatenar o
comparar correctamente.

**Lo típico que sale mal**
- Concatenar texto y número sin `str()` y provocar un error de tipo.
- Usar coma en lugar de punto para decimales (Python necesita punto).

## Paso 3: Conversiones explícitas y datos de entrada
Cuando el dato viene como texto (por ejemplo, de un archivo), necesitas convertirlo antes de operar.

**Aprende esto**
- Aprenderás a convertir texto numérico a entero y a validar el resultado.
- Verás cómo separar la conversión del cálculo para depurar más fácil.

**Haz esto**
print("ok")  # Confirmamos
```
texto = "42"  # Texto numérico proveniente de entrada
numero = int(texto)  # Convertimos el texto a entero
incremento = 8  # Definimos cuánto vamos a sumar
resultado = numero + incremento  # Sumamos el entero con el incremento
etiqueta = "Total"  # Definimos una etiqueta descriptiva
mensaje = etiqueta + ": " + str(resultado)  # Convertimos para mostrar
print(mensaje)  # Mostramos el mensaje
print(resultado)  # Mostramos el número final
print("ok")  # Confirmamos
```

**Verás esto**
Verás un mensaje como `Total: 50` y el número `50`.

**Por qué funciona**
Primero conviertes el texto a entero con `int()`, luego haces el cálculo y solo al final lo conviertes a texto para
mostrar. Así se separan transformación y presentación.

**Lo típico que sale mal**
- Intentar sumar un string con un int sin convertir.
- Convertir sin validar y fallar si el texto no es numérico.

## Paso 4: Mutabilidad (listas) vs inmutabilidad (strings)
Algunos objetos cambian en el mismo lugar (mutables) y otros no (inmutables). Esto afecta cómo interpretas resultados.

**Aprende esto**
- Aprenderás que las listas se modifican en el mismo objeto.
- Verás que los strings crean un nuevo valor cuando se transforman.

**Haz esto**
print("ok")  # Confirmamos
```
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # Agregamos un elemento en sitio
compras.append("azúcar")  # Agregamos otro elemento
texto = "hola"  # Texto original
texto_mayus = texto.upper()  # Creamos un nuevo texto en mayúsculas
resumen = texto + " -> " + texto_mayus  # Resumimos el cambio
print(compras)  # Mostramos la lista modificada
print(resumen)  # Mostramos el resumen
print("ok")  # Confirmamos
```

**Verás esto**
Verás la lista con cuatro elementos y un resumen como `hola -> HOLA`.

**Por qué funciona**
`append()` modifica la lista original, pero `upper()` devuelve un nuevo string porque los textos son inmutables.

**Lo típico que sale mal**
- Esperar que `upper()` cambie el texto sin reasignarlo.
- Creer que `append()` devuelve una lista nueva (no lo hace).

## Paso 5: Alias y copias
Asignar una lista a otra variable crea un alias. Para una copia real necesitas duplicar la lista.

**Aprende esto**
- Aprenderás a distinguir alias de copia superficial.
- Verás cómo evitar cambios involuntarios en datos compartidos.

**Haz esto**
print("ok")  # Confirmamos
```
original = [1, 2]  # Lista original
alias = original  # Alias al mismo objeto
alias.append(3)  # Modificamos la lista original
copia = original.copy()  # Copia superficial independiente
copia.append(99)  # Solo cambia la copia
estado_original = str(original)  # Convertimos la lista original a texto
estado_copia = str(copia)  # Convertimos la copia a texto
print(estado_original)  # Mostramos la lista original
print(estado_copia)  # Mostramos la copia
print("ok")  # Confirmamos
```

**Verás esto**
Verás que `original` es `[1, 2, 3]` y `copia` es `[1, 2, 3, 99]`.

**Por qué funciona**
`alias` apunta al mismo objeto, por eso `append()` afecta a ambos. `copy()` crea una lista nueva con los mismos valores.

**Lo típico que sale mal**
- Usar `b = a` pensando que es una copia.
- Modificar un alias y luego buscar “el error” en otro lugar.

## Paso 6: None y valores booleanos
`None` representa ausencia de valor. No es igual a 0 ni a una cadena vacía.

**Aprende esto**
- Aprenderás a usar `None` como marcador de “aún no calculado”.
- Verás cómo comprobarlo con `is` de forma segura.

**Haz esto**
print("ok")  # Confirmamos
```
resultado = None  # Aún no hay resultado
texto = "5"  # Texto de entrada
numero = int(texto)  # Convertimos a entero
resultado = numero * 2  # Calculamos el doble
hay_resultado = resultado is not None  # Verificamos si existe resultado
print(hay_resultado)  # Mostramos True si existe
print(resultado)  # Mostramos el resultado numérico
print("ok")  # Confirmamos
```

**Verás esto**
Verás `True` y el número `10`.

**Por qué funciona**
`is` comprueba identidad con el singleton `None`. Al actualizar `resultado`, la condición cambia y lo confirmas con el
booleano.

**Lo típico que sale mal**
- Usar `== None` en lugar de `is None`.
- Asumir que `None` significa 0 o un texto vacío.

## Más allá (nivel pro): copias profundas e identidad
En proyectos reales hay listas anidadas y comparaciones sutiles. Entender identidad y copias profundas evita bugs.

**Aprende esto**
- Aprenderás por qué una copia superficial no duplica listas internas.
- Verás cómo `is` se usa para identidad y no para comparar valores.

**Haz esto**
print("ok")  # Confirmamos
```
matriz = [[1], [2]]  # Lista con listas internas
copia_superficial = matriz.copy()  # Copia la lista externa
copia_superficial[0].append(9)  # Modifica la sublista compartida
es_el_mismo = matriz[0] is copia_superficial[0]  # Comprobamos identidad
valor = 10  # Número para comparar
mismo_valor = valor == 10  # Comparamos valores
print(matriz)  # Mostramos la matriz afectada
print(es_el_mismo)  # True: misma sublista interna
print(mismo_valor)  # True: mismo valor
print("ok")  # Confirmamos
```

**Verás esto**
Verás que la primera sublista queda como `[1, 9]`, y que `is` confirma identidad mientras `==` compara valores.

**Por qué funciona**
La copia superficial solo duplica la lista externa. Las listas internas siguen siendo las mismas referencias, por eso se
modifican juntas. `is` compara identidad (mismo objeto), mientras `==` compara contenido.

**Lo típico que sale mal**
- Pensar que `copy()` también copia listas internas.
- Usar `is` para comparar números o textos y obtener resultados inconsistentes.
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
            (
                "No convertir antes de concatenar",
                "Concatenar texto y números sin str() produce errores de tipo.",
            ),
            (
                "Asumir que copy() duplica todo",
                "copy() no copia listas internas; usa copy profundo cuando haya anidaciones.",
            ),
            (
                "Comparar objetos por identidad",
                "is solo sirve para identidad, no para comparar valores numéricos o texto.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Nombres claros para variables",
                """# Aprende esto
# Aprenderás a nombrar variables con claridad.
# Verás cómo reutilizarlas para formar mensajes.
# Entenderás que el nombre documenta la intención.
#
# Haz esto
nombre = \"Ana\"  # Definimos el nombre
apellido = \"López\"  # Definimos el apellido
separador = \" \"  # Guardamos un separador
nombre_completo = nombre + separador + apellido  # Unimos textos
rol = \"Cliente\"  # Definimos un rol
mensaje = rol + ": " + nombre_completo  # Construimos el mensaje
longitud = len(mensaje)  # Contamos caracteres
print(mensaje)  # Mostramos el mensaje
print(longitud)  # Mostramos la longitud
#
# Verás esto
# Verás "Cliente: Ana López" y la longitud del texto.
#
# Por qué funciona
# Cada variable apunta a un string y len cuenta caracteres.
#
# Lo típico que sale mal
# - Usar nombres genéricos y perder contexto.
# - Olvidar espacios en la concatenación.
""",
            ),
            (
                "Identificar tipos con type",
                """# Aprende esto
# Aprenderás a inspeccionar el tipo de un dato.
# Verás cómo afecta las operaciones disponibles.
# Mantendrás claridad al depurar errores de tipo.
#
# Haz esto
edad = 28  # Guardamos un entero
altura = 1.65  # Guardamos un decimal
activo = False  # Guardamos un booleano
print(type(edad))  # Mostramos el tipo de edad
print(type(altura))  # Mostramos el tipo de altura
print(type(activo))  # Mostramos el tipo de activo
texto_edad = str(edad)  # Convertimos para mostrar
print(\"Edad: \" + texto_edad)  # Mostramos el mensaje
#
# Verás esto
# Verás <class 'int'>, <class 'float'> y <class 'bool'>.
#
# Por qué funciona
# type() revela la clase y str() permite concatenar textos.
#
# Lo típico que sale mal
# - Concatenar texto con int sin convertir.
# - Asumir que 1 y True son lo mismo en operaciones.
""",
            ),
            (
                "Conversión de texto a número",
                """# Aprende esto
# Aprenderás a convertir texto numérico a int.
# Verás cómo separar conversión y cálculo.
# Evitarás mezclar tipos en el mismo paso.
#
# Haz esto
texto = \"100\"  # Texto numérico de entrada
numero = int(texto)  # Convertimos a entero
bono = 25  # Definimos un bono
total = numero + bono  # Sumamos valores numéricos
mensaje = \"Total: \" + str(total)  # Convertimos para mostrar
print(mensaje)  # Mostramos el mensaje
print(total)  # Mostramos el total numérico
print(type(total))  # Confirmamos el tipo final
#
# Verás esto
# Verás "Total: 125", el número 125 y el tipo int.
#
# Por qué funciona
# int() transforma el texto y luego operas como número.
#
# Lo típico que sale mal
# - Convertir sin validar y fallar con texto no numérico.
# - Concatenar sin str() al final.
""",
            ),
            (
                "Booleanos y condiciones simples",
                """# Aprende esto
# Aprenderás a trabajar con bool en decisiones.
# Verás cómo comparar valores para obtener True o False.
# Podrás usar esos booleanos en lógicas futuras.
#
# Haz esto
stock = 5  # Guardamos unidades disponibles
umbral = 3  # Definimos un mínimo aceptable
hay_stock = stock > umbral  # Comparamos para obtener un booleano
mensaje = \"Stock suficiente\"  # Texto base
print(hay_stock)  # Mostramos el booleano
print(mensaje)  # Mostramos el texto base
print(type(hay_stock))  # Confirmamos el tipo booleano
print(stock == 5)  # Comparamos igualdad exacta
#
# Verás esto
# Verás True, el mensaje y el tipo bool.
#
# Por qué funciona
# Las comparaciones devuelven bool y puedes inspeccionarlas con type().
#
# Lo típico que sale mal
# - Confundir = con == en comparaciones.
# - Usar números como si fueran booleanos sin claridad.
""",
            ),
            (
                "Mutabilidad en listas",
                """# Aprende esto
# Aprenderás que append modifica la lista original.
# Verás cómo cambia la lista sin crear otra.
# Confirmarás el tamaño con len.
#
# Haz esto
compras = [\"pan\", \"leche\"]  # Lista inicial
compras.append(\"café\")  # Agregamos un elemento
compras.append(\"azúcar\")  # Agregamos otro elemento
cantidad = len(compras)  # Contamos elementos
resumen = \"Items: \" + str(cantidad)  # Creamos un resumen
print(compras)  # Mostramos la lista
print(resumen)  # Mostramos el resumen
print(compras[0])  # Accedemos al primer elemento
#
# Verás esto
# Verás la lista con cuatro elementos y un resumen "Items: 4".
#
# Por qué funciona
# append modifica la lista y len cuenta los elementos actuales.
#
# Lo típico que sale mal
# - Creer que append devuelve una nueva lista.
# - Olvidar que la lista se modifica en sitio.
""",
            ),
            (
                "Inmutabilidad en strings",
                """# Aprende esto
# Aprenderás que los strings no cambian en sitio.
# Verás cómo guardar el resultado en otra variable.
# Evitarás perder transformaciones por no reasignar.
#
# Haz esto
texto = \" hola \"  # Texto con espacios
texto_limpio = texto.strip()  # Creamos un nuevo texto sin espacios
texto_mayus = texto_limpio.upper()  # Creamos un nuevo texto en mayúsculas
resumen = texto + \"->\" + texto_mayus  # Creamos un resumen
print(texto)  # Mostramos el original
print(texto_limpio)  # Mostramos el texto limpio
print(texto_mayus)  # Mostramos el texto en mayúsculas
print(resumen)  # Mostramos el resumen
#
# Verás esto
# Verás el texto original con espacios y la versión limpia en mayúsculas.
#
# Por qué funciona
# strip() y upper() devuelven nuevos strings porque son inmutables.
#
# Lo típico que sale mal
# - Esperar que el original cambie sin reasignar.
# - Encadenar sin guardar el resultado intermedio.
""",
            ),
            (
                "Alias vs copia en listas",
                """# Aprende esto
# Aprenderás a distinguir alias y copia real.
# Verás cómo una copia evita cambios inesperados.
# Entenderás por qué copy() es importante.
#
# Haz esto
original = [1, 2]  # Lista original
alias = original  # Alias a la misma lista
alias.append(3)  # Modificamos la lista original
copia = original.copy()  # Creamos una copia
copia.append(99)  # Modificamos solo la copia
print(original)  # Mostramos la original
print(copia)  # Mostramos la copia
print(alias is original)  # Comprobamos identidad
#
# Verás esto
# Verás [1, 2, 3] en original y [1, 2, 3, 99] en copia.
#
# Por qué funciona
# alias apunta al mismo objeto, copy() crea uno nuevo.
#
# Lo típico que sale mal
# - Usar b = a cuando se espera una copia.
# - Modificar alias y buscar el fallo en otro lado.
""",
            ),
            (
                "Uso de None como marcador",
                """# Aprende esto
# Aprenderás a usar None para indicar ausencia de valor.
# Verás cómo comprobarlo con is de forma segura.
# Evitarás confundir None con 0.
#
# Haz esto
resultado = None  # Aún no hay resultado
texto = \"7\"  # Texto de entrada
numero = int(texto)  # Convertimos el texto
resultado = numero * 3  # Calculamos un valor
hay_resultado = resultado is not None  # Verificamos existencia
print(hay_resultado)  # Mostramos el booleano
print(resultado)  # Mostramos el resultado
print(resultado == 0)  # Comprobamos si es cero
#
# Verás esto
# Verás True, el número 21 y False para la comparación con 0.
#
# Por qué funciona
# None representa ausencia y is compara identidad con None.
#
# Lo típico que sale mal
# - Usar == None en lugar de is None.
# - Suponer que None es equivalente a 0.
""",
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
                "question": "Convierte un entero a texto y concaténalo en un mensaje.",
                "hints": ["Usa str()"],
                "solution": "edad = 30\nmensaje = 'Edad: ' + str(edad)\nprint(mensaje)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
