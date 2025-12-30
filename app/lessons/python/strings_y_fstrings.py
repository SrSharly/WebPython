from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class StringsFStringsLesson(Lesson):
    TITLE = "Strings y f-strings"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["strings", "f-strings", "formato", "texto"]

    def summary(self) -> str:
        return (
            "Aprende desde cero cómo trabajar con texto en Python: crear strings, "
            "limpiarlos, cortarlos y formatearlos con f-strings de forma clara y segura."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: el texto es dato, no solo un mensaje
Los strings están en todas partes: nombres, rutas, etiquetas, mensajes, archivos y datos de usuario. Saber manipularlos
significa saber limpiar, formatear y presentar información con precisión. En esta lección aprenderás a crear strings,
recortar, buscar, reemplazar y usar f-strings para construir mensajes legibles con datos dinámicos.

## Paso 1: Crear strings y concatenar
Crear strings es simple, pero la claridad importa desde la primera línea.

**Aprende esto**
- Aprenderás a definir strings y a concatenarlos con intención.
- Verás cómo usar `str()` cuando quieres unir texto con números.

**Haz esto**
print("ok")  # Confirmamos
```
nombre = "Ana"  # Texto base
apellido = "López"  # Texto adicional
separador = " "  # Espacio entre palabras
nombre_completo = nombre + separador + apellido  # Concatenamos
edad = 30  # Número entero
mensaje = "Nombre: " + nombre_completo + ", Edad: " + str(edad)  # Mensaje
print(mensaje)  # Mostramos el mensaje
print(len(nombre_completo))  # Mostramos la longitud
print("ok")  # Confirmamos
```

**Verás esto**
Verás un mensaje completo y la longitud del nombre.

**Por qué funciona**
El operador `+` concatena strings y `str()` convierte números para que puedan unirse a texto.

**Lo típico que sale mal**
- Concatenar texto y números sin `str()`.
- Olvidar espacios entre palabras al unir strings.

## Paso 2: Indexar y cortar strings
Los strings son secuencias, por lo tanto admiten índices y cortes.

**Aprende esto**
- Aprenderás a acceder a caracteres individuales.
- Verás cómo extraer partes con slicing.

**Haz esto**
print("ok")  # Confirmamos
```
texto = "Python"  # String base
primera = texto[0]  # Primer carácter
ultima = texto[-1]  # Último carácter
subtexto = texto[0:3]  # Primeros tres caracteres
longitud = len(texto)  # Longitud total
resumen = primera + "-" + ultima + "-" + subtexto  # Resumen
print(texto)  # Mostramos el texto
print(resumen)  # Mostramos el resumen
print(longitud)  # Mostramos la longitud
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Python`, un resumen como `P-n-Pyt` y el número 6.

**Por qué funciona**
Los índices positivos y negativos acceden a caracteres y el slicing crea un nuevo string con el rango solicitado.

**Lo típico que sale mal**
- Pedir un índice fuera de rango y causar error.
- Confundir slicing con índices únicos.

## Paso 3: Limpiar y transformar texto
Los métodos de string te ayudan a limpiar datos que vienen con espacios o formato inconsistente.

**Aprende esto**
- Aprenderás a usar `strip()`, `lower()` y `upper()`.
- Verás cómo encadenar transformaciones guardando resultados.

**Haz esto**
print("ok")  # Confirmamos
```
texto = "  Hola Mundo  "  # Texto con espacios
texto_limpio = texto.strip()  # Quitamos espacios extremos
texto_minus = texto_limpio.lower()  # Convertimos a minúsculas
texto_mayus = texto_limpio.upper()  # Convertimos a mayúsculas
resumen = texto_minus + " | " + texto_mayus  # Resumen
print(texto)  # Mostramos el texto original
print(texto_limpio)  # Mostramos el texto limpio
print(resumen)  # Mostramos el resumen
print("ok")  # Confirmamos
```

**Verás esto**
Verás el texto original con espacios, el texto limpio y el resumen con minúsculas y mayúsculas.

**Por qué funciona**
`strip()` devuelve un string nuevo sin espacios y los métodos de cambio de caso también devuelven nuevos strings.

**Lo típico que sale mal**
- Esperar que `strip()` modifique el texto original.
- Olvidar guardar el resultado de un método.

## Paso 4: Buscar y reemplazar
Buscar y reemplazar es básico para limpiar datos provenientes de usuarios o archivos.

**Aprende esto**
- Aprenderás a usar `in` y `replace()` con seguridad.
- Verás cómo construir un mensaje con el resultado.

**Haz esto**
print("ok")  # Confirmamos
```
frase = "Precio: $100"  # Frase de ejemplo
hay_signo = "$" in frase  # Verificamos si aparece el símbolo
frase_limpia = frase.replace("$", "")  # Quitamos el símbolo
monto = frase_limpia.split(": ")[1]  # Tomamos la parte del monto
mensaje = "Monto encontrado: " + monto  # Construimos el mensaje
print(hay_signo)  # Mostramos el booleano
print(frase_limpia)  # Mostramos la frase limpia
print(mensaje)  # Mostramos el mensaje
print("ok")  # Confirmamos
```

**Verás esto**
Verás `True`, la frase sin `$` y el mensaje con el monto.

**Por qué funciona**
`in` verifica presencia, `replace()` genera un nuevo string y `split()` divide por un separador.

**Lo típico que sale mal**
- Usar `split()` sin verificar que el separador existe.
- Reemplazar más de lo esperado por usar un patrón demasiado amplio.

## Paso 5: Formatear con f-strings
Las f-strings son la forma más clara de inyectar variables en texto.

**Aprende esto**
- Aprenderás a usar f-strings para construir mensajes dinámicos.
- Verás cómo formatear números con precisión.

**Haz esto**
print("ok")  # Confirmamos
```
producto = "Café"  # Nombre del producto
precio = 3.5  # Precio base
cantidad = 2  # Unidades
subtotal = precio * cantidad  # Calculamos el subtotal
mensaje = f"Producto: {producto} | Subtotal: {subtotal:.2f}"  # Formateo
print(mensaje)  # Mostramos el mensaje
print(type(mensaje))  # Confirmamos el tipo
print("ok")  # Confirmamos
```

**Verás esto**
Verás un mensaje con el subtotal en dos decimales, por ejemplo `Subtotal: 7.00`.

**Por qué funciona**
Las f-strings evalúan expresiones dentro de `{}` y permiten formatear números con especificadores como `.2f`.

**Lo típico que sale mal**
- Olvidar la `f` antes de las comillas y ver los `{}` sin evaluar.
- Formatear números sin controlar decimales.

## Paso 6: Strings multilínea y escape
Cuando necesitas texto largo, puedes usar strings multilínea y caracteres de escape.

**Aprende esto**
- Aprenderás a usar comillas triples para texto largo.
- Verás cómo incluir saltos de línea y comillas dentro del texto.

**Haz esto**
print("ok")  # Confirmamos
```
linea1 = "Primera línea"  # Texto base
linea2 = "Segunda línea"  # Texto base
texto = linea1 + "\n" + linea2  # Unimos con salto de línea
titulo = "\"Reporte\""  # Texto con comillas escapadas
resumen = titulo + "\n" + texto  # Construimos el texto final
print(resumen)  # Mostramos el texto
print(len(resumen))  # Mostramos la longitud
print("ok")  # Confirmamos
```

**Verás esto**
Verás un texto con salto de línea y un título con comillas.

**Por qué funciona**
`\n` crea un salto de línea dentro del string y `\"` permite insertar comillas dobles en texto.

**Lo típico que sale mal**
- Olvidar escapar comillas y romper la cadena.
- Contar mal los saltos de línea al calcular longitudes.

## Más allá (nivel pro): plantillas y limpieza robusta
En proyectos reales, formatear textos suele incluir datos opcionales y limpieza consistente.

**Aprende esto**
- Aprenderás a construir plantillas con valores opcionales.
- Verás cómo asegurar formatos consistentes en reportes.

**Haz esto**
print("ok")  # Confirmamos
```
cliente = "Ana"  # Nombre del cliente
ciudad = "Lima"  # Ciudad del cliente
saldo = 1520.5  # Saldo numérico
plantilla = f"Cliente: {cliente} | Ciudad: {ciudad}"  # Plantilla base
detalle = f"Saldo: {saldo:,.2f}"  # Formato con separador de miles
reporte = plantilla + "\n" + detalle  # Reporte final
print(reporte)  # Mostramos el reporte
print("ok")  # Confirmamos
```

**Verás esto**
Verás un reporte con dos líneas y el saldo formateado con separador de miles.

**Por qué funciona**
Las f-strings permiten insertar variables y aplicar formatos numéricos avanzados, manteniendo el texto legible.

**Lo típico que sale mal**
- Mezclar concatenación y f-strings sin necesidad.
- No estandarizar el formato y generar reportes inconsistentes.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenar sin str()",
                "Intentar unir texto y números sin convertir causa error.",
            ),
            (
                "Índices fuera de rango",
                "Acceder a posiciones inexistentes en un string provoca IndexError.",
            ),
            (
                "Olvidar reasignar",
                "Métodos como strip o lower devuelven un nuevo string.",
            ),
            (
                "Olvidar la f en f-strings",
                "Sin la f, las variables no se evalúan.",
            ),
            (
                "Reemplazar demasiado",
                "replace() sustituye todas las coincidencias si no limitas.",
            ),
            (
                "Usar split sin validar",
                "split() puede devolver menos partes si el separador no existe.",
            ),
            (
                "Confundir slicing con índice",
                "texto[0:3] devuelve tres caracteres, texto[3] uno solo.",
            ),
            (
                "No limpiar espacios",
                "Olvidar strip() deja espacios que rompen comparaciones.",
            ),
            (
                "Comparar sin normalizar",
                "Comparar textos sin lower() produce resultados inesperados.",
            ),
            (
                "Escapar comillas mal",
                "Olvidar el escape rompe la cadena de texto.",
            ),
            (
                "Ignorar encoding",
                "Al leer archivos, un encoding incorrecto da caracteres raros.",
            ),
            (
                "Crear mensajes ambiguos",
                "Concatenar sin separadores genera textos difíciles de leer.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenación básica",
                """# Aprende esto
# Aprenderás a concatenar strings con claridad.
# Verás cómo convertir números a texto.
# Construirás mensajes legibles.
#
# Haz esto
nombre = "Ana"  # Nombre
apellido = "López"  # Apellido
nombre_completo = nombre + " " + apellido  # Concatenamos
edad = 30  # Número entero
mensaje = "Nombre: " + nombre_completo + ", Edad: " + str(edad)  # Mensaje
print(mensaje)  # Mostramos el mensaje
print(len(nombre_completo))  # Longitud
print(type(mensaje))  # Tipo del mensaje
#
# Verás esto
# Verás el mensaje completo y la longitud del nombre.
#
# Por qué funciona
# str() permite unir números con texto y + concatena strings.
#
# Lo típico que sale mal
# - Olvidar str() al concatenar.
# - No incluir espacios.
""",
            ),
            (
                "Indexar caracteres",
                """# Aprende esto
# Aprenderás a acceder a caracteres con índices.
# Verás el primer y último carácter.
# Entenderás índices positivos y negativos.
#
# Haz esto
texto = "Python"  # String base
primera = texto[0]  # Primer carácter
ultima = texto[-1]  # Último carácter
subtexto = texto[0:3]  # Substring
resumen = primera + "-" + ultima + "-" + subtexto  # Resumen
print(texto)  # Mostramos el texto
print(resumen)  # Mostramos el resumen
print(len(texto))  # Longitud
#
# Verás esto
# Verás P-n-Pyt y la longitud 6.
#
# Por qué funciona
# Los strings son secuencias y permiten slicing.
#
# Lo típico que sale mal
# - Pedir un índice fuera de rango.
# - Confundir slicing con un solo índice.
""",
            ),
            (
                "Limpiar con strip",
                """# Aprende esto
# Aprenderás a quitar espacios al inicio y fin.
# Verás cómo guardar el resultado limpio.
# Evitarás comparar con espacios ocultos.
#
# Haz esto
texto = "  Hola Mundo  "  # Texto con espacios
texto_limpio = texto.strip()  # Quitamos espacios
texto_mayus = texto_limpio.upper()  # Mayúsculas
resumen = texto_limpio + " | " + texto_mayus  # Resumen
print(texto)  # Original
print(texto_limpio)  # Limpio
print(resumen)  # Resumen
print(texto == texto_limpio)  # Comparación
#
# Verás esto
# Verás el texto limpio y False en la comparación.
#
# Por qué funciona
# strip() devuelve un nuevo string sin espacios.
#
# Lo típico que sale mal
# - Esperar que el original cambie.
# - Olvidar guardar el resultado.
""",
            ),
            (
                "Buscar y reemplazar",
                """# Aprende esto
# Aprenderás a buscar texto con in.
# Verás cómo reemplazar caracteres.
# Limpiarás un valor para usarlo como número.
#
# Haz esto
frase = "Precio: $100"  # Frase con símbolo
hay_signo = "$" in frase  # Verificamos presencia
frase_limpia = frase.replace("$", "")  # Quitamos símbolo
monto = frase_limpia.split(": ")[1]  # Extraemos monto
mensaje = "Monto: " + monto  # Mensaje final
print(hay_signo)  # Mostramos booleano
print(frase_limpia)  # Mostramos limpio
print(mensaje)  # Mostramos mensaje
#
# Verás esto
# Verás True, la frase sin $ y el monto extraído.
#
# Por qué funciona
# replace() y split() devuelven nuevos strings.
#
# Lo típico que sale mal
# - No verificar separador antes de split.
# - Reemplazar más texto del necesario.
""",
            ),
            (
                "f-strings básicos",
                """# Aprende esto
# Aprenderás a usar f-strings para insertar variables.
# Verás cómo formatear un número con decimales.
# Harás el texto más legible.
#
# Haz esto
producto = "Café"  # Producto
precio = 3.5  # Precio base
cantidad = 2  # Unidades
subtotal = precio * cantidad  # Subtotal
mensaje = f"Producto: {producto} | Subtotal: {subtotal:.2f}"  # f-string
print(mensaje)  # Mostramos el mensaje
print(type(mensaje))  # Tipo
print(subtotal)  # Subtotal numérico
#
# Verás esto
# Verás el subtotal con dos decimales.
#
# Por qué funciona
# Las f-strings evalúan expresiones dentro de {}.
#
# Lo típico que sale mal
# - Olvidar la f en la cadena.
# - No controlar decimales.
""",
            ),
            (
                "Saltos de línea",
                """# Aprende esto
# Aprenderás a usar \n para saltos de línea.
# Verás cómo unir líneas en un mismo texto.
# Mantendrás claridad en mensajes largos.
#
# Haz esto
linea1 = "Primera línea"  # Línea 1
linea2 = "Segunda línea"  # Línea 2
texto = linea1 + "\n" + linea2  # Unimos con salto
titulo = "\"Reporte\""  # Texto con comillas
reporte = titulo + "\n" + texto  # Reporte final
print(reporte)  # Mostramos reporte
print(len(reporte))  # Longitud
print("\n" in reporte)  # Verificamos salto
#
# Verás esto
# Verás un texto con saltos y True en la verificación.
#
# Por qué funciona
# \n crea un salto de línea dentro del string.
#
# Lo típico que sale mal
# - Olvidar escapar comillas.
# - Contar mal caracteres por saltos.
""",
            ),
            (
                "Formateo con separador de miles",
                """# Aprende esto
# Aprenderás a formatear números grandes.
# Verás separadores de miles y decimales.
# Harás reportes más legibles.
#
# Haz esto
cliente = "Ana"  # Nombre
saldo = 1520.5  # Saldo base
saldo_formateado = f"{saldo:,.2f}"  # Formato con miles
mensaje = f"Cliente: {cliente} | Saldo: {saldo_formateado}"  # Mensaje
longitud = len(mensaje)  # Longitud del mensaje
print(mensaje)  # Mostramos mensaje
print(type(saldo_formateado))  # Tipo
print(saldo_formateado)  # Mostramos saldo
print(longitud)  # Mostramos longitud
#
# Verás esto
# Verás el saldo con separador de miles y dos decimales.
#
# Por qué funciona
# El especificador :,.2f agrega coma de miles y decimales.
#
# Lo típico que sale mal
# - Usar formato incorrecto y perder decimales.
# - Mezclar formatos con strings normales.
""",
            ),
            (
                "Normalizar texto para comparación",
                """# Aprende esto
# Aprenderás a normalizar texto para comparar.
# Verás cómo usar lower() y strip().
# Evitarás falsos negativos en comparaciones.
#
# Haz esto
entrada = "  Sí  "  # Texto con espacios y mayúsculas
normalizado = entrada.strip().lower()  # Normalizamos
es_si = normalizado == "sí"  # Comparamos
mensaje = "Respuesta válida" if es_si else "Respuesta inválida"  # Mensaje
longitud = len(normalizado)  # Longitud del texto
print(normalizado)  # Mostramos normalizado
print(es_si)  # Mostramos booleano
print(mensaje)  # Mostramos mensaje
print(longitud)  # Mostramos longitud
#
# Verás esto
# Verás "sí", True y el mensaje de respuesta válida.
#
# Por qué funciona
# strip() elimina espacios y lower() uniforma el caso.
#
# Lo típico que sale mal
# - Comparar sin normalizar.
# - Olvidar que los acentos importan.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Concatena tu nombre y apellido con un espacio entre ellos.",
                "hints": ["Usa + y un espacio"],
                "solution": "nombre = 'Ana'\napellido = 'López'\nprint(nombre + ' ' + apellido)",
            },
            {
                "question": "Obtén el primer y último carácter de la palabra 'Python'.",
                "hints": ["Usa índices 0 y -1"],
                "solution": "texto = 'Python'\nprint(texto[0])\nprint(texto[-1])",
            },
            {
                "question": "Limpia los espacios de un texto usando strip().",
                "hints": ["texto.strip()"],
                "solution": "texto = '  Hola  '\nprint(texto.strip())",
            },
            {
                "question": "Reemplaza el símbolo '$' en 'Precio: $50'.",
                "hints": ["Usa replace"],
                "solution": "frase = 'Precio: $50'\nprint(frase.replace('$', ''))",
            },
            {
                "question": "Crea un f-string que muestre un precio con dos decimales.",
                "hints": ["Usa {precio:.2f}"],
                "solution": "precio = 3.5\nmensaje = f'Precio: {precio:.2f}'\nprint(mensaje)",
            },
            {
                "question": "Normaliza la respuesta '  SI  ' para compararla con 'si'.",
                "hints": ["Usa strip().lower()"],
                "solution": "respuesta = '  SI  '\nnormalizada = respuesta.strip().lower()\nprint(normalizada == 'si')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
