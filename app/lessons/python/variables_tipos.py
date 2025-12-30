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
Una variable es un nombre que apunta a un dato. Esa idea tan simple es la base de todo lo que harás en Python. Si lo
piensas como una etiqueta, entiendes por qué al cambiar el contenido la etiqueta sigue siendo la misma y por qué dos
etiquetas pueden apuntar al mismo dato sin que te des cuenta. Los tipos, en cambio, describen la forma del dato y lo que
puedes hacer con él. Un número se suma, un texto se concatena, una lista se modifica en sitio. Mezclar estos comportamientos
sin entenderlos es lo que produce los errores más comunes al empezar.

En este tutorial vas a construir esa base paso a paso. Aprenderás a nombrar variables con intención, a reconocer tipos
básicos, a convertir datos cuando vienen como texto, y a distinguir entre objetos mutables e inmutables. También verás cómo
detectar alias, hacer copias correctas y trabajar con `None` sin confundirlo con un valor real. Al final tendrás un mapa claro
para leer y escribir código sin adivinar.

### Buenas prácticas (CalloutBox: best_practice)
Nombrar tus variables con intención evita comentarios innecesarios. Un nombre bien elegido explica el propósito, y eso te
ayuda a ti y a cualquier otra persona que lea tu código a entender el flujo sin suposiciones.

## Paso 1: nombrar datos con intención
Cuando le das nombre a un dato, estás documentando una decisión. Si el nombre es claro, la línea se entiende sin contexto.
Si el nombre es confuso, el código se vuelve frágil. La meta es que cada variable te cuente qué guarda y para qué la usas.

Piensa en una variable como una nota adhesiva: la nota dice “precio_total” y el objeto real es el número. Si cambias el
número, la nota sigue diciendo lo mismo. Esa idea te ayudará también cuando trabajes con listas y diccionarios.

## Paso 2: reconocer tipos básicos
Python tiene tipos básicos como `int`, `float`, `str` y `bool`. Reconocerlos te permite escoger operaciones seguras. Un
`int` se suma, un `str` se concatena, un `bool` se usa para decidir. Cuando el tipo no está claro, es mejor inspeccionarlo con
`type()` o con una impresión controlada antes de avanzar.

Este paso también te enseña a ser explícito al mezclar datos. Si necesitas unir texto y número, conviertes el número a texto.
Si necesitas sumar dos cosas, aseguras que ambas sean números. Este hábito te ahorra errores en tiempo de ejecución.

### Nota (CalloutBox: note)
Python es dinámico: puedes reasignar una variable con otro tipo. Eso no significa que sea buena idea. Mantener el tipo
consistente hace que el código sea más fácil de seguir y de depurar.

## Paso 3: conversiones explícitas cuando el dato viene como texto
Muchos datos llegan como texto: entradas de usuario, archivos, respuestas de red. Antes de hacer cálculos necesitas convertir
ese texto a un número. Una conversión explícita también te permite atrapar errores, porque si el texto no es numérico,
Python te lo dirá inmediatamente.

La regla práctica es: primero conviertes, luego calculas, y al final presentas el resultado como texto. Separar esas fases
te ayuda a verificar cada paso en lugar de hacerlo todo en una sola línea y perder visibilidad.

## Paso 4: mutabilidad e inmutabilidad en la práctica
Los textos (`str`) son inmutables: cada cambio crea un texto nuevo. Las listas, en cambio, son mutables: puedes agregar,
quitar o cambiar elementos sin crear una nueva lista. Esto afecta cómo lees resultados y por qué una función puede alterar
la lista que le pasaste.

Cuando usas métodos como `append`, modificas el mismo objeto. Cuando usas métodos de texto como `upper`, obtienes una copia
nueva. Aprender esa diferencia evita sorpresas al revisar tu salida.

### Advertencia (CalloutBox: warning)
Si dos variables apuntan a la misma lista, cualquier modificación se verá en ambas. Esa es la raíz de muchos bugs en código
inicial.

## Paso 5: alias y copias, el origen de los cambios “misteriosos”
Cuando haces `b = a`, no creas una copia: solo creas una segunda etiqueta. Eso se llama alias. Si quieres una lista nueva
con los mismos valores, debes copiarla. Para listas simples puedes usar `copy()` o slicing. Para estructuras anidadas
necesitarás copias más profundas, pero por ahora la idea clave es: alias y copia no son lo mismo.

Esta distinción también te prepara para entender por qué algunas funciones parecen “modificar” cosas sin devolver nada:
cuando reciben un objeto mutable, pueden cambiarlo directamente.

## Paso 6: None y valores booleanos
`None` significa “no hay valor”. No es 0, no es una cadena vacía. Es un marcador explícito para indicar que algo aún no se
ha calculado o no existe. Por eso se compara con `is None`, que verifica identidad, no igualdad de valor.

Los booleanos (`True` y `False`) son otro tipo básico. Usarlos con claridad te permite escribir condiciones que se leen como
frases: “si está activo”, “si hay saldo”, “si hay elementos”. Evita comparar con `True` directamente si no lo necesitas.

## Paso 7: resumen mental para evitar errores
Piensa en tres preguntas antes de escribir una línea: ¿qué tipo es?, ¿es mutable?, ¿necesito convertir? Si respondes esas
preguntas, puedes evitar la mayoría de errores típicos del inicio. Cuando tengas dudas, imprime el valor y su tipo. No es un
truco de novatos, es una técnica útil incluso para personas con experiencia.

## Más allá (nivel pro)
Cuando tu código crece, las variables no solo guardan datos: también cuentan historias. Las decisiones de tipo y mutabilidad
impactan el diseño entero de tus funciones y estructuras. En lugar de adivinar, puedes apoyarte en patrones simples para
mantener claridad.

### Consejos pro
- Usa nombres que indiquen unidades: `precio_eur`, `edad_anios`, `duracion_seg`. Te ayuda a detectar mezclas peligrosas.
- Separa datos “crudos” de datos “procesados”, por ejemplo `texto_entrada` y `edad_int`.
- Prefiere `None` como marcador y evita valores mágicos como `-1` si eso no está documentado.
- Cuando compartas listas entre funciones, documenta si se modifican en sitio o no.
- Si necesitas copiar estructuras anidadas, considera `copy.deepcopy` y explica por qué.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar `b = a` solo crea otra referencia. Si modificas `b`, también cambias `a`. Usa `copy()` cuando quieras independencia.",
            ),
            (
                "Concatenar texto y número",
                "`\"Edad: \" + 30` falla porque str e int no se suman. Convierte con `str(30)` antes de unir.",
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
                "`""10"" + ""5""` concatena, no suma. Convierte a int si quieres cálculo real.",
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
