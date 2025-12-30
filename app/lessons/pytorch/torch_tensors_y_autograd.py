from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class TorchTensorsAutogradLesson(Lesson):
    TITLE = "Tensors y autograd"
    CATEGORY = "PyTorch"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["tensors", "autograd", "pytorch", "gradientes"]

    def summary(self) -> str:
        return (
            "PyTorch usa tensors para computación numérica y autograd para "
            "diferenciación automática. Aprende a crear tensores y calcular gradientes."
        )

    def guide(self) -> str:
        return """
- torch.tensor crea tensores desde listas.
- Usa dtype para controlar precisión.
- requires_grad=True habilita autograd.
- backward() calcula gradientes.
- Los gradientes se almacenan en tensor.grad.
- Usa torch.no_grad() para inferencia.
- Zero_grad limpia gradientes acumulados.
- Operaciones son vectorizadas y rápidas.
- Usa .item() para convertir a número Python.
- Los tensores pueden estar en CPU o GPU.
- Usa torch.cuda.is_available() para comprobar GPU.
- autograd construye un grafo dinámico en cada forward.

## Operaciones y métodos más útiles
### Tensores (PyTorch)
1) `.shape` ⭐  
Qué hace: devuelve la forma del tensor.  
Así se escribe:
```py
t = torch.tensor([[1, 2], [3, 4]])
forma = t.shape
```
Error típico:
```py
forma = t.shape()
```
Verás esto: `torch.Size([2, 2])`.  
Por qué funciona: `shape` es un atributo.  
Lo típico que sale mal: llamarlo como función; asumir orden distinto.

2) `.dtype` ⭐  
Qué hace: muestra el tipo de datos.  
Así se escribe:
```py
t = torch.tensor([1, 2])
tipo = t.dtype
```
Error típico:
```py
tipo = t.dtype()
```
Verás esto: `torch.int64`.  
Por qué funciona: `dtype` es atributo.  
Lo típico que sale mal: mezclar tipos sin convertir; asumir float por defecto.

3) `.to(device)` ⭐  
Qué hace: mueve el tensor a CPU/GPU.  
Así se escribe:
```py
device = "cuda" if torch.cuda.is_available() else "cpu"
t = t.to(device)
```
Error típico:
```py
t = t.to("gpu")
```
Verás esto: tensor en el dispositivo indicado.  
Por qué funciona: PyTorch reconoce "cpu"/"cuda".  
Lo típico que sale mal: usar string inválido; mezclar tensores en dispositivos distintos.

4) `.backward()` ⭐  
Qué hace: calcula gradientes.  
Así se escribe:
```py
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2
y.backward()
```
Error típico:
```py
y = x * 2
y.backward()
```
Verás esto: `x.grad` con el gradiente.  
Por qué funciona: autograd recorre el grafo.  
Lo típico que sale mal: usar en tensor no escalar; olvidar `requires_grad=True`.

5) `torch.no_grad()` ⭐  
Qué hace: desactiva gradientes temporalmente.  
Así se escribe:
```py
with torch.no_grad():
    y = x * 2
```
Error típico:
```py
torch.no_grad()
y = x * 2
```
Verás esto: operaciones sin gradientes.  
Por qué funciona: el contexto desactiva autograd.  
Lo típico que sale mal: olvidar el bloque `with`; esperar gradientes después.

6) `.item()`  
Qué hace: convierte tensor escalar a número Python.  
Así se escribe:
```py
valor = x.item()
```
Error típico:
```py
valor = x.item
```
Verás esto: número Python.  
Por qué funciona: extrae el valor escalar.  
Lo típico que sale mal: usarlo en tensores no escalares; olvidar paréntesis.

7) `zero_grad()`  
Qué hace: limpia gradientes del optimizador.  
Así se escribe:
```py
optimizer.zero_grad()
```
Error típico:
```py
optimizer.zero_grad
```
Verás esto: gradientes reiniciados.  
Por qué funciona: evita acumulación.  
Lo típico que sale mal: olvidar llamarlo; limpiar después del backward.

## Micro-ejemplo: `backward` necesita un escalar

### Así se escribe
```py
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x * 3
y.backward()
print(x.grad)
```

### Error típico: salida no escalar
```py
import torch

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = x * 2
y.backward()
```

```py
RuntimeError: grad can be implicitly created only for scalar outputs
```

Explicación breve: usa `y.sum().backward()` cuando el resultado es un vector.


## Micro-ejemplo incremental: tensores y gradientes

### Así se escribe
```py
import torch

x = torch.tensor([2.0], requires_grad=True)
y = x * 3
z = y.sum()
z.backward()
print(x.grad)
```

### Error típico: backward en tensor no escalar
```py
import torch

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = x * 2
y.backward()
```

```py
RuntimeError: grad can be implicitly created only for scalar outputs
```

Explicación breve: usa `y.sum()` o pasa `gradient` a `backward()`.

### Error típico: mezclar tipos sin convertir
```py
import torch

t = torch.tensor([1, 2])
resultado = t + 0.5
```

```py
RuntimeError: expected scalar type Float but found Long
```

Explicación breve: convierte a `float()` antes de operar con decimales.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar zero_grad",
                "Los gradientes se acumulan por defecto.",
            ),
            (
                "No usar no_grad",
                "En inferencia, se gasta memoria sin necesidad.",
            ),
            (
                "Modificar tensor en-place",
                "Puede romper el grafo de autograd.",
            ),
            (
                "Usar .data",
                "Puede causar errores silenciosos; evita usar .data.",
            ),
            (
                "No fijar dtype",
                "Mezclar float32/float64 puede ser costoso.",
            ),
            (
                "No mover a GPU",
                "Si hay GPU disponible, olvidarla reduce rendimiento.",
            ),
            (
                "Comparar tensores",
                "Usa torch.allclose para floats.",
            ),
            (
                "Gradientes None",
                "Si no hay requires_grad, grad será None.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear tensor",
                """import torch\n\nx = torch.tensor([1.0, 2.0, 3.0])\nprint(x)""",
            ),
            (
                "requires_grad",
                """x = torch.tensor([1.0, 2.0], requires_grad=True)""",
            ),
            (
                "Backward",
                """x = torch.tensor([2.0], requires_grad=True)\ny = x ** 2\ny.backward()\nprint(x.grad)""",
            ),
            (
                "No grad",
                """with torch.no_grad():\n    y = x * 2""",
            ),
            (
                "Zero grad",
                """optimizer.zero_grad()""",
            ),
            (
                "Mover a GPU",
                """device = "cuda" if torch.cuda.is_available() else "cpu"\nx = x.to(device)""",
            ),
            (
                "item()",
                """valor = x.item()""",
            ),
            (
                "Operación vectorizada",
                """x = torch.arange(0, 5)\nprint(x * 2)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un tensor 2x2 con requires_grad=True.",
                "hints": ["torch.tensor"],
                "solution": "x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)",
            },
            {
                "question": "Calcula el gradiente de y = x^3 para x=2.",
                "hints": ["y.backward()"],
                "solution": "x = torch.tensor([2.0], requires_grad=True)\ny = x ** 3\ny.backward()\nprint(x.grad)",
            },
            {
                "question": "¿Para qué sirve torch.no_grad()?",
                "hints": ["Inferencia"],
                "solution": "Desactiva autograd para ahorrar memoria y acelerar inferencia.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["torch"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("torch")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok:
            layout.addWidget(QLabel(message or "PyTorch no disponible."))
            return widget

        import torch

        x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
        y = (x * 2).sum()
        y.backward()
        layout.addWidget(QLabel("Demo: gradientes calculados sobre un tensor."))
        layout.addWidget(QLabel(f"Gradientes: {x.grad.tolist()}"))
        return widget
