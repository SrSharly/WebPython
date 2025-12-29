from __future__ import annotations

import ast
import io
import sys
import threading
from contextlib import redirect_stderr, redirect_stdout

BANNED_NAMES = {
    "__import__",
    "eval",
    "exec",
    "open",
    "compile",
    "input",
    "globals",
    "locals",
    "vars",
}

BANNED_MODULES = {
    "os",
    "sys",
    "subprocess",
    "pathlib",
    "socket",
    "shutil",
    "importlib",
    "inspect",
    "ctypes",
}

SAFE_BUILTINS = {
    "abs": abs,
    "all": all,
    "any": any,
    "bool": bool,
    "dict": dict,
    "enumerate": enumerate,
    "float": float,
    "int": int,
    "len": len,
    "list": list,
    "max": max,
    "min": min,
    "print": print,
    "range": range,
    "repr": repr,
    "set": set,
    "str": str,
    "sum": sum,
    "tuple": tuple,
}


class SnippetResult:
    def __init__(self, ok: bool, output: str, error: str | None = None):
        self.ok = ok
        self.output = output
        self.error = error


class SnippetRunner:
    def __init__(self, timeout_s: float = 2.0) -> None:
        self.timeout_s = timeout_s

    def can_run(self, code: str) -> tuple[bool, str | None]:
        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            return False, f"Sintaxis inválida: {exc}"

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                return False, "Los imports están deshabilitados en este entorno."
            if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
                return False, "Acceso a atributos internos no permitido."
            if isinstance(node, ast.Name):
                if node.id in BANNED_NAMES or node.id in BANNED_MODULES:
                    return False, f"Uso de '{node.id}' no permitido."
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in BANNED_NAMES:
                    return False, f"Llamada a '{node.func.id}' no permitida."
        return True, None

    def run(self, code: str) -> SnippetResult:
        allowed, reason = self.can_run(code)
        if not allowed:
            return SnippetResult(False, "", reason)

        stdout = io.StringIO()
        stderr = io.StringIO()
        exec_globals = {"__builtins__": SAFE_BUILTINS}
        exec_locals: dict[str, object] = {}

        def _execute() -> None:
            try:
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    exec(code, exec_globals, exec_locals)
            except Exception as exc:  # noqa: BLE001 - safe sandbox
                stderr.write(str(exc))

        thread = threading.Thread(target=_execute, daemon=True)
        thread.start()
        thread.join(self.timeout_s)
        if thread.is_alive():
            return SnippetResult(False, stdout.getvalue(), "Tiempo de ejecución excedido.")

        err = stderr.getvalue().strip()
        output = stdout.getvalue().strip()
        if err:
            return SnippetResult(False, output, err)
        return SnippetResult(True, output)
