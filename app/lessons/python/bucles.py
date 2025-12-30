from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class BuclesLesson(Lesson):
    TITLE = "Bucles"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["for", "while", "iteración", "break", "continue"]

    def summary(self) -> str:
        return (
            "Aprende a repetir tareas con for y while, controlar bucles con break/continue "
            "y elegir la estructura correcta para cada caso."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: repetir sin repetir código
Los bucles permiten ejecutar una misma tarea varias veces: recorrer listas, sumar valores o esperar una condición.
Aprenderás cuándo usar `for` y cuándo usar `while`, además de cómo controlar el flujo con `break` y `continue`.

## Paso 1: Bucle for sobre listas
`for` recorre cada elemento de una secuencia.

**Aprende esto**
- Aprenderás a iterar sobre una lista con for.
- Verás cómo acumular resultados durante la iteración.

**Haz esto**
```
ventas = [100, 200, 150]  # Lista de ventas
suma = 0  # Acumulador inicial
for venta in ventas:  # Recorremos cada venta
    suma = suma + venta  # Sumamos al acumulador
promedio = suma / len(ventas)  # Calculamos promedio
print(promedio)  # Mostramos el promedio
```

**Verás esto**
Verás un promedio numérico (por ejemplo 150.0).

**Por qué funciona**
El bucle recorre cada venta y la suma se acumula paso a paso.

**Lo típico que sale mal**
- Olvidar inicializar el acumulador.
- Usar len dentro del bucle innecesariamente.

## Paso 2: range para contar
`range` genera secuencias de números y se usa con for.

**Aprende esto**
- Aprenderás a crear rangos controlados.
- Verás cómo usar un contador en un bucle.

**Haz esto**
```
conteo = 0  # Inicializamos contador
for numero in range(1, 4):  # Generamos 1, 2, 3
    conteo = conteo + numero  # Sumamos cada número
print(conteo)  # Mostramos el total
```

**Verás esto**
Verás `6` como resultado.

**Por qué funciona**
`range(1, 4)` produce 1, 2 y 3; el bucle los suma.

**Lo típico que sale mal**
- Pensar que el límite superior se incluye.
- Usar range sin definir un inicio claro.

## Paso 3: Bucle while con condición
`while` repite mientras una condición sea verdadera.

**Aprende esto**
- Aprenderás a controlar un bucle con una condición.
- Verás cómo evitar bucles infinitos.

**Haz esto**
```
contador = 0  # Inicializamos contador
limite = 3  # Definimos un límite
while contador < limite:  # Condición del bucle
    contador = contador + 1  # Incrementamos
print(contador)  # Mostramos el contador final
```

**Verás esto**
Verás `3`.

**Por qué funciona**
La condición se evalúa en cada iteración; al llegar al límite, el bucle termina.

**Lo típico que sale mal**
- Olvidar incrementar el contador y crear un bucle infinito.
- Usar condiciones que nunca se vuelven falsas.

## Paso 4: break y continue
`break` corta el bucle, `continue` salta a la siguiente iteración.

**Aprende esto**
- Aprenderás a detener un bucle cuando encuentras lo que buscas.
- Verás cómo saltar elementos específicos.

**Haz esto**
```
numeros = [1, 2, 3, 4, 5]  # Lista base
for numero in numeros:  # Recorremos la lista
    if numero == 3:  # Condición para saltar
        continue  # Saltamos el 3
    if numero == 5:  # Condición para detener
        break  # Terminamos el bucle
    print(numero)  # Mostramos el número
```

**Verás esto**
Verás `1`, `2` y `4` en líneas separadas.

**Por qué funciona**
`continue` salta el 3 y `break` detiene el bucle al llegar al 5.

**Lo típico que sale mal**
- Usar break sin un motivo claro y perder datos.
- Olvidar que continue salta el resto del bloque.

## Paso 5: Enumerar con índice
`enumerate` te da el índice y el valor al mismo tiempo.

**Aprende esto**
- Aprenderás a recorrer con índice sin manejarlo manualmente.
- Verás cómo construir mensajes con posición.

**Haz esto**
```
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
for indice, fruta in enumerate(frutas, start=1):  # Índice desde 1
    mensaje = str(indice) + ". " + fruta  # Creamos el texto
    print(mensaje)  # Mostramos el mensaje
```

**Verás esto**
Verás una lista numerada: 1. manzana, 2. pera, 3. uva.

**Por qué funciona**
`enumerate` produce pares (índice, valor) y start=1 ajusta el inicio.

**Lo típico que sale mal**
- Olvidar start y comenzar en 0 cuando no se quiere.
- Usar índices manuales y desalinearlos.

## Más allá (nivel pro)
Puedes combinar bucles con condiciones para hacer filtros claros.

**Aprende esto**
- Aprenderás a filtrar elementos durante la iteración.
- Verás cómo construir una lista nueva con un bucle simple.

**Haz esto**
```
ventas = [50, 120, 80, 200]  # Lista de ventas
altas = []  # Lista para ventas altas
for venta in ventas:  # Recorremos ventas
    if venta >= 100:  # Condición de filtro
        altas.append(venta)  # Guardamos la venta alta
print(altas)  # Mostramos la lista filtrada
```

**Verás esto**
Verás `[120, 200]`.

**Por qué funciona**
El bucle revisa cada venta y agrega solo las que cumplen la condición.

**Lo típico que sale mal**
- Olvidar inicializar la lista antes del bucle.
- Usar append fuera del if y agregar todo.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            ("Bucle infinito", "No modificar la condición en while causa bucles infinitos."),
            ("Olvidar el acumulador", "Debe inicializarse antes de sumar en un for."),
            ("Límites de range", "El límite superior no se incluye."),
            ("Usar break demasiado pronto", "Puedes cortar el bucle antes de procesar todo."),
            ("Olvidar continue", "No usar continue cuando se necesita saltar elementos."),
            ("Modificar lista mientras se itera", "Cambiar la lista dentro del bucle puede crear errores."),
            ("No usar enumerate", "Incrementar índices manualmente puede desalinear datos."),
            ("Condiciones mal definidas", "Una condición siempre True bloquea el bucle."),
            ("Acumuladores fuera del bucle", "Si se reinician en cada iteración, el resultado es incorrecto."),
            ("No usar listas nuevas", "Si filtras, guarda resultados en una lista separada."),
            ("Confundir for con while", "Usa for para secuencias conocidas y while para condiciones dinámicas."),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Suma con for",
                """# Aprende esto
# Aprenderás a recorrer una lista y acumular resultados.
# Verás cómo calcular un promedio simple.
#
# Haz esto
ventas = [100, 200, 150]  # Lista de ventas
suma = 0  # Acumulador
for venta in ventas:  # Recorremos cada venta
    suma = suma + venta  # Sumamos
promedio = suma / len(ventas)  # Calculamos promedio
print(promedio)  # Mostramos el resultado
#
# Verás esto
# Verás 150.0 como promedio.
#
# Por qué funciona
# El acumulador suma cada valor de la lista.
#
# Lo típico que sale mal
# - No inicializar suma.
# - Dividir dentro del bucle.
""",
            ),
            (
                "range con contador",
                """# Aprende esto
# Aprenderás a usar range para contar.
# Verás cómo sumar números consecutivos.
#
# Haz esto
conteo = 0  # Contador inicial
for numero in range(1, 4):  # Generamos 1 a 3
    conteo = conteo + numero  # Sumamos
print(conteo)  # Mostramos el total
#
# Verás esto
# Verás 6.
#
# Por qué funciona
# range excluye el límite superior y produce 1, 2 y 3.
#
# Lo típico que sale mal
# - Esperar incluir el 4.
# - Usar un inicio incorrecto.
""",
            ),
            (
                "while controlado",
                """# Aprende esto
# Aprenderás a usar while con una condición.
# Verás cómo evitar un bucle infinito.
#
# Haz esto
contador = 0  # Inicializamos
limite = 3  # Límite final
while contador < limite:  # Condición del bucle
    contador = contador + 1  # Incrementamos
print(contador)  # Mostramos el contador final
#
# Verás esto
# Verás 3.
#
# Por qué funciona
# La condición deja de cumplirse cuando contador llega a 3.
#
# Lo típico que sale mal
# - No actualizar el contador.
# - Usar una condición que nunca cambia.
""",
            ),
            (
                "break y continue",
                """# Aprende esto
# Aprenderás a saltar o cortar un bucle.
# Verás cómo controlar el flujo.
#
# Haz esto
numeros = [1, 2, 3, 4, 5]  # Lista base
for numero in numeros:  # Recorremos
    if numero == 3:  # Si es 3
        continue  # Saltamos
    if numero == 5:  # Si es 5
        break  # Cortamos
    print(numero)  # Mostramos el número
#
# Verás esto
# Verás 1, 2 y 4.
#
# Por qué funciona
# continue salta el 3 y break detiene en 5.
#
# Lo típico que sale mal
# - Usar break sin razón.
# - Olvidar que continue omite el resto del bloque.
""",
            ),
            (
                "Enumerate con índice",
                """# Aprende esto
# Aprenderás a usar enumerate para índices.
# Verás cómo crear mensajes numerados.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista base
for indice, fruta in enumerate(frutas, start=1):  # Índice desde 1
    mensaje = str(indice) + ". " + fruta  # Construimos el texto
    print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás una lista numerada.
#
# Por qué funciona
# enumerate devuelve pares (índice, valor).
#
# Lo típico que sale mal
# - Olvidar start=1.
# - Usar índices manuales innecesarios.
""",
            ),
            (
                "Filtrar con for",
                """# Aprende esto
# Aprenderás a filtrar elementos durante la iteración.
# Verás cómo construir una lista nueva.
#
# Haz esto
ventas = [50, 120, 80, 200]  # Lista de ventas
altas = []  # Lista filtrada
for venta in ventas:  # Recorremos ventas
    if venta >= 100:  # Condición
        altas.append(venta)  # Agregamos si cumple
print(altas)  # Mostramos la lista filtrada
#
# Verás esto
# Verás [120, 200].
#
# Por qué funciona
# Solo se agregan las ventas que cumplen la condición.
#
# Lo típico que sale mal
# - No inicializar la lista.
# - Agregar fuera del if.
""",
            ),
            (
                "Acumulador con condición",
                """# Aprende esto
# Aprenderás a sumar solo valores que cumplen una condición.
# Verás cómo controlar el acumulador.
#
# Haz esto
numeros = [2, 5, 8, 11]  # Lista de números
suma = 0  # Acumulador
for numero in numeros:  # Recorremos
    if numero % 2 == 0:  # Solo pares
        suma = suma + numero  # Sumamos pares
print(suma)  # Mostramos la suma
#
# Verás esto
# Verás 10.
#
# Por qué funciona
# Se suman solo los pares encontrados en el bucle.
#
# Lo típico que sale mal
# - Olvidar el módulo.
# - No inicializar suma.
""",
            ),
            (
                "Bucle con contador manual",
                """# Aprende esto
# Aprenderás a manejar un contador manual.
# Verás cómo avanzar por una lista con while.
#
# Haz esto
nombres = ["Ana", "Luis", "Marta"]  # Lista base
indice = 0  # Índice inicial
while indice < len(nombres):  # Condición con tamaño
    print(nombres[indice])  # Mostramos el nombre
    indice = indice + 1  # Avanzamos el índice
#
# Verás esto
# Verás los tres nombres en orden.
#
# Por qué funciona
# El índice avanza y el bucle termina al llegar al tamaño.
#
# Lo típico que sale mal
# - No incrementar el índice.
# - Usar un límite incorrecto.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Suma todos los números de una lista usando for.",
                "hints": ["Usa un acumulador"],
                "solution": "numeros = [1, 2, 3]\nsuma = 0\nfor n in numeros:\n    suma += n\nprint(suma)",
            },
            {
                "question": "Imprime los números del 1 al 5 con range.",
                "hints": ["Usa range(1, 6)"],
                "solution": "for n in range(1, 6):\n    print(n)",
            },
            {
                "question": "Usa while para contar hasta 3.",
                "hints": ["Incrementa un contador"],
                "solution": "contador = 0\nwhile contador < 3:\n    contador += 1\nprint(contador)",
            },
            {
                "question": "Salta el número 3 en una lista usando continue.",
                "hints": ["Usa if numero == 3"],
                "solution": "numeros = [1, 2, 3, 4]\nfor n in numeros:\n    if n == 3:\n        continue\n    print(n)",
            },
            {
                "question": "Crea una lista con números pares usando un for y un if.",
                "hints": ["Usa append"],
                "solution": "numeros = [1, 2, 3, 4]\npares = []\nfor n in numeros:\n    if n % 2 == 0:\n        pares.append(n)\nprint(pares)",
            },
            {
                "question": "Enumera una lista de frutas con índices desde 1.",
                "hints": ["Usa enumerate"],
                "solution": "frutas = ['manzana', 'pera']\nfor i, fruta in enumerate(frutas, start=1):\n    print(i, fruta)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
