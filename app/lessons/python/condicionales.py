from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class CondicionalesLesson(Lesson):
    TITLE = "Condicionales"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["condicionales", "if", "elif", "else", "booleanos"]

    def summary(self) -> str:
        return (
            "Aprende a tomar decisiones con if/elif/else, escribir condiciones legibles y evitar "
            "errores típicos de comparación e indentación."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: decidir en función de datos
Los condicionales permiten que tu programa elija rutas distintas según un valor. En Python, la sintaxis es clara pero
estricta: necesitas `if`, `elif` y `else`, y la indentación es obligatoria.

En esta lección aprenderás la sintaxis paso a paso con micro-snippets correctos e incorrectos, para que veas el error en el
momento exacto en que suele aparecer.

## Paso 1: sintaxis básica de if
Un `if` evalúa una condición booleana y ejecuta un bloque indentado.

**Así se escribe**
```py
edad = 20
if edad >= 18:
    print("Mayor de edad")
```

**Error típico (❌)**
```py
edad = 20
if edad >= 18
    print("Mayor de edad")
```

**Qué significa el error**
`SyntaxError` aparece porque falta el `:` al final de la línea del `if`.

**Cómo se arregla**
Agrega `:` y mantén la indentación del bloque.

### Así se escribe: decidir con input (recuerda que devuelve str)
```py
respuesta = input("¿Eres mayor de edad? (s/n) ")
if respuesta == "s":
    print("Puedes entrar")
```

### Error típico: comparar input con número
```py
edad = input("Edad: ")
if edad >= 18:
    print("Mayor de edad")
```

```py
TypeError: '>=' not supported between instances of 'str' and 'int'
```

Explicación breve: `input()` devuelve `str`. Convierte con `int(edad)` antes de comparar.

## Paso 2: elif y else para más casos
`elif` permite evaluar otra condición si la anterior no se cumplió, y `else` cubre el caso final.

**Así se escribe**
```py
nota = 7
if nota >= 9:
    resultado = "Excelente"
elif nota >= 5:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"
```

**Error típico (❌)**
```py
nota = 7
if nota >= 9:
    resultado = "Excelente"
else nota >= 5:
    resultado = "Aprobado"
```

**Qué significa el error**
`SyntaxError` indica que `else` no lleva condición. Debe ser `elif` cuando hay condición.

**Cómo se arregla**
Cambia `else` por `elif` si quieres evaluar otra condición.

## Paso 3: indentación obligatoria
La indentación define el bloque que pertenece al `if`. Si no indentas, Python no sabe qué ejecutar.

**Así se escribe**
```py
activo = True
if activo:
    print("Activo")
```

**Error típico (❌)**
```py
activo = True
if activo:
print("Activo")
```

**Qué significa el error**
`IndentationError` indica que el bloque no está indentado correctamente.

**Cómo se arregla**
Indenta el bloque con cuatro espacios.

## Paso 4: comparación correcta
Para comparar valores usa `==`. `=` es asignación y no funciona dentro de una condición.

**Así se escribe**
```py
color = "rojo"
if color == "rojo":
    print("Semáforo en rojo")
```

**Error típico (❌)**
```py
color = "rojo"
if color = "rojo":
    print("Semáforo en rojo")
```

**Qué significa el error**
`SyntaxError` aparece porque `=` no es válido en una condición. Solo `==` compara.

**Cómo se arregla**
Usa `==` para comparar y reserva `=` para asignar.

## Paso 5: condiciones legibles
Condiciones claras se leen como frases: “si hay saldo”, “si está activo”. Evita comparaciones innecesarias.

**Así se escribe**
```py
saldo = 50
if saldo:
    print("Hay saldo")
```

**Error típico (❌)**
```py
saldo = 0
if saldo == True:
    print("Hay saldo")
```

**Qué significa el error**
No hay error de sintaxis, pero la comparación es confusa y puede fallar con valores no booleanos.

**Cómo se arregla**
Deja que Python evalúe la verdad del valor con `if saldo:`.

## Paso 6: resumen para decidir sin errores
Recuerda: `if` requiere `:`, la indentación es parte de la sintaxis y la comparación se hace con `==`. Con eso evitas la
mayoría de errores al empezar.



## Operaciones y métodos más útiles
### Strings (`str`)
1) `upper()` ⭐  
Qué hace: convierte a mayúsculas.  
Así se escribe:
```py
texto = "hola"
resultado = texto.upper()
```
Error típico:
```py
resultado = texto.upper
```
Verás esto: `"HOLA"`.  
Por qué funciona: `upper()` crea un texto nuevo con mayúsculas.  
Lo típico que sale mal: olvidar paréntesis; creer que cambia el string original.

2) `lower()` ⭐  
Qué hace: convierte a minúsculas.  
Así se escribe:
```py
texto = "HoLa"
resultado = texto.lower()
```
Error típico:
```py
resultado = texto.lower
```
Verás esto: `"hola"`.  
Por qué funciona: normaliza el texto para comparar.  
Lo típico que sale mal: no normalizar ambos lados; asumir mutación in-place.

3) `strip()` ⭐  
Qué hace: quita espacios al inicio y final.  
Así se escribe:
```py
texto = "  hola  "
resultado = texto.strip()
```
Error típico:
```py
resultado = texto.strip
```
Verás esto: `"hola"`.  
Por qué funciona: recorta whitespace en bordes.  
Lo típico que sale mal: esperar que quite espacios internos; no guardar el resultado.

4) `replace()` ⭐  
Qué hace: reemplaza un fragmento por otro.  
Así se escribe:
```py
texto = "hola mundo"
resultado = texto.replace("mundo", "Python")
```
Error típico:
```py
resultado = texto.replace("mundo")
```
Verás esto: `"hola Python"`.  
Por qué funciona: genera un string nuevo con reemplazo.  
Lo típico que sale mal: olvidar el segundo argumento; creer que modifica en sitio.

5) `split()` ⭐  
Qué hace: separa el texto en una lista.  
Así se escribe:
```py
texto = "a,b,c"
partes = texto.split(",")
```
Error típico:
```py
partes = texto.split
```
Verás esto: `['a', 'b', 'c']`.  
Por qué funciona: corta según el separador.  
Lo típico que sale mal: confundir split con slicing; usar separador incorrecto.

6) `join()`  
Qué hace: une textos con un separador.  
Así se escribe:
```py
partes = ["a", "b", "c"]
resultado = ",".join(partes)
```
Error típico:
```py
resultado = partes.join(",")
```
Verás esto: `"a,b,c"`.  
Por qué funciona: `join()` es método del separador.  
Lo típico que sale mal: pasar elementos no string; invertir el orden.

### Números (`int` / `float`)
1) `round()` ⭐  
Qué hace: redondea a n decimales.  
Así se escribe:
```py
precio = 3.1416
aprox = round(precio, 2)
```
Error típico:
```py
aprox = round("3.1416", 2)
```
Verás esto: `3.14`.  
Por qué funciona: `round` opera sobre números.  
Lo típico que sale mal: pasar strings; esperar más decimales sin indicar n.

2) `abs()` ⭐  
Qué hace: devuelve el valor absoluto.  
Así se escribe:
```py
delta = abs(-5)
```
Error típico:
```py
delta = abs[-5]
```
Verás esto: `5`.  
Por qué funciona: elimina el signo negativo.  
Lo típico que sale mal: olvidar paréntesis; pasar texto no numérico.

3) `int()` ⭐  
Qué hace: convierte a entero (trunca decimales).  
Así se escribe:
```py
cantidad = int("12")
```
Error típico:
```py
cantidad = int("12.5")
```
Verás esto: `12`.  
Por qué funciona: `int` convierte strings numéricos enteros.  
Lo típico que sale mal: usar strings con punto; asumir redondeo en vez de truncado.

4) `float()` ⭐  
Qué hace: convierte a flotante.  
Así se escribe:
```py
valor = float("3.5")
```
Error típico:
```py
valor = float("tres")
```
Verás esto: `3.5`.  
Por qué funciona: `float` interpreta strings numéricos.  
Lo típico que sale mal: usar textos no numéricos; confundir coma con punto.

5) `//` (división entera)  
Qué hace: divide y descarta decimales.  
Así se escribe:
```py
resultado = 7 // 2
```
Error típico:
```py
resultado = 7 // 0
```
Verás esto: `3`.  
Por qué funciona: aplica división entera.  
Lo típico que sale mal: división por cero; asumir que redondea (en realidad trunca).

6) `%` (módulo)  
Qué hace: devuelve el resto de una división.  
Así se escribe:
```py
resto = 7 % 2
```
Error típico:
```py
resto = 7 % 0
```
Verás esto: `1`.  
Por qué funciona: calcula el residuo.  
Lo típico que sale mal: división por cero; usarlo con floats y esperar enteros.

### Booleanos (`bool`)
1) `bool()` ⭐  
Qué hace: convierte un valor a True/False.  
Así se escribe:
```py
activo = bool(1)
```
Error típico:
```py
activo = bool("0")
```
Verás esto: `True`.  
Por qué funciona: cualquier string no vacío es True.  
Lo típico que sale mal: asumir que "0" es False; no validar entradas.

2) `not` ⭐  
Qué hace: niega una condición.  
Así se escribe:
```py
es_vacio = not True
```
Error típico:
```py
es_vacio = not
```
Verás esto: `False`.  
Por qué funciona: invierte el valor booleano.  
Lo típico que sale mal: usarlo sin operando; encadenar sin paréntesis.

3) `and` ⭐  
Qué hace: True solo si ambas condiciones son True.  
Así se escribe:
```py
permitido = True and False
```
Error típico:
```py
permitido = True and
```
Verás esto: `False`.  
Por qué funciona: evalúa ambas condiciones.  
Lo típico que sale mal: olvidar el segundo operando; confiar en el orden sin paréntesis.

4) `or` ⭐  
Qué hace: True si alguna condición es True.  
Así se escribe:
```py
permitido = False or True
```
Error típico:
```py
permitido = False or
```
Verás esto: `True`.  
Por qué funciona: basta un True para pasar.  
Lo típico que sale mal: olvidar el segundo operando; asumir que evalúa siempre ambas partes.

5) `==` (comparación)  
Qué hace: compara igualdad.  
Así se escribe:
```py
es_cero = (0 == 0)
```
Error típico:
```py
es_cero = (0 = 0)
```
Verás esto: `True`.  
Por qué funciona: `==` compara valores.  
Lo típico que sale mal: usar `=` por accidente; comparar tipos incompatibles.

6) `is` (identidad)  
Qué hace: comprueba identidad, útil con `None`.  
Así se escribe:
```py
valor = None
es_nulo = valor is None
```
Error típico:
```py
es_nulo = valor == None
```
Verás esto: `True`.  
Por qué funciona: `is` compara identidad exacta.  
Lo típico que sale mal: usar `==` en lugar de `is`; comparar objetos mutables.

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
                "Olvidar el dos puntos",
                "`if condicion` sin `:` provoca `SyntaxError`. Siempre termina la línea con `:`.",
            ),
            (
                "No indentar el bloque",
                "`IndentationError` ocurre cuando el bloque no está indentado con espacios.",
            ),
            (
                "Usar = en lugar de ==",
                "`if x = 3` da `SyntaxError`. Usa `==` para comparar.",
            ),
            (
                "Usar else con condición",
                "`else condicion:` no existe. Si hay condición, usa `elif`.",
            ),
            (
                "Comparar con True o False",
                "`if activo == True` es redundante. Usa `if activo:`.",
            ),
            (
                "Condiciones demasiado complejas",
                "Si la condición es larga, guarda partes en variables para legibilidad.",
            ),
            (
                "Olvidar cubrir el caso else",
                "Si no hay else, algunos caminos quedan sin manejar y el flujo se vuelve incierto.",
            ),
            (
                "Confundir igualdad con identidad",
                "Usa `==` para comparar valores y `is` para comparar `None`.",
            ),
            (
                "Usar strings vacíos sin considerar",
                "Un string vacío es falso. Asegúrate de que eso sea lo que quieres.",
            ),
            (
                "Mutar datos dentro del if sin control",
                "Si modificas listas dentro del if, documenta el efecto para evitar sorpresas.",
            ),
            (
                "Olvidar paréntesis en comparaciones múltiples",
                "En expresiones largas, usa paréntesis para evitar lógica incorrecta.",
            ),
            (
                "No usar elif para rangos",
                "Si usas varios if independientes, pueden ejecutarse varios bloques.",
            ),
            (
                "Comparar números como texto",
                "`""10"" > ""2""` es True por orden alfabético. Convierte a int primero.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "If básico",
                """# Aprende esto
# Aprenderás a ejecutar un bloque cuando se cumple una condición.
# Verás cómo se usa la indentación.
# Entenderás la lectura de un if simple.
#
# Haz esto
edad = 20  # Definimos la edad
if edad >= 18:  # Comprobamos si es mayor
    mensaje = "Mayor de edad"  # Texto de salida
    print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Mayor de edad".
#
# Por qué funciona
# La condición es True y el bloque indentado se ejecuta.
#
# Lo típico que sale mal
# - Olvidar el : al final del if.
# - No indentar el bloque.
""",
            ),
            (
                "If/else",
                """# Aprende esto
# Aprenderás a manejar dos caminos con else.
# Verás cómo cubrir el caso contrario.
# Entenderás la estructura completa.
#
# Haz esto
saldo = 0  # Saldo inicial
if saldo > 0:  # Comprobamos si hay saldo
    mensaje = "Hay saldo"  # Texto positivo
else:  # Caso contrario
    mensaje = "Sin saldo"  # Texto negativo
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Sin saldo".
#
# Por qué funciona
# La condición es False, así que se ejecuta else.
#
# Lo típico que sale mal
# - Escribir else con condición.
# - Usar if separados y ejecutar ambos bloques.
""",
            ),
            (
                "If/elif/else",
                """# Aprende esto
# Aprenderás a evaluar rangos con elif.
# Verás cómo se encadenan condiciones.
# Entenderás el primer bloque que se cumple.
#
# Haz esto
nota = 7  # Nota obtenida
if nota >= 9:  # Primer rango
    resultado = "Excelente"  # Texto 1
elif nota >= 5:  # Segundo rango
    resultado = "Aprobado"  # Texto 2
else:  # Último caso
    resultado = "Reprobado"  # Texto 3
print(resultado)  # Mostramos el resultado
#
# Verás esto
# Verás "Aprobado".
#
# Por qué funciona
# El primer if falla y el elif se cumple.
#
# Lo típico que sale mal
# - Olvidar elif y usar else mal.
# - Ordenar rangos de forma incorrecta.
""",
            ),
            (
                "Comparaciones correctas",
                """# Aprende esto
# Aprenderás a comparar con ==.
# Verás la diferencia con asignar.
# Entenderás el uso en condiciones.
#
# Haz esto
estado = "activo"  # Estado actual
if estado == "activo":  # Comparamos valores
    print("Usuario activo")  # Mensaje
#
# Verás esto
# Verás "Usuario activo".
#
# Por qué funciona
# == compara el valor del string.
#
# Lo típico que sale mal
# - Usar = en lugar de ==.
# - Comparar con mayúsculas distintas.
""",
            ),
            (
                "Condición booleana directa",
                """# Aprende esto
# Aprenderás a usar un booleano directamente.
# Verás una condición legible.
# Entenderás que no hace falta == True.
#
# Haz esto
activo = True  # Estado
if activo:  # Usamos el booleano directo
    print("Activo")  # Mensaje
#
# Verás esto
# Verás "Activo".
#
# Por qué funciona
# True evalúa a verdadero en el if.
#
# Lo típico que sale mal
# - Comparar con True y hacer el código ruidoso.
# - Asumir que cualquier valor es booleano.
""",
            ),
            (
                "Condiciones con strings vacíos",
                """# Aprende esto
# Aprenderás a evaluar textos vacíos.
# Verás el uso en validaciones.
# Entenderás valores truthy y falsy.
#
# Haz esto
nombre = ""  # Texto vacío
if nombre:  # Evaluamos si hay texto
    print("Nombre válido")  # Mensaje si hay texto
else:  # Caso vacío
    print("Nombre vacío")  # Mensaje si no hay texto
#
# Verás esto
# Verás "Nombre vacío".
#
# Por qué funciona
# Un string vacío es falsy.
#
# Lo típico que sale mal
# - Comparar con "" en lugar de usar la verdad del valor.
# - Olvidar el else y no mostrar nada.
""",
            ),
            (
                "Combinación con and",
                """# Aprende esto
# Aprenderás a combinar condiciones con and.
# Verás cómo se leen como una frase.
# Entenderás el orden lógico.
#
# Haz esto
edad = 20  # Edad
permiso = True  # Tiene permiso
if edad >= 18 and permiso:  # Ambas condiciones
    print("Puede entrar")  # Mensaje
#
# Verás esto
# Verás "Puede entrar".
#
# Por qué funciona
# Ambas condiciones son True.
#
# Lo típico que sale mal
# - Mezclar and/or sin paréntesis.
# - Olvidar una de las condiciones.
""",
            ),
            (
                "Rangos con elif ordenado",
                """# Aprende esto
# Aprenderás a ordenar rangos correctamente.
# Verás cómo evitar condiciones solapadas.
# Entenderás la importancia del orden.
#
# Haz esto
puntaje = 85  # Puntaje
if puntaje >= 90:  # Rango alto
    nivel = "A"  # Nivel A
elif puntaje >= 80:  # Rango medio
    nivel = "B"  # Nivel B
else:  # Rango bajo
    nivel = "C"  # Nivel C
print(nivel)  # Mostramos el nivel
#
# Verás esto
# Verás "B".
#
# Por qué funciona
# El primer if falla y el segundo se cumple.
#
# Lo típico que sale mal
# - Poner el rango menor primero.
# - Usar varios if y ejecutar más de un bloque.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una variable `edad` y muestra 'Mayor' si es >= 18, si no 'Menor'.",
                "hints": ["Usa if/else.", "Recuerda el : y la indentación."],
                "solution": """edad = 16
if edad >= 18:
    print("Mayor")
else:
    print("Menor")""",
            },
            {
                "question": "Crea un sistema de notas con if/elif/else: 9-10 Excelente, 5-8 Aprobado, resto Reprobado.",
                "hints": ["Ordena los rangos de mayor a menor.", "Usa elif para el segundo rango."],
                "solution": """nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")""",
            },
            {
                "question": "Comprueba si una variable `activo` es verdadera y muestra un mensaje.",
                "hints": ["No compares con True.", "Usa if activo:."],
                "solution": """activo = True
if activo:
    print("Activo")""",
            },
            {
                "question": "Valida que un string `nombre` no esté vacío y muestra un mensaje en ambos casos.",
                "hints": ["Un string vacío es falsy.", "Usa else para el caso vacío."],
                "solution": """nombre = ""
if nombre:
    print("Nombre válido")
else:
    print("Nombre vacío")""",
            },
            {
                "question": "Usa una condición con and: edad >= 18 y permiso True para mostrar 'Puede entrar'.",
                "hints": ["Define edad y permiso.", "Usa and entre condiciones."],
                "solution": """edad = 20
permiso = True
if edad >= 18 and permiso:
    print("Puede entrar")""",
            },
            {
                "question": "Crea una variable `color` y muestra un mensaje solo si es igual a 'rojo'.",
                "hints": ["Usa == para comparar.", "No uses = en el if."],
                "solution": """color = "rojo"
if color == "rojo":
    print("Semáforo en rojo")""",
            },
        ]
