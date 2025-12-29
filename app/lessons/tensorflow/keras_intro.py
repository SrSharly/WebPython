from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class KerasIntroLesson(Lesson):
    TITLE = "Keras intro"
    CATEGORY = "TensorFlow"
    SUBCATEGORY = "Redes neuronales"
    LEVEL = "Intermedio"
    TAGS = ["keras", "tensorflow", "modelos", "entrenamiento"]

    def summary(self) -> str:
        return (
            "Keras es la API de alto nivel de TensorFlow para construir redes neuronales. "
            "Aprende el flujo básico de modelado, compilación y entrenamiento."
        )

    def guide(self) -> str:
        return """
- Keras usa modelos secuenciales o funcionales.
- Define capas con tf.keras.layers.
- Compila con optimizer, loss y metrics.
- Entrena con model.fit().
- Evalúa con model.evaluate().
- Predice con model.predict().
- Usa callbacks para early stopping y checkpoints.
- Normaliza datos para mejorar convergencia.
- Separa train/validation/test.
- Ajusta epochs y batch_size.
- Guarda modelos con model.save().
- Usa TensorBoard para monitoreo.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No normalizar datos",
                "Entrenamiento lento o inestable.",
            ),
            (
                "Loss incorrecta",
                "Elegir una loss incompatible con el problema.",
            ),
            (
                "Overfitting",
                "Muchas epochs sin regularización.",
            ),
            (
                "Batch size extremo",
                "Muy grande o pequeño puede afectar convergencia.",
            ),
            (
                "No separar test",
                "Evaluas con datos vistos, métricas infladas.",
            ),
            (
                "Inputs mal dimensionados",
                "Las capas esperan shapes específicos.",
            ),
            (
                "Olvidar activar GPU",
                "Entrenamiento lento si hay GPU disponible.",
            ),
            (
                "No usar callbacks",
                "Pierdes oportunidades de early stopping.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Modelo secuencial",
                """import tensorflow as tf\n\nmodel = tf.keras.Sequential([\n    tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),\n    tf.keras.layers.Dense(1, activation='sigmoid')\n])""",
            ),
            (
                "Compilar",
                """model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])""",
            ),
            (
                "Entrenar",
                """history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)""",
            ),
            (
                "Evaluar",
                """loss, acc = model.evaluate(X_test, y_test)""",
            ),
            (
                "Predecir",
                """pred = model.predict(X_new)""",
            ),
            (
                "Guardar",
                """model.save('modelo.keras')""",
            ),
            (
                "EarlyStopping",
                """callback = tf.keras.callbacks.EarlyStopping(patience=3)""",
            ),
            (
                "Funcional API",
                """inputs = tf.keras.Input(shape=(4,))\noutputs = tf.keras.layers.Dense(1)(inputs)\nmodel = tf.keras.Model(inputs, outputs)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "¿Qué método entrenaría un modelo en Keras?",
                "hints": ["fit"],
                "solution": "model.fit(X_train, y_train, epochs=10)",
            },
            {
                "question": "¿Por qué separamos validación y test?",
                "hints": ["Evitar sesgo"],
                "solution": "La validación ayuda a ajustar hiperparámetros; el test evalúa desempeño final.",
            },
            {
                "question": "Crea una capa Dense con 4 neuronas y activación relu.",
                "hints": ["tf.keras.layers.Dense"],
                "solution": "layer = tf.keras.layers.Dense(4, activation='relu')",
            },
        ]

    def requirements(self) -> list[str]:
        return ["tensorflow"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("tensorflow")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok:
            layout.addWidget(QLabel(message or "TensorFlow no disponible."))
            return widget

        import numpy as np
        import tensorflow as tf

        X = np.random.rand(200, 3)
        y = (X.sum(axis=1) > 1.5).astype(int)

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(8, activation="relu", input_shape=(3,)),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ])
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        model.fit(X, y, epochs=3, verbose=0)
        loss, acc = model.evaluate(X, y, verbose=0)

        layout.addWidget(QLabel("Demo: modelo entrenado con datos sintéticos."))
        layout.addWidget(QLabel(f"Accuracy en entrenamiento: {acc:.2f}"))
        return widget
