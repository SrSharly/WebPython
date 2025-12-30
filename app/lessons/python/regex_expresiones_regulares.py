from __future__ import annotations

from app.lesson_base import Lesson


class RegexExpresionesRegularesLesson(Lesson):
    TITLE = "Regex y expresiones regulares"
    CATEGORY = "Python"
    SUBCATEGORY = "Texto y datos"
    LEVEL = "Avanzado"
    TAGS = ["regex", "re", "texto", "validación", "búsqueda"]

    def summary(self) -> str:
        return (
            "Aprende a buscar, validar y extraer texto con regex usando el módulo re, "
            "con ejemplos claros, errores típicos y patrones reales."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
🧠 LECCIÓN PRO

## Qué son las expresiones regulares
Una expresión regular (regex) es un patrón que describe texto. Sirve para **buscar**, **validar**
formato y **extraer** partes de cadenas. En Python se usan con el módulo `re`.

Micro-ejemplo correcto:
```py
import re

texto = "Pedido #1234"
hay_numero = re.search(r"\d+", texto) is not None
```

Micro-ejemplo incorrecto:
```py
import re

re.search("(", "hola")
```

Error real:
```py
re.error: missing ), unterminated subpattern at position 0
```

Cómo se arregla: cierra los paréntesis o escapa el carácter si lo quieres literal.

## Sintaxis mínima que debes reconocer
- `\d` = dígito
- `+` = uno o más
- `.` = cualquier carácter
- `^` = inicio de texto
- `$` = fin de texto

Micro-ejemplo correcto:
```py
import re

patron = r"^\d{4}$"
re.search(patron, "2024")
```

Micro-ejemplo incorrecto:
```py
import re

patron = r"^\d{4}$"
re.search(patron, "2024a")
```

Error real:
```py
TypeError: 'NoneType' object is not subscriptable
```

Cómo se arregla: valida el resultado antes de usarlo porque `re.search` puede devolver `None`.

## Escapar caracteres y usar raw strings
El punto `.` coincide con cualquier carácter. Si quieres un punto literal, debes escaparlo.
Usa raw strings (`r""`) para no duplicar escapes.

Micro-ejemplo correcto:
```py
import re

texto = "v1.2"
patron = r"\."
coincidencia = re.search(patron, texto)
```

Micro-ejemplo incorrecto:
```py
import re

texto = "v1.2"
patron = r"\."
coincidencia = re.search(patron)
```

Error real:
```py
TypeError: search() missing 1 required positional argument: 'string'
```

Cómo se arregla: pasa siempre el texto donde buscar la coincidencia.

## Ejemplo principal: extraer datos de un log
### 1) Aprende esto
Extraer partes de texto con grupos para convertir líneas “planas” en datos útiles.

### 2) Haz esto
```py
import re

linea = "INFO 2024-06-02 usuario=ana accion=login"
patron = r"^(INFO|ERROR) (\d{4}-\d{2}-\d{2}) usuario=(\w+) accion=(\w+)"

coincidencia = re.search(patron, linea)
if coincidencia:
    nivel = coincidencia.group(1)
    fecha = coincidencia.group(2)
    usuario = coincidencia.group(3)
    accion = coincidencia.group(4)
    print(nivel, fecha, usuario, accion)
```

### 3) Verás esto
```text
INFO 2024-06-02 ana login
```

### 4) Por qué funciona
El patrón usa grupos `(...)` para capturar partes específicas. `re.search` devuelve un objeto
coincidencia con los grupos accesibles por índice usando `group(n)`.

### 5) Lo típico que sale mal
1) Olvidar verificar `None`:
```py
coincidencia = re.search(patron, linea)
print(coincidencia.group(1))
```
```py
AttributeError: 'NoneType' object has no attribute 'group'
```

2) Usar un patrón demasiado estricto:
```py
patron = r"^ERROR (\d{4}-\d{2}-\d{2})"
coincidencia = re.search(patron, linea)
```
```py
AttributeError: 'NoneType' object has no attribute 'group'
```

## Buscar todas las coincidencias con re.findall
`re.findall` devuelve una lista con todas las coincidencias del patrón.

Micro-ejemplo correcto:
```py
import re

texto = "IDs: A12, B34, C56"
ids = re.findall(r"[A-Z]\d{2}", texto)
```

Micro-ejemplo incorrecto:
```py
import re

ids = re.findall(r"[A-Z]\d{2}")
```

Error real:
```py
TypeError: findall() missing 1 required positional argument: 'string'
```

Cómo se arregla: pasa siempre el texto como segundo argumento.

## Compilar patrones cuando se reutilizan
Si vas a usar el mismo patrón muchas veces, compílalo una vez.

Micro-ejemplo correcto:
```py
import re

patron = re.compile(r"\b\w+\b")
resultado = patron.findall("hola mundo")
```

Micro-ejemplo incorrecto:
```py
import re

patron = re.compile(r"\b\w+\b")
resultado = patron.findall()
```

Error real:
```py
TypeError: findall() missing 1 required positional argument: 'string'
```

Cómo se arregla: pasa el texto al método `findall` del patrón compilado.

## Ejemplo ampliado con contexto: validar IDs y extraer el número
### 1) Aprende esto
Combina validación con extracción usando un patrón compilado y un chequeo explícito.

### 2) Haz esto
```py
import re

patron = re.compile(r"^ID-(\d{3})$")
ids = ["ID-007", "ID-42", "ID-123"]

for item in ids:
    coincidencia = re.search(patron, item)
    if coincidencia:
        numero = coincidencia.group(1)
        print(f"Válido: {numero}")
    else:
        print(f"Inválido: {item}")
```

### 3) Verás esto
```text
Válido: 007
Inválido: ID-42
Válido: 123
```

### 4) Por qué funciona
El patrón exige exactamente tres dígitos. `re.search` devuelve `None` si no coincide, y
`group(1)` extrae el bloque numérico capturado cuando sí hay match.

### 5) Lo típico que sale mal
1) Usar `group(1)` sin comprobar `None`:
```py
coincidencia = re.search(patron, "ID-42")
print(coincidencia.group(1))
```
```py
AttributeError: 'NoneType' object has no attribute 'group'
```

## Errores típicos rápidos
- Usar regex para todo cuando `str.split` o `in` sería suficiente.
- Olvidar que `.` no incluye saltos de línea a menos que uses `re.DOTALL`.
- No escapar caracteres especiales como `.` o `?` cuando quieres literal.

## Ejercicios
1) Valida un código postal de 5 dígitos con `^\d{5}$`.
2) Extrae todos los hashtags de un texto usando `#\w+`.
3) Captura nombre y dominio de un email con `([^@]+)@([^@]+)`.

## Checklist final
- [ ] Sé cuándo usar `re.search` vs `re.findall`.
- [ ] Verifico `None` antes de usar `group()`.
- [ ] Compilo patrones si los reutilizo muchas veces.
"""
