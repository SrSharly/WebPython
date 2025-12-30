from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QComboBoxLesson(Lesson):
    TITLE = "QComboBox"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QComboBox", "select", "items", "signals"]

    def summary(self) -> str:
        return (
            "QComboBox permite seleccionar un valor de una lista. Aprende a poblarla, "
            "escuchar cambios y permitir entradas personalizadas."
        )

    def guide(self) -> str:
        return """
## Qué es
QComboBox es un selector desplegable que permite elegir una opción de una lista.

## Cuándo se usa
Cuando hay pocas opciones posibles y quieres ahorrar espacio en pantalla.

## Conceptos previos
- Widgets básicos y layouts.
- Señales en PySide6.

## Paso 1: Crear y poblar el combo
```
combo = QComboBox()
combo.addItems(["Rojo", "Verde", "Azul"])
```

## Paso 2: Leer la selección
```
texto = combo.currentText()
```

## Paso 3: Escuchar cambios
```
combo.currentIndexChanged.connect(lambda _: print(combo.currentText()))
```

## Paso 4: Permitir edición
```
combo.setEditable(True)
```

## Operaciones y métodos más útiles
### QComboBox
1) `addItems()` ⭐  
Qué hace: agrega varios items.  
Así se escribe:
```py
combo.addItems(["Rojo", "Verde"])
```
Error típico:
```py
combo.addItems("Rojo")
```
Verás esto: opciones en la lista.  
Por qué funciona: espera un iterable de strings.  
Lo típico que sale mal: pasar string y separar letras; olvidar limpiar antes de recargar.

2) `currentText()` ⭐  
Qué hace: devuelve el texto seleccionado.  
Así se escribe:
```py
texto = combo.currentText()
```
Error típico:
```py
texto = combo.currentText
```
Verás esto: la opción actual.  
Por qué funciona: lee el estado del combo.  
Lo típico que sale mal: olvidar paréntesis; asumir que devuelve índice.

3) `currentIndexChanged.connect()` ⭐  
Qué hace: reacciona a cambios de selección.  
Así se escribe:
```py
combo.currentIndexChanged.connect(lambda _: print(combo.currentText()))
```
Error típico:
```py
combo.currentIndexChanged.connect(print())
```
Verás esto: acción al cambiar.  
Por qué funciona: conecta la señal a un slot.  
Lo típico que sale mal: ejecutar la función al conectar; ignorar el argumento índice.

4) `setEditable()`  
Qué hace: permite escribir texto.  
Así se escribe:
```py
combo.setEditable(True)
```
Error típico:
```py
combo.setEditable("True")
```
Verás esto: combo editable.  
Por qué funciona: activa modo editable.  
Lo típico que sale mal: pasar string; no validar el texto ingresado.

5) `findText()`  
Qué hace: busca el índice de un texto.  
Así se escribe:
```py
indice = combo.findText("Verde")
```
Error típico:
```py
indice = combo.findText
```
Verás esto: índice o -1.  
Por qué funciona: recorre los items.  
Lo típico que sale mal: olvidar paréntesis; no manejar -1.

6) `setCurrentIndex()`  
Qué hace: selecciona por índice.  
Así se escribe:
```py
combo.setCurrentIndex(0)
```
Error típico:
```py
combo.setCurrentIndex("0")
```
Verás esto: selección actualizada.  
Por qué funciona: usa índice entero.  
Lo típico que sale mal: pasar string; índice fuera de rango.

7) `clear()`  
Qué hace: elimina todos los items.  
Así se escribe:
```py
combo.clear()
```
Error típico:
```py
combo.clear
```
Verás esto: combo vacío.  
Por qué funciona: limpia la lista interna.  
Lo típico que sale mal: olvidar paréntesis; limpiar sin repoblar.

## Mini-reto
Mini-reto 1: Agrega un elemento “Otro” si el usuario escribe algo nuevo.
Solución:
```
combo.setEditable(True)
combo.editTextChanged.connect(lambda t: combo.addItem(t) if combo.findText(t) == -1 else None)
```

## Errores típicos (mal vs bien)
Mal: usar índices mágicos.
```
combo.setCurrentIndex(2)
```
Bien: buscar por texto o data.
```
indice = combo.findText("Verde")
combo.setCurrentIndex(indice)
```

## Nota
Nota: usa setPlaceholderText para indicar qué debe elegir el usuario.

## Advertencia
Advertencia: si el combo es editable, valida la entrada escrita.

## Checklist final
- Creo un QComboBox y agrego items.
- Leo la opción seleccionada.
- Escucho cambios con señales.
- Habilito edición cuando aplica.

## Ver también
- QLineEdit
- QLabel
- QPushButton


## Micro-ejemplo incremental: widgets y ciclo de eventos

### Así se escribe
```py
app = QApplication([])
label = QLabel("Hola Qt")
label.show()
app.exec()
```

### Error típico: crear un widget antes de QApplication
```py
label = QLabel("Hola Qt")
app = QApplication([])
```

```py
QWidget: Must construct a QApplication before a QWidget
```

Explicación breve: el motor de Qt necesita `QApplication` antes de cualquier widget.

### Error típico: olvidar mostrar el widget
```py
app = QApplication([])
label = QLabel("Hola Qt")
app.exec()
```

```py
(no window appears)
```

Explicación breve: si no llamas a `show()`, el widget no se pinta en pantalla.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Lista vacía",
                "Si no agregas items, el combo se ve vacío; usa addItems().",
            ),
            (
                "No manejar cambios",
                "Sin currentIndexChanged no reaccionas a selección.",
            ),
            (
                "Editable sin validar",
                "Si habilitas escritura, valida el texto ingresado.",
            ),
            (
                "Usar índices mágicos",
                "Si cambian los items, los índices cambian; usa texto o data.",
            ),
            (
                "No definir selección inicial",
                "El usuario puede ver una opción incorrecta; setCurrentIndex.",
            ),
            (
                "No limpiar",
                "Al recargar datos, usa clear() para evitar duplicados.",
            ),
            (
                "Items duplicados",
                "Dificultan la selección; controla el contenido antes de agregar.",
            ),
            (
                "No mostrar placeholder",
                "Sin hint, el usuario no entiende qué elegir.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Agregar items",
                """combo = QComboBox()  # Creamos el combo
combo.addItems(["Rojo", "Verde", "Azul"])  # Agregamos opciones""",
            ),
            (
                "Leer selección",
                """combo = QComboBox()  # Creamos el combo
print(combo.currentText())  # Leemos el texto""",
            ),
            (
                "Señal de cambio",
                """combo = QComboBox()  # Creamos el combo
combo.currentIndexChanged.connect(print)  # Conectamos señal""",
            ),
            (
                "Editable",
                """combo = QComboBox()  # Creamos el combo
combo.setEditable(True)  # Permitimos escritura""",
            ),
            (
                "Agregar con data",
                """combo = QComboBox()  # Creamos el combo
combo.addItem("Lima", "PE-LIM")  # Agregamos texto y data""",
            ),
            (
                "Insertar al inicio",
                """combo = QComboBox()  # Creamos el combo
combo.insertItem(0, "Selecciona...")  # Insertamos al inicio""",
            ),
            (
                "Eliminar item",
                """combo = QComboBox()  # Creamos el combo
combo.removeItem(2)  # Eliminamos el tercer item""",
            ),
            (
                "Seleccionar índice",
                """combo = QComboBox()  # Creamos el combo
combo.setCurrentIndex(1)  # Seleccionamos el índice""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QComboBox con tres colores.",
                "hints": ["Usa addItems"],
                "solution": "combo = QComboBox()\ncombo.addItems(['Rojo', 'Verde', 'Azul'])",
            },
            {
                "question": "Muestra en consola la opción seleccionada cuando cambie.",
                "hints": ["currentIndexChanged"],
                "solution": "combo = QComboBox()\ncombo.currentIndexChanged.connect(lambda: print(combo.currentText()))",
            },
            {
                "question": "Permite escritura y lee el texto editado.",
                "hints": ["setEditable", "editTextChanged"],
                "solution": "combo = QComboBox()\ncombo.setEditable(True)\ncombo.editTextChanged.connect(print)",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        title = QLabel("Demo: selección y edición en QComboBox.")
        status = QLabel("Selecciona una opción")

        combo = QComboBox()
        combo.setPlaceholderText("Elige una fruta")
        combo.addItems(["Manzana", "Banana", "Cereza"])

        add_btn = QPushButton("Agregar 'Mango'")
        edit_btn = QPushButton("Hacer editable")

        def update_status() -> None:
            status.setText(f"Actual: {combo.currentText()}")

        def add_item() -> None:
            if combo.findText("Mango") == -1:
                combo.addItem("Mango")
            update_status()

        def make_editable() -> None:
            combo.setEditable(True)
            status.setText("Editable: escribe una opción")

        combo.currentIndexChanged.connect(lambda _: update_status())
        combo.editTextChanged.connect(lambda text: status.setText(f"Editable: {text}"))
        add_btn.clicked.connect(add_item)
        edit_btn.clicked.connect(make_editable)

        layout.addWidget(title)
        layout.addWidget(combo)
        layout.addWidget(status)
        layout.addWidget(add_btn)
        layout.addWidget(edit_btn)
        return widget
