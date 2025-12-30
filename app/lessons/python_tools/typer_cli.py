from __future__ import annotations

from app.lesson_base import Lesson


class TyperCLILesson(Lesson):
    TITLE = "Typer: CLI modernas con tipado"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas"
    LEVEL = "Avanzado"
    TAGS = ["typer", "cli", "argumentos", "opciones", "typing"]

    def summary(self) -> str:
        return (
            "Crea CLIs modernas con Typer: argumentos tipados, opciones claras y ayuda automática, "
            "con ejemplos reales, errores típicos y checklist final."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Qué es Typer y por qué existe?
Typer es una librería para crear **CLIs tipadas** (líneas de comandos) usando anotaciones de
Python. Genera ayuda automática, valida tipos y permite construir comandos reales con poco
código.

Micro-ejemplo correcto:
```py
import typer

app = typer.Typer()
```

Micro-ejemplo incorrecto:
```py
app = Typer()
```

Error real:
```py
NameError: name 'Typer' is not defined
```

Cómo se arregla: importa `typer` y usa `typer.Typer()`.

## Comando mínimo con Typer
Micro-ejemplo correcto:
```py
import typer

app = typer.Typer()

@app.command()
def saluda(nombre: str):
    print(f"Hola, {nombre}")
```

Micro-ejemplo incorrecto:
```py
@app.command
```

Error real:
```py
TypeError: command() missing 1 required positional argument: 'name'
```

Cómo se arregla: usa el decorador con paréntesis `@app.command()`.

## Argumentos vs opciones
- **Argumento**: posición obligatoria.
- **Opción**: va con `--bandera` y puede ser opcional.

Micro-ejemplo correcto:
```py
import typer

app = typer.Typer()

@app.command()
def crear(nombre: str, verbose: bool = typer.Option(False, "--verbose")):
    if verbose:
        print("Modo verbose")
    print(f"Creado: {nombre}")
```

Micro-ejemplo incorrecto:
```py
verbose = typer.Option
```

Error real:
```py
TypeError: Option() missing 1 required positional argument: 'default'
```

Cómo se arregla: usa `typer.Option(valor_por_defecto, ...)`.

## Ejemplo principal: CLI real con argumentos, opciones y validación
### 1) Aprende esto
Typer usa tipos para validar entradas y documentar comandos con ayuda automática.

### 2) Haz esto
```py
import typer

app = typer.Typer()

@app.command()
def calcular(total: float, personas: int = typer.Argument(..., min=1)):
    """Divide un total entre personas con validación mínima."""
    resultado = total / personas
    typer.echo(f"Total por persona: {resultado:.2f}")

@app.command()
def registrar(nombre: str, ciudad: str = typer.Option("Lima", "--ciudad")):
    typer.echo(f"Registro: {nombre} ({ciudad})")

if __name__ == "__main__":
    app()
```

### 3) Verás esto
```text
$ python app.py calcular 100 4
Total por persona: 25.00
```

### 4) Por qué funciona
- `typer.Argument(..., min=1)` valida que `personas` sea al menos 1.
- `typer.Option(...)` crea una bandera opcional con valor por defecto.
- `typer.echo(...)` imprime con compatibilidad extra para CLI.

### 5) Lo típico que sale mal
1) Pasar texto donde se espera número:
```text
$ python app.py calcular cien 4
```
```text
Error: Invalid value for 'TOTAL': 'cien' is not a valid float
```

2) Olvidar el argumento obligatorio:
```text
$ python app.py calcular 100
```
```text
Error: Missing argument 'PERSONAS'
```

Cómo se arregla: respeta tipos y argumentos obligatorios.

## Ejemplo ampliado con contexto: subcomandos y opciones de salida
### 1) Aprende esto
Los subcomandos permiten CLIs más grandes sin perder claridad.

### 2) Haz esto
```py
import json
import typer

app = typer.Typer()

@app.command()
def exportar(nombre: str, formato: str = typer.Option("txt", "--formato")):
    datos = {"nombre": nombre, "estado": "activo"}
    if formato == "json":
        typer.echo(json.dumps(datos, ensure_ascii=False))
    else:
        typer.echo(f"{datos['nombre']} - {datos['estado']}")

if __name__ == "__main__":
    app()
```

### 3) Verás esto
```text
$ python app.py exportar Ada --formato json
{"nombre": "Ada", "estado": "activo"}
```

### 4) Por qué funciona
`typer.Option` valida el argumento `--formato` y el comando `exportar` queda aislado,
lo que hace la CLI extensible sin duplicar lógica.

### 5) Lo típico que sale mal
1) Escribir una opción no reconocida:
```text
$ python app.py exportar Ada --formatoo json
```
```text
Error: no such option: --formatoo
```

Cómo se arregla: usa el nombre exacto de la opción.

## Errores típicos rápidos
- Usar `print(...)` en lugar de `typer.echo(...)` y perder consistencia de salida.
- Mezclar lógica compleja en el comando en vez de extraer funciones.
- Olvidar `if __name__ == "__main__": app()` y no tener punto de entrada.

## Ejercicios
1) Agrega una opción `--moneda` con valor por defecto.
2) Crea un subcomando `estado` que muestre si una tarea está activa.
3) Añade validación para que el nombre tenga al menos 3 caracteres.

## Checklist final
- [ ] Uso `typer.Typer()` para definir mi app.
- [ ] Distingo argumentos obligatorios de opciones.
- [ ] Aprovecho tipos y validaciones para errores claros.
"""
