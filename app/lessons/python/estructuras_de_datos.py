from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class EstructurasDatosLesson(Lesson):
    TITLE = "Estructuras de datos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["listas", "tuplas", "diccionarios", "sets"]

    def summary(self) -> str:
        return (
            "Aprende a elegir entre listas, tuplas, diccionarios y sets. Entiende qué guardar, "
            "cómo acceder y por qué cada estructura existe."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: elegir bien evita código confuso
En Python, las estructuras de datos te permiten organizar información: una lista guarda elementos en orden, una tupla guarda
valores fijos, un diccionario relaciona claves con valores y un set guarda elementos únicos sin orden. Elegir la estructura
correcta no es un detalle menor: define cómo accedes a los datos, cómo los modificas y qué tan fácil es entender tu código.

Este tutorial parte desde cero: verás qué problema resuelve cada estructura, cómo se crea, cómo se accede a sus datos y cómo
elegir una u otra según el caso. También aprenderás sobre mutabilidad, duplicados y rendimiento básico sin entrar en temas
avanzados. La meta es que no adivines: que sepas qué usar y por qué.

### Buenas prácticas (CalloutBox: best_practice)
Si necesitas orden, usa listas o tuplas. Si necesitas claves con significado, usa diccionarios. Si necesitas unicidad, usa
sets. Esa regla simple te ayuda a elegir el 80% del tiempo.

## Paso 1: listas para colecciones ordenadas y mutables
Una lista es una colección ordenada. Puedes acceder por índice y modificar elementos. Es la estructura más común porque es
flexible: puedes agregar, quitar y reorganizar. Si tienes una lista de tareas o productos, una lista es la elección natural.

Aprenderás a crear listas, a usar índices y a modificar elementos sin perder el orden. También entenderás qué significa que
sea mutable: los cambios ocurren en el mismo objeto.

## Paso 2: tuplas para grupos fijos
Una tupla es similar a una lista, pero inmutable. Se usa cuando los datos forman un grupo fijo que no quieres modificar.
Por ejemplo, coordenadas `(x, y)` o un registro con valores que no deben cambiar en el flujo.

Al ser inmutable, una tupla es más segura para representar datos que no deberían alterarse. También comunica intención: si
ves una tupla, asumes que sus valores son estables.

## Paso 3: diccionarios para relacionar claves y valores
Un diccionario permite mapear una clave a un valor. Esta es la estructura más útil cuando cada dato tiene un nombre o
identificador. En vez de recordar que un elemento está en el índice 2, puedes escribir `cliente["nombre"]`.

Aprenderás a crear diccionarios, acceder por clave y actualizar valores. Este patrón es esencial en proyectos reales porque
te permite trabajar con datos “etiquetados”.

### Nota (CalloutBox: note)
Una clave de diccionario debe ser inmutable (por ejemplo, un string o una tupla). Las listas no pueden ser claves.

## Paso 4: sets para unicidad y operaciones rápidas
Un set guarda elementos únicos sin orden. Es ideal para eliminar duplicados o comprobar pertenencia de forma eficiente. Si
necesitas saber si algo “está o no está”, un set suele ser la mejor opción.

Los sets también permiten operaciones como unión e intersección, que son útiles para comparar grupos.

## Paso 5: escoger la estructura adecuada
No todas las estructuras sirven para lo mismo. Si el orden importa, usa lista o tupla. Si necesitas claves con significado,
usa diccionario. Si solo quieres unicidad, usa set. En la práctica, muchas soluciones combinan estas estructuras. Lo
importante es que cada elección tenga un motivo claro.

## Paso 6: mutabilidad y alias en estructuras
Listas y diccionarios son mutables. Si compartes la misma estructura entre variables, los cambios se reflejan en todas. Las
estructuras inmutables como tuplas ayudan a prevenir modificaciones accidentales. Esta idea también es clave al pasar datos
entre funciones.

### Advertencia (CalloutBox: warning)
Cuando duplicas una lista o un diccionario con `copy()`, solo copias el primer nivel. Si hay estructuras internas, siguen
compartidas.

## Más allá (nivel pro)
Elegir bien una estructura es un acto de diseño. Un diccionario puede hacer que tu código sea autoexplicativo; un set puede
mejorar rendimiento sin cambiar el resultado. Cuando domines las opciones básicas, podrás construir modelos de datos claros
para tu aplicación.

### Consejos pro
- Usa tuplas para representar datos que no deben cambiar, como coordenadas o fechas fijas.
- En diccionarios, define claves consistentes y documentadas; evita claves mágicas.
- Convierte listas a sets para eliminar duplicados y luego vuelve a lista si necesitas orden.
- Prefiere listas de diccionarios cuando tengas registros con múltiples campos.
- Cuando compartas estructuras mutables entre funciones, documenta si se modifican en sitio.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Usar lista cuando se necesita diccionario",
                "Si accedes por nombres, un diccionario es más claro que recordar índices.",
            ),
            (
                "Olvidar que las listas son mutables",
                "Modificar una lista compartida afecta a todas las referencias. Haz copias si necesitas aislamiento.",
            ),
            (
                "Intentar cambiar una tupla",
                "Las tuplas son inmutables. Si necesitas cambiar valores, usa una lista.",
            ),
            (
                "Usar listas como claves en dict",
                "Las listas no son hashables. Convierte a tupla si necesitas usarla como clave.",
            ),
            (
                "Asumir orden en un set",
                "Los sets no garantizan orden. Si lo necesitas, usa una lista y ordena.",
            ),
            (
                "Duplicar listas con *",
                "`[[0]] * 3` crea referencias repetidas. Modificar una afecta a todas.",
            ),
            (
                "No validar claves inexistentes",
                "Acceder a una clave que no existe genera error. Usa `.get()` si no estás seguro.",
            ),
            (
                "Confundir append con extend",
                "append agrega un elemento; extend agrega varios. Usarlos mal produce listas anidadas.",
            ),
            (
                "No entender la diferencia entre lista y tupla",
                "Las tuplas son para datos fijos; las listas para datos que cambian.",
            ),
            (
                "Modificar dict mientras iteras",
                "Cambiar un diccionario durante un bucle puede causar errores. Crea una copia si necesitas hacerlo.",
            ),
            (
                "Perder unicidad al usar listas",
                "Si el dato no debe repetirse, usa set para evitar duplicados.",
            ),
            (
                "No copiar estructuras anidadas",
                "`copy()` no duplica estructuras internas. Cambios profundos pueden propagarse sin querer.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear y usar listas",
                """# Aprende esto
# Aprenderás a crear listas y acceder por índice.
# Verás cómo modificar un elemento.
# Entenderás que la lista mantiene el orden.
#
# Haz esto
tareas = ["comprar", "leer", "estudiar"]  # Lista inicial
primera = tareas[0]  # Tomamos el primer elemento
print(primera)  # Mostramos el primer elemento
tareas[1] = "descansar"  # Modificamos el segundo elemento
print(tareas)  # Mostramos la lista actualizada
cantidad = len(tareas)  # Contamos elementos
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás el primer elemento y la lista modificada.
#
# Por qué funciona
# Las listas guardan orden y permiten acceso por índice.
#
# Lo típico que sale mal
# - Usar un índice fuera del rango.
# - Olvidar que el índice empieza en 0.
""",
            ),
            (
                "Tuplas para datos fijos",
                """# Aprende esto
# Aprenderás a usar tuplas para valores fijos.
# Verás cómo acceder a sus posiciones.
# Entenderás que no se pueden modificar.
#
# Haz esto
coordenada = (10, 20)  # Tupla con dos valores
x = coordenada[0]  # Extraemos x
y = coordenada[1]  # Extraemos y
print(x)  # Mostramos x
print(y)  # Mostramos y
etiqueta = f"({x}, {y})"  # Construimos una etiqueta
print(etiqueta)  # Mostramos la etiqueta
#
# Verás esto
# Verás 10, 20 y "(10, 20)".
#
# Por qué funciona
# Las tuplas son ordenadas e inmutables.
#
# Lo típico que sale mal
# - Intentar cambiar una tupla.
# - Tratarla como lista mutable.
""",
            ),
            (
                "Diccionarios con claves",
                """# Aprende esto
# Aprenderás a crear diccionarios con claves.
# Verás cómo acceder y actualizar valores.
# Entenderás que las claves dan significado.
#
# Haz esto
cliente = {"nombre": "Ana", "edad": 30}  # Diccionario base
nombre = cliente["nombre"]  # Accedemos por clave
print(nombre)  # Mostramos el nombre
cliente["edad"] = 31  # Actualizamos la edad
print(cliente)  # Mostramos el diccionario
existe = "email" in cliente  # Verificamos una clave
print(existe)  # Mostramos el resultado
#
# Verás esto
# Verás el nombre, el diccionario actualizado y False.
#
# Por qué funciona
# Las claves permiten acceso directo a cada valor.
#
# Lo típico que sale mal
# - Usar claves inconsistentes.
# - Acceder a una clave que no existe.
""",
            ),
            (
                "Diccionarios con get",
                """# Aprende esto
# Aprenderás a usar get para evitar errores.
# Verás cómo definir un valor por defecto.
# Entenderás cuándo usarlo.
#
# Haz esto
producto = {"nombre": "Pan", "precio": 2.5}  # Diccionario base
categoria = producto.get("categoria", "sin categoría")  # Valor por defecto
print(categoria)  # Mostramos la categoría
precio = producto.get("precio", 0)  # Obtenemos precio
print(precio)  # Mostramos el precio
mensaje = f"{producto['nombre']} cuesta {precio}"  # Mensaje final
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "sin categoría", 2.5 y el mensaje final.
#
# Por qué funciona
# get devuelve un valor por defecto si falta la clave.
#
# Lo típico que sale mal
# - Usar [] cuando no estás seguro de la clave.
# - Olvidar definir el valor por defecto.
""",
            ),
            (
                "Sets para unicidad",
                """# Aprende esto
# Aprenderás a crear sets para eliminar duplicados.
# Verás cómo comprobar pertenencia.
# Entenderás que no hay orden.
#
# Haz esto
etiquetas = {"python", "datos", "python"}  # Set con duplicados
print(etiquetas)  # Mostramos el set sin duplicados
existe = "python" in etiquetas  # Comprobamos pertenencia
print(existe)  # Mostramos el resultado
etiquetas.add("bases")  # Agregamos una etiqueta
print(etiquetas)  # Mostramos el set actualizado
#
# Verás esto
# Verás un set sin duplicados y el resultado True.
#
# Por qué funciona
# Los sets guardan elementos únicos.
#
# Lo típico que sale mal
# - Esperar que mantenga el orden de inserción.
# - Usar listas dentro de un set.
""",
            ),
            (
                "Operaciones con sets",
                """# Aprende esto
# Aprenderás a hacer unión e intersección.
# Verás cómo comparar grupos.
# Entenderás la utilidad práctica.
#
# Haz esto
grupo_a = {"ana", "luis", "maria"}  # Primer grupo
grupo_b = {"maria", "pablo"}  # Segundo grupo
union = grupo_a | grupo_b  # Unión de grupos
interseccion = grupo_a & grupo_b  # Intersección
print(union)  # Mostramos la unión
print(interseccion)  # Mostramos la intersección
#
# Verás esto
# Verás todos los nombres y luego solo los comunes.
#
# Por qué funciona
# | y & aplican operaciones de conjunto.
#
# Lo típico que sale mal
# - Intentar usar + con sets.
# - Olvidar que el orden no existe.
""",
            ),
            (
                "Combinar estructuras",
                """# Aprende esto
# Aprenderás a usar listas de diccionarios.
# Verás cómo acceder a datos por clave.
# Entenderás la utilidad en registros.
#
# Haz esto
usuarios = [
    {"nombre": "Ana", "rol": "admin"},  # Primer usuario
    {"nombre": "Luis", "rol": "viewer"},  # Segundo usuario
]  # Lista de diccionarios
primer_rol = usuarios[0]["rol"]  # Accedemos al rol del primero
print(primer_rol)  # Mostramos el rol
usuarios[1]["rol"] = "editor"  # Actualizamos rol
print(usuarios)  # Mostramos la lista actualizada
#
# Verás esto
# Verás "admin" y luego la lista con el rol actualizado.
#
# Por qué funciona
# Combinamos orden de lista con claves de diccionario.
#
# Lo típico que sale mal
# - Olvidar el índice correcto.
# - Cambiar la estructura y romper accesos.
""",
            ),
            (
                "Copias superficiales",
                """# Aprende esto
# Aprenderás qué es una copia superficial.
# Verás cómo afecta a estructuras anidadas.
# Entenderás cuándo necesitas otra estrategia.
#
# Haz esto
original = [[1, 2], [3, 4]]  # Lista anidada
copia = original.copy()  # Copia superficial
copia[0].append(99)  # Modificamos la lista interna
print(original)  # Mostramos original
print(copia)  # Mostramos copia
#
# Verás esto
# Verás que ambas listas cambian.
#
# Por qué funciona
# copy() no duplica las listas internas.
#
# Lo típico que sale mal
# - Creer que copy() es profundo.
# - No planear cómo aislar cambios.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una lista de 3 colores y muestra el segundo.",
                "hints": ["Usa índice 1 para el segundo elemento."],
                "solution": """colores = ["rojo", "verde", "azul"]
print(colores[1])""",
            },
            {
                "question": "Crea una tupla con (ciudad, país) y muestra ambos valores.",
                "hints": ["Accede con índices 0 y 1."],
                "solution": """ubicacion = ("Lima", "Perú")
print(ubicacion[0])
print(ubicacion[1])""",
            },
            {
                "question": "Crea un diccionario con `nombre` y `edad` y actualiza la edad.",
                "hints": ["Asigna un nuevo valor a la clave `edad`."],
                "solution": """persona = {"nombre": "Ana", "edad": 30}
persona["edad"] = 31
print(persona)""",
            },
            {
                "question": "Usa un set para eliminar duplicados de una lista de números.",
                "hints": ["Convierte la lista a set.", "Luego imprime el set."],
                "solution": """numeros = [1, 2, 2, 3]
unicos = set(numeros)
print(unicos)""",
            },
            {
                "question": "Crea una lista de diccionarios con dos productos y muestra el nombre del primero.",
                "hints": ["Accede con [0][""nombre""]"],
                "solution": """productos = [
    {"nombre": "Pan", "precio": 2},
    {"nombre": "Leche", "precio": 3},
]
print(productos[0]["nombre"])""",
            },
            {
                "question": "Crea un diccionario y usa get para una clave que no existe.",
                "hints": ["Pasa un valor por defecto a get."],
                "solution": """datos = {"a": 1}
valor = datos.get("b", 0)
print(valor)""",
            },
        ]
