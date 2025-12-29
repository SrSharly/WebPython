from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)

from app.lesson_base import Lesson


class DialogsFilePickerLesson(Lesson):
    TITLE = "Diálogos y File Picker"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Interacciones"
    LEVEL = "Intermedio"
    TAGS = ["QMessageBox", "QFileDialog", "dialogos", "confirmacion"]

    def summary(self) -> str:
        return (
            "Los diálogos informan, confirman acciones y permiten seleccionar rutas. "
            "Aprende a usarlos sin bloquear la UI y registrando resultados." 
        )

    def guide(self) -> str:
        return """
TL;DR: Usa QMessageBox y QFileDialog para comunicar y pedir confirmación al usuario.
- QMessageBox muestra info, warning, error o preguntas.
- question devuelve el botón elegido por el usuario.
- QFileDialog permite seleccionar archivos o carpetas.
- Valida la ruta resultante antes de usarla.
- Maneja el caso de cancelación (ruta vacía).
- Evita bloqueos largos antes o después del diálogo.
- Usa diálogos de confirmación para acciones destructivas.
- Personaliza títulos y textos para claridad.
- Usa logs en UI para registrar decisiones.
- Preferir diálogos modales para decisiones críticas.
- No asumas permisos de escritura/lectura sin validar.
- Mantén los diálogos simples y enfocados.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Ignorar cancel",
                "Si el usuario cancela, la ruta estará vacía.",
            ),
            (
                "Bloquear la UI",
                "Operaciones largas deben ir fuera del hilo principal.",
            ),
            (
                "No validar rutas",
                "Una ruta inválida rompe el flujo posterior.",
            ),
            (
                "Textos ambiguos",
                "Mensajes confusos aumentan errores del usuario.",
            ),
            (
                "Usar warning por todo",
                "Reserva warning/error para casos importantes.",
            ),
            (
                "No registrar decisiones",
                "Sin logs, es difícil depurar comportamiento.",
            ),
            (
                "Diálogos encadenados",
                "Demasiados diálogos seguidos frustran al usuario.",
            ),
            (
                "No manejar retorno",
                "question devuelve un botón; úsalo para decidir.",
            ),
            (
                "Forzar rutas absolutas",
                "Permite al usuario elegir y valida después.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Información",
                """QMessageBox.information(None, "Info", "Operación completada")""",
            ),
            (
                "Error",
                """QMessageBox.critical(None, "Error", "Fallo al guardar")""",
            ),
            (
                "Confirmación",
                """respuesta = QMessageBox.question(None, "Confirmar", "¿Eliminar?")\nif respuesta == QMessageBox.Yes:\n    print("ok")""",
            ),
            (
                "File picker",
                """archivo, _ = QFileDialog.getOpenFileName(None, "Seleccionar", "", "*.txt")""",
            ),
            (
                "Seleccionar carpeta",
                """ruta = QFileDialog.getExistingDirectory(None, "Carpeta")""",
            ),
            (
                "Warning",
                """QMessageBox.warning(None, "Cuidado", "Acción irreversible")""",
            ),
            (
                "Botones personalizados",
                """box = QMessageBox()\nbox.setText("Continuar?")\nbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)\nbox.exec()""",
            ),
            (
                "Validar cancel",
                """ruta, _ = QFileDialog.getOpenFileName(None, "Archivo")\nif not ruta:\n    print("cancelado")""",
            ),
            (
                "Título claro",
                """QMessageBox.information(None, "Datos guardados", "El archivo se guardó correctamente")""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Muestra un QMessageBox de información con título y mensaje.",
                "hints": ["information"],
                "solution": "QMessageBox.information(None, 'Info', 'Proceso listo')",
            },
            {
                "question": "Pide confirmación y actúa solo si es Yes.",
                "hints": ["question", "QMessageBox.Yes"],
                "solution": "resp = QMessageBox.question(None, 'Confirmar', '¿Continuar?')\nif resp == QMessageBox.Yes:\n    print('ok')",
            },
            {
                "question": "Abre un file picker y maneja cancelación.",
                "hints": ["getOpenFileName", "ruta vacía"],
                "solution": "ruta, _ = QFileDialog.getOpenFileName(None, 'Archivo')\nif not ruta:\n    print('cancelado')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo: diálogos con registro de resultados."))

        log = QTextEdit()
        log.setReadOnly(True)
        info_btn = QPushButton("Info")
        error_btn = QPushButton("Error")
        confirm_btn = QPushButton("Confirmar")
        file_btn = QPushButton("Elegir archivo")

        def show_info() -> None:
            QMessageBox.information(widget, "Info", "Operación completada")
            log.append("[Info] Mostrado")

        def show_error() -> None:
            QMessageBox.critical(widget, "Error", "Algo salió mal")
            log.append("[Error] Mostrado")

        def show_confirm() -> None:
            respuesta = QMessageBox.question(widget, "Confirmar", "¿Continuar?")
            log.append(f"[Confirmación] {respuesta == QMessageBox.Yes}")

        def show_file() -> None:
            ruta, _ = QFileDialog.getOpenFileName(widget, "Seleccionar archivo")
            if ruta:
                log.append(f"[Archivo] {ruta}")
            else:
                log.append("[Archivo] Cancelado")

        info_btn.clicked.connect(show_info)
        error_btn.clicked.connect(show_error)
        confirm_btn.clicked.connect(show_confirm)
        file_btn.clicked.connect(show_file)

        layout.addWidget(info_btn)
        layout.addWidget(error_btn)
        layout.addWidget(confirm_btn)
        layout.addWidget(file_btn)
        layout.addWidget(log)
        return widget
