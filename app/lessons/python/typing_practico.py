from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class TypingPracticoLesson(Lesson):
    TITLE = "Typing práctico"
    CATEGORY = "Python"
    SUBCATEGORY = "Buenas prácticas"
    LEVEL = "Intermedio"
    TAGS = ["typing", "Optional", "Protocol", "TypeVar", "hints"]

    def summary(self) -> str:
        return (
            "El tipado gradual ayuda a comunicar intención, detectar errores y "
            "documentar APIs con hints como Optional, Union y Protocol."
        )

    def guide(self) -> str:
        return """
TL;DR: Usa typing para describir contratos y detectar problemas antes de ejecutar.
- Optional[T] es lo mismo que Union[T, None].
- Literal restringe valores válidos (p. ej., Literal["A", "B"]).
- TypedDict describe dicts con claves y tipos esperados.
- Protocol define interfaces estructurales (duck typing tipado).
- Sequence es más general que list; Mapping más general que dict.
- Callable[[args], retorno] describe funciones invocables.
- TypeVar permite funciones genéricas reutilizables.
- Evita Any si quieres validación; se propaga y desactiva chequeos.
- Preferir tipos inmutables para defaults (None + asignación interna).
- Usa comentarios de tipo para casos complejos.
- type checkers detectan incompatibilidades de forma estática.
- Mantén hints simples y consistentes en toda la API.


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

### Diccionarios (`dict`)
1) `get()` ⭐  
Qué hace: obtiene un valor sin lanzar KeyError.  
Así se escribe:
```py
config = {"host": "localhost"}
host = config.get("host")
```
Error típico:
```py
host = config["puerto"]
```
Verás esto: `"localhost"`.  
Por qué funciona: `get` devuelve None o un default si no existe.  
Lo típico que sale mal: usar `[]` y provocar `KeyError`; olvidar el valor por defecto.

2) `keys()`  
Qué hace: devuelve las claves.  
Así se escribe:
```py
config = {"host": "localhost"}
claves = list(config.keys())
```
Error típico:
```py
claves = config.keys
```
Verás esto: `['host']`.  
Por qué funciona: `keys()` expone una vista de claves.  
Lo típico que sale mal: olvidar paréntesis; asumir que es lista sin convertir.

3) `values()`  
Qué hace: devuelve los valores.  
Así se escribe:
```py
config = {"host": "localhost"}
valores = list(config.values())
```
Error típico:
```py
valores = config.values
```
Verás esto: `['localhost']`.  
Por qué funciona: `values()` expone una vista.  
Lo típico que sale mal: olvidar paréntesis; modificar mientras iteras.

4) `items()` ⭐  
Qué hace: devuelve pares (clave, valor).  
Así se escribe:
```py
config = {"host": "localhost"}
pares = list(config.items())
```
Error típico:
```py
pares = config.items
```
Verás esto: `[("host", "localhost")]`.  
Por qué funciona: permite iterar claves y valores juntos.  
Lo típico que sale mal: olvidar paréntesis; asumir orden fijo.

5) `update()` ⭐  
Qué hace: mezcla claves nuevas o existentes.  
Así se escribe:
```py
config = {"host": "localhost"}
config.update({"puerto": 5432})
```
Error típico:
```py
config.update("puerto")
```
Verás esto: `{"host": "localhost", "puerto": 5432}`.  
Por qué funciona: actualiza el diccionario con otro mapping.  
Lo típico que sale mal: pasar un string; sobrescribir claves sin querer.

6) `pop()`  
Qué hace: elimina una clave y devuelve su valor.  
Así se escribe:
```py
config = {"host": "localhost"}
host = config.pop("host")
```
Error típico:
```py
host = config.pop("puerto")
```
Verás esto: `host = "localhost"`.  
Por qué funciona: quita la entrada y retorna su valor.  
Lo típico que sale mal: `KeyError` si no existe; mutar mientras iteras.

7) `setdefault()`  
Qué hace: obtiene valor o crea si no existe.  
Así se escribe:
```py
config = {}
puerto = config.setdefault("puerto", 5432)
```
Error típico:
```py
config.setdefault("puerto")
```
Verás esto: `puerto = 5432`.  
Por qué funciona: inserta default cuando falta.  
Lo típico que sale mal: olvidar el default; usarlo sin querer mutar el dict.

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
                "Optional mal usado",
                "Si un valor nunca es None, no lo marques como Optional.",
            ),
            (
                "Any contagioso",
                "Una función que acepta Any propaga el tipo dinámico a todo.",
            ),
            (
                "Default mutable",
                "list/dict como default rompe el tipado y el comportamiento.",
            ),
            (
                "TypeVar sin restricciones",
                "Puede generar resultados demasiado genéricos o inútiles.",
            ),
            (
                "Union excesivo",
                "Unión grande dificulta la lectura y el mantenimiento.",
            ),
            (
                "Usar list en APIs genéricas",
                "Sequence permite pasar tuplas o rangos sin copiar.",
            ),
            (
                "TypedDict incompleto",
                "Si falta una clave obligatoria, el checker no puede validar.",
            ),
            (
                "Protocol no importado",
                "Necesitas typing.Protocol para interfaces estructurales.",
            ),
            (
                "Callable sin firma",
                "Callable sin args ni retorno pierde información útil.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Optional vs Union",
                """from typing import Optional  # Importamos Optional\n+def buscar(nombre: str) -> Optional[int]:  # Definimos función\n+    return 1 if nombre else None  # Retornamos""",
            ),
            (
                "Literal",
                """from typing import Literal  # Importamos Literal\n+def modo(color: Literal["rojo", "azul"]) -> str:  # Definimos función\n+    return color  # Retornamos""",
            ),
            (
                "TypedDict",
                """from typing import TypedDict  # Importamos TypedDict\n+class Usuario(TypedDict):  # Definimos TypedDict\n+    nombre: str  # Campo nombre\n+    edad: int  # Campo edad\n+u: Usuario = {"nombre": "Ana", "edad": 30}  # Creamos dict""",
            ),
            (
                "Protocol",
                """from typing import Protocol  # Importamos Protocol\n+class Escribible(Protocol):  # Definimos Protocol\n+    def escribir(self, texto: str) -> None: ...  # Método requerido""",
            ),
            (
                "Sequence vs list",
                """from typing import Sequence  # Importamos Sequence\n+def total(valores: Sequence[int]) -> int:  # Definimos función\n+    return sum(valores)  # Sumamos""",
            ),
            (
                "Mapping vs dict",
                """from typing import Mapping  # Importamos Mapping\n+def leer(cfg: Mapping[str, str]) -> str:  # Definimos función\n+    return cfg.get("host", "")  # Leemos clave""",
            ),
            (
                "Callable",
                """from typing import Callable  # Importamos Callable\n+def aplicar(x: int, fn: Callable[[int], int]) -> int:  # Definimos función\n+    return fn(x)  # Aplicamos""",
            ),
            (
                "TypeVar",
                """from typing import TypeVar  # Importamos TypeVar\n+T = TypeVar("T")  # Definimos TypeVar\n+def primero(valores: list[T]) -> T:  # Definimos función\n+    return valores[0]  # Retornamos primero""",
            ),
            (
                "Default seguro",
                """from typing import Optional  # Importamos Optional\n+def agregar(item: int, datos: Optional[list[int]] = None) -> list[int]:  # Función\n+    if datos is None:  # Validamos None\n+        datos = []  # Creamos lista\n+    datos.append(item)  # Agregamos\n+    return datos  # Retornamos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Define una función que reciba Sequence[str] y devuelva su longitud.",
                "hints": ["Sequence", "len"],
                "solution": "from typing import Sequence\n\ndef contar(textos: Sequence[str]) -> int:\n    return len(textos)",
            },
            {
                "question": "Crea un TypedDict para un producto con nombre y precio.",
                "hints": ["TypedDict"],
                "solution": "from typing import TypedDict\n\nclass Producto(TypedDict):\n    nombre: str\n    precio: float",
            },
            {
                "question": "Escribe un Protocol llamado Exportable con método exportar().",
                "hints": ["Protocol"],
                "solution": "from typing import Protocol\n\nclass Exportable(Protocol):\n    def exportar(self) -> str: ...",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo textual: ejemplos de firmas buenas y malas."))
        layout.addWidget(
            QLabel(
                "Buen hint: def total(valores: Sequence[int]) -> int\n"
                "Mal hint: def total(valores) -> Any\n"
                "Buen hint: def cargar(cfg: Mapping[str, str]) -> str"
            )
        )
        return widget
