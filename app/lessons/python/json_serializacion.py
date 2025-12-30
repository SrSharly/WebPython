from __future__ import annotations

from app.lesson_base import Lesson


class JsonSerializacionLesson(Lesson):
    TITLE = "JSON con Python (serialización básica)"
    CATEGORY = "Python"
    SUBCATEGORY = "Datos y formatos"
    LEVEL = "Intermedio"
    BADGES = ["⭐"]
    TAGS = ["json", "serializacion", "api", "archivos", "dict"]

    def summary(self) -> str:
        return (
            "Aprende a convertir dicts y listas a JSON con json.dumps, cargar JSON con "
            "json.loads y guardar archivos correctamente con ejemplos reales."
        )

    def guide(self) -> str:
        return """
⭐ LECCIÓN ESTRELLA

## Qué es JSON y por qué lo verás en todas partes
JSON es un formato de texto para intercambiar datos. Se parece a un dict de Python, pero
usa **comillas dobles** y no acepta todo lo que Python acepta (por ejemplo, sets).

Micro-ejemplo correcto:
```py
import json

datos = {"nombre": "Ana", "tags": ["python", "json"]}
texto = json.dumps(datos)
```

Micro-ejemplo incorrecto:
```py
import json

datos = {"tags": {"python", "json"}}
texto = json.dumps(datos)
```

Error real:
```
TypeError: Object of type set is not JSON serializable
```

Cómo se arregla: convierte el set a lista antes de serializar.

## json.dumps: convertir Python → JSON (texto)
**Aprende esto:** `json.dumps` devuelve un string JSON que puedes guardar o enviar por red.

Micro-ejemplo correcto:
```py
import json

payload = {"ok": True, "cantidad": 3}
texto = json.dumps(payload)
```

Micro-ejemplo incorrecto:
```py
import json

payload = {"ok": True, "cantidad": 3}
texto = json.dumps(payload, indent="dos")
```

Error real:
```
TypeError: '<' not supported between instances of 'str' and 'int'
```

Cómo se arregla: `indent` debe ser un entero (ej. 2) o None.

## json.loads: convertir JSON (texto) → Python
**Aprende esto:** `json.loads` recibe un string JSON válido.

Micro-ejemplo correcto:
```py
import json

texto = '{"nombre": "Ana", "edad": 30}'
datos = json.loads(texto)
```

Micro-ejemplo incorrecto:
```py
import json

texto = "{'nombre': 'Ana'}"
datos = json.loads(texto)
```

Error real:
```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

Cómo se arregla: usa comillas dobles en JSON.

## Ejemplo grande con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** leer un JSON de ventas, calcular un resumen y guardarlo formateado.

**Haz esto (8–25 líneas con contexto):**
```py
from pathlib import Path
import json

ruta = Path("datos/ventas.json")
contenido = ruta.read_text(encoding="utf-8")
ventas = json.loads(contenido)

total = sum(v["monto"] for v in ventas)
resumen = {"total": total, "cantidad": len(ventas)}

salida = Path("salidas/resumen.json")
salida.parent.mkdir(parents=True, exist_ok=True)
salida.write_text(json.dumps(resumen, indent=2, ensure_ascii=False), encoding="utf-8")

print("Resumen guardado.")
```

**Verás esto (salida real):**
```
Resumen guardado.
```

**Por qué funciona:** `read_text()` carga el archivo como texto, `json.loads` lo transforma a
estructuras de Python y `json.dumps` genera un JSON legible con indentación.

**Lo típico que sale mal (con error real):**
```py
contenido = ""
ventas = json.loads(contenido)
```
```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
Solución: valida que el archivo no esté vacío y que tenga JSON válido.

## json.dump / json.load: trabajar directo con archivos
**Aprende esto:** estas funciones leen/escriben sin convertir manualmente a string.

**Micro-ejemplo correcto**
```py
import json

with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump({"ok": True}, archivo, indent=2)
```

**Micro-ejemplo incorrecto**
```py
import json

with open("datos.json", "w", encoding="utf-8") as archivo:
    datos = json.load(archivo)
```

**Error real**
```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Cómo se corrige:** usa `json.load` en un archivo abierto en modo lectura.

## Checklist final
- ¿El JSON usa comillas dobles y tipos válidos (listas/dicts/números)?
- ¿Usaste `json.dumps` para obtener texto y `json.loads` para leerlo?
- ¿Elegiste `json.dump`/`json.load` cuando trabajas con archivos?
- ¿Formateaste con `indent` para que sea legible?
- ¿Controlaste errores de JSON vacío o mal formado?
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir dict de Python con JSON",
                "JSON exige comillas dobles y no acepta sets ni tuples.",
            ),
            (
                "Usar json.loads con strings inválidos",
                "Valida el contenido y controla JSONDecodeError.",
            ),
            (
                "Olvidar encoding en archivos",
                "Usa encoding='utf-8' para evitar caracteres corruptos.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Serializar un dict a JSON",
                """import json

datos = {"producto": "Café", "precio": 4.5}
texto = json.dumps(datos, ensure_ascii=False)
print(texto)""",
            ),
            (
                "Cargar JSON desde texto",
                """import json

texto = '{"items": [1, 2, 3]}'
datos = json.loads(texto)
print(datos["items"])""",
            ),
            (
                "Guardar JSON en archivo",
                """import json

with open("salida.json", "w", encoding="utf-8") as archivo:
    json.dump({"ok": True}, archivo, indent=2)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Convierte una lista de dicts a JSON y guarda el texto en un archivo.",
                "hints": ["Usa json.dumps y write_text con pathlib."],
                "solution": (
                    "import json\n"
                    "from pathlib import Path\n"
                    "datos = [{'producto': 'A', 'precio': 10}, {'producto': 'B', 'precio': 20}]\n"
                    "texto = json.dumps(datos, indent=2, ensure_ascii=False)\n"
                    "Path('salidas').mkdir(parents=True, exist_ok=True)\n"
                    "Path('salidas/datos.json').write_text(texto, encoding='utf-8')"
                ),
            },
            {
                "question": "Lee un JSON con usuarios y muestra cuántos hay.",
                "hints": ["Usa json.loads sobre el texto leído."],
                "solution": (
                    "import json\n"
                    "from pathlib import Path\n"
                    "contenido = Path('usuarios.json').read_text(encoding='utf-8')\n"
                    "usuarios = json.loads(contenido)\n"
                    "print(len(usuarios))"
                ),
            },
            {
                "question": "Usa json.dump para guardar un resumen directamente en un archivo.",
                "hints": ["Abre el archivo en modo 'w'."],
                "solution": (
                    "import json\n"
                    "resumen = {'total': 120, 'cantidad': 4}\n"
                    "with open('resumen.json', 'w', encoding='utf-8') as archivo:\n"
                    "    json.dump(resumen, archivo, indent=2)"
                ),
            },
        ]
