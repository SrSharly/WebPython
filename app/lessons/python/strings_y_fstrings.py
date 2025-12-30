from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class StringsYFStringsLesson(Lesson):
    TITLE = "Strings y f-strings"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["strings", "f-strings", "formato", "texto"]

    def summary(self) -> str:
        return (
            "Aprende a trabajar con texto en Python: concatenar, acceder a caracteres, usar métodos útiles "
            "y formatear con f-strings de forma clara y segura."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: el texto es parte de casi todo
Los strings aparecen en nombres, mensajes, rutas de archivo y resultados. Saber manejarlos evita errores de formato
y mejora la claridad de tu código. Aquí aprenderás a crear strings, a transformarlos y a construir mensajes con
f-strings.

## Paso 1: Concatenar textos de forma segura
Concatenar es unir dos o más strings.

**Aprende esto**
- Aprenderás a unir textos sin perder legibilidad.
- Verás cómo convertir números a texto cuando sea necesario.

**Haz esto**
```
nombre = "Ana"  # Nombre del usuario
apellido = "López"  # Apellido del usuario
edad = 30  # Edad como número
nombre_completo = nombre + " " + apellido  # Unimos nombre y apellido
mensaje = nombre_completo + " tiene " + str(edad) + " años"  # Convertimos edad
print(mensaje)  # Mostramos el mensaje
```

**Verás esto**
Verás un texto como `Ana López tiene 30 años`.

**Por qué funciona**
`str(edad)` convierte el número a texto y permite concatenar con otros strings.

**Lo típico que sale mal**
- Olvidar convertir el número a string antes de concatenar.
- Juntar textos sin espacios y obtener palabras pegadas.

## Paso 2: Acceder a caracteres y rebanar
Puedes leer partes de un string usando índices y slicing.

**Aprende esto**
- Aprenderás a tomar un carácter específico y un fragmento del texto.
- Verás cómo los índices empiezan en 0.

**Haz esto**
```
texto = "Python"  # Texto base
primera = texto[0]  # Primer carácter
ultima = texto[-1]  # Último carácter
fragmento = texto[1:4]  # Substring desde índice 1 hasta 3
mensaje = primera + "-" + fragmento + "-" + ultima  # Combinamos partes
print(mensaje)  # Mostramos el resultado
```

**Verás esto**
Verás algo como `P-yth-n`.

**Por qué funciona**
Los índices negativos cuentan desde el final y el slicing toma un rango sin incluir el extremo derecho.

**Lo típico que sale mal**
- Usar índices fuera de rango.
- Pensar que el extremo derecho del slice se incluye.

## Paso 3: Métodos comunes
Los métodos de string devuelven **nuevos textos** (los strings son inmutables).

**Aprende esto**
- Aprenderás a limpiar y transformar texto con métodos comunes.
- Verás que cada método devuelve un nuevo string.

**Haz esto**
```
texto = "  Hola Mundo  "  # Texto con espacios extra
limpio = texto.strip()  # Quitamos espacios externos
mayus = limpio.upper()  # Pasamos a mayúsculas
reemplazo = mayus.replace("MUNDO", "PYTHON")  # Reemplazamos una palabra
resultado = reemplazo + "!"  # Añadimos un signo
print(resultado)  # Mostramos el resultado
```

**Verás esto**
Verás `HOLA PYTHON!`.

**Por qué funciona**
`strip`, `upper` y `replace` crean nuevos strings sin modificar el original.

**Lo típico que sale mal**
- Esperar que el string original cambie sin reasignar.
- Usar replace sin cuidar mayúsculas/minúsculas.

## Paso 4: f-strings para formatear
Las f-strings permiten insertar variables directamente en un texto.

**Aprende esto**
- Aprenderás a crear mensajes claros sin concatenar demasiado.
- Verás cómo formatear números dentro del texto.

**Haz esto**
```
producto = "Café"  # Nombre del producto
precio = 9.5  # Precio base
cantidad = 3  # Cantidad
subtotal = precio * cantidad  # Calculamos subtotal
mensaje = f"{cantidad}x {producto} cuesta {subtotal:.2f}"  # Formateamos
print(mensaje)  # Mostramos el mensaje
```

**Verás esto**
Verás `3x Café cuesta 28.50`.

**Por qué funciona**
Las f-strings evalúan variables dentro de `{}` y permiten formatos como `.2f`.

**Lo típico que sale mal**
- Olvidar la `f` al inicio del string.
- Usar formatos numéricos incorrectos.

## Paso 5: Plantillas simples con join
`join` permite unir listas de textos con un separador.

**Aprende esto**
- Aprenderás a unir varias palabras con un separador.
- Verás cómo evitar concatenaciones largas.

**Haz esto**
```
items = ["pan", "leche", "café"]  # Lista de textos
separador = ", "  # Separador con coma y espacio
lista_texto = separador.join(items)  # Unimos los elementos
mensaje = f"Necesitas: {lista_texto}"  # Construimos el mensaje
print(mensaje)  # Mostramos el mensaje
```

**Verás esto**
Verás `Necesitas: pan, leche, café`.

**Por qué funciona**
`join` inserta el separador entre cada elemento de la lista.

**Lo típico que sale mal**
- Usar `join` con elementos que no son strings.
- Olvidar el separador y obtener un texto pegado.

## Más allá (nivel pro)
Una buena práctica es normalizar texto para comparaciones seguras.

**Aprende esto**
- Aprenderás a comparar texto sin diferencias de mayúsculas o espacios.
- Verás cómo construir claves normalizadas para búsquedas.

**Haz esto**
```
entrada = "  Lima "  # Texto con espacios y mayúsculas
normalizada = entrada.strip().lower()  # Quitamos espacios y pasamos a minúsculas
ciudades = ["lima", "cusco", "arequipa"]  # Lista normalizada
existe = normalizada in ciudades  # Comparamos texto limpio
print(normalizada)  # Mostramos el texto normalizado
print(existe)  # Mostramos True
```

**Verás esto**
Verás `lima` y `True`.

**Por qué funciona**
Al normalizar eliminas variaciones de formato y comparas textos de forma consistente.

**Lo típico que sale mal**
- Comparar texto sin limpiar y fallar por espacios extra.
- Mezclar mayúsculas y minúsculas en listas de referencia.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenar número y texto",
                "Debes convertir el número con str() antes de concatenar.",
            ),
            (
                "Olvidar la f en f-strings",
                "Sin la f, el texto no interpreta variables.",
            ),
            (
                "Indices fuera de rango",
                "Acceder a un índice inexistente genera IndexError.",
            ),
            (
                "Confundir slicing",
                "El límite derecho del slice no se incluye.",
            ),
            (
                "No reasignar tras usar métodos",
                "Los métodos de string devuelven un nuevo texto.",
            ),
            (
                "Usar join con números",
                "join requiere strings; convierte antes.",
            ),
            (
                "Ignorar espacios en comparaciones",
                "strip() evita errores por espacios invisibles.",
            ),
            (
                "Comparar mayúsculas con minúsculas",
                "Normaliza con lower() o upper() antes de comparar.",
            ),
            (
                "Usar replace sin cuidado",
                "replace distingue mayúsculas y minúsculas.",
            ),
            (
                "Concatenaciones largas",
                "Usa f-strings o join para mantener legibilidad.",
            ),
            (
                "Olvidar escapar comillas",
                "Usa comillas simples o dobles correctamente para evitar errores.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenación con conversión",
                """# Aprende esto
# Aprenderás a unir texto con un número.
# Verás cómo usar str() para evitar errores.
#
# Haz esto
nombre = "Ana"  # Nombre del usuario
edad = 30  # Edad numérica
nombre_completo = nombre + " Pérez"  # Agregamos apellido
mensaje = nombre_completo + " tiene " + str(edad) + " años"  # Convertimos edad
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Ana Pérez tiene 30 años".
#
# Por qué funciona
# str convierte el número a texto para poder concatenar.
#
# Lo típico que sale mal
# - Olvidar str() y generar un error de tipo.
# - No agregar espacios entre palabras.
""",
            ),
            (
                "Slicing básico",
                """# Aprende esto
# Aprenderás a tomar partes de un string.
# Verás cómo usar índices positivos y negativos.
#
# Haz esto
texto = "Python"  # Texto base
primera = texto[0]  # Primer carácter
ultima = texto[-1]  # Último carácter
fragmento = texto[1:4]  # Substring
mensaje = primera + "-" + fragmento + "-" + ultima  # Combinamos
print(mensaje)  # Mostramos el resultado
#
# Verás esto
# Verás "P-yth-n".
#
# Por qué funciona
# Los índices siguen el orden y el slice excluye el final.
#
# Lo típico que sale mal
# - Usar índices fuera de rango.
# - Pensar que el slice incluye el extremo derecho.
""",
            ),
            (
                "Métodos de limpieza",
                """# Aprende esto
# Aprenderás a limpiar texto con strip.
# Verás cómo transformar a mayúsculas.
#
# Haz esto
texto = "  Hola Mundo  "  # Texto con espacios
limpio = texto.strip()  # Quitamos espacios externos
mayus = limpio.upper()  # Pasamos a mayúsculas
resultado = mayus + "!"  # Añadimos signo
print(resultado)  # Mostramos el texto final
#
# Verás esto
# Verás "HOLA MUNDO!".
#
# Por qué funciona
# strip y upper devuelven nuevos strings.
#
# Lo típico que sale mal
# - No reasignar el resultado.
# - Confundir upper con title.
""",
            ),
            (
                "Replace con cuidado",
                """# Aprende esto
# Aprenderás a reemplazar partes del texto.
# Verás cómo evitar reemplazos inesperados.
#
# Haz esto
texto = "Curso de Python"  # Texto base
nuevo = texto.replace("Python", "SQL")  # Reemplazamos una palabra
mensaje = "Antes: " + texto  # Mensaje original
mensaje += " | Después: " + nuevo  # Mensaje final
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Antes: Curso de Python | Después: Curso de SQL".
#
# Por qué funciona
# replace crea un nuevo string con el reemplazo.
#
# Lo típico que sale mal
# - Usar replace con mayúsculas diferentes.
# - Olvidar que el original no cambia.
""",
            ),
            (
                "f-strings con formato",
                """# Aprende esto
# Aprenderás a formatear números en f-strings.
# Verás cómo construir mensajes claros.
#
# Haz esto
producto = "Café"  # Producto
precio = 9.5  # Precio base
cantidad = 3  # Cantidad
subtotal = precio * cantidad  # Calculamos subtotal
mensaje = f"{cantidad}x {producto} cuesta {subtotal:.2f}"  # Formateamos
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "3x Café cuesta 28.50".
#
# Por qué funciona
# Las f-strings insertan valores y el formato .2f limita decimales.
#
# Lo típico que sale mal
# - Olvidar la f.
# - Usar formato incompatible.
""",
            ),
            (
                "join para listas",
                """# Aprende esto
# Aprenderás a unir una lista de textos.
# Verás cómo evitar concatenaciones largas.
#
# Haz esto
items = ["pan", "leche", "café"]  # Lista de textos
separador = ", "  # Separador
lista_texto = separador.join(items)  # Unimos elementos
mensaje = f"Necesitas: {lista_texto}"  # Texto final
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Necesitas: pan, leche, café".
#
# Por qué funciona
# join inserta el separador entre cada elemento.
#
# Lo típico que sale mal
# - Usar join con números.
# - Olvidar el separador.
""",
            ),
            (
                "Normalizar texto",
                """# Aprende esto
# Aprenderás a comparar texto de forma segura.
# Verás cómo quitar espacios y usar minúsculas.
#
# Haz esto
entrada = "  Lima "  # Texto con espacios
normalizada = entrada.strip().lower()  # Limpiamos y convertimos
ciudades = ["lima", "cusco", "arequipa"]  # Lista normalizada
existe = normalizada in ciudades  # Comparamos
print(normalizada)  # Mostramos el texto limpio
print(existe)  # Mostramos True
#
# Verás esto
# Verás "lima" y True.
#
# Por qué funciona
# Normalizar texto evita diferencias de formato.
#
# Lo típico que sale mal
# - Comparar sin limpiar.
# - Mezclar mayúsculas y minúsculas.
""",
            ),
            (
                "Interpolación con variables",
                """# Aprende esto
# Aprenderás a combinar variables en un texto.
# Verás cómo usar f-strings para claridad.
#
# Haz esto
usuario = "Ana"  # Nombre del usuario
saldo = 120.5  # Saldo numérico
mensaje = f"{usuario} tiene {saldo:.1f} créditos"  # Formato con 1 decimal
confirmacion = "Estado: " + "OK"  # Texto adicional
print(mensaje)  # Mostramos el mensaje
print(confirmacion)  # Mostramos la confirmación
#
# Verás esto
# Verás "Ana tiene 120.5 créditos" y "Estado: OK".
#
# Por qué funciona
# f-strings insertan valores y permiten formatear decimales.
#
# Lo típico que sale mal
# - Olvidar el formato.
# - Usar concatenaciones largas sin claridad.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Concatena nombre y apellido y muestra el resultado.",
                "hints": ["Usa + y un espacio"],
                "solution": "nombre = 'Ana'\napellido = 'Pérez'\nprint(nombre + ' ' + apellido)",
            },
            {
                "question": "Extrae los tres primeros caracteres de una palabra.",
                "hints": ["Usa slicing"],
                "solution": "palabra = 'Python'\nprint(palabra[:3])",
            },
            {
                "question": "Convierte un texto a mayúsculas usando upper().",
                "hints": ["Recuerda reasignar"],
                "solution": "texto = 'hola'\nmayus = texto.upper()\nprint(mayus)",
            },
            {
                "question": "Crea un mensaje con f-string que muestre un precio con 2 decimales.",
                "hints": ["Usa :.2f"],
                "solution": "precio = 12.5\nprint(f'Precio: {precio:.2f}')",
            },
            {
                "question": "Une una lista de palabras con join y una coma.",
                "hints": ["Usa ', '.join"],
                "solution": "palabras = ['pan', 'leche']\nprint(', '.join(palabras))",
            },
            {
                "question": "Normaliza un texto eliminando espacios y pasando a minúsculas.",
                "hints": ["Usa strip() y lower()"],
                "solution": "texto = '  LIMA '\nnormalizado = texto.strip().lower()\nprint(normalizado)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
