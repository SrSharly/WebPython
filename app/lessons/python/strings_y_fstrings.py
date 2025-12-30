from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class StringsFStringsLesson(Lesson):
    TITLE = "Strings y f-strings"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["strings", "f-strings", "format", "texto"]

    def summary(self) -> str:
        return (
            "Domina los textos en Python: creación, concatenación, f-strings, escapes y formato seguro para "
            "mensajes claros y legibles."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: los textos son tu interfaz con el mundo
En Python, los textos (`str`) aparecen en todas partes: mensajes en pantalla, nombres, rutas de archivo, respuestas de una API
o el contenido de un formulario. Aprender a manejarlos bien es lo que convierte un script que “funciona” en uno que se puede
leer, mantener y explicar. Además, los textos son inmutables: cada vez que “modificas” un texto en realidad creas uno nuevo.
Entender esto te ayuda a escribir código más claro y eficiente.

En esta lección vas a aprender desde cero cómo crear textos, cómo unirlos, cómo insertar valores usando f-strings y cómo
formatear resultados de manera legible. También aprenderás a trabajar con saltos de línea, comillas y escapes sin romper el
programa. Al final tendrás un conjunto de patrones para construir mensajes precisos sin adivinar.

### Nota (CalloutBox: note)
Los textos en Python siempre son inmutables. Eso significa que métodos como `replace` o `upper` devuelven un texto nuevo en
lugar de cambiar el original. Si quieres conservar el cambio, debes reasignarlo.

## Paso 1: crear textos y elegir comillas
Puedes crear textos con comillas simples o dobles. Lo importante es ser consistente y escoger la que te permita escribir
sin escapar demasiado. Si tu texto contiene comillas simples, usa dobles y viceversa. Esto evita caracteres extraños y mejora
la legibilidad.

Cuando necesitas un texto largo o con saltos de línea, usa triple comilla. Es útil para mensajes largos, descripciones o
plantillas donde la forma importa.

## Paso 2: concatenación básica y lectura clara
Concatenar es unir textos. Puedes usar `+` para unir dos strings, pero debes cuidar los espacios. Este enfoque es directo,
pero se vuelve difícil de leer cuando agregas números o demasiados fragmentos. Por eso es importante saber cuándo pasar a un
formato más claro como f-strings.

## Paso 3: f-strings para insertar variables con precisión
Las f-strings son la forma más clara de construir textos en Python moderno. Pones una `f` antes del texto y luego insertas
variables con `{}`. Esto mantiene la frase completa visible, sin interrupciones por operadores `+`.

Además, las f-strings permiten formatear números: puedes controlar decimales, alineación y relleno. Este detalle es clave
cuando quieres resultados consistentes en reportes o logs.

### Buenas prácticas (CalloutBox: best_practice)
Si un mensaje tiene variables, prioriza f-strings. Son más legibles, evitan errores de concatenación y hacen el código más
explicativo.

## Paso 4: saltos de línea y textos multilínea
Los saltos de línea (`\\n`) te permiten construir mensajes con varias líneas dentro de un solo texto. También puedes usar
triple comilla para mantener la forma original. Elige el método según el tipo de texto: `\\n` es útil para mensajes cortos,
la triple comilla es ideal para plantillas largas.

## Paso 5: escapes y caracteres especiales
Si necesitas escribir comillas dentro de un texto, usa el escape `\\`. Por ejemplo, `\"` o `\\'`. También puedes escribir
caracteres especiales como tabulaciones con `\\t`. Usar escapes te permite mantener la sintaxis correcta sin romper el código.

## Paso 6: formateo numérico y alineación
En reportes o interfaces es común alinear números, controlar decimales o rellenar con ceros. Las f-strings permiten esto con
formatos como `{valor:.2f}` para dos decimales o `{numero:03d}` para rellenar con ceros. Estos detalles hacen que tu salida
sea profesional y consistente.

## Paso 7: resumen para escribir textos confiables
Cuando construyas un texto, piensa en tres cosas: qué valores insertarás, cómo quieres que se vea y cómo evitar errores de
concatenación. Si el texto es simple, `+` puede bastar; si tiene variables, usa f-strings; si tiene formato, agrega un
especificador. Esa regla simple te cubre casi todo.

## Más allá (nivel pro)
Conforme tu código crece, los textos se convierten en parte del diseño. La claridad en los mensajes facilita depuración,
pruebas y soporte. Un texto bien construido puede ser la diferencia entre un bug difícil y una solución inmediata.

### Consejos pro
- Prefiere f-strings para mensajes que incluyan variables: son más rápidos y legibles.
- Usa nombres descriptivos en las variables insertadas para que la frase se entienda sola.
- Si el texto será traducido o reutilizado, guárdalo en una plantilla y luego inserta valores.
- Para reportes numéricos, fija decimales y alineación para que la salida sea estable.
- Cuando una cadena crece demasiado, considera dividirla en partes y documentar la intención.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenar texto con número",
                "`""Total: "" + 10` falla. Convierte el número con `str(10)` o usa f-strings.",
            ),
            (
                "Olvidar espacios en concatenación",
                "Unir `""Hola"" + ""Mundo""` produce `HolaMundo`. Agrega el espacio manualmente o usa f-strings.",
            ),
            (
                "Asumir que upper() modifica el texto",
                "Los strings son inmutables. `texto.upper()` devuelve uno nuevo; si no lo reasignas, no cambia.",
            ),
            (
                "Escapar comillas incorrectamente",
                "Si usas comillas dobles dentro de un texto con dobles, debes escaparlas o cambiar de comillas.",
            ),
            (
                "Mezclar \n con triple comilla sin intención",
                "Cuando mezclas ambos puedes obtener saltos de línea duplicados. Elige un método consistente.",
            ),
            (
                "Formatear decimales sin redondear",
                "Mostrar un float sin formato puede dar muchos decimales. Usa `{valor:.2f}` para control.",
            ),
            (
                "Usar f-strings sin la letra f",
                "Olvidar la `f` convierte `{nombre}` en texto literal. Revisa siempre el prefijo.",
            ),
            (
                "Concatenar muchas partes con +",
                "Muchas concatenaciones reducen legibilidad. Usa f-strings o `"".join`.",
            ),
            (
                "Confundir \t con espacios",
                "Un tabulador cambia el ancho según el entorno. Úsalo solo si controlas el formato final.",
            ),
            (
                "Esperar que format() sea mágico",
                "Si no das formato explícito, `format` no alinea ni redondea como esperas. Define el especificador.",
            ),
            (
                "Reusar variables con otro tipo",
                "Si una variable era texto y luego se vuelve número, las f-strings se vuelven confusas.",
            ),
            (
                "No validar entradas de usuario",
                "Si un valor viene como texto, conviértelo antes y maneja el error si no es numérico.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear textos con comillas",
                """# Aprende esto
# Aprenderás a crear strings con comillas simples y dobles.
# Verás cómo evitar escapes innecesarios.
# Entenderás la importancia de la consistencia.
#
# Haz esto
saludo = "Hola"  # Texto con comillas dobles
nombre = 'Ana'  # Texto con comillas simples
mensaje = saludo + " " + nombre  # Unimos con espacio
print(mensaje)  # Mostramos el mensaje
frase = "Ella dijo: 'sí'"  # Comillas simples dentro de dobles
print(frase)  # Mostramos la frase
#
# Verás esto
# Verás "Hola Ana" y "Ella dijo: 'sí'".
#
# Por qué funciona
# Las comillas externas delimitan el string sin conflicto.
#
# Lo típico que sale mal
# - Usar el mismo tipo de comillas y olvidar escapes.
# - Mezclar estilos sin una regla clara.
""",
            ),
            (
                "Concatenar con +",
                """# Aprende esto
# Aprenderás a concatenar strings simples.
# Verás la importancia de los espacios.
# Entenderás cuándo cambiar a f-strings.
#
# Haz esto
ciudad = "Lima"  # Guardamos una ciudad
pais = "Perú"  # Guardamos un país
ubicacion = ciudad + ", " + pais  # Unimos con coma y espacio
print(ubicacion)  # Mostramos la ubicación
prefijo = "Ciudad: "  # Definimos un prefijo
mensaje = prefijo + ubicacion  # Unimos todo
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Lima, Perú" y "Ciudad: Lima, Perú".
#
# Por qué funciona
# El operador + une strings en orden.
#
# Lo típico que sale mal
# - Olvidar la coma o el espacio.
# - Concatenar números sin convertir.
""",
            ),
            (
                "F-strings para insertar variables",
                """# Aprende esto
# Aprenderás a insertar variables con f-strings.
# Verás cómo mejora la legibilidad.
# Entenderás que no necesitas +.
#
# Haz esto
producto = "Café"  # Guardamos un producto
precio = 3.5  # Guardamos un precio
mensaje = f"Producto: {producto}, precio: {precio}"  # Insertamos variables
print(mensaje)  # Mostramos el mensaje
stock = 12  # Guardamos un stock
mensaje_stock = f"Stock disponible: {stock}"  # Insertamos el stock
print(mensaje_stock)  # Mostramos el mensaje
#
# Verás esto
# Verás textos con las variables insertadas.
#
# Por qué funciona
# f-strings evalúan expresiones dentro de {}.
#
# Lo típico que sale mal
# - Olvidar la letra f.
# - Escribir mal el nombre de la variable.
""",
            ),
            (
                "Formato de decimales",
                """# Aprende esto
# Aprenderás a controlar decimales con f-strings.
# Verás cómo redondear para reportes.
# Entenderás por qué es útil en salidas.
#
# Haz esto
precio = 19.9876  # Precio original
precio_redondeado = f"{precio:.2f}"  # Formato con 2 decimales
print(precio_redondeado)  # Mostramos el precio
impuesto = 1.2345  # Impuesto original
impuesto_redondeado = f"{impuesto:.1f}"  # Formato con 1 decimal
print(impuesto_redondeado)  # Mostramos el impuesto
#
# Verás esto
# Verás 19.99 y 1.2.
#
# Por qué funciona
# El especificador .2f define dos decimales.
#
# Lo típico que sale mal
# - Mostrar demasiados decimales sin querer.
# - Usar formato incorrecto para enteros.
""",
            ),
            (
                "Textos multilínea",
                """# Aprende esto
# Aprenderás a crear textos con saltos de línea.
# Verás el uso de \\n y triple comilla.
# Entenderás cuándo usar cada uno.
#
# Haz esto
linea1 = "Línea uno"  # Primera línea
linea2 = "Línea dos"  # Segunda línea
mensaje = linea1 + "\\n" + linea2  # Unimos con salto de línea
print(mensaje)  # Mostramos el mensaje
bloque = \"\"\"Bloque A\nBloque B\"\"\"  # Texto con triple comilla
print(bloque)  # Mostramos el bloque
#
# Verás esto
# Verás dos líneas separadas en pantalla.
#
# Por qué funciona
# \\n crea salto de línea; triple comilla mantiene formato.
#
# Lo típico que sale mal
# - Mezclar \\n y triple comilla sin intención.
# - Esperar que los espacios se mantengan igual.
""",
            ),
            (
                "Escapar comillas",
                """# Aprende esto
# Aprenderás a escribir comillas dentro de textos.
# Verás el uso del escape \" y \\\'.
# Entenderás cómo evitar errores de sintaxis.
#
# Haz esto
frase = "Ella dijo: \"hola\""  # Comillas dobles escapadas
print(frase)  # Mostramos la frase
otra = 'Él respondió: \'sí\''  # Comillas simples escapadas
print(otra)  # Mostramos la frase
mensaje = frase + " | " + otra  # Unimos textos
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás las frases con comillas visibles.
#
# Por qué funciona
# El backslash evita que la comilla cierre el string.
#
# Lo típico que sale mal
# - Olvidar el escape y romper la cadena.
# - Usar el escape en exceso sin necesidad.
""",
            ),
            (
                "Alineación simple",
                """# Aprende esto
# Aprenderás a alinear textos con formato.
# Verás cómo rellenar con espacios.
# Entenderás la utilidad en reportes.
#
# Haz esto
producto = "Pan"  # Producto
cantidad = 4  # Cantidad
linea = f"{producto:<10} {cantidad:>3}"  # Alineamos izquierda y derecha
print(linea)  # Mostramos la línea
producto2 = "Leche"  # Segundo producto
cantidad2 = 12  # Segunda cantidad
linea2 = f"{producto2:<10} {cantidad2:>3}"  # Alineamos
print(linea2)  # Mostramos la línea
#
# Verás esto
# Verás columnas alineadas para producto y cantidad.
#
# Por qué funciona
# Los especificadores < y > controlan la alineación.
#
# Lo típico que sale mal
# - Usar anchos distintos y perder alineación.
# - Mezclar tipos sin formatear.
""",
            ),
            (
                "Insertar expresiones simples",
                """# Aprende esto
# Aprenderás a usar expresiones dentro de f-strings.
# Verás cómo calcular dentro del texto.
# Entenderás cuándo mantenerlo simple.
#
# Haz esto
precio = 5  # Precio unitario
cantidad = 3  # Cantidad
total = precio * cantidad  # Calculamos total
mensaje = f"Total: {total} (3 x 5)"  # Insertamos el total
print(mensaje)  # Mostramos el mensaje
ahorro = total - 2  # Calculamos un ahorro
mensaje_ahorro = f"Con descuento: {ahorro}"  # Insertamos el ahorro
print(mensaje_ahorro)  # Mostramos el mensaje
#
# Verás esto
# Verás el total y el total con descuento.
#
# Por qué funciona
# f-strings evalúan variables ya calculadas.
#
# Lo típico que sale mal
# - Poner expresiones complejas dentro del texto.
# - Olvidar calcular antes y perder claridad.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea dos variables `nombre` y `ciudad` y muestra un saludo con f-string.",
                "hints": ["Usa f\"Hola {nombre} de {ciudad}\".", "Asegúrate de escribir la letra f."],
                "solution": """nombre = "Luis"
ciudad = "Quito"
print(f"Hola {nombre} de {ciudad}")""",
            },
            {
                "question": "Convierte el número 12.345 a texto con 1 decimal usando f-strings.",
                "hints": ["Usa {valor:.1f}.", "Guarda el resultado en una variable."],
                "solution": """valor = 12.345
texto = f"{valor:.1f}"
print(texto)""",
            },
            {
                "question": "Construye un texto multilínea con triple comilla que tenga dos líneas.",
                "hints": ["Usa triple comilla."],
                "solution": """mensaje = \"\"\"Línea uno\nLínea dos\"\"\"\nprint(mensaje)""",
            },
            {
                "question": "Muestra una frase con comillas dobles internas usando escape.",
                "hints": ["Usa \\\\ dentro del string."],
                "solution": """frase = "Ella dijo: \"hola\""
print(frase)""",
            },
            {
                "question": "Alinea a la derecha una cantidad en un espacio de 4 caracteres.",
                "hints": ["Usa {cantidad:>4}."],
                "solution": """cantidad = 7
linea = f"Cantidad: {cantidad:>4}"
print(linea)""",
            },
            {
                "question": "Concatena dos palabras con un espacio usando +.",
                "hints": ["Agrega el espacio manualmente."],
                "solution": """palabra1 = "Hola"
palabra2 = "mundo"
texto = palabra1 + " " + palabra2
print(texto)""",
            },
        ]
