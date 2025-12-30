from __future__ import annotations

from app.lesson_base import Lesson


class RichIntroLesson(Lesson):
    TITLE = "Rich: salida elegante en terminal"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas"
    LEVEL = "Intermedio"
    TAGS = ["rich", "terminal", "cli", "formato", "consola"]

    def summary(self) -> str:
        return (
            "Aprende a usar Rich para imprimir texto con estilo en la terminal, con paneles, "
            "colores y mensajes claros sin perder compatibilidad con Python."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Qué es Rich y por qué usarlo?
Rich es una librería para imprimir texto con **colores, estilos y layouts** en la terminal.
Sirve para hacer CLIs más legibles sin depender de frameworks pesados.

Micro-ejemplo correcto:
```py
from rich import print

print("[bold green]Todo bien[/]")
```

Micro-ejemplo incorrecto:
```py
print = rich.print
```

Error real:
```py
NameError: name 'rich' is not defined
```

Cómo se arregla: importa desde Rich con `from rich import print` o `import rich`.

## Console: el centro de la salida
La clase `rich.console.Console` te permite controlar estilos y salida avanzada.

Micro-ejemplo correcto:
```py
from rich.console import Console

console = Console()
console.print("Mensaje controlado")
```

Micro-ejemplo incorrecto:
```py
from rich.console import Console

console = Console()
console.prnit("Mensaje")
```

Error real:
```py
AttributeError: 'Console' object has no attribute 'prnit'
```

Cómo se arregla: usa el método correcto `console.print(...)`.

## Paneles para destacar información
`rich.panel.Panel` permite encerrar texto en un recuadro con título.

Micro-ejemplo correcto:
```py
from rich.console import Console
from rich.panel import Panel

console = Console()
console.print(Panel("Proceso finalizado", title="Estado"))
```

Micro-ejemplo incorrecto:
```py
from rich.panel import Panel

panel = Panel("Ok")
panel.print()
```

Error real:
```py
AttributeError: 'Panel' object has no attribute 'print'
```

Cómo se arregla: imprime el panel con `console.print(panel)`.

## Ejemplo principal: salida bonita para un resumen de tareas
### 1) Aprende esto
Combina `rich.print` y `Console` para mostrar estados claros y fáciles de leer.

### 2) Haz esto
```py
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

print("[bold cyan]Resumen del día[/]")
console.print(Panel("Tareas completadas: 4", title="OK", border_style="green"))
console.print(Panel("Pendientes: 2", title="Pendiente", border_style="yellow"))
```

### 3) Verás esto
```text
Resumen del día
┌─ OK ───────────────┐
│ Tareas completadas │
│ 4                  │
└────────────────────┘
┌─ Pendiente ────────┐
│ Pendientes: 2      │
└────────────────────┘
```

### 4) Por qué funciona
- `rich.print` interpreta etiquetas como `[bold cyan]` para estilo rápido.
- `Console` imprime objetos Rich (como `Panel`) con bordes y color.
- `Panel` encapsula el texto para que destaque.

### 5) Lo típico que sale mal
1) Olvidar instalar la librería:
```text
ModuleNotFoundError: No module named 'rich'
```

Cómo se arregla: instala con `pip install rich` antes de usarla.

2) Olvidar el cierre de etiqueta:
```py
print("[bold cyan]Resumen")
```
```text
MarkupError: closing tag '[/]' at end of string not found
```

Cómo se arregla: cierra el estilo con `[/]`.

## Ejemplo ampliado con contexto: notificar estado de un proceso
### 1) Aprende esto
Rich te ayuda a destacar qué pasos se completaron y cuáles fallaron.

### 2) Haz esto
```py
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

print("[bold]Deploy[/]")
console.print(Panel("Descarga OK", title="Paso 1", border_style="green"))
console.print(Panel("Migraciones fallaron", title="Paso 2", border_style="red"))
```

### 3) Verás esto
```text
Deploy
┌─ Paso 1 ───────────┐
│ Descarga OK        │
└────────────────────┘
┌─ Paso 2 ───────────┐
│ Migraciones fallaron │
└────────────────────┘
```

### 4) Por qué funciona
`Panel` deja claro el estado visualmente, y los colores resaltan el nivel de urgencia.

### 5) Lo típico que sale mal
1) Crear el panel pero no imprimirlo:
```py
from rich.panel import Panel

panel = Panel("Listo")
```
```text
(no se muestra nada en pantalla)
```

Cómo se arregla: pasa el panel a `console.print(panel)`.

## Ejercicios
1) Imprime un título con `rich.print` usando `[bold magenta]`.
2) Crea un panel con el texto "Carga completa" y título "Estado".
3) Usa dos paneles seguidos para estados OK y ERROR.

## Checklist final
- [ ] Sé cuándo usar `rich.print` vs `console.print`.
- [ ] Puedo crear un `Console` y reutilizarlo.
- [ ] Uso `Panel` para destacar mensajes críticos.
"""
