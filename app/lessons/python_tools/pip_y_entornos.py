from __future__ import annotations

from app.lesson_base import Lesson


class PipEntornosLesson(Lesson):
    TITLE = "Pip y entornos virtuales (venv)"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas"
    LEVEL = "Intermedio"
    BADGES = ["🧠"]
    TAGS = ["pip", "venv", "entornos", "dependencias", "requirements"]

    def summary(self) -> str:
        return (
            "Aprende a aislar dependencias con entornos virtuales, instalar paquetes con pip "
            "y mantener un requirements.txt limpio para que tu proyecto sea reproducible."
        )

    def guide(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Por qué usar entornos virtuales?
Un entorno virtual aísla las dependencias de cada proyecto. Así evitas conflictos entre
versiones y haces tu proyecto reproducible.

Micro-ejemplo correcto:
```bash
python -m venv .venv
```

Micro-ejemplo incorrecto:
```bash
python -m venv
```

Error real:
```text
error: the following arguments are required: ENV_DIR
```

Cómo se arregla: indica la carpeta destino, por ejemplo `.venv`.

## Activar el entorno (paso obligatorio)
Si no activas, puedes terminar instalando paquetes en el Python global.

Micro-ejemplo correcto (macOS/Linux):
```bash
source .venv/bin/activate
```

Micro-ejemplo incorrecto (ruta de otro sistema):
```bash
source .venv\\Scripts\\activate
```

Error real:
```text
bash: .venv\\Scripts\\activate: No such file or directory
```

Cómo se arregla: usa la ruta correcta según tu sistema operativo.

## Instalar paquetes con pip
Instala siempre con `python -m pip` para asegurarte de usar el pip del entorno.

Micro-ejemplo correcto:
```bash
python -m pip install requests
```

Micro-ejemplo incorrecto:
```bash
python -m pip install reqests
```

Error real:
```text
ERROR: Could not find a version that satisfies the requirement reqests
```

Cómo se arregla: revisa el nombre real del paquete en PyPI.

## Guardar dependencias en requirements.txt
Esto permite que otra persona instale exactamente lo mismo en otra máquina.

Micro-ejemplo correcto:
```bash
python -m pip freeze > requirements.txt
```

Micro-ejemplo incorrecto:
```bash
python -m pip freze > requirements.txt
```

Error real:
```text
ERROR: unknown command "freze"
```

Cómo se arregla: el comando correcto es `freeze`.

## Ejemplo principal con contexto
**Aprende esto:** crear un entorno limpio, instalar dependencias y documentarlas.

**Haz esto (8–25 líneas con contexto):**
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install requests pandas
python -m pip list
python -m pip freeze > requirements.txt
```

**Verás esto (salida real):**
```text
Package    Version
---------- -------
pandas     2.2.2
requests   2.32.3
```

**Por qué funciona**
`venv` crea un entorno aislado; al activarlo, `python -m pip` instala paquetes dentro de
esa carpeta. `pip freeze` genera un listado reproducible.

**Lo típico que sale mal (errores reales + mensajes):**
```bash
pip install -r requirements.txt
```
```text
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```
Solución: verifica que el archivo exista y que estés en la carpeta correcta.

## Checklist final (antes de compartir tu proyecto)
- ¿El entorno virtual existe y está activado?
- ¿Las dependencias están en `requirements.txt`?
- ¿Puedes recrear el entorno desde cero en otra carpeta?
""".strip()
