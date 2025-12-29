import importlib.util
import sys


def run():
    if importlib.util.find_spec("PySide6") is None:
        print("Falta PySide6 en este Python")
        print("Ejecuta: python -m pip install -r requirements.txt")
        print(f"Python ejecutable: {sys.executable}")
        print('Comprueba con: python -c "import PySide6"')
        return

    from app.main import main

    main()
