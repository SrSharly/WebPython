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
            "Aprende desde cero qué es una variable, cómo reconocer tipos, y cómo evitar errores "
            "al convertir datos, copiar listas y trabajar con valores ausentes."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: por qué variables y tipos importan desde el primer día
Una variable es un nombre que apunta a un dato. Esa idea es la base de todo lo que harás en Python. Los tipos describen la
forma del dato y lo que puedes hacer con él: un número se suma, un texto se concatena, una lista se modifica. Entender esto
te evita errores típicos cuando empiezas.

En este tutorial vas a construir esa base paso a paso. Verás cómo asignar variables, cómo distinguir tipos básicos, cómo
convertir datos que vienen como texto y cómo trabajar con `None`. Cada concepto viene con un micro-ejemplo correcto y un
error típico, para que aprendas la sintaxis en el momento exacto.

### Buenas prácticas (CalloutBox: best_practice)
Nombrar tus variables con intención evita comentarios innecesarios. Un nombre claro explica el propósito y reduce errores.

## Paso 1: asignación y nombres claros
Asignar es guardar un dato con `=`. Tu variable debe explicar lo que contiene.

**Así se escribe**
```py
precio_total = 120
cliente = "Ana"
```

**Error típico (❌)**
```py
precio_total == 120
```

**Qué significa el error**
`==` compara, no asigna. Si lo usas en una asignación, Python lo interpreta como una comparación aislada.

**Cómo se arregla**
Usa `=` para asignar y reserva `==` para comparaciones.

## Paso 2: strings y comillas
Los textos (`str`) se escriben entre comillas simples o dobles. Si no pones comillas, Python busca una variable con ese
nombre.

**Así se escribe**
```py
saludo = "Hola"
nombre = 'Lucía'
```

**Error típico (❌)**
```py
saludo = "Hola
```

**Qué significa el error**
`SyntaxError` indica que la cadena no se cerró. Python llegó al fin de línea sin encontrar la comilla final.

**Cómo se arregla**
Cierra siempre las comillas o usa el tipo de comillas que no se repita dentro del texto.

**Error típico (❌)**
```py
saludo = Hola
```

**Qué significa el error**
`NameError` aparece porque `Hola` no está definido como variable. Python no lo interpreta como texto.

**Cómo se arregla**
Encierra el texto entre comillas: `"Hola"` o `'Hola'`.

## Paso 3: números int y float
Los enteros (`int`) no tienen decimales. Los flotantes (`float`) sí. Esto cambia cómo se muestran y se calculan.

**Así se escribe**
```py
edad = 30
altura = 1.75
```

### Así se escribe: crear y combinar tipos básicos
```py
entero = 4
decimal = 2.5
texto = "Total"
activo = True
vacio = None
resultado = entero + decimal  # float
mensaje = texto + ": " + str(resultado)
division = entero / 2  # cambia a float
```

### Error típico: mezclar tipos sin convertir
```py
entero = 4
mensaje = "Total: " + entero
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: la suma de `str` con `int` no es válida. Convierte con `str()` o usa f-strings.

**Error típico (❌)**
```py
altura = 1,75
```

**Qué significa el error**
Python interpreta `1,75` como una tupla, no como un número. Es un error lógico más que de sintaxis.

**Cómo se arregla**
Usa el punto como separador decimal: `1.75`.

## Paso 4: concatenación de texto y números
No puedes sumar texto con número directamente. Debes convertir el número a texto.

**Así se escribe**
```py
edad = 30
mensaje = "Edad: " + str(edad)
```

**Error típico (❌)**
```py
edad = 30
mensaje = "Edad: " + edad
```

**Qué significa el error**
`TypeError` indica que `str` e `int` no se pueden sumar. Son tipos distintos.

**Cómo se arregla**
Convierte el número a texto con `str()` o usa f-strings.

### Así se escribe: print e input en variables iniciales
```py
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```

### Error típico: asumir que input devuelve número
```py
edad = input("Edad: ")
edad_en_10 = edad + 10
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: `input()` siempre devuelve `str`. Convierte con `int()` si necesitas sumar.

## Paso 5: mutabilidad rápida: listas vs strings
Las listas se pueden modificar en sitio; los strings no. Esa diferencia afecta cómo copias y cómo reasignas.

**Así se escribe**
```py
frutas = ["manzana", "pera"]
frutas.append("uva")
```

**Error típico (❌)**
```py
texto = "hola"
texto.upper()
```

**Qué significa el error**
No hay error, pero `upper()` devuelve un nuevo texto. El original no cambia.

**Cómo se arregla**
Guarda el resultado: `texto = texto.upper()`.

## Paso 6: None como ausencia real
`None` significa “no hay valor” y se compara con `is None`.

**Así se escribe**
```py
resultado = None
if resultado is None:
    resultado = 10
```

**Error típico (❌)**
```py
resultado = None
if resultado == None:
    resultado = 10
```

**Qué significa el error**
No siempre falla, pero `==` compara valor, no identidad. Puede dar falsos positivos en objetos complejos.

**Cómo se arregla**
Usa `is None` para comprobar ausencia de valor.

## Paso 7: resumen para evitar errores
Antes de escribir una línea, piensa: ¿qué tipo es?, ¿necesito convertirlo?, ¿es mutable? Si respondes esas preguntas,
reduces la mayoría de errores de inicio.

## Más allá (nivel pro)
Los tipos influyen en cómo diseñas funciones y estructuras. Ser explícito con nombres, conversiones y mutabilidad ayuda a
que tu código escale sin sorpresas.



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
                "Confundir alias con copia",
                "Asignar `b = a` solo crea otra referencia. Si modificas `b`, también cambias `a`. Usa `copy()` cuando quieras independencia.",
            ),
            (
                "Concatenar texto y número",
                "`\"Edad: \" + 30` falla con `TypeError`. Convierte con `str(30)` o usa f-strings.",
            ),
            (
                "No cerrar comillas en strings",
                "`SyntaxError` aparece si abres una comilla y no la cierras. Revisa la línea y el tipo de comilla usado.",
            ),
            (
                "Usar texto sin comillas",
                "`NameError` ocurre cuando escribes `Hola` sin comillas. Python cree que es una variable.",
            ),
            (
                "Cambiar el tipo sin intención",
                "Reutilizar la misma variable para un int y luego un str confunde la lectura. Mantén un tipo claro por variable.",
            ),
            (
                "Usar `is` para comparar números",
                "`is` compara identidad, no valor. Para números y textos usa `==` y reserva `is` para `None`.",
            ),
            (
                "Asumir que `upper()` modifica el string",
                "Los strings son inmutables. `texto.upper()` devuelve otro texto; si no lo reasignas, pierdes el cambio.",
            ),
            (
                "Modificar listas pensando que son copias",
                "Si pasas una lista a una función y la modificas, el cambio vive fuera. Documenta si la función muta datos.",
            ),
            (
                "Confundir `None` con 0",
                "`None` significa ausencia. Compararlo con números provoca errores lógicos y condiciones engañosas.",
            ),
            (
                "Usar nombres reservados",
                "Nombrar una variable `list` o `dict` pisa funciones del lenguaje y rompe llamadas posteriores.",
            ),
            (
                "Creer que `copy()` es profundo",
                "`copy()` solo copia el primer nivel. Si hay listas dentro, siguen compartidas.",
            ),
            (
                "Operar con texto numérico sin convertir",
                "`\"10\" + \"5\"` concatena, no suma. Convierte a int si quieres cálculo real.",
            ),
            (
                "Usar `bool` como número sin querer",
                "`True` y `False` también son 1 y 0. Eso puede colarse en sumas si no eres explícito.",
            ),
            (
                "Depurar sin imprimir el tipo",
                "Cuando algo falla, imprime el valor y su tipo. Evitas suposiciones y detectas conversiones fallidas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Variables con intención",
                """# Aprende esto
# Aprenderás a nombrar variables para que expliquen el propósito.
# Verás cómo reutilizarlas en un mensaje legible.
# Entenderás que el nombre documenta el dato.
#
# Haz esto
nombre = "Ana"  # Guardamos el nombre
apellido = "López"  # Guardamos el apellido
separador = " "  # Definimos un espacio
nombre_completo = nombre + separador + apellido  # Unimos el nombre
rol = "Cliente"  # Definimos el rol
mensaje = rol + ": " + nombre_completo  # Construimos el mensaje
longitud = len(mensaje)  # Contamos caracteres
print(mensaje)  # Mostramos el mensaje
print(longitud)  # Mostramos la longitud
#
# Verás esto
# Verás "Cliente: Ana López" y el número de caracteres.
#
# Por qué funciona
# Cada variable apunta a un string y len cuenta su longitud.
#
# Lo típico que sale mal
# - Usar nombres genéricos como x y perder contexto.
# - Olvidar espacios y obtener textos pegados.
""",
            ),
            (
                "Inspeccionar tipos básicos",
                """# Aprende esto
# Aprenderás a identificar tipos con type().
# Verás cómo varían las operaciones según el tipo.
# Entenderás cuándo convertir para mostrar.
#
# Haz esto
edad = 28  # Guardamos un entero
altura = 1.68  # Guardamos un decimal
activo = True  # Guardamos un booleano
print(type(edad))  # Mostramos el tipo de edad
print(type(altura))  # Mostramos el tipo de altura
print(type(activo))  # Mostramos el tipo de activo
texto_edad = str(edad)  # Convertimos a texto
print("Edad: " + texto_edad)  # Mostramos el mensaje
#
# Verás esto
# Verás <class 'int'>, <class 'float'> y <class 'bool'>.
#
# Por qué funciona
# type() revela el tipo real y str() permite concatenar.
#
# Lo típico que sale mal
# - Concatenar texto y número sin str().
# - Asumir que todos los números son int.
""",
            ),
            (
                "Convertir texto a número",
                """# Aprende esto
# Aprenderás a convertir texto numérico a int.
# Verás cómo separar conversión y cálculo.
# Entenderás cuándo presentar el resultado.
#
# Haz esto
texto = "42"  # Texto numérico de entrada
numero = int(texto)  # Convertimos a entero
incremento = 8  # Definimos un incremento
resultado = numero + incremento  # Sumamos los enteros
etiqueta = "Total"  # Definimos una etiqueta
mensaje = etiqueta + ": " + str(resultado)  # Convertimos para mostrar
print(mensaje)  # Mostramos el mensaje
print(resultado)  # Mostramos el número final
#
# Verás esto
# Verás "Total: 50" y el número 50.
#
# Por qué funciona
# int() transforma el texto y la suma ya es numérica.
#
# Lo típico que sale mal
# - Sumar sin convertir y obtener error de tipo.
# - Convertir texto no numérico y fallar.
""",
            ),
            (
                "Mutabilidad: lista vs string",
                """# Aprende esto
# Aprenderás que las listas se modifican en sitio.
# Verás que los strings generan un valor nuevo.
# Entenderás por qué necesitas reasignar textos.
#
# Haz esto
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # Agregamos un producto
compras.append("azúcar")  # Agregamos otro producto
texto = "hola"  # Texto original
texto_mayus = texto.upper()  # Creamos texto en mayúsculas
resumen = texto + " -> " + texto_mayus  # Resumimos el cambio
print(compras)  # Mostramos la lista
print(resumen)  # Mostramos el resumen
#
# Verás esto
# Verás la lista con 4 elementos y "hola -> HOLA".
#
# Por qué funciona
# append() muta la lista; upper() devuelve otro string.
#
# Lo típico que sale mal
# - Esperar que upper() cambie el texto original.
# - Creer que append() devuelve una lista nueva.
""",
            ),
            (
                "Alias y copias",
                """# Aprende esto
# Aprenderás a distinguir alias de copia.
# Verás cómo afecta modificar una lista compartida.
# Entenderás cuándo usar copy().
#
# Haz esto
original = [1, 2]  # Lista base
alias = original  # Alias al mismo objeto
alias.append(3)  # Modificamos la lista original
copia = original.copy()  # Copia superficial
copia.append(99)  # Modificamos solo la copia
print(original)  # Mostramos la original
print(copia)  # Mostramos la copia
#
# Verás esto
# Verás [1, 2, 3] y [1, 2, 3, 99].
#
# Por qué funciona
# alias apunta al mismo objeto; copy() crea otra lista.
#
# Lo típico que sale mal
# - Pensar que b = a crea copia.
# - Asumir que copy() clona listas internas.
""",
            ),
            (
                "None como ausencia",
                """# Aprende esto
# Aprenderás a usar None como marcador.
# Verás cómo comprobarlo con is.
# Entenderás la diferencia con cero.
#
# Haz esto
resultado = None  # Aún no calculamos
calculo_listo = False  # Estado inicial
if resultado is None:  # Comprobamos ausencia
    resultado = 10  # Asignamos un valor
    calculo_listo = True  # Marcamos como listo
print(resultado)  # Mostramos el valor
print(calculo_listo)  # Mostramos el estado
#
# Verás esto
# Verás 10 y True después del cálculo.
#
# Por qué funciona
# is None valida ausencia real; luego asignamos valor.
#
# Lo típico que sale mal
# - Comparar con == y confundir identidad.
# - Tratar None como si fuera 0.
""",
            ),
            (
                "Reasignación con tipo consistente",
                """# Aprende esto
# Aprenderás a mantener el tipo consistente.
# Verás cómo ayuda a leer el flujo.
# Entenderás por qué separar etapas.
#
# Haz esto
precio = 12.5  # Precio numérico
cantidad = 3  # Cantidad entera
total = precio * cantidad  # Calculamos total
total_texto = str(total)  # Convertimos para mostrar
mensaje = "Total: " + total_texto  # Construimos el mensaje
print(mensaje)  # Mostramos el mensaje
print(type(total))  # Mostramos el tipo del total
#
# Verás esto
# Verás "Total: 37.5" y <class 'float'>.
#
# Por qué funciona
# Mantienes números como números y conviertes al final.
#
# Lo típico que sale mal
# - Reusar total como texto y luego intentar sumar.
# - Mezclar tipos en una sola línea.
""",
            ),
            (
                "Comparar valores correctamente",
                """# Aprende esto
# Aprenderás a comparar valores con ==.
# Verás que is es para identidad.
# Entenderás cuándo usar cada uno.
#
# Haz esto
a = 5  # Guardamos un número
b = 5  # Guardamos otro número
mismo_valor = a == b  # Comparamos valores
mismo_objeto = a is b  # Comparamos identidad
print(mismo_valor)  # Mostramos comparación de valor
print(mismo_objeto)  # Mostramos comparación de identidad
#
# Verás esto
# Verás True y probablemente True por optimización.
#
# Por qué funciona
# == compara contenido; is compara el objeto.
#
# Lo típico que sale mal
# - Usar is para comparar strings o números.
# - Confiar en resultados de identidad como regla.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea dos variables: `nombre` y `edad`. Construye un mensaje como 'Ana tiene 30 años'.",
                "hints": ["Convierte `edad` a texto con str().", "Usa concatenación con +."],
                "solution": """nombre = "Ana"
edad = 30
mensaje = nombre + " tiene " + str(edad) + " años"
print(mensaje)""",
            },
            {
                "question": "Convierte el texto '7' a int, súmale 5 y muestra el resultado.",
                "hints": ["Usa int() para convertir.", "Guarda el resultado en una variable."],
                "solution": """texto = "7"
numero = int(texto)
resultado = numero + 5
print(resultado)""",
            },
            {
                "question": "Crea una lista con dos frutas y agrega una tercera usando append().",
                "hints": ["Las listas son mutables.", "append modifica en sitio."],
                "solution": """frutas = ["manzana", "pera"]
frutas.append("uva")
print(frutas)""",
            },
            {
                "question": "Demuestra que `b = a` no es copia: crea una lista, asigna b = a, agrega un elemento y muestra ambas.",
                "hints": ["Imprime las dos listas.", "Observa que cambian igual."],
                "solution": """a = [1, 2]
b = a
b.append(3)
print(a)
print(b)""",
            },
            {
                "question": "Usa None como marcador inicial y luego asigna un valor si está vacío.",
                "hints": ["Comprueba con `is None`.", "Asigna dentro del if."],
                "solution": """valor = None
if valor is None:
    valor = 10
print(valor)""",
            },
            {
                "question": "Imprime el tipo de una variable float y explica con un comentario qué es.",
                "hints": ["Usa type().", "Crea una variable con decimal."],
                "solution": """altura = 1.75
print(type(altura))  # Es un float (decimal)""",
            },
        ]
