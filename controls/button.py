CONTROL = {
    "nombre": "QPushButton",
    "descripcion": (
        "Un botón que el usuario puede pulsar para ejecutar una acción. "
        "Se usa para disparar eventos como guardar, enviar o confirmar."
    ),
    "usos": [
        "Conectar la señal clicked para ejecutar lógica de negocio.",
        "Cambiar su texto para guiar al usuario (por ejemplo: 'Guardar').",
        "Deshabilitarlo cuando no hay datos válidos." 
    ],
    "errores": [
        "Olvidar conectar la señal clicked y no ejecutar ninguna acción.",
        "No actualizar su estado habilitado/deshabilitado según el formulario.",
        "Usar un texto ambiguo que no indique la acción." 
    ],
}
