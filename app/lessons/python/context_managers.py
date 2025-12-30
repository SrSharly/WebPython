from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ContextManagersLesson(Lesson):
    TITLE = "Context managers"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["with", "context manager", "recursos", "archivos"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es un context manager, cómo usar with para cerrar recursos, "
            "y cómo crear tus propios manejadores con buenas prácticas."
        )

    def guide(self) -> str:
        return """
## ¿Qué problema resuelven?
Cuando abres un archivo o una conexión, debes **cerrarla**. Si olvidas, puedes perder datos o
bloquear recursos. Un context manager lo hace por ti.

Ejemplo del problema (con comentarios):
```
archivo = open("datos.txt", "w")  # abrimos archivo
archivo.write("Hola")  # escribimos contenido
archivo.close()  # cerramos manualmente
```
Si ocurre un error antes de `close()`, el archivo queda abierto.

## ¿Qué es un context manager?
Es un **objeto** que define cómo entrar y salir de un bloque. En términos simples:
"abre y luego limpia". Se usa con la palabra clave `with`.

## Conceptos previos (sin asumir nada)
- **función**: bloque reutilizable de código.
- **método**: función asociada a un objeto.
- **variable**: nombre que apunta a un valor.
- **print**: función que muestra texto en la salida.
- **len**: función que devuelve longitud (por ejemplo, de un texto).

### Buenas prácticas (CalloutBox: best_practice)
- Usa nombres en **snake_case**.
- Prefiere `with` en lugar de `try/finally` manual.
- Mantén el bloque `with` pequeño y claro.

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

### Archivos (`io.TextIOBase`)

1) `read()` ⭐  
Qué hace: lee todo el contenido.  
Así se escribe:
```py
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```
Error típico:
```py
contenido = archivo.read
```
Verás esto: el texto completo del archivo.  
Por qué funciona: `read()` consume el contenido disponible.  
Lo típico que sale mal: olvidar paréntesis; asumir que deja el cursor al inicio.

2) `readline()`  
Qué hace: lee una sola línea.  
Así se escribe:
```py
with open("datos.txt", "r") as archivo:
    linea = archivo.readline()
```
Error típico:
```py
linea = archivo.readline("")
```
Verás esto: la primera línea.  
Por qué funciona: avanza el cursor una línea.  
Lo típico que sale mal: pasar argumentos innecesarios; olvidar que incluye salto de línea.

3) `readlines()`  
Qué hace: lee todas las líneas en una lista.  
Así se escribe:
```py
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
```
Error típico:
```py
lineas = archivo.readlines
```
Verás esto: `['linea1\\n', 'linea2\\n']`.  
Por qué funciona: devuelve una lista de líneas.  
Lo típico que sale mal: olvidar paréntesis; cargar archivos enormes en memoria.

4) `write()` ⭐  
Qué hace: escribe texto en el archivo.  
Así se escribe:
```py
with open("datos.txt", "w") as archivo:
    archivo.write("Hola")
```
Error típico:
```py
archivo.write(123)
```
Verás esto: el archivo contiene "Hola".  
Por qué funciona: `write()` acepta strings.  
Lo típico que sale mal: pasar números sin convertir; olvidar abrir en modo escritura.

5) `seek()`  
Qué hace: mueve el cursor de lectura/escritura.  
Así se escribe:
```py
with open("datos.txt", "r") as archivo:
    archivo.seek(0)
```
Error típico:
```py
archivo.seek("0")
```
Verás esto: el cursor vuelve al inicio.  
Por qué funciona: `seek()` espera un entero.  
Lo típico que sale mal: pasar strings; olvidar que afecta lecturas posteriores.

6) `tell()`  
Qué hace: indica la posición actual del cursor.  
Así se escribe:
```py
with open("datos.txt", "r") as archivo:
    posicion = archivo.tell()
```
Error típico:
```py
posicion = archivo.tell
```
Verás esto: un número entero.  
Por qué funciona: consulta el offset interno.  
Lo típico que sale mal: olvidar paréntesis; asumir que devuelve líneas en vez de bytes.

7) `close()` ⭐  
Qué hace: cierra el archivo.  
Así se escribe:
```py
archivo = open("datos.txt", "r")
archivo.close()
```
Error típico:
```py
archivo.close
```
Verás esto: el archivo ya no se puede leer/escribir.  
Por qué funciona: libera el recurso del sistema.  
Lo típico que sale mal: olvidar cerrar; intentar usarlo después de cerrado.

### ExitStack (`contextlib.ExitStack`)
1) `enter_context()` ⭐  
Qué hace: registra un context manager dinámicamente.  
Así se escribe:
```py
from contextlib import ExitStack
with ExitStack() as stack:
    archivo = stack.enter_context(open("a.txt", "w"))
```
Error típico:
```py
stack.enter_context
```
Verás esto: el recurso queda gestionado por el stack.  
Por qué funciona: `ExitStack` almacena los `__exit__` para cerrarlos al final.  
Lo típico que sale mal: olvidar paréntesis; usarlo fuera de un `with`.

2) `callback()`  
Qué hace: registra una función de limpieza manual.  
Así se escribe:
```py
from contextlib import ExitStack
with ExitStack() as stack:
    stack.callback(print, "Limpiar")
```
Error típico:
```py
stack.callback("Limpiar")
```
Verás esto: se ejecuta `print` al salir del `with`.  
Por qué funciona: guarda callbacks para salida.  
Lo típico que sale mal: pasar argumentos incompletos; asumir ejecución inmediata.

3) `push()`  
Qué hace: registra un objeto con `__exit__`.  
Así se escribe:
```py
from contextlib import ExitStack
class Recurso:
    def __exit__(self, exc_type, exc, tb):
        print("Cerrar")

with ExitStack() as stack:
    stack.push(Recurso())
```
Error típico:
```py
stack.push("recurso")
```
Verás esto: se ejecuta `Cerrar` al salir.  
Por qué funciona: `push` espera algo con `__exit__`.  
Lo típico que sale mal: pasar un string; olvidar que necesita `__exit__`.

4) `pop_all()`  
Qué hace: extrae todos los callbacks para transferirlos.  
Así se escribe:
```py
from contextlib import ExitStack
with ExitStack() as stack:
    nuevo_stack = stack.pop_all()
```
Error típico:
```py
stack.pop_all
```
Verás esto: un ExitStack con callbacks movidos.  
Por qué funciona: mueve los registros a otro stack.  
Lo típico que sale mal: olvidar paréntesis; asumir que cierra recursos automáticamente.

5) `close()`  
Qué hace: ejecuta la limpieza registrada.  
Así se escribe:
```py
stack = ExitStack()
stack.close()
```
Error típico:
```py
stack.close
```
Verás esto: callbacks ejecutados y stack vacío.  
Por qué funciona: cierra como si salieras del `with`.  
Lo típico que sale mal: olvidar paréntesis; cerrarlo dos veces sin necesidad.

6) `__enter__()` / `__exit__()`  
Qué hace: permiten usar `ExitStack` con `with`.  
Así se escribe:
```py
with ExitStack() as stack:
    pass
```
Error típico:
```py
ExitStack().__enter__
```
Verás esto: el bloque `with` funciona correctamente.  
Por qué funciona: implementa el protocolo de context manager.  
Lo típico que sale mal: llamar `__enter__` manualmente; olvidar `with`.

### Listas (`list`)
1) `append()` ⭐  
Qué hace: agrega un elemento al final.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.append("pera")
```
Error típico:
```py
frutas.append
```
Verás esto: `['manzana', 'pera']`.  
Por qué funciona: muta la lista en sitio.  
Lo típico que sale mal: olvidar paréntesis; asumir que devuelve una lista nueva.

2) `extend()` ⭐  
Qué hace: agrega varios elementos.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.extend(["pera", "uva"])
```
Error típico:
```py
frutas.extend("uva")
```
Verás esto: `['manzana', 'pera', 'uva']`.  
Por qué funciona: recorre el iterable y añade cada elemento.  
Lo típico que sale mal: pasar un string y separar por caracteres; confundir con `append`.

3) `insert()`  
Qué hace: inserta en una posición.  
Así se escribe:
```py
frutas = ["manzana", "uva"]
frutas.insert(1, "pera")
```
Error típico:
```py
frutas.insert("1", "pera")
```
Verás esto: `['manzana', 'pera', 'uva']`.  
Por qué funciona: usa un índice entero.  
Lo típico que sale mal: índice fuera de rango; pasar índice como string.

4) `pop()` ⭐  
Qué hace: quita y devuelve el último (o por índice).  
Así se escribe:
```py
frutas = ["manzana", "pera"]
ultima = frutas.pop()
```
Error típico:
```py
frutas.pop(5)
```
Verás esto: `ultima = 'pera'`.  
Por qué funciona: elimina el elemento y lo retorna.  
Lo típico que sale mal: `IndexError` por índice inválido; mutar lista mientras iteras.

5) `remove()`  
Qué hace: elimina el primer valor encontrado.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
frutas.remove("pera")
```
Error típico:
```py
frutas.remove("uva")
```
Verás esto: `['manzana']`.  
Por qué funciona: busca el valor y lo elimina.  
Lo típico que sale mal: `ValueError` si no existe; confundir valor con índice.

6) `sort()` ⭐  
Qué hace: ordena la lista.  
Así se escribe:
```py
numeros = [3, 1, 2]
numeros.sort()
```
Error típico:
```py
ordenados = numeros.sort()
```
Verás esto: `[1, 2, 3]`.  
Por qué funciona: ordena en sitio y devuelve `None`.  
Lo típico que sale mal: esperar una lista nueva; mezclar tipos incompatibles.

7) `reverse()`  
Qué hace: invierte el orden.  
Así se escribe:
```py
numeros = [1, 2, 3]
numeros.reverse()
```
Error típico:
```py
numeros = numeros.reverse()
```
Verás esto: `[3, 2, 1]`.  
Por qué funciona: invierte en sitio.  
Lo típico que sale mal: esperar retorno; confundir con `sorted(..., reverse=True)`.

8) `len()` ⭐  
Qué hace: cuenta elementos.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
total = len(frutas)
```
Error típico:
```py
total = frutas.len()
```
Verás esto: `2`.  
Por qué funciona: `len()` es función global.  
Lo típico que sale mal: usar `.len()`; olvidar que algunas operaciones dependen del tamaño.

9) `sum()` ⭐  
Qué hace: suma los valores de la lista.  
Así se escribe:
```py
numeros = [1, 2, 3]
total = sum(numeros)
```
Error típico:
```py
total = sum([1, "2", 3])
```
Verás esto: `6`.  
Por qué funciona: suma elementos numéricos.  
Lo típico que sale mal: mezclar tipos; pasar lista vacía y esperar un promedio.

10) `max()`  
Qué hace: devuelve el mayor valor.  
Así se escribe:
```py
numeros = [4, 8, 15]
mayor = max(numeros)
```
Error típico:
```py
mayor = max([])
```
Verás esto: `15`.  
Por qué funciona: compara valores y retorna el más alto.  
Lo típico que sale mal: lista vacía (`ValueError`); mezclar tipos no comparables.

11) `min()`  
Qué hace: devuelve el menor valor.  
Así se escribe:
```py
numeros = [4, 8, 15]
menor = min(numeros)
```
Error típico:
```py
menor = min([])
```
Verás esto: `4`.  
Por qué funciona: compara valores y retorna el más bajo.  
Lo típico que sale mal: lista vacía (`ValueError`); comparar tipos incompatibles.

## Paso 1: Usar with con archivos
`with` garantiza el cierre aunque haya errores.
```
with open("datos.txt", "w") as archivo:  # abrimos con with
    archivo.write("Hola")  # escribimos dentro del bloque
print("Listo")  # fuera del bloque, archivo cerrado
```

## Paso 2: Leer con seguridad
```
with open("datos.txt", "r") as archivo:  # abrimos en lectura
    contenido = archivo.read()  # leemos todo
print(contenido)  # mostramos
```

## Paso 3: Explicar métodos importantes
- `read()` lee el contenido completo.
- `write()` escribe texto.
- `close()` cierra el recurso.

## Paso 4: Context managers propios (clase)
Un context manager propio implementa `__enter__` y `__exit__`.
```
class Temporizador:  # clase ejemplo
    def __enter__(self):  # entramos al bloque
        print("Inicio")  # mensaje
        return self  # devolvemos el objeto

    def __exit__(self, exc_type, exc, traceback):  # salimos
        print("Fin")  # mensaje final
```

Uso con `with`:
```
with Temporizador() as t:  # usamos el context manager
    print("Trabajando")  # acción dentro
```

## Paso 5: Múltiples recursos en un solo with
Puedes abrir varios recursos en una sola línea.
```
with open("a.txt", "w") as a, open("b.txt", "w") as b:  # dos archivos
    a.write("A")  # escribimos en el primero
    b.write("B")  # escribimos en el segundo
```

## Paso 6: Control de errores con __exit__
Si `__exit__` devuelve `True`, puede suprimir la excepción.
```
class Silenciador:  # context manager
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, traceback):
        print("Error controlado")  # mensaje
        return True  # suprime el error
```

## Más allá (nivel pro)
- **`contextlib.contextmanager` (decorador simple)**: crea un context manager con `yield`.
  ```
  from contextlib import contextmanager  # importamos decorador
  @contextmanager  # convertimos función en context manager
  def abrir_archivo(ruta):  # función con yield
      archivo = open(ruta, "r")  # abrimos recurso
      try:  # protegemos la apertura
          yield archivo  # entregamos el recurso
      finally:  # limpieza garantizada
          archivo.close()  # cerramos siempre
  ```
  Úsalo cuando quieras algo rápido sin crear una clase.
  Evítalo si necesitas estado complejo entre __enter__ y __exit__.
- **`ExitStack` para recursos dinámicos**: maneja varios recursos en un solo bloque.
  ```
  from contextlib import ExitStack  # importamos ExitStack
  rutas = ["a.txt", "b.txt"]  # lista de archivos
  with ExitStack() as stack:  # manejador dinámico
      archivos = [stack.enter_context(open(r, "w")) for r in rutas]  # abrimos
      archivos[0].write("A")  # escribimos
  ```
  Úsalo cuando el número de recursos se decide en tiempo de ejecución.
  Evítalo si solo necesitas uno o dos `with` simples.
- **No ocultar errores por accidente**: `__exit__` debe devolver False normalmente.
  ```
  class RegistroErrores:  # clase
      def __enter__(self):  # entrada
          return self  # devolvemos
      def __exit__(self, exc_type, exc, traceback):  # salida
          if exc_type:  # si hay error
              print("Error:", exc)  # registramos
          return False  # no suprime
  ```
  Úsalo cuando quieras registrar pero no ocultar fallos.
  Evítalo si necesitas suprimir errores de forma consciente y documentada.
- **Bloques `with` pequeños**: reduce el tiempo de recursos abiertos.
  ```
  with open("datos.txt", "r") as archivo:  # abrimos archivo
      contenido = archivo.read()  # leemos rápido
  print(contenido)  # fuera del bloque
  ```
  Úsalo para minimizar riesgos de bloqueo.
  Evítalo si necesitas el recurso durante toda una operación larga.
- **Context manager para tiempos (medición simple)**: encapsula inicio/fin.
  ```
  import time  # módulo de tiempo
  class Temporizador:  # clase simple
      def __enter__(self):  # entrada
          self.inicio = time.time()  # guardamos inicio
          return self  # devolvemos
      def __exit__(self, exc_type, exc, traceback):  # salida
          duracion = time.time() - self.inicio  # calculamos duración
          print(f"Duración: {duracion:.2f}s")  # mostramos
  ```
  Úsalo para medir bloques de código en desarrollo.
  Evítalo en producción si ya tienes herramientas de observabilidad.

## Micro-ejemplo: `with` requiere `as`

### Así se escribe
```py
with open("datos.txt") as archivo:
    pass
```

### Error típico: olvidar `as`
```py
with open("datos.txt") archivo:
    pass
```

```py
SyntaxError: invalid syntax
```

Explicación breve: `with` necesita la forma `with recurso as nombre`.
Solución: agrega `as` para capturar el manejador y usarlo dentro del bloque.


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
                "Olvidar cerrar recursos",
                "Solución: usa with para cerrar automáticamente aunque haya error.",
            ),
            (
                "Usar try sin finally",
                "Solución: reemplaza por with o añade finally para cerrar.",
            ),
            (
                "Silenciar errores sin intención",
                "Solución: en __exit__ devuelve False para no ocultar excepciones.",
            ),
            (
                "Anidar muchos with",
                "Solución: usa una sola línea with con comas cuando sea posible.",
            ),
            (
                "Bloques with demasiado grandes",
                "Solución: reduce el bloque a lo esencial para claridad.",
            ),
            (
                "Usar rutas mágicas",
                "Solución: guarda rutas en variables con nombres claros.",
            ),
            (
                "No explicar métodos",
                "Solución: comenta read(), write() y close() cuando enseñes a principiantes.",
            ),
            (
                "Reutilizar el mismo archivo cerrado",
                "Solución: abre un nuevo recurso si necesitas otra operación.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "with con escritura",
                """with open("datos.txt", "w") as archivo:  # abrimos archivo
    archivo.write("Hola")  # escribimos
print("Listo")  # fuera del bloque""",
            ),
            (
                "with con lectura",
                """with open("datos.txt", "r") as archivo:  # abrimos en lectura
    contenido = archivo.read()  # leemos contenido
print(contenido)  # mostramos""",
            ),
            (
                "Context manager propio",
                """class Temporizador:  # clase
    def __enter__(self):  # entramos
        print("Inicio")  # mensaje
        return self  # retornamos
    def __exit__(self, exc_type, exc, traceback):  # salimos
        print("Fin")  # mensaje
with Temporizador() as t:  # usamos with
    print("Trabajando")  # acción""",
            ),
            (
                "Varios recursos",
                """with open("a.txt", "w") as a, open("b.txt", "w") as b:  # dos archivos
    a.write("A")  # escribimos en a
    b.write("B")  # escribimos en b""",
            ),
            (
                "Suprimir error",
                """class Silenciador:  # clase
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, traceback):
        print("Error controlado")  # mensaje
        return True  # suprime el error
with Silenciador():
    1 / 0  # error que se suprime""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Abre un archivo en modo append y escribe una línea usando with.",
                "hints": ["Usa open(..., 'a')"],
                "solution": "with open('log.txt', 'a') as f:\n    f.write('nuevo\n')",
            },
            {
                "question": "Crea un context manager simple que imprima 'inicio' y 'fin'.",
                "hints": ["Implementa __enter__ y __exit__"],
                "solution": (
                    "class CM:\n"
                    "    def __enter__(self):\n"
                    "        print('inicio')\n"
                    "        return self\n"
                    "    def __exit__(self, exc_type, exc, traceback):\n"
                    "        print('fin')"
                ),
            },
            {
                "question": "Lee un archivo con with y guarda el contenido en una variable.",
                "hints": ["Usa .read()"],
                "solution": "with open('datos.txt', 'r') as f:\n    contenido = f.read()",
            },
            {
                "question": "Abre dos archivos en una sola línea with.",
                "hints": ["Usa with ... as a, ... as b"],
                "solution": "with open('a.txt', 'w') as a, open('b.txt', 'w') as b:\n    a.write('A')\n    b.write('B')",
            },
            {
                "question": "Crea un context manager que NO suprima errores.",
                "hints": ["__exit__ debe retornar False"],
                "solution": (
                    "class Registro:\n"
                    "    def __enter__(self):\n"
                    "        return self\n"
                    "    def __exit__(self, exc_type, exc, traceback):\n"
                    "        if exc_type:\n"
                    "            print('Error:', exc)\n"
                    "        return False"
                ),
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Prueba los ejemplos con archivos de texto simples."))
        return widget
