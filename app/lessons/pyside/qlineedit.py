from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QLineEditLesson(Lesson):
    TITLE = "QLineEdit"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QLineEdit", "inputs", "signals", "validacion"]

    def summary(self) -> str:
        return (
            "QLineEdit permite capturar texto del usuario. Aprende señales, validación "
            "y formatos para crear formularios robustos."
        )

    def guide(self) -> str:
        return """
## Qué es
QLineEdit es un campo de texto de una sola línea para entradas cortas como nombres, emails o contraseñas.

## Cuándo se usa
En formularios, barras de búsqueda y cualquier entrada de texto breve.

## Conceptos previos
- Señales básicas en PySide6.
- Uso de layouts para ordenar widgets.

## Paso 1: Crear un QLineEdit
```
line = QLineEdit()
```

## Paso 2: Ayudar al usuario con placeholder
```
line.setPlaceholderText("Nombre")
```

## Paso 3: Escuchar cambios de texto
```
line.textChanged.connect(lambda text: print(text))
```

## Paso 4: Capturar Enter
```
line.returnPressed.connect(lambda: print(line.text()))
```

## Paso 5: Modo contraseña y validación
```
line.setEchoMode(QLineEdit.Password)
```

## Operaciones y métodos más útiles
### QLineEdit
1) `setText()` ⭐  
Qué hace: coloca texto en el input.  
Así se escribe:
```py
line.setText("Ana")
```
Error típico:
```py
line.setText
```
Verás esto: el campo con "Ana".  
Por qué funciona: asigna el contenido.  
Lo típico que sale mal: olvidar paréntesis; pasar tipos no string sin convertir.

2) `text()` ⭐  
Qué hace: lee el texto actual.  
Así se escribe:
```py
valor = line.text()
```
Error típico:
```py
valor = line.text
```
Verás esto: el texto del input.  
Por qué funciona: devuelve el estado interno.  
Lo típico que sale mal: olvidar paréntesis; leer antes de que el usuario escriba.

3) `setPlaceholderText()` ⭐  
Qué hace: muestra un hint.  
Así se escribe:
```py
line.setPlaceholderText("Nombre")
```
Error típico:
```py
line.setPlaceholderText
```
Verás esto: placeholder visible.  
Por qué funciona: establece el texto guía.  
Lo típico que sale mal: olvidar paréntesis; creer que es el valor real.

4) `textChanged.connect()` ⭐  
Qué hace: reacciona a cambios de texto.  
Así se escribe:
```py
line.textChanged.connect(lambda t: print(t))
```
Error típico:
```py
line.textChanged.connect(print())
```
Verás esto: se imprime en cada cambio.  
Por qué funciona: conecta la señal al slot.  
Lo típico que sale mal: llamar la función en vez de pasarla; olvidar argumentos.

5) `returnPressed.connect()`  
Qué hace: captura Enter.  
Así se escribe:
```py
line.returnPressed.connect(lambda: print(line.text()))
```
Error típico:
```py
line.returnPressed.connect(lambda: print(line.text))
```
Verás esto: se dispara al pulsar Enter.  
Por qué funciona: señal del teclado.  
Lo típico que sale mal: olvidar paréntesis en `text()`; no manejar foco.

6) `setEchoMode()` ⭐  
Qué hace: cambia cómo se ve el texto.  
Así se escribe:
```py
line.setEchoMode(QLineEdit.Password)
```
Error típico:
```py
line.setEchoMode("Password")
```
Verás esto: texto oculto.  
Por qué funciona: usa enums de QLineEdit.  
Lo típico que sale mal: usar string; olvidar importar QLineEdit.

7) `setMaxLength()`  
Qué hace: limita la longitud.  
Así se escribe:
```py
line.setMaxLength(20)
```
Error típico:
```py
line.setMaxLength("20")
```
Verás esto: límite aplicado.  
Por qué funciona: espera entero.  
Lo típico que sale mal: pasar string; limitar sin avisar al usuario.

## Mini-reto
Mini-reto 1: Deshabilita un botón hasta que el usuario escriba 5 caracteres.
Solución:
```
line.textChanged.connect(lambda t: btn.setEnabled(len(t) >= 5))
```

## Errores típicos (mal vs bien)
Mal: no validar y aceptar cualquier texto.
```
print(line.text())
```
Bien: validar antes de usar el dato.
```
texto = line.text()
if len(texto) >= 5:
    print(texto)
```

## Nota
Nota: usa setMaxLength para evitar textos demasiado largos.

## Advertencia
Advertencia: si el input es contraseña, usa Password para ocultar caracteres.

## Micro-ejemplo: `text()` devuelve `str`

### Así se escribe
```py
line = QLineEdit()
line.setText("21")
edad = int(line.text())
```

### Error típico: sumar sin convertir
```py
line = QLineEdit()
line.setText("21")
edad = line.text()
edad + 1
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: convierte a `int` si vas a hacer cálculos.

## Checklist final
- Creo un QLineEdit y muestro placeholder.
- Manejo textChanged y returnPressed.
- Uso modos de echo y límites cuando aplica.

## Ver también
- QLabel
- QPushButton
- QComboBox


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
                "No validar",
                "Entradas libres pueden causar errores en lógica posterior.",
            ),
            (
                "Usar echo incorrecto",
                "No uses Normal para contraseñas; usa Password.",
            ),
            (
                "No manejar enter",
                "Si se espera envío, conecta returnPressed.",
            ),
            (
                "No limitar longitud",
                "Textos largos pueden romper layouts.",
            ),
            (
                "No usar placeholder",
                "El usuario no sabe qué escribir.",
            ),
            (
                "Validación tardía",
                "Validar al final genera fricción; valida en vivo.",
            ),
            (
                "No limpiar errores",
                "Si corriges, actualiza mensajes de error.",
            ),
            (
                "No deshabilitar",
                "Deshabilita si depende de otra entrada.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Placeholder",
                """line = QLineEdit()  # Creamos input
line.setPlaceholderText("Nombre")  # Mostramos ayuda""",
            ),
            (
                "Capturar enter",
                """line = QLineEdit()  # Creamos input
line.returnPressed.connect(lambda: print(line.text()))  # Enter imprime texto""",
            ),
            (
                "Modo contraseña",
                """line = QLineEdit()  # Creamos input
line.setEchoMode(QLineEdit.Password)  # Ocultamos texto""",
            ),
            (
                "Limitar longitud",
                """line = QLineEdit()  # Creamos input
line.setMaxLength(12)  # Limitamos caracteres""",
            ),
            (
                "Solo lectura",
                """line = QLineEdit()  # Creamos input
line.setReadOnly(True)  # Evitamos edición""",
            ),
            (
                "Señal textChanged",
                """line = QLineEdit()  # Creamos input
line.textChanged.connect(lambda text: print(text))  # Escuchamos cambios""",
            ),
            (
                "Limpiar input",
                """line = QLineEdit()  # Creamos input
line.clear()  # Limpiamos el texto""",
            ),
            (
                "Seleccionar todo",
                """line = QLineEdit()  # Creamos input
line.selectAll()  # Seleccionamos todo""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QLineEdit con placeholder 'Email'.",
                "hints": ["Usa setPlaceholderText"],
                "solution": "line = QLineEdit()\nline.setPlaceholderText('Email')",
            },
            {
                "question": "Conecta returnPressed para imprimir el texto.",
                "hints": ["line.text()"],
                "solution": "line = QLineEdit()\nline.returnPressed.connect(lambda: print(line.text()))",
            },
            {
                "question": "Configura un QLineEdit en modo contraseña.",
                "hints": ["QLineEdit.Password"],
                "solution": "line = QLineEdit()\nline.setEchoMode(QLineEdit.Password)",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        info = QLabel("Demo: validación simple de longitud.")
        line = QLineEdit()
        line.setPlaceholderText("Escribe al menos 5 caracteres")
        status = QLabel("Estado: esperando")
        submit = QPushButton("Enviar")
        submit.setEnabled(False)

        def on_change(text: str) -> None:
            ok = len(text) >= 5
            submit.setEnabled(ok)
            status.setText("Estado: listo" if ok else "Estado: mínimo 5 caracteres")

        line.textChanged.connect(on_change)
        submit.clicked.connect(lambda: status.setText(f"Enviado: {line.text()}"))

        layout.addWidget(info)
        layout.addWidget(line)
        layout.addWidget(submit)
        layout.addWidget(status)
        return widget
