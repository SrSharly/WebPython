from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class FuncionesLesson(Lesson):
    TITLE = "Funciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["funciones", "def", "return", "parametros"]

    def summary(self) -> str:
        return (
            "Aprende a crear funciones claras, con parámetros, valores de retorno y reglas de alcance para reutilizar "
            "tu lógica sin repetir código."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: las funciones son herramientas reutilizables
Una función es un bloque de código con nombre que puedes ejecutar cuando lo necesites. Sirve para evitar repetir lógica,
organizar el flujo y describir intenciones. En lugar de copiar y pegar, defines una función y la llamas las veces que sea
necesario. Esto hace que tu código sea más corto, más claro y más fácil de probar.

En esta lección aprenderás desde cero cómo definir funciones, cómo pasar parámetros, cómo devolver resultados y cómo entender
el alcance de las variables. También verás valores por defecto y cómo escribir funciones con responsabilidades pequeñas.

### Buenas prácticas (CalloutBox: best_practice)
Una función debe hacer una sola cosa bien. Si hace demasiadas cosas, es difícil de entender y de reutilizar.

## Paso 1: definir y llamar una función
La palabra clave `def` crea una función. Dentro del bloque defines qué hace. Luego la llamas con su nombre seguido de
paréntesis. Si no la llamas, el código dentro no se ejecuta.

## Paso 2: parámetros de entrada
Los parámetros son valores que recibe la función para trabajar. Permiten que una función sea flexible. En vez de usar
variables globales, pasas lo que necesitas como parámetros. Esto hace que la función sea más clara y fácil de probar.

## Paso 3: return y resultados
Una función puede devolver un valor con `return`. Ese valor se puede guardar en una variable o usar directamente. Si no
usas `return`, la función devuelve `None`. Entender esta diferencia es clave para evitar errores.

### Nota (CalloutBox: note)
`print` muestra algo en pantalla, pero no devuelve un valor. Si necesitas usar el resultado después, usa `return`.

## Paso 4: valores por defecto
Puedes definir valores por defecto para parámetros. Esto hace que la función sea más cómoda de usar porque puedes omitir
argumentos cuando el valor por defecto es suficiente. Aun así, debes evitar valores mutables como listas por defecto.

## Paso 5: alcance de variables
Las variables que se crean dentro de una función son locales. No existen fuera de ella. Esto evita conflictos y te obliga a
pasar información de forma explícita. Si necesitas reutilizar un valor fuera, debes devolverlo con `return`.

### Advertencia (CalloutBox: warning)
No uses variables globales para compartir estado entre funciones si puedes evitarlo. Es una fuente común de bugs.

## Paso 6: diseñar funciones legibles
Una función con un nombre claro y parámetros simples se entiende sin leer su implementación. Si el nombre suena como una
acción (“calcular_total”, “validar_email”), probablemente estás haciendo lo correcto.

## Más allá (nivel pro)
Las funciones son el lenguaje del diseño de software. Dividir bien tu lógica permite probar, reutilizar y refactorizar sin
miedo. No se trata de tener muchas funciones, sino de tener funciones con un propósito claro.

### Consejos pro
- Prefiere funciones pequeñas con nombres de acción.
- Separa la lógica de cálculo de la lógica de impresión.
- Evita parámetros con demasiada responsabilidad: mejor varios parámetros claros.
- Documenta con un comentario corto si la función no es obvia.
- Si una función crece, divide en subfunciones y reutiliza.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar llamar la función",
                "Definirla no la ejecuta. Debes llamarla con paréntesis.",
            ),
            (
                "Confundir print con return",
                "`print` muestra, `return` devuelve. Si necesitas el resultado, debes usar return.",
            ),
            (
                "Usar variables globales innecesarias",
                "Las variables globales ocultan dependencias y hacen difícil seguir el flujo.",
            ),
            (
                "No pasar parámetros",
                "Si la función depende de variables externas, se vuelve frágil y difícil de probar.",
            ),
            (
                "Valores por defecto mutables",
                "Usar `[]` o `{}` como default comparte el mismo objeto entre llamadas.",
            ),
            (
                "No devolver nada",
                "Si olvidas `return`, la función devuelve None y tu resultado se pierde.",
            ),
            (
                "Demasiadas responsabilidades",
                "Una función que hace muchas cosas es difícil de entender y mantener.",
            ),
            (
                "Sobrescribir variables",
                "Reusar nombres de variables con otro propósito dentro de la función confunde la lectura.",
            ),
            (
                "No documentar parámetros",
                "Si no está claro qué se espera, la función se usa mal.",
            ),
            (
                "Olvidar el orden de argumentos",
                "Si pasas argumentos por posición, debes respetar el orden definido.",
            ),
            (
                "Retornar tipos inconsistentes",
                "Si a veces devuelves int y otras str, el código que consume la función se rompe.",
            ),
            (
                "Modificar argumentos mutables",
                "Si alteras una lista recibida, puedes afectar datos fuera de la función sin querer.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Función simple",
                """# Aprende esto
# Aprenderás a definir y llamar una función.
# Verás que el código no se ejecuta hasta llamarla.
# Entenderás la estructura básica con def.
#
# Haz esto
def saludar():  # Definimos la función
    print("Hola")  # Mostramos un saludo
saludar()  # Llamamos a la función
saludar()  # Llamamos otra vez
#
# Verás esto
# Verás "Hola" dos veces.
#
# Por qué funciona
# La función se ejecuta cada vez que la llamas.
#
# Lo típico que sale mal
# - Definir la función y olvidar llamarla.
# - No respetar la indentación.
""",
            ),
            (
                "Parámetros de entrada",
                """# Aprende esto
# Aprenderás a pasar parámetros a una función.
# Verás cómo usar esos valores dentro.
# Entenderás la diferencia entre dato y lógica.
#
# Haz esto
def saludar(nombre):  # Definimos parámetro
    mensaje = f"Hola {nombre}"  # Construimos mensaje
    print(mensaje)  # Mostramos mensaje
saludar("Ana")  # Llamamos con un nombre
saludar("Luis")  # Llamamos con otro nombre
#
# Verás esto
# Verás dos saludos distintos.
#
# Por qué funciona
# El parámetro recibe el valor al llamar la función.
#
# Lo típico que sale mal
# - Llamar sin argumentos.
# - Reusar nombres ambiguos.
""",
            ),
            (
                "Return para resultados",
                """# Aprende esto
# Aprenderás a devolver un valor con return.
# Verás cómo usar el resultado fuera.
# Entenderás que print no devuelve.
#
# Haz esto
def sumar(a, b):  # Definimos función
    resultado = a + b  # Sumamos
    return resultado  # Devolvemos resultado
suma = sumar(3, 4)  # Guardamos el retorno
print(suma)  # Mostramos el resultado
#
# Verás esto
# Verás 7.
#
# Por qué funciona
# return envía el resultado al código que llamó.
#
# Lo típico que sale mal
# - Usar print esperando un retorno.
# - Olvidar return y obtener None.
""",
            ),
            (
                "Valores por defecto",
                """# Aprende esto
# Aprenderás a usar parámetros con default.
# Verás cómo omitir un argumento.
# Entenderás cuándo usar defaults.
#
# Haz esto
def saludar(nombre, saludo="Hola"):  # Default en saludo
    mensaje = f"{saludo} {nombre}"  # Construimos mensaje
    print(mensaje)  # Mostramos mensaje
saludar("Ana")  # Usa el default
saludar("Luis", "Buenas")  # Cambiamos el saludo
#
# Verás esto
# Verás "Hola Ana" y "Buenas Luis".
#
# Por qué funciona
# El parámetro default se usa si no se pasa valor.
#
# Lo típico que sale mal
# - Usar listas como default.
# - Reordenar parámetros con default mal.
""",
            ),
            (
                "Alcance de variables",
                """# Aprende esto
# Aprenderás que las variables internas son locales.
# Verás que no existen fuera de la función.
# Entenderás la importancia de return.
#
# Haz esto
def calcular_total(precio, cantidad):  # Definimos función
    total = precio * cantidad  # Variable local
    return total  # Devolvemos total
resultado = calcular_total(5, 3)  # Guardamos retorno
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás 15.
#
# Por qué funciona
# total vive dentro de la función y se retorna.
#
# Lo típico que sale mal
# - Intentar usar total fuera sin retornarlo.
# - Depender de variables globales.
""",
            ),
            (
                "Funciones con listas",
                """# Aprende esto
# Aprenderás a recibir listas en funciones.
# Verás cómo calcular un resultado.
# Entenderás la diferencia entre mutar y retornar.
#
# Haz esto
def contar_items(items):  # Recibimos una lista
    cantidad = len(items)  # Contamos elementos
    return cantidad  # Devolvemos cantidad
lista = ["a", "b", "c"]  # Lista de ejemplo
resultado = contar_items(lista)  # Llamamos la función
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás 3.
#
# Por qué funciona
# La función usa len y devuelve un valor.
#
# Lo típico que sale mal
# - Modificar la lista sin intención.
# - No retornar el resultado.
""",
            ),
            (
                "Combinar funciones",
                """# Aprende esto
# Aprenderás a componer funciones pequeñas.
# Verás cómo reutilizar resultados.
# Entenderás el flujo paso a paso.
#
# Haz esto
def total_con_impuesto(total):  # Calculamos impuesto
    return total * 1.18  # Devolvemos con impuesto

def calcular_compra(precio, cantidad):  # Calculamos subtotal
    subtotal = precio * cantidad  # Subtotal
    return total_con_impuesto(subtotal)  # Llamamos otra función
resultado = calcular_compra(10, 2)  # Ejecutamos
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás 23.6.
#
# Por qué funciona
# Una función llama a otra y reutiliza su lógica.
#
# Lo típico que sale mal
# - Mezclar demasiada lógica en una sola función.
# - No devolver el valor intermedio.
""",
            ),
            (
                "Retornos consistentes",
                """# Aprende esto
# Aprenderás a mantener retornos consistentes.
# Verás que siempre devolvemos el mismo tipo.
# Entenderás por qué eso evita errores.
#
# Haz esto
def es_mayor(edad):  # Función booleana
    return edad >= 18  # Retornamos True o False
resultado = es_mayor(20)  # Guardamos el retorno
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás True.
#
# Por qué funciona
# La función siempre devuelve un booleano.
#
# Lo típico que sale mal
# - Devolver int en algunos casos y bool en otros.
# - Usar print en lugar de return.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función `saludar` que reciba un nombre y muestre un saludo.",
                "hints": ["Usa def saludar(nombre).", "Usa print dentro."],
                "solution": """def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ana")""",
            },
            {
                "question": "Crea una función `sumar` que devuelva la suma de dos números.",
                "hints": ["Usa return.", "Guarda el resultado en una variable."],
                "solution": """def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)""",
            },
            {
                "question": "Crea una función con parámetro por defecto para saludar.",
                "hints": ["Define saludo=\"Hola\".", "Permite cambiarlo."] ,
                "solution": """def saludar(nombre, saludo="Hola"):
    print(f"{saludo} {nombre}")

saludar("Luis")
saludar("Ana", "Buenas")""",
            },
            {
                "question": "Crea una función que calcule el total con impuesto (18%).",
                "hints": ["Multiplica por 1.18.", "Devuelve el resultado."],
                "solution": """def total_con_impuesto(total):
    return total * 1.18

print(total_con_impuesto(100))""",
            },
            {
                "question": "Crea una función que reciba una lista y devuelva su longitud.",
                "hints": ["Usa len().", "Devuelve el valor."],
                "solution": """def contar(lista):
    return len(lista)

print(contar([1, 2, 3]))""",
            },
            {
                "question": "Crea una función que devuelva True si un número es par.",
                "hints": ["Usa el operador %.", "Retorna un booleano."],
                "solution": """def es_par(numero):
    return numero % 2 == 0

print(es_par(4))""",
            },
        ]
