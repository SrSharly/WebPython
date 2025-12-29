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
