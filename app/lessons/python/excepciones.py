from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ExcepcionesLesson(Lesson):
    TITLE = "Excepciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐", "🧠"]
    TAGS = ["errores", "try/except", "raise", "finally"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es una excepción, cómo manejar errores con try/except, "
            "y cuándo crear errores propios con buenas prácticas claras."
        )

    def guide(self) -> str:
        return """
## ¿Qué es una excepción?
Una **excepción** es una señal de error que Python lanza cuando algo sale mal. No es "misterioso":
solo indica que una instrucción no pudo completarse. Por ejemplo, convertir texto a número.

Ejemplo inmediato (con comentarios):
```
edad_texto = "veinte"  # variable con texto
edad = int(edad_texto)  # int intenta convertir y lanza ValueError
```

## ¿Por qué existen?
Sirven para separar el **flujo normal** del **flujo de error**. Así tu programa puede reaccionar
sin detenerse de golpe.

## Ejemplo grande con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** cómo validar datos con `try/except/else`, reportar errores claros y no perder
el flujo principal del programa.

**Haz esto (ejemplo completo con contexto):**
```py
entradas = ["18", "x", "-2", "21"]
edades_validas = []

for texto in entradas:
    try:
        edad = int(texto)
        if edad < 0:
            raise ValueError("Edad negativa")
    except ValueError:
        print(f"Entrada inválida: {texto}")
    else:
        edades_validas.append(edad)

print("Edades válidas:", edades_validas)
```

**Verás esto (salida real):**
```
Entrada inválida: x
Entrada inválida: -2
Edades válidas: [18, 21]
```

**Por qué funciona:** `try` encapsula la conversión; `raise` fuerza un error cuando detectas un
valor inválido; `except` captura el error y `else` solo se ejecuta si todo fue correcto.

**Lo típico que sale mal (con error real):**
```py
edad = int("x")
```
```
ValueError: invalid literal for int() with base 10: 'x'
```
Solución: captura `ValueError` y muestra un mensaje claro con el texto fallido.

## Conceptos previos (sin asumir nada)
- **función**: bloque reutilizable de código.
- **objeto**: dato con estado y comportamiento.
- **método**: función que pertenece a un objeto (por ejemplo, `append` en una lista).
- **variable**: nombre que apunta a un valor.
- **print**: función que muestra texto en la salida.

### Buenas prácticas (CalloutBox: best_practice)
- Usa nombres en **snake_case**.
- Captura errores específicos (por ejemplo, `ValueError`).
- Mantén el `try` lo más pequeño posible.

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

## Paso 1: Un error típico explicado
Dividir por cero no tiene resultado válido, por eso Python lanza `ZeroDivisionError`.
```
numero = 10  # variable con valor
resultado = numero / 0  # error: división por cero
```

## Paso 2: Manejar errores con try/except
`try` envuelve el código que puede fallar y `except` responde con una solución.
```
try:  # bloque protegido
    numero = int("25")  # convertimos texto a número
    print(numero)  # mostramos el resultado
except ValueError:  # error de conversión
    print("No es un número válido")  # mensaje de salida
```

## Paso 3: else y finally (control detallado)
- **else** se ejecuta si NO hubo error.
- **finally** se ejecuta SIEMPRE, haya error o no.
```
try:  # bloque protegido
    valor = 10 / 2  # operación segura
except ZeroDivisionError:  # manejo del error
    print("No dividir por cero")  # mensaje
else:  # solo si no hubo error
    print("Resultado:", valor)  # usamos el resultado
finally:  # siempre
    print("Cerrar recursos")  # limpieza final
```

Micro-ejemplo correcto:
```py
try:
    numero = int("7")
except ValueError:
    print("No válido")
else:
    print("Convertido:", numero)
```

Micro-ejemplo incorrecto:
```py
try:
    numero = int("7")
else:
    print("Convertido:", numero)
```

Error real:
```
SyntaxError: expected 'except' or 'finally' block
```

Corrección: `else` solo existe si antes declaraste `except` o `finally`.

## Paso 4: Lanzar errores propios con raise
Si detectas un dato inválido, puedes lanzar una excepción con `raise`.
```
def validar_edad(edad):  # función de validación
    if edad < 0:  # condición inválida
        raise ValueError("Edad inválida")  # lanzamos error
```

Micro-ejemplo correcto:
```py
saldo = -10
if saldo < 0:
    raise ValueError("Saldo negativo")
```

Micro-ejemplo incorrecto:
```py
raise "Saldo negativo"
```

Error real:
```
TypeError: exceptions must derive from BaseException
```

Corrección: lanza una clase de excepción (por ejemplo, `ValueError`), no un string.

## Paso 5: Excepciones personalizadas
Creas tus propios errores cuando quieres un mensaje más claro.
```
class DatosInvalidosError(Exception):  # clase de error
    pass  # sin lógica extra
```

## Paso 6: Encadenar errores para no perder contexto
Cuando transformas un error, usa `from` para mantener el original.
```
try:  # intentamos
    int("abc")  # error de conversión
except ValueError as exc:  # capturamos error original
    raise RuntimeError("Entrada inválida") from exc  # encadenamos
```

## Paso 7: Explicar funciones y utilidades comunes
- `len()` devuelve la longitud de una lista o texto.
- `print()` muestra información útil para depurar.

Ejemplo simple con comentarios:
```
texto = "hola"  # texto de ejemplo
cantidad = len(texto)  # len cuenta caracteres
print(cantidad)  # print muestra el número
```

## Más allá (nivel pro)
- **Captura específica por jerarquía**: `Exception` es muy general; empieza por el error real.
  ```
  try:  # bloque protegido
      numero = int("abc")  # error de conversión
  except ValueError:  # error específico
      print("Texto no convertible")  # mensaje claro
  ```
  Úsalo cuando sepas qué puede fallar.
  Evítalo si capturas `Exception` y ocultas errores inesperados.
- **Re-raise para no perder contexto**: vuelve a lanzar el error después de registrar.
  ```
  try:  # intentamos
      1 / 0  # error
  except ZeroDivisionError:  # capturamos
      print("División inválida")  # log simple
      raise  # relanzamos el mismo error
  ```
  Úsalo cuando necesitas registrar y dejar que el error suba.
  Evítalo si quieres recuperar y continuar con valores seguros.
- **`raise ... from` para encadenar**: mantiene el error original.
  ```
  try:  # bloque
      int("abc")  # conversión fallida
  except ValueError as exc:  # error original
      raise RuntimeError("Entrada inválida") from exc  # nuevo error
  ```
  Úsalo cuando transformes un error técnico en uno de dominio.
  Evítalo si no necesitas contexto adicional.
- **Excepciones propias con intención**: nombre específico comunica el problema.
  ```
  class ConfigError(Exception):  # error propio
      pass  # sin lógica extra
  raise ConfigError("Falta API_KEY")  # lanzamos
  ```
  Úsalo cuando quieras diferenciar fallos de configuración.
  Evítalo si un error estándar ya describe bien el problema.
- **Logging en lugar de print**: `logging` permite niveles y salida ordenada.
  ```
  import logging  # módulo de logging
  logger = logging.getLogger(__name__)  # logger del módulo
  try:  # bloque protegido
      int("abc")  # error
  except ValueError:  # captura
      logger.exception("Entrada inválida")  # registra con traceback
  ```
  Úsalo en proyectos reales donde necesitas trazas.
  Evítalo en ejemplos muy simples donde print es suficiente.
- **`finally` para limpieza confiable**: se ejecuta siempre.
  ```
  recurso = None  # variable inicial
  try:  # intento principal
      recurso = open("datos.txt", "r")  # abrimos archivo
      _ = recurso.read()  # leemos
  finally:  # limpieza segura
      if recurso is not None:  # validamos
          recurso.close()  # cerramos
  ```
  Úsalo cuando debas cerrar recursos aunque haya errores.
  Evítalo si usas `with`, que ya se encarga de cerrar.


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
                "Capturar Exception genérico",
                "Solución: captura tipos específicos (ValueError, ZeroDivisionError) para no ocultar errores.",
            ),
            (
                "Usar except vacío",
                "Solución: indica el error exacto y muestra un mensaje útil con print().",
            ),
            (
                "Ignorar finally",
                "Solución: usa finally para liberar recursos aunque haya error.",
            ),
            (
                "Lanzar errores sin contexto",
                "Solución: encadena con 'raise NuevoError from exc' para conservar el origen.",
            ),
            (
                "Usar excepciones como flujo normal",
                "Solución: valida antes (if) y reserva excepciones para fallos reales.",
            ),
            (
                "No explicar el error al usuario",
                "Solución: muestra mensajes claros y específicos en lugar de solo 'Error'.",
            ),
            (
                "Abrir recursos sin cerrar",
                "Solución: usa with o un finally que haga close().",
            ),
            (
                "Confundir error con None",
                "Solución: distingue entre valor válido None y un error real.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Try/except básico",
                """try:  # bloque protegido
    numero = int("10")  # convertimos texto
    print(numero)  # mostramos número
except ValueError:  # error específico
    print("Entrada inválida")  # mensaje""",
            ),
            (
                "Try/except/else/finally",
                """try:  # bloque principal
    resultado = 12 / 3  # operación segura
except ZeroDivisionError:  # error posible
    print("No dividir por cero")  # aviso
else:  # si no hubo error
    print("Resultado:", resultado)  # usamos resultado
finally:  # limpieza
    print("Fin del bloque")  # siempre""",
            ),
            (
                "Raise con validación",
                """def validar_edad(edad):  # función
    if edad < 0:  # condición inválida
        raise ValueError("Edad inválida")  # lanzamos error
validar_edad(5)  # llamada""",
            ),
            (
                "Excepción personalizada",
                """class ConfigError(Exception):  # clase de error
    pass  # sin lógica extra
raise ConfigError("Falta API_KEY")  # lanzamos""",
            ),
            (
                "Encadenar errores",
                """try:  # intentamos convertir
    int("abc")  # error de conversión
except ValueError as exc:  # capturamos
    raise RuntimeError("Entrada no válida") from exc  # encadenamos""",
            ),
            (
                "Uso de len y print",
                """texto = "hola"  # texto de ejemplo
cantidad = len(texto)  # len cuenta caracteres
print(cantidad)  # print muestra el resultado""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función que divida dos números y maneje ZeroDivisionError.",
                "hints": ["Devuelve None si hay error", "Usa try/except"],
                "solution": (
                    "def dividir(a, b):\n"
                    "    try:\n"
                    "        return a / b\n"
                    "    except ZeroDivisionError:\n"
                    "        return None"
                ),
            },
            {
                "question": "Convierte un texto a entero y muestra un mensaje claro si falla.",
                "hints": ["Usa int()", "Captura ValueError"],
                "solution": (
                    "def convertir(texto):\n"
                    "    try:\n"
                    "        return int(texto)\n"
                    "    except ValueError:\n"
                    "        print('Entrada inválida')\n"
                    "        return None"
                ),
            },
            {
                "question": "Define una excepción personalizada llamada DataError.",
                "hints": ["Hereda de Exception"],
                "solution": "class DataError(Exception):\n    pass",
            },
            {
                "question": "Usa finally para cerrar un recurso simulado.",
                "hints": ["Usa un try con print()"],
                "solution": "try:\n    print('abriendo')\nfinally:\n    print('cerrando')",
            },
            {
                "question": "Encadena un ValueError dentro de RuntimeError con from.",
                "hints": ["Usa raise ... from exc"],
                "solution": (
                    "try:\n"
                    "    int('abc')\n"
                    "except ValueError as exc:\n"
                    "    raise RuntimeError('Entrada inválida') from exc"
                ),
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Explora los bloques try/except en los ejemplos."))
        return widget
