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
