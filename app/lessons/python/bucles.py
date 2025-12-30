from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class BuclesLesson(Lesson):
    TITLE = "Bucles"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["for", "while", "range", "iteración"]

    def summary(self) -> str:
        return "Aprende a repetir tareas con for y while, controlar iteraciones y evitar bucles infinitos."

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: repetir sin copiar
Un bucle te permite repetir una acción sin escribirla muchas veces. Eso hace tu código más corto, más fácil de cambiar y más
confiable. En Python, los bucles principales son `for` y `while`. El primero recorre colecciones; el segundo repite mientras
se cumpla una condición.

En esta lección aprenderás desde cero cómo iterar listas, cómo usar `range`, cómo controlar un `while` y cómo detener una
iteración con `break` o saltar con `continue`. También verás cómo evitar bucles infinitos y cómo hacer que cada iteración sea
legible.

### Buenas prácticas (CalloutBox: best_practice)
Piensa en qué cambia en cada vuelta. Si nada cambia, el bucle nunca termina. Define la variable de control con claridad.

## Paso 1: for para recorrer colecciones
El bucle `for` recorre elementos uno por uno. Es perfecto para listas, tuplas, diccionarios y cadenas. No necesitas manejar
índices manualmente si no son necesarios. Si necesitas el índice, puedes usar `enumerate`.

## Paso 2: range para contar
`range` genera una secuencia de números. Es la forma estándar de contar repeticiones. Puedes indicar inicio, fin y paso.
Recuerda que el límite superior no se incluye, lo cual es muy útil para iterar por índices.

## Paso 3: while para condiciones
`while` repite mientras la condición sea verdadera. Es ideal cuando no sabes cuántas vueltas necesitas y la decisión depende
de algo que cambia dentro del bucle. Siempre debes asegurarte de modificar la condición para evitar ciclos infinitos.

### Nota (CalloutBox: note)
`while` es poderoso, pero más propenso a errores. Si puedes expresar el recorrido con `for`, hazlo.

## Paso 4: break y continue
`break` detiene el bucle por completo. `continue` salta a la siguiente iteración. Son herramientas útiles para casos
especiales, pero hay que usarlas con moderación para no ocultar la lógica principal.

## Paso 5: recorrer diccionarios
Cuando iteras un diccionario puedes recorrer claves, valores o ambos. Esto te permite procesar datos con significado, no
solo con posición. Es más claro y evita errores de índice.

## Paso 6: legibilidad y control
Un buen bucle debe leerse como una historia: “para cada producto, calcula el total”. Si el bucle es largo, considera extraer
partes a funciones. La claridad es más importante que el ahorro de líneas.

### Advertencia (CalloutBox: warning)
Evita modificar la lista que estás recorriendo. Eso puede saltarse elementos o generar resultados inesperados.

## Más allá (nivel pro)
Los bucles son básicos, pero su uso define la calidad de tu código. Un bucle claro comunica intención y facilita pruebas.
Un bucle confuso crea bugs silenciosos.

### Consejos pro
- Usa `enumerate` cuando necesites índice y valor a la vez.
- Prefiere `for` sobre `while` si tienes una colección clara.
- Usa `break` solo cuando sea una condición de salida evidente.
- Si un bucle crece, divide el trabajo en funciones pequeñas.
- En listas grandes, evita operaciones costosas dentro de cada iteración.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Bucle infinito en while",
                "Si la condición nunca cambia, el bucle no termina. Actualiza la variable de control.",
            ),
            (
                "Olvidar que range no incluye el final",
                "`range(5)` genera 0 a 4. Si esperas 5, debes usar `range(6)`.",
            ),
            (
                "Modificar la lista mientras iteras",
                "Agregar o quitar elementos durante el recorrido puede saltarse elementos o romper el bucle.",
            ),
            (
                "Usar índices cuando no hace falta",
                "Recorrer por índice es más verboso y propenso a errores. Usa el elemento directamente.",
            ),
            (
                "Confundir break con continue",
                "`break` termina el bucle; `continue` solo salta esa vuelta.",
            ),
            (
                "No inicializar la variable del while",
                "Si la variable no existe antes del while, obtendrás un error de nombre.",
            ),
            (
                "Olvidar actualizar la variable del while",
                "Sin actualización, la condición nunca cambia y el bucle se repite sin fin.",
            ),
            (
                "Iterar sobre un dict sin saber qué devuelve",
                "Iterar un diccionario devuelve claves, no valores. Usa `.items()` si necesitas ambos.",
            ),
            (
                "Reusar la variable del bucle",
                "Si usas la misma variable fuera del bucle sin intención, puedes pisar valores.",
            ),
            (
                "No controlar el paso en range",
                "Si necesitas saltos, define el paso. `range(0, 10, 2)` evita cálculos manuales.",
            ),
            (
                "Usar else del for sin entender",
                "El else del for se ejecuta si no hubo break. Evita usarlo si no es claro.",
            ),
            (
                "Ignorar el rendimiento en bucles grandes",
                "Operaciones pesadas en cada iteración pueden ralentizar el programa.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "For sobre lista",
                """# Aprende esto
# Aprenderás a recorrer una lista con for.
# Verás cómo procesar cada elemento.
# Entenderás que no necesitas índices.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
for fruta in frutas:  # Recorremos cada fruta
    mensaje = f"Fruta: {fruta}"  # Construimos mensaje
    print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás cada fruta en una línea.
#
# Por qué funciona
# for toma cada elemento de la lista en orden.
#
# Lo típico que sale mal
# - Usar índices sin necesidad.
# - Cambiar la lista mientras se recorre.
""",
            ),
            (
                "Range básico",
                """# Aprende esto
# Aprenderás a usar range para contar.
# Verás que el final no se incluye.
# Entenderás cómo usarlo en un for.
#
# Haz esto
for numero in range(3):  # Generamos 0,1,2
    print(numero)  # Mostramos el número
suma = 0  # Iniciamos suma
for valor in range(1, 4):  # Generamos 1,2,3
    suma += valor  # Acumulamos suma
print(suma)  # Mostramos la suma
#
# Verás esto
# Verás 0, 1, 2 y luego 6.
#
# Por qué funciona
# range genera una secuencia de números.
#
# Lo típico que sale mal
# - Esperar que incluya el número final.
# - Usar límites incorrectos.
""",
            ),
            (
                "Range con paso",
                """# Aprende esto
# Aprenderás a usar un paso en range.
# Verás cómo saltar números.
# Entenderás la utilidad en series.
#
# Haz esto
for numero in range(0, 10, 2):  # Saltamos de 2 en 2
    print(numero)  # Mostramos el número
contador = 0  # Iniciamos contador
for numero in range(5, 0, -1):  # Cuenta regresiva
    contador += numero  # Acumulamos suma
print(contador)  # Mostramos la suma
#
# Verás esto
# Verás 0, 2, 4, 6, 8 y luego 15.
#
# Por qué funciona
# El tercer argumento de range define el paso.
#
# Lo típico que sale mal
# - Usar un paso incorrecto.
# - Olvidar que el límite sigue sin incluirse.
""",
            ),
            (
                "While con control",
                """# Aprende esto
# Aprenderás a usar while con una condición.
# Verás cómo actualizar la variable.
# Entenderás cómo evitar bucles infinitos.
#
# Haz esto
contador = 0  # Iniciamos contador
while contador < 3:  # Condición de salida
    print(contador)  # Mostramos contador
    contador += 1  # Actualizamos contador
print("Fin")  # Indicamos fin
#
# Verás esto
# Verás 0, 1, 2 y luego "Fin".
#
# Por qué funciona
# La condición cambia y el bucle termina.
#
# Lo típico que sale mal
# - No actualizar contador.
# - Usar una condición incorrecta.
""",
            ),
            (
                "break en un for",
                """# Aprende esto
# Aprenderás a detener un bucle con break.
# Verás cómo salir antes de tiempo.
# Entenderás cuándo usarlo.
#
# Haz esto
numeros = [1, 4, 7, 10]  # Lista de números
for numero in numeros:  # Recorremos la lista
    if numero == 7:  # Condición de salida
        print("Encontrado")  # Mensaje
        break  # Salimos del bucle
    print(numero)  # Mostramos número
#
# Verás esto
# Verás 1, 4 y luego "Encontrado".
#
# Por qué funciona
# break termina el bucle inmediatamente.
#
# Lo típico que sale mal
# - Usar break sin necesidad.
# - Olvidar que rompe el bucle completo.
""",
            ),
            (
                "continue en un for",
                """# Aprende esto
# Aprenderás a saltar una iteración con continue.
# Verás cómo omitir ciertos casos.
# Entenderás la diferencia con break.
#
# Haz esto
numeros = [1, 2, 3, 4]  # Lista de números
for numero in numeros:  # Recorremos la lista
    if numero % 2 == 0:  # Si es par
        continue  # Saltamos
    print(numero)  # Mostramos impares
#
# Verás esto
# Verás 1 y 3.
#
# Por qué funciona
# continue omite el resto y pasa a la siguiente vuelta.
#
# Lo típico que sale mal
# - Usar continue y olvidar lógica posterior.
# - Saltar casos sin darse cuenta.
""",
            ),
            (
                "Enumerate",
                """# Aprende esto
# Aprenderás a usar enumerate para índice y valor.
# Verás cómo evitar range(len()).
# Entenderás la claridad que aporta.
#
# Haz esto
nombres = ["Ana", "Luis", "Marta"]  # Lista de nombres
for indice, nombre in enumerate(nombres):  # Índice y valor
    mensaje = f"{indice}: {nombre}"  # Mensaje con índice
    print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás 0: Ana, 1: Luis, 2: Marta.
#
# Por qué funciona
# enumerate entrega índice y valor a la vez.
#
# Lo típico que sale mal
# - Olvidar desempaquetar los dos valores.
# - Revertir el orden de índice y valor.
""",
            ),
            (
                "Recorrer diccionarios",
                """# Aprende esto
# Aprenderás a iterar claves y valores de un dict.
# Verás cómo usar items().
# Entenderás cómo construir mensajes.
#
# Haz esto
precios = {"pan": 2, "leche": 3}  # Diccionario de precios
for producto, precio in precios.items():  # Clave y valor
    mensaje = f"{producto}: {precio}"  # Construimos mensaje
    print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "pan: 2" y "leche: 3".
#
# Por qué funciona
# items() entrega pares clave-valor.
#
# Lo típico que sale mal
# - Iterar solo por claves y olvidar el valor.
# - Modificar el dict dentro del bucle.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Imprime los números del 1 al 5 usando range.",
                "hints": ["Usa range(1, 6)."],
                "solution": """for numero in range(1, 6):
    print(numero)""",
            },
            {
                "question": "Recorre una lista de nombres y muestra cada uno.",
                "hints": ["Usa for nombre in nombres."],
                "solution": """nombres = ["Ana", "Luis"]
for nombre in nombres:
    print(nombre)""",
            },
            {
                "question": "Crea un while que cuente de 0 a 2.",
                "hints": ["Actualiza el contador dentro del bucle."],
                "solution": """contador = 0
while contador <= 2:
    print(contador)
    contador += 1""",
            },
            {
                "question": "Usa break para detener un bucle cuando encuentres el número 3.",
                "hints": ["Compara el número dentro del for."],
                "solution": """for numero in [1, 2, 3, 4]:
    if numero == 3:
        break
    print(numero)""",
            },
            {
                "question": "Usa continue para imprimir solo números impares del 1 al 5.",
                "hints": ["Comprueba si es par y salta."],
                "solution": """for numero in range(1, 6):
    if numero % 2 == 0:
        continue
    print(numero)""",
            },
            {
                "question": "Recorre un diccionario de edades y muestra nombre y edad.",
                "hints": ["Usa items() en el for."],
                "solution": """edades = {"Ana": 30, "Luis": 28}
for nombre, edad in edades.items():
    print(nombre, edad)""",
            },
        ]
