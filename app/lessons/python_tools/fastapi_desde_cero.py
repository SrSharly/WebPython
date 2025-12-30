from __future__ import annotations

from app.lesson_base import Lesson


class FastAPIDesdeCeroLesson(Lesson):
    TITLE = "FastAPI desde cero: primeros endpoints"
    CATEGORY = "Python"
    SUBCATEGORY = "Web / APIs"
    LEVEL = "Avanzado"
    BADGES = ["⭐", "🧠"]
    TAGS = ["fastapi", "apis", "web", "http", "pydantic"]

    def summary(self) -> str:
        return (
            "Construye tu primera API con FastAPI: crea la app, define endpoints "
            "GET/POST, valida datos con modelos y evita errores típicos."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
⭐🧠 LECCIÓN PRO

## ¿Qué es FastAPI y cuándo usarlo?
FastAPI es un framework moderno para crear APIs rápidas con validación automática.
Es ideal cuando necesitas endpoints claros, tipados y con documentación automática.

Micro-ejemplo correcto:
```py
from fastapi import FastAPI

app = FastAPI()
```

Micro-ejemplo incorrecto:
```py
from fastapi import FastAPI

app = FastApi()
```

Error real:
```py
NameError: name 'FastApi' is not defined
```

Cómo se arregla: respeta la clase `FastAPI` con mayúsculas exactas.

## Endpoint GET: responder texto o JSON
Un endpoint GET se define con `@app.get("/ruta")`.

Micro-ejemplo correcto:
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
def saludo():
    return {"mensaje": "Hola"}
```

Micro-ejemplo incorrecto:
```py
@app.get
def saludo():
    return {"mensaje": "Hola"}
```

Error real:
```py
TypeError: get() missing 1 required positional argument: 'path'
```

Cómo se arregla: usa el decorador con paréntesis y ruta.

## Endpoint POST con validación (pydantic.BaseModel)
Los modelos de Pydantic validan tipos automáticamente.

Micro-ejemplo correcto:
```py
from pydantic import BaseModel

class Pedido(BaseModel):
    producto: str
    cantidad: int
```

Micro-ejemplo incorrecto:
```py
from pydantic import BaseModel

class Pedido(BaseModel):
    cantidad: int

Pedido(cantidad="dos")
```

Error real:
```py
pydantic.error_wrappers.ValidationError: 1 validation error for Pedido
cantidad
  value is not a valid integer (type=type_error.integer)
```

Cómo se arregla: envía `cantidad` como entero.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** crear una API mínima con GET, POST y validación de datos.

**Haz esto (código con contexto):**
```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int

@app.get("/estado")
def estado():
    return {"ok": True}

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {"mensaje": f"Usuario {usuario.nombre} creado", "edad": usuario.edad}
```

**Verás esto (salida real):**
```
GET /estado -> {"ok": true}
POST /usuarios {"nombre":"Ada","edad":30} -> {"mensaje":"Usuario Ada creado","edad":30}
```

**Por qué funciona:** `fastapi.FastAPI` crea la app, `app.get` y `app.post`
registran rutas, y `pydantic.BaseModel` valida tipos antes de ejecutar la función.

**Lo típico que sale mal (con error real):**
```py
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {"mensaje": usuario.nombre, "edad": usuario.edad}
```
Si envías `edad` como texto:
```
pydantic.error_wrappers.ValidationError: 1 validation error for Usuario
edad
  value is not a valid integer (type=type_error.integer)
```
Solución: manda `edad` como número.

## Ejecutar la app con Uvicorn
Puedes ejecutar la app con `uvicorn.run(...)` en desarrollo.

Micro-ejemplo correcto:
```py
import uvicorn

uvicorn.run("main:app", reload=True)
```

Micro-ejemplo incorrecto:
```py
uvicorn.run(main.app)
```

Error real:
```py
NameError: name 'main' is not defined
```

Cómo se arregla: pasa el módulo como string `"main:app"` o importa `main`.

## Errores típicos rápidos
- Definir rutas sin el decorador (`@app.get` / `@app.post`) y esperar que funcionen.
- Confundir tipos en modelos y recibir `ValidationError`.
- No usar `reload=True` en desarrollo y creer que los cambios no aplican.

## Ejercicios
1) Crea un endpoint `GET /ping` que devuelva `{"pong": True}`.
2) Crea un modelo `Producto` con `nombre: str` y `precio: float`.
3) Agrega un `POST /productos` que devuelva el producto recibido.

## Checklist final
- [ ] Sé crear una app con `fastapi.FastAPI`.
- [ ] Distingo rutas GET y POST con `app.get` / `app.post`.
- [ ] Uso `pydantic.BaseModel` para validar datos.
- [ ] Puedo ejecutar la app con `uvicorn.run`.
"""
