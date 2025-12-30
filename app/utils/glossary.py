from __future__ import annotations

GLOSSARY = {
    "variable": {
        "tooltip": "Espacio de memoria con un nombre que guarda un valor.",
        "definition_parts": {
            "que_es": (
                "Un nombre que referencia un valor en memoria durante la ejecución."
            ),
            "para_que": (
                "Permite guardar datos, reutilizarlos y hacer el código más legible y "
                "fácil de mantener."
            ),
            "sintaxis": "nombre = valor",
            "ejemplo": "x = 5 guarda el valor 5 en la variable x.",
            "matiz": (
                "El nombre puede reasignarse para apuntar a otro valor más adelante."
            ),
        },
    },
    "función": {
        "tooltip": "Bloque reutilizable de código que realiza una tarea específica.",
        "definition_parts": {
            "que_es": (
                "Un bloque de código con nombre que puede ejecutarse varias veces."
            ),
            "para_que": (
                "Sirve para encapsular lógica, evitar repetición y dividir un problema "
                "grande en piezas pequeñas."
            ),
            "sintaxis": "def nombre(parametros): ...",
            "ejemplo": "def saludar(): print('Hola')",
            "matiz": (
                "Puede devolver un valor con return o no devolver nada (None)."
            ),
        },
    },
    "método": {
        "tooltip": "Función asociada a un objeto o clase.",
        "definition_parts": {
            "que_es": (
                "Una función asociada a una clase u objeto que opera sobre su estado."
            ),
            "para_que": (
                "Modela comportamientos del objeto, como transformar datos o validar "
                "su estado interno."
            ),
            "sintaxis": "objeto.metodo(args)",
            "ejemplo": "'hola'.upper() devuelve 'HOLA'.",
            "matiz": (
                "Si olvidas los paréntesis, obtienes la referencia al método en lugar "
                "de ejecutarlo."
            ),
        },
    },
    "clase": {
        "tooltip": "Molde que define atributos y comportamientos para crear objetos.",
        "definition_parts": {
            "que_es": (
                "Una plantilla que define atributos (datos) y métodos (acciones)."
            ),
            "para_que": (
                "Se usa para modelar entidades con estado y comportamiento, facilitando "
                "la reutilización y la organización del código."
            ),
            "sintaxis": "class Nombre: ...",
            "ejemplo": "class Perro: def ladrar(self): print('guau')",
            "matiz": (
                "Definir la clase no crea objetos; hay que instanciar con Perro()."
            ),
        },
    },
    "objeto": {
        "tooltip": "Instancia de una clase con estado y comportamiento.",
        "definition_parts": {
            "que_es": (
                "Una instancia concreta creada a partir de una clase."
            ),
            "para_que": (
                "Permite usar los datos y comportamientos definidos por la clase en "
                "casos reales."
            ),
            "sintaxis": "objeto = Clase()",
            "ejemplo": "perro = Perro() crea un objeto de la clase Perro.",
            "matiz": (
                "No confundir la clase (molde) con el objeto (instancia en memoria)."
            ),
        },
    },
    "módulo": {
        "tooltip": "Archivo de Python que agrupa código reutilizable.",
        "definition_parts": {
            "que_es": (
                "Un módulo es un archivo .py que contiene funciones, clases, variables "
                "y constantes reutilizables."
            ),
            "para_que": (
                "Organizar el código por responsabilidades, reutilizar lógica y separar "
                "funcionalidades en piezas independientes."
            ),
            "sintaxis": "import math o from mi_modulo import funcion",
            "ejemplo": "import math permite usar math.sqrt(9).",
            "matiz": (
                "Evita nombrar tu archivo igual que módulos estándar para no ocultarlos "
                "en el import."
            ),
            "error_tipico": (
                "crear un archivo con el mismo nombre que un módulo estándar y bloquear la importación "
                "correcta."
            ),
        },
    },
    "paquete": {
        "tooltip": "Carpeta con módulos y un __init__.py para organizar código.",
        "definition_parts": {
            "que_es": (
                "Un paquete es una carpeta que agrupa módulos relacionados y expone "
                "una jerarquía de importación."
            ),
            "para_que": (
                "Estructurar proyectos grandes, separar dominios y reutilizar "
                "funcionalidades en distintos niveles."
            ),
            "sintaxis": "from mi_paquete import utilidades",
            "ejemplo": "from mi_paquete import utilidades.",
            "matiz": "en Python clásico necesita un __init__.py para ser importable como paquete.",
        },
    },
    "import": {
        "tooltip": "Instrucción que carga un módulo para poder usarlo.",
        "definition_parts": {
            "que_es": (
                "import le dice a Python que cargue un módulo y exponga sus nombres."
            ),
            "para_que": (
                "Permite reutilizar código estándar o propio sin copiarlo en cada archivo."
            ),
            "sintaxis": "import modulo",
            "ejemplo": "import math habilita math.sqrt.",
            "matiz": (
                "Si el módulo no existe en sys.path, verás ModuleNotFoundError."
            ),
            "error_tipico": (
                "usar funciones del módulo sin importarlo primero."
            ),
        },
    },
    "from import": {
        "tooltip": "Forma de importar nombres específicos desde un módulo.",
        "definition_parts": {
            "que_es": (
                "Una variante de import que trae solo los nombres indicados."
            ),
            "para_que": (
                "Evitar escribir el prefijo del módulo cuando necesitas pocos elementos."
            ),
            "sintaxis": "from modulo import nombre",
            "ejemplo": "from math import sqrt permite usar sqrt(9).",
            "matiz": (
                "Si el nombre no existe en el módulo, se lanza ImportError."
            ),
            "error_tipico": (
                "importar un nombre mal escrito y obtener ImportError."
            ),
        },
    },
    "alias": {
        "tooltip": "Nombre alternativo para un módulo o función importada.",
        "definition_parts": {
            "que_es": (
                "Un alias es un nombre corto creado con la palabra clave as."
            ),
            "para_que": (
                "Facilitar la lectura o evitar conflictos de nombres."
            ),
            "sintaxis": "import modulo as alias",
            "ejemplo": "import numpy as np.",
            "matiz": (
                "Después de usar el alias, el nombre original no se usa en ese archivo."
            ),
        },
    },
    "__init__.py": {
        "tooltip": "Archivo que marca un directorio como paquete y define su API.",
        "definition_parts": {
            "que_es": (
                "__init__.py se ejecuta cuando se importa un paquete."
            ),
            "para_que": (
                "Permite agrupar importaciones y definir qué expone el paquete."
            ),
            "sintaxis": "mi_paquete/__init__.py",
            "ejemplo": "from .util import helper dentro de __init__.py.",
            "matiz": (
                "Puede estar vacío si solo necesitas declarar el paquete."
            ),
        },
    },
    "importerror": {
        "tooltip": "Excepción cuando falla una importación de nombre.",
        "definition_parts": {
            "que_es": (
                "ImportError aparece cuando un nombre solicitado no existe en el módulo."
            ),
            "para_que": (
                "Indica que la importación fue parcial o incorrecta."
            ),
            "sintaxis": "from modulo import NombreInexistente",
            "ejemplo": "ImportError: cannot import name 'x' from 'modulo'.",
            "matiz": (
                "Diferente de ModuleNotFoundError, que indica que el módulo no existe."
            ),
        },
    },
    "modulenotfounderror": {
        "tooltip": "Excepción cuando el módulo no se encuentra en sys.path.",
        "definition_parts": {
            "que_es": (
                "ModuleNotFoundError ocurre cuando Python no puede localizar el módulo."
            ),
            "para_que": (
                "Señala rutas incorrectas, paquetes no instalados o nombres mal escritos."
            ),
            "sintaxis": "import modulo_inexistente",
            "ejemplo": "ModuleNotFoundError: No module named 'mi_paquete'.",
            "matiz": (
                "Verifica el entorno activo, la carpeta actual y el nombre del módulo."
            ),
        },
    },
    "sys.path": {
        "tooltip": "Lista de rutas donde Python busca módulos para importar.",
        "definition_parts": {
            "que_es": (
                "sys.path es una lista de directorios que el intérprete recorre al importar."
            ),
            "para_que": (
                "Define dónde buscar módulos propios o instalados en el entorno."
            ),
            "sintaxis": "import sys\nsys.path",
            "ejemplo": "sys.path[0] suele ser la carpeta del script actual.",
            "matiz": (
                "Modificarla puede resolver imports, pero debe hacerse con cuidado."
            ),
        },
    },
    "sqrt": {
        "tooltip": "Función matemática que devuelve la raíz cuadrada.",
        "definition_parts": {
            "que_es": (
                "sqrt es una función del módulo math que calcula la raíz cuadrada."
            ),
            "para_que": (
                "Resolver cálculos comunes de geometría y estadísticas."
            ),
            "sintaxis": "from math import sqrt\nsqrt(9)",
            "ejemplo": "sqrt(16) devuelve 4.0.",
            "matiz": (
                "Si pasas un valor negativo obtendrás un ValueError."
            ),
        },
    },
    "total_con_impuesto": {
        "tooltip": "Función de ejemplo para sumar un impuesto a un precio.",
        "definition_parts": {
            "que_es": (
                "Una función definida en el ejemplo de módulos y paquetes."
            ),
            "para_que": (
                "Ilustrar cómo exponer una función desde un paquete."
            ),
            "sintaxis": "total_con_impuesto(precio, tasa)",
            "ejemplo": "total_con_impuesto(100, 0.19) devuelve 119.0.",
            "matiz": (
                "Pendiente de ampliar con validaciones y redondeo."
            ),
        },
    },
    "parámetro": {
        "tooltip": "Nombre definido en la función para recibir valores.",
        "definition_parts": {
            "que_es": (
                "Un parámetro es el nombre dentro de la función que recibirá un valor "
                "cuando se la invoque."
            ),
            "para_que": (
                "Hacer funciones flexibles que acepten diferentes datos sin duplicar "
                "código."
            ),
            "sintaxis": "def sumar(a, b): ...",
            "ejemplo": "def sumar(a, b): return a + b.",
            "matiz": (
                "Los parámetros pueden tener valores por defecto y tipos anotados para "
                "mejorar la claridad."
            ),
            "error_tipico": "confundir parámetro (nombre) con argumento (valor real).",
        },
    },
    "argumento": {
        "tooltip": "Valor real que se envía a una función al llamarla.",
        "definition_parts": {
            "que_es": (
                "Un argumento es el valor concreto que pasas cuando llamas a una "
                "función."
            ),
            "para_que": (
                "Alimentar los parámetros y ejecutar la función con datos específicos."
            ),
            "sintaxis": "sumar(2, 3) o sumar(a=2, b=3)",
            "ejemplo": "sumar(2, 3) usa 2 y 3 como argumentos.",
            "matiz": "los argumentos pueden ser posicionales o con nombre.",
        },
    },
    "return": {
        "tooltip": "Palabra clave que devuelve un valor desde una función.",
        "definition_parts": {
            "que_es": (
                "return finaliza la ejecución de una función y envía un valor al lugar "
                "donde se llamó."
            ),
            "para_que": "Producir resultados reutilizables y controlar el flujo.",
            "sintaxis": "return resultado",
            "ejemplo": "return a + b devuelve la suma.",
            "matiz": "Si no se indica valor, la función devuelve None.",
            "error_tipico": "usar return sin valor pensando que devuelve un string vacío.",
        },
    },
    "none": {
        "tooltip": "Objeto especial que representa ausencia de valor.",
        "definition_parts": {
            "que_es": (
                "None representa ausencia de valor y se usa como marcador explícito."
            ),
            "para_que": (
                "Indicar que algo aún no está calculado, no existe o no aplica."
            ),
            "sintaxis": "valor is None",
            "ejemplo": "resultado = None antes de calcular.",
            "matiz": "None no es lo mismo que 0, '' o False.",
        },
    },
    "typing": {
        "tooltip": "Módulo estándar para declarar y documentar tipos.",
        "definition_parts": {
            "que_es": (
                "typing es el módulo que define constructores como Optional, Literal, "
                "TypedDict, Protocol o TypeVar."
            ),
            "para_que": (
                "Sirve para comunicar contratos, ayudar a los type checkers y "
                "documentar APIs sin cambiar el runtime."
            ),
            "sintaxis": "from typing import Optional, TypedDict",
            "ejemplo": "from typing import Optional define tipos opcionales.",
            "matiz": (
                "Los tipos no validan en tiempo de ejecución salvo que agregues "
                "checks manuales."
            ),
        },
    },
    "type hint": {
        "tooltip": "Anotación que describe el tipo esperado.",
        "definition_parts": {
            "que_es": (
                "Un type hint es una anotación (o pista) que describe el tipo de un "
                "valor o retorno."
            ),
            "para_que": (
                "Mejorar la legibilidad, habilitar análisis estático y documentar "
                "interfaces."
            ),
            "sintaxis": "def total(valores: list[int]) -> int: ...",
            "ejemplo": "nombre: str = 'Ana'",
            "matiz": (
                "Son opcionales y no obligan al intérprete, pero sí a los chequeadores."
            ),
        },
    },
    "type checker": {
        "tooltip": "Herramienta que valida tipos de forma estática.",
        "definition_parts": {
            "que_es": (
                "Un type checker analiza tu código y detecta incompatibilidades de tipos."
            ),
            "para_que": (
                "Atrapar errores antes de ejecutar, especialmente en proyectos grandes."
            ),
            "sintaxis": "Ejemplos: mypy, pyright, pyre",
            "ejemplo": "mypy detecta si pasas str donde se espera int.",
            "matiz": (
                "El checker no ejecuta el código; interpreta anotaciones y flujos."
            ),
        },
    },
    "optional": {
        "tooltip": "Tipo que permite un valor o None.",
        "definition_parts": {
            "que_es": "Optional[T] equivale a Union[T, None].",
            "para_que": (
                "Modelar valores que pueden faltar o no estar disponibles aún."
            ),
            "sintaxis": "from typing import Optional\nvalor: Optional[int] = None",
            "ejemplo": "def buscar() -> Optional[str]: ...",
            "matiz": (
                "Si el valor no puede ser None, no lo marques como Optional."
            ),
        },
    },
    "union": {
        "tooltip": "Tipo que acepta múltiples alternativas.",
        "definition_parts": {
            "que_es": "Union[A, B] acepta valores de tipo A o B.",
            "para_que": (
                "Expresar entradas flexibles, como int o float, sin perder claridad."
            ),
            "sintaxis": "from typing import Union\nvalor: Union[int, float]",
            "ejemplo": "def convertir(x: Union[int, float]) -> float: ...",
            "matiz": "Uniones muy grandes dificultan la lectura y el mantenimiento.",
        },
    },
    "literal": {
        "tooltip": "Tipo que restringe valores posibles.",
        "definition_parts": {
            "que_es": (
                "Literal define un conjunto finito de valores válidos."
            ),
            "para_que": (
                "Evitar strings mágicos y garantizar modos o flags controlados."
            ),
            "sintaxis": "from typing import Literal\nColor = Literal['rojo', 'azul']",
            "ejemplo": "def pintar(color: Literal['rojo', 'azul']) -> str: ...",
            "matiz": (
                "La restricción la aplica el checker; en runtime puedes validar manualmente."
            ),
        },
    },
    "typeddict": {
        "tooltip": "Tipo que describe dicts con claves fijas.",
        "definition_parts": {
            "que_es": (
                "TypedDict describe la forma esperada de un diccionario con claves y tipos."
            ),
            "para_que": (
                "Modelar datos tipo JSON y validar presencia de claves en análisis estático."
            ),
            "sintaxis": "class Usuario(TypedDict): nombre: str",
            "ejemplo": "usuario: Usuario = {'nombre': 'Ana'}",
            "matiz": "No valida en runtime salvo que agregues comprobaciones.",
        },
    },
    "protocol": {
        "tooltip": "Interfaz estructural para duck typing tipado.",
        "definition_parts": {
            "que_es": (
                "Protocol define un contrato basado en métodos/atributos, no en herencia."
            ),
            "para_que": (
                "Aceptar cualquier objeto que cumpla la interfaz sin depender de clases."
            ),
            "sintaxis": "class Escribible(Protocol): def escribir(self, t: str) -> None: ...",
            "ejemplo": "def exportar(x: Escribible) -> None: ...",
            "matiz": "Ideal para inyección de dependencias y testing.",
        },
    },
    "sequence": {
        "tooltip": "Tipo abstracto para secuencias indexables.",
        "definition_parts": {
            "que_es": "Sequence representa listas, tuplas y otros iterables indexables.",
            "para_que": (
                "Recibir colecciones sin forzar a que sean list."
            ),
            "sintaxis": "from typing import Sequence\nvalores: Sequence[int]",
            "ejemplo": "def total(xs: Sequence[int]) -> int: ...",
            "matiz": "Usa Sequence si no necesitas mutar la colección.",
        },
    },
    "mapping": {
        "tooltip": "Tipo abstracto para diccionarios y mapas.",
        "definition_parts": {
            "que_es": "Mapping describe objetos con claves y valores (como dict).",
            "para_que": "Evitar depender de dict cuando solo necesitas lectura.",
            "sintaxis": "from typing import Mapping\ncfg: Mapping[str, str]",
            "ejemplo": "def leer(cfg: Mapping[str, str]) -> str: ...",
            "matiz": "Mapping no garantiza mutabilidad; es más general que dict.",
        },
    },
    "callable": {
        "tooltip": "Tipo para objetos invocables (funciones o lambdas).",
        "definition_parts": {
            "que_es": "Callable describe una firma: argumentos y tipo de retorno.",
            "para_que": (
                "Tipar callbacks, funciones de orden superior y estrategias."
            ),
            "sintaxis": "from typing import Callable\nfn: Callable[[int], int]",
            "ejemplo": "def aplicar(x: int, fn: Callable[[int], int]) -> int: ...",
            "matiz": "Si omites la firma, pierdes información útil para el checker.",
        },
    },
    "typevar": {
        "tooltip": "Variable de tipo para genéricos.",
        "definition_parts": {
            "que_es": "TypeVar define un tipo genérico reutilizable.",
            "para_que": (
                "Escribir funciones o clases que preservan el tipo de entrada."
            ),
            "sintaxis": "from typing import TypeVar\nT = TypeVar('T')",
            "ejemplo": "def primero(valores: list[T]) -> T: ...",
            "matiz": "Puedes restringirlo con bound o constraints si hace falta.",
        },
    },
    "bool": {
        "tooltip": "Tipo de dato lógico con valores True o False.",
        "definition_parts": {
            "que_es": (
                "bool es el tipo lógico con dos valores posibles: True o False."
            ),
            "para_que": (
                "Evaluar condiciones en if, while y expresiones de control de flujo."
            ),
            "sintaxis": "es_mayor = edad > 18",
            "ejemplo": "es_mayor = edad > 18.",
            "matiz": (
                "En Python, bool es un subtipo de int, por eso True equivale a 1 y "
                "False a 0."
            ),
            "error_tipico": "comparar con 'True' en vez de evaluar la condición directa.",
        },
    },
    "int": {
        "tooltip": "Tipo numérico para enteros.",
        "definition_parts": {
            "que_es": (
                "int representa números enteros sin decimales y con precisión exacta."
            ),
            "para_que": "Contar, indexar, iterar y manejar cantidades discretas.",
            "sintaxis": "contador = 0",
            "ejemplo": "cantidad = 42.",
            "matiz": "dividir con / produce float aunque uses ints.",
        },
    },
    "float": {
        "tooltip": "Tipo numérico para decimales.",
        "definition_parts": {
            "que_es": (
                "float representa números con decimales y precisión aproximada."
            ),
            "para_que": (
                "Realizar cálculos con medidas, porcentajes o resultados no enteros."
            ),
            "sintaxis": "precio = 19.99",
            "ejemplo": "precio = 19.99.",
            "matiz": (
                "La representación binaria puede introducir pequeñas diferencias en "
                "comparaciones exactas."
            ),
            "error_tipico": "comparar floats con == por problemas de precisión.",
        },
    },
    "print": {
        "tooltip": "Función que muestra valores en la salida estándar.",
        "definition_parts": {
            "que_es": "Función incorporada que imprime texto o valores en pantalla.",
            "para_que": (
                "Depurar, mostrar resultados o comunicar estados al usuario."
            ),
            "sintaxis": "print(valor1, valor2)",
            "ejemplo": "print('Hola', 42).",
            "matiz": "Acepta varios argumentos y agrega un salto de línea al final.",
        },
    },
    "input": {
        "tooltip": "Función que lee texto desde la entrada estándar.",
        "definition_parts": {
            "que_es": "Función incorporada que solicita datos al usuario.",
            "para_que": "Recibir texto escrito por el usuario en consola.",
            "sintaxis": "texto = input('Pregunta: ')",
            "ejemplo": "nombre = input('Nombre: ').",
            "matiz": "Siempre devuelve un `str`, incluso si el usuario escribe números.",
        },
    },
    "type": {
        "tooltip": "Función que devuelve el tipo de un objeto.",
        "definition_parts": {
            "que_es": "Función incorporada que revela la clase de un valor.",
            "para_que": "Inspeccionar el tipo real de un dato durante depuración.",
            "sintaxis": "type(valor)",
            "ejemplo": "type(3.14) devuelve <class 'float'>.",
            "matiz": "Úsala para diagnóstico; para validación usa isinstance().",
        },
    },
    "isinstance": {
        "tooltip": "Función que verifica si un valor es de un tipo.",
        "definition_parts": {
            "que_es": "Función incorporada que comprueba tipo o herencia.",
            "para_que": "Validar datos antes de operar o convertir.",
            "sintaxis": "isinstance(valor, tipo) o isinstance(valor, (tipo1, tipo2))",
            "ejemplo": "isinstance('hola', str) devuelve True.",
            "matiz": "El segundo argumento debe ser un tipo o tupla de tipos.",
        },
    },
    "len": {
        "tooltip": "Función que devuelve la longitud de una colección.",
        "definition_parts": {
            "que_es": "Función incorporada que cuenta elementos en una colección.",
            "para_que": "Saber el tamaño de listas, strings, tuplas u otras colecciones.",
            "sintaxis": "cantidad = len(coleccion)",
            "ejemplo": "len([1, 2, 3]) devuelve 3.",
            "matiz": "No modifica la colección; solo devuelve un número.",
        },
    },
    "sum": {
        "tooltip": "Función que suma elementos de un iterable.",
        "definition_parts": {
            "que_es": "Función incorporada que suma números en una lista o iterable.",
            "para_que": "Calcular totales de forma rápida y legible.",
            "sintaxis": "total = sum([1, 2, 3])",
            "ejemplo": "sum([2, 3, 4]) devuelve 9.",
            "matiz": "Si hay strings u otros tipos, puede lanzar TypeError.",
        },
    },
    "range": {
        "tooltip": "Función que genera una secuencia de enteros.",
        "definition_parts": {
            "que_es": (
                "Función incorporada que crea una secuencia iterable de números."
            ),
            "para_que": "Iterar un número de veces en bucles for.",
            "sintaxis": "range(inicio, fin, paso)",
            "ejemplo": "for i in range(3): ...",
            "matiz": "El valor de fin no se incluye.",
        },
    },
    "enumerate": {
        "tooltip": "Función que devuelve pares índice-valor al iterar.",
        "definition_parts": {
            "que_es": (
                "Función incorporada que envuelve un iterable y produce parejas "
                "(índice, valor)."
            ),
            "para_que": (
                "Recorrer una lista mientras conservas la posición sin crear un "
                "contador manual."
            ),
            "sintaxis": "enumerate(iterable, start=0)",
            "ejemplo": "for i, valor in enumerate(lista, start=1): ...",
            "matiz": "El índice comienza en 0 por defecto, pero puedes cambiarlo con start.",
            "error_tipico": (
                "intentar desempaquetar dos valores sin usar enumerate y recibir "
                "ValueError."
            ),
        },
    },
    "zip": {
        "tooltip": "Función que combina elementos de varios iterables.",
        "definition_parts": {
            "que_es": (
                "Función incorporada que agrupa elementos en tuplas, una por cada "
                "iterable proporcionado."
            ),
            "para_que": "Recorrer listas en paralelo y sincronizar columnas de datos.",
            "sintaxis": "zip(iterable1, iterable2, ...)",
            "ejemplo": "for nombre, edad in zip(nombres, edades): ...",
            "matiz": "Se detiene cuando el iterable más corto se agota.",
            "error_tipico": (
                "pasar un solo iterable y tratar de desempaquetar dos valores."
            ),
        },
    },
    "open": {
        "tooltip": "Función que abre archivos y devuelve un manejador.",
        "definition_parts": {
            "que_es": (
                "Función incorporada que abre un archivo en un modo específico."
            ),
            "para_que": "Leer o escribir archivos en disco.",
            "sintaxis": "archivo = open('ruta.txt', 'r')",
            "ejemplo": "with open('datos.txt') as f: ...",
            "matiz": "Usa `with` para asegurar el cierre automático.",
        },
    },
    "read": {
        "tooltip": "Método que lee el contenido completo de un archivo.",
        "definition_parts": {
            "que_es": "Método de archivos que devuelve todo el contenido como texto.",
            "para_que": "Cargar el archivo completo en memoria cuando es pequeño.",
            "sintaxis": "contenido = archivo.read()",
            "ejemplo": "with open('datos.txt') as f: texto = f.read().",
            "matiz": "Si el archivo es grande, lee por líneas en lugar de todo.",
        },
    },
    "write": {
        "tooltip": "Método que escribe texto en un archivo abierto.",
        "definition_parts": {
            "que_es": "Método de archivos que añade o sobrescribe contenido.",
            "para_que": "Guardar texto en un archivo de forma controlada.",
            "sintaxis": "archivo.write('línea')",
            "ejemplo": "with open('log.txt', 'a') as f: f.write('ok\\n').",
            "matiz": "Devuelve el número de caracteres escritos.",
        },
    },
    "splitlines": {
        "tooltip": "Método que separa un string en líneas.",
        "definition_parts": {
            "que_es": "Convierte un texto con saltos de línea en una lista de líneas.",
            "para_que": "Procesar archivos de texto línea por línea.",
            "sintaxis": "lineas = texto.splitlines()",
            "ejemplo": "'a\\n b'.splitlines() -> ['a', ' b'].",
            "matiz": "Elimina los saltos de línea en los resultados.",
        },
    },
    "pathlib": {
        "tooltip": "Módulo para manejar rutas de forma multiplataforma.",
        "definition_parts": {
            "que_es": (
                "Biblioteca estándar que provee la clase Path para rutas."
            ),
            "para_que": "Construir rutas seguras sin concatenar strings.",
            "sintaxis": "from pathlib import Path",
            "ejemplo": "ruta = Path('datos') / 'archivo.txt'.",
            "matiz": "Funciona igual en Windows, macOS y Linux.",
        },
    },
    "path": {
        "tooltip": "Objeto que representa la ubicación de un archivo o carpeta.",
        "definition_parts": {
            "que_es": (
                "Ruta absoluta o relativa que apunta a un recurso del disco."
            ),
            "para_que": "Localizar archivos, crear carpetas y validar existencia.",
            "sintaxis": "ruta = Path('carpeta') / 'archivo.txt'",
            "ejemplo": "ruta.exists() devuelve True si el archivo existe.",
            "matiz": "Las rutas pueden ser relativas al directorio actual.",
        },
    },
    "read_text": {
        "tooltip": "Método de Path que lee un archivo como texto.",
        "definition_parts": {
            "que_es": "Lee el contenido completo de un archivo como string.",
            "para_que": "Cargar archivos pequeños rápidamente con pathlib.",
            "sintaxis": "texto = ruta.read_text(encoding='utf-8')",
            "ejemplo": "Path('datos.txt').read_text(encoding='utf-8').",
            "matiz": "Usa encoding para evitar caracteres corruptos.",
        },
    },
    "write_text": {
        "tooltip": "Método de Path que escribe texto en un archivo.",
        "definition_parts": {
            "que_es": "Escribe un string en un archivo (crea o sobrescribe).",
            "para_que": "Guardar texto sin abrir manualmente el archivo.",
            "sintaxis": "ruta.write_text('hola', encoding='utf-8')",
            "ejemplo": "Path('salida.txt').write_text('ok\\n').",
            "matiz": "Sobrescribe el archivo si ya existe.",
        },
    },
    "exists": {
        "tooltip": "Método de Path que indica si un archivo o carpeta existe.",
        "definition_parts": {
            "que_es": "Devuelve True si la ruta apunta a algo real en disco.",
            "para_que": "Evitar FileNotFoundError al leer archivos.",
            "sintaxis": "ruta.exists()",
            "ejemplo": "if ruta.exists(): ...",
            "matiz": "No crea nada; solo verifica existencia.",
        },
    },
    "mkdir": {
        "tooltip": "Método de Path que crea carpetas.",
        "definition_parts": {
            "que_es": "Crea el directorio indicado por la ruta.",
            "para_que": "Preparar carpetas de salida antes de escribir archivos.",
            "sintaxis": "ruta.mkdir(parents=True, exist_ok=True)",
            "ejemplo": "Path('salidas').mkdir(parents=True, exist_ok=True).",
            "matiz": "parents=True crea carpetas intermedias.",
        },
    },
    "str": {
        "tooltip": "Tipo de texto (cadena de caracteres).",
        "definition_parts": {
            "que_es": (
                "str es el tipo de dato para texto en Python y representa cadenas de "
                "caracteres Unicode."
            ),
            "para_que": (
                "Guardar palabras, frases, rutas, JSON o datos formateados."
            ),
            "sintaxis": "mensaje = 'Hola' o mensaje = \"Hola\"",
            "ejemplo": "nombre = 'Ana'.",
            "matiz": "los strings son inmutables; no se pueden cambiar en sitio.",
        },
    },
    "list": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition_parts": {
            "que_es": (
                "Una lista es una colección ordenada y mutable de elementos."
            ),
            "para_que": (
                "Guardar varios elementos en un solo lugar y modificarlos en tiempo "
                "de ejecución."
            ),
            "sintaxis": "numeros = [1, 2, 3]",
            "ejemplo": "numeros = [1, 2, 3].",
            "matiz": (
                "Las listas pueden contener tipos distintos, pero mezclar tipos puede "
                "complicar el mantenimiento."
            ),
            "error_tipico": "compartir la misma lista entre variables sin copiarla.",
        },
    },
    "lista": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition_parts": {
            "que_es": (
                "Una lista es una colección ordenada y mutable de elementos."
            ),
            "para_que": (
                "Guardar varios elementos en un solo lugar y modificarlos en tiempo "
                "de ejecución."
            ),
            "sintaxis": "numeros = [1, 2, 3]",
            "ejemplo": "numeros = [1, 2, 3].",
            "matiz": (
                "Al modificar una lista mientras la recorres, puedes saltarte elementos."
            ),
            "error_tipico": "modificarla mientras la recorres con un for.",
        },
    },
    "listas": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition_parts": {
            "que_es": (
                "Las listas guardan elementos en orden y permiten modificaciones."
            ),
            "para_que": (
                "Agrupar datos relacionados y mantener un orden útil para indexación."
            ),
            "sintaxis": "frutas = ['manzana', 'pera']",
            "ejemplo": "frutas = ['manzana', 'pera'].",
            "matiz": "los índices empiezan en 0.",
        },
    },
    "tuple": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition_parts": {
            "que_es": (
                "Una tupla es una colección ordenada e inmutable de elementos."
            ),
            "para_que": "Agrupar datos fijos o valores que no deberían cambiar.",
            "sintaxis": "punto = (3, 4)",
            "ejemplo": "punto = (3, 4).",
            "matiz": (
                "Se usan a menudo para devolver múltiples valores desde una función."
            ),
            "error_tipico": "intentar hacer punto[0] = 5.",
        },
    },
    "tupla": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition_parts": {
            "que_es": "Una tupla es una colección ordenada que no se puede modificar",
            "para_que": "para datos que no deberían cambiar.",
            "sintaxis": "dimensiones = (1920, 1080) o (valor,)",
            "ejemplo": "dimensiones = (1920, 1080).",
            "matiz": "una tupla de un solo elemento lleva coma: (5,).",
        },
    },
    "tuplas": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition_parts": {
            "que_es": "Las tuplas son colecciones ordenadas e inmutables",
            "para_que": "para registrar datos fijos.",
            "sintaxis": "colores = ('rojo', 'azul')",
            "ejemplo": "colores = ('rojo', 'azul').",
            "matiz": "se usan para agrupar valores relacionados sin intención de mutarlos.",
            "error_tipico": "pensar que son listas y tratar de modificar elementos.",
        },
    },
    "dict": {
        "tooltip": "Colección de pares clave-valor.",
        "definition_parts": {
            "que_es": (
                "Un diccionario guarda pares clave-valor para búsquedas rápidas."
            ),
            "para_que": (
                "Representar mapas, configuraciones, catálogos o datos estructurados."
            ),
            "sintaxis": "edades = {'Ana': 20}",
            "ejemplo": "edades = {'Ana': 20}.",
            "matiz": (
                "las claves deben ser únicas e inmutables, y las búsquedas son rápidas gracias a tablas "
                "hash."
            ),
        },
    },
    "diccionario": {
        "tooltip": "Colección de pares clave-valor.",
        "definition_parts": {
            "que_es": (
                "Un diccionario relaciona claves con valores y permite acceso directo."
            ),
            "para_que": "Acceder a información por nombre, id o identificador.",
            "sintaxis": "colores = {'rojo': '#ff0000'}",
            "ejemplo": "colores = {'rojo': '#ff0000'}.",
            "matiz": (
                "Las claves pueden ser strings, números o tuplas, pero deben ser "
                "inmutables."
            ),
            "error_tipico": "acceder a una clave inexistente y provocar KeyError.",
        },
    },
    "diccionarios": {
        "tooltip": "Colección de pares clave-valor.",
        "definition_parts": {
            "que_es": "Los diccionarios organizan datos en pares clave-valor",
            "para_que": "para búsquedas rápidas por clave.",
            "sintaxis": "precios = {'pan': 1.2, 'leche': 0.9}",
            "ejemplo": "precios = {'pan': 1.2, 'leche': 0.9}.",
            "matiz": "usa get para evitar errores si no existe la clave.",
        },
    },
    "set": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition_parts": {
            "que_es": (
                "Un set es una colección sin orden y sin elementos repetidos."
            ),
            "para_que": (
                "Eliminar duplicados, comprobar pertenencia y hacer operaciones de "
                "conjuntos."
            ),
            "sintaxis": "unicos = {1, 2, 3} o set([1, 2, 3])",
            "ejemplo": "unicos = {1, 2, 3}.",
            "matiz": (
                "Aunque los sets no tienen orden, desde Python 3.7 suelen iterar en "
                "orden de inserción, pero no es garantía contractual."
            ),
            "error_tipico": "esperar un orden fijo al iterar.",
        },
    },
    "conjunto": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition_parts": {
            "que_es": "Un conjunto guarda valores únicos y no garantiza orden",
            "para_que": "para comprobar pertenencia rápidamente.",
            "sintaxis": "vistos = {'ana', 'luis'} o set(['ana', 'luis'])",
            "ejemplo": "vistos = {'ana', 'luis'}.",
            "matiz": "no puedes indexar un set con [0].",
        },
    },
    "conjuntos": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition_parts": {
            "que_es": "Los conjuntos almacenan elementos únicos sin orden",
            "para_que": "para eliminar duplicados o comparar colecciones.",
            "sintaxis": "set([1, 1, 2])",
            "ejemplo": "set([1, 1, 2]) produce {1, 2}.",
            "matiz": "el orden de iteración no es un contrato, aunque parezca estable.",
            "error_tipico": "pensar que mantienen el orden de inserción.",
        },
    },
    "mutable": {
        "tooltip": "Se puede modificar después de ser creado.",
        "definition_parts": {
            "que_es": "Un objeto mutable puede cambiar su contenido después de crearse",
            "para_que": "cuando necesitas actualizar datos en sitio.",
            "sintaxis": "lista.append(4) o diccionario['k'] = 'v'",
            "ejemplo": "una lista es mutable, puedes hacer lista.append(4).",
            "matiz": "mutar un objeto compartido afecta a todas las referencias.",
        },
    },
    "inmutable": {
        "tooltip": "No se puede modificar después de ser creado.",
        "definition_parts": {
            "que_es": "Un objeto inmutable no puede cambiarse; si lo 'modificas' creas otro",
            "para_que": "para valores fijos o claves de diccionario.",
            "sintaxis": "texto = 'hola' o coordenadas = (1, 2)",
            "ejemplo": "strings y tuplas son inmutables.",
            "matiz": "si necesitas modificarlo, debes crear una nueva instancia.",
            "error_tipico": "intentar modificar un string con asignación por índice.",
        },
    },
    "iterador": {
        "tooltip": "Objeto que permite recorrer elementos uno a uno.",
        "definition_parts": {
            "que_es": "Un iterador devuelve elementos de una colección uno a uno",
            "para_que": "con for o next() para recorrer datos.",
            "ejemplo": "iter([1, 2]) crea un iterador.",
            "matiz": "un iterador se agota cuando llegas al final.",
        },
    },
    "generador": {
        "tooltip": "Función o expresión que produce valores bajo demanda.",
        "definition_parts": {
            "que_es": "Un generador produce valores uno por uno sin guardar todos en memoria",
            "para_que": "para secuencias grandes o infinitas.",
            "sintaxis": "(x * 2 for x in range(3)) o def gen(): yield x",
            "ejemplo": "(x * 2 for x in range(3)) crea un generador.",
            "matiz": "al consumirlo una vez, no puedes reiniciarlo sin recrearlo.",
            "error_tipico": "intentar indexarlo como si fuera una lista.",
        },
    },
    "excepción": {
        "tooltip": "Evento que interrumpe el flujo normal por un error.",
        "definition_parts": {
            "que_es": "Una excepción es un error que interrumpe el flujo normal del programa",
            "para_que": "para señalar fallos y tratarlos con try/except.",
            "ejemplo": "int('a') lanza ValueError.",
            "matiz": "si no la manejas, el programa se detiene.",
        },
    },
    "raise": {
        "tooltip": "Palabra clave para lanzar una excepción manualmente.",
        "definition_parts": {
            "que_es": "raise crea y lanza una excepción de forma explícita.",
            "para_que": "para señalar datos inválidos o estados imposibles.",
            "sintaxis": "raise ValueError('mensaje')",
            "ejemplo": "if edad < 0: raise ValueError('Edad inválida')",
            "matiz": "debe lanzar una excepción real, no un string.",
            "error_tipico": "usar raise 'mensaje' y provocar TypeError.",
        },
    },
    "ValueError": {
        "tooltip": "Excepción para valores con tipo correcto pero contenido inválido.",
        "definition_parts": {
            "que_es": "ValueError aparece cuando un valor no cumple el formato esperado.",
            "para_que": "para señalar conversiones fallidas o datos fuera de rango.",
            "sintaxis": "int('x')",
            "ejemplo": "int('x') lanza ValueError.",
            "matiz": "se usa cuando el tipo es válido pero el valor no.",
        },
    },
    "TypeError": {
        "tooltip": "Excepción para operaciones con tipos incompatibles.",
        "definition_parts": {
            "que_es": "TypeError ocurre cuando combinas tipos incorrectos.",
            "para_que": "para detectar usos inválidos de operadores o funciones.",
            "sintaxis": "'hola' + 3",
            "ejemplo": "'hola' + 3 lanza TypeError.",
            "matiz": "revísalo cuando pasas datos con tipo incorrecto.",
        },
    },
    "ZeroDivisionError": {
        "tooltip": "Excepción por dividir entre cero.",
        "definition_parts": {
            "que_es": "ZeroDivisionError aparece cuando divides por 0.",
            "para_que": "para detener operaciones matemáticas inválidas.",
            "sintaxis": "10 / 0",
            "ejemplo": "10 / 0 lanza ZeroDivisionError.",
            "matiz": "valida el denominador antes de dividir.",
        },
    },
    "RuntimeError": {
        "tooltip": "Excepción genérica para errores en tiempo de ejecución.",
        "definition_parts": {
            "que_es": "RuntimeError indica un fallo que no encaja en otras categorías.",
            "para_que": "para envolver errores cuando necesitas un mensaje de dominio.",
            "sintaxis": "raise RuntimeError('Mensaje')",
            "ejemplo": "raise RuntimeError('Entrada inválida').",
            "matiz": "usa ValueError cuando sea más específico.",
        },
    },
    "else": {
        "tooltip": "Bloque que se ejecuta cuando no ocurre el error.",
        "definition_parts": {
            "que_es": "else en try/except se ejecuta solo si no hubo excepción.",
            "para_que": "para separar el camino exitoso del manejo de errores.",
            "sintaxis": "try: ... except Error: ... else: ...",
            "ejemplo": "else: resultados.append(valor).",
            "matiz": "requiere un except o finally antes.",
        },
    },
    "try": {
        "tooltip": "Bloque para capturar errores potenciales.",
        "definition_parts": {
            "que_es": "try delimita el código que podría fallar",
            "para_que": "junto con except para manejar errores.",
            "sintaxis": "try: ... except Error: ...",
            "ejemplo": "try: abrir_archivo() except FileNotFoundError: ...",
            "matiz": "se recomienda capturar excepciones específicas y registrar fallos.",
            "error_tipico": "poner demasiado código dentro y ocultar bugs.",
        },
    },
    "except": {
        "tooltip": "Bloque que maneja una excepción específica.",
        "definition_parts": {
            "que_es": "except captura una excepción y ejecuta código alternativo",
            "para_que": "para manejar errores esperables.",
            "ejemplo": "except ZeroDivisionError: print('No dividir entre 0').",
            "matiz": "evita usar except sin tipo porque oculta errores reales.",
        },
    },
    "finally": {
        "tooltip": "Bloque que se ejecuta siempre al finalizar un try.",
        "definition_parts": {
            "que_es": "finally se ejecuta siempre, haya error o no",
            "para_que": "para liberar recursos.",
            "ejemplo": "finally: archivo.close().",
            "matiz": "no reemplaza el manejo de errores, solo asegura limpieza.",
        },
    },
    "with": {
        "tooltip": "Bloque que gestiona recursos con context manager.",
        "definition_parts": {
            "que_es": "with abre un bloque que administra recursos automáticamente",
            "para_que": "para abrir archivos o conexiones y cerrarlas al final.",
            "sintaxis": "with open('a.txt') as f: ...",
            "ejemplo": "with open('a.txt') as f: leer = f.read().",
            "matiz": "también se usa con locks o transacciones que deben cerrarse.",
            "error_tipico": "olvidar usar with y dejar recursos abiertos.",
        },
    },
    "context manager": {
        "tooltip": "Objeto que controla la entrada y salida de un bloque with.",
        "definition_parts": {
            "que_es": "Un context manager define qué hacer al entrar y salir de un with",
            "para_que": "para gestionar recursos de forma segura.",
            "ejemplo": "open() es un context manager para archivos.",
            "matiz": "implementa __enter__ y __exit__.",
        },
    },
    "scope": {
        "tooltip": "Alcance donde una variable es visible y válida.",
        "definition_parts": {
            "que_es": "El scope indica dónde una variable puede ser usada",
            "para_que": "para entender por qué un nombre existe o no existe en un bloque.",
            "sintaxis": "def funcion(): variable_local = 1",
            "ejemplo": "una variable creada en una función no existe fuera.",
            "matiz": "Python sigue la regla LEGB (local, enclosing, global, built-in).",
            "error_tipico": "intentar leer una variable local fuera de su función.",
        },
    },
    "global": {
        "tooltip": "Palabra clave para usar una variable del ámbito global.",
        "definition_parts": {
            "que_es": "global permite modificar una variable definida fuera de una función",
            "para_que": "con cuidado cuando necesitas cambiar un valor global.",
            "ejemplo": "global contador dentro de una función.",
            "matiz": "su abuso hace el código más difícil de mantener.",
        },
    },
    "local": {
        "tooltip": "Variable definida dentro de un bloque o función.",
        "definition_parts": {
            "que_es": "Una variable local existe solo dentro de la función o bloque donde se crea",
            "para_que": "para mantener datos temporales.",
            "sintaxis": "def fn(): temp = 5",
            "ejemplo": "dentro de una función, temp = 5.",
            "matiz": "cada llamada crea un nuevo scope local independiente.",
            "error_tipico": "intentar usarla fuera de su alcance.",
        },
    },
    "snake_case": {
        "tooltip": "Convención de nombres con minúsculas y guiones bajos.",
        "definition_parts": {
            "que_es": "snake_case es una forma de nombrar variables con minúsculas y guiones bajos",
            "para_que": "en Python para nombres de variables y funciones.",
            "ejemplo": "total_ventas = 10.",
            "matiz": "ayuda a la legibilidad y sigue PEP 8.",
        },
    },
    "pascalcase": {
        "tooltip": "Convención de nombres con cada palabra en mayúscula.",
        "definition_parts": {
            "que_es": "PascalCase escribe cada palabra con inicial en mayúscula",
            "para_que": "en Python sobre todo para nombres de clases.",
            "sintaxis": "class UsuarioPremium: ...",
            "ejemplo": "class UsuarioPremium.",
            "matiz": "es común en lenguajes tipados para tipos, clases y componentes.",
            "error_tipico": "usarlo para variables en lugar de snake_case.",
        },
    },
    "pep8": {
        "tooltip": "Guía de estilo oficial para escribir código Python.",
        "definition_parts": {
            "que_es": "PEP 8 es la guía de estilo oficial para escribir Python legible",
            "para_que": "para nombrar, espaciar y organizar el código.",
            "ejemplo": "4 espacios por indentación.",
            "matiz": "seguirla facilita trabajar en equipo.",
        },
    },
    "indentación": {
        "tooltip": "Espacios o tabulaciones que delimitan bloques de código.",
        "definition_parts": {
            "que_es": "La indentación en Python define bloques de código",
            "para_que": "para delimitar if, for, funciones, etc.",
            "sintaxis": "    cuatro espacios por nivel",
            "ejemplo": "cuatro espacios antes de una línea dentro de una función.",
            "matiz": "la indentación es sintaxis, no solo estilo, y afecta la ejecución.",
            "error_tipico": "mezclar tabs y espacios y provocar errores de indentación.",
        },
    },
    "f-string": {
        "tooltip": "Cadena con interpolación usando prefijo f.",
        "definition_parts": {
            "que_es": "Una f-string permite insertar variables en un string con { }",
            "para_que": "para crear textos dinámicos de forma clara.",
            "ejemplo": "f'Hola {nombre}'.",
            "matiz": "las expresiones dentro de { } se evalúan al momento.",
        },
    },
    "slice": {
        "tooltip": "Subsección de una secuencia usando índices y rango.",
        "definition_parts": {
            "que_es": "Un slice extrae una parte de una secuencia usando inicio y fin",
            "para_que": "con listas, strings o tuplas.",
            "sintaxis": "secuencia[inicio:fin:paso]",
            "ejemplo": "texto[0:3] devuelve los primeros 3 caracteres.",
            "matiz": "puedes omitir inicio/fin para tomar desde el principio o el final.",
            "error_tipico": "olvidar que el índice final no se incluye.",
        },
    },
    "comprehension": {
        "tooltip": "Sintaxis compacta para construir colecciones.",
        "definition_parts": {
            "que_es": "Una comprehension crea listas, sets o dicts en una sola línea",
            "para_que": "para transformar datos de forma concisa.",
            "ejemplo": "[x * 2 for x in numeros].",
            "matiz": "si se vuelve muy larga, pierde legibilidad.",
        },
    },
    "append": {
        "tooltip": "Método de listas que agrega un elemento al final.",
        "definition_parts": {
            "que_es": "append añade un elemento al final de una lista",
            "para_que": "para crecer listas paso a paso.",
            "sintaxis": "lista.append(valor)",
            "ejemplo": "lista.append(10).",
            "matiz": "modifica la lista en sitio y devuelve None.",
            "error_tipico": "asignar lista = lista.append(10) y perder la lista.",
        },
    },
    "extend": {
        "tooltip": "Método de listas que agrega varios elementos.",
        "definition_parts": {
            "que_es": "extend añade varios elementos de otra colección a una lista",
            "para_que": "para concatenar listas.",
            "ejemplo": "lista.extend([4, 5]).",
            "matiz": "extend recibe una colección, append recibiría la lista completa.",
        },
    },
    "insert": {
        "tooltip": "Método de listas que agrega en una posición específica.",
        "definition_parts": {
            "que_es": "insert agrega un elemento en una posición específica de la lista",
            "para_que": "para insertar sin reemplazar.",
            "sintaxis": "lista.insert(indice, valor)",
            "ejemplo": "lista.insert(1, 'nuevo').",
            "matiz": "insertar al inicio puede ser costoso en listas grandes.",
            "error_tipico": "usar índices fuera del rango sin entender el resultado.",
        },
    },
    "pop": {
        "tooltip": "Método que extrae y devuelve un elemento.",
        "definition_parts": {
            "que_es": "pop elimina y devuelve un elemento de una lista (por defecto el último)",
            "para_que": "para procesar elementos y quitarlos.",
            "ejemplo": "ultimo = lista.pop().",
            "matiz": "si la lista está vacía, lanza IndexError.",
        },
    },
    "remove": {
        "tooltip": "Método que elimina la primera coincidencia.",
        "definition_parts": {
            "que_es": "remove elimina la primera aparición de un valor en una lista",
            "para_que": "para borrar por valor.",
            "sintaxis": "lista.remove(valor)",
            "ejemplo": "lista.remove('a').",
            "matiz": "si hay duplicados, solo borra la primera coincidencia.",
            "error_tipico": "si el valor no existe, lanza ValueError.",
        },
    },
    "sort": {
        "tooltip": "Método que ordena los elementos en su lugar.",
        "definition_parts": {
            "que_es": "sort ordena una lista en el mismo lugar",
            "para_que": "para ordenar sin crear otra lista.",
            "ejemplo": "numeros.sort().",
            "matiz": "sort no devuelve la lista; devuelve None.",
        },
    },
    "upper": {
        "tooltip": "Método de strings que convierte a mayúsculas.",
        "definition_parts": {
            "que_es": "upper crea una versión en mayúsculas del string",
            "para_que": "para normalizar texto.",
            "ejemplo": "'hola'.upper() -> 'HOLA'.",
            "matiz": "no modifica el string original.",
        },
    },
    "lower": {
        "tooltip": "Método de strings que convierte a minúsculas.",
        "definition_parts": {
            "que_es": "lower crea una versión en minúsculas del string",
            "para_que": "para comparar sin importar el caso.",
            "ejemplo": "'Hola'.lower() -> 'hola'.",
            "matiz": "devuelve un nuevo string, no modifica el original.",
        },
    },
    "strip": {
        "tooltip": "Método que quita espacios al inicio y final.",
        "definition_parts": {
            "que_es": "strip elimina espacios (u otros caracteres) al inicio y final",
            "para_que": "para limpiar entradas de usuario.",
            "ejemplo": "'  hola  '.strip() -> 'hola'.",
            "matiz": "no quita espacios del medio.",
        },
    },
    "split": {
        "tooltip": "Método que separa un string en partes.",
        "definition_parts": {
            "que_es": "split divide un string en una lista usando un separador",
            "para_que": "para procesar texto.",
            "ejemplo": "'a,b'.split(',') -> ['a', 'b'].",
            "matiz": "si no das separador, usa espacios en blanco.",
        },
    },
    "join": {
        "tooltip": "Método que une una lista de strings.",
        "definition_parts": {
            "que_es": "join une una colección de strings usando un separador",
            "para_que": "para construir textos.",
            "ejemplo": "','.join(['a', 'b']) -> 'a,b'.",
            "error_tipico": "incluir elementos que no son strings.",
        },
    },
    "replace": {
        "tooltip": "Método que reemplaza subcadenas.",
        "definition_parts": {
            "que_es": "replace sustituye una subcadena por otra",
            "para_que": "para limpiar o cambiar texto.",
            "ejemplo": "'hola'.replace('h', 'H') -> 'Hola'.",
            "matiz": "reemplaza todas las apariciones por defecto.",
        },
    },
    "startswith": {
        "tooltip": "Método que comprueba el prefijo.",
        "definition_parts": {
            "que_es": "startswith verifica si un string comienza con un prefijo",
            "para_que": "para validar formatos.",
            "ejemplo": "'https://'.startswith('http') -> True.",
            "matiz": "distingue mayúsculas y minúsculas.",
        },
    },
    "endswith": {
        "tooltip": "Método que comprueba el sufijo.",
        "definition_parts": {
            "que_es": "endswith verifica si un string termina con un sufijo",
            "para_que": "para validar extensiones.",
            "ejemplo": "'archivo.txt'.endswith('.txt') -> True.",
            "matiz": "también distingue mayúsculas y minúsculas.",
        },
    },
    "get": {
        "tooltip": "Método de dict que devuelve un valor con clave.",
        "definition_parts": {
            "que_es": "get obtiene el valor de una clave en un diccionario",
            "para_que": "para evitar errores si la clave no existe.",
            "ejemplo": "datos.get('edad', 0).",
            "matiz": "puedes dar un valor por defecto.",
        },
    },
    "items": {
        "tooltip": "Método de dict que devuelve pares clave-valor.",
        "definition_parts": {
            "que_es": "items devuelve pares clave-valor como tuplas",
            "para_que": "para recorrer diccionarios.",
            "ejemplo": "for k, v in datos.items(): ...",
            "matiz": "el resultado es una vista, no una lista real.",
        },
    },
    "keys": {
        "tooltip": "Método de dict que devuelve las claves.",
        "definition_parts": {
            "que_es": "keys devuelve todas las claves de un diccionario",
            "para_que": "para iterar o verificar claves.",
            "ejemplo": "'nombre' in datos.keys().",
            "matiz": "también es una vista dinámica.",
        },
    },
    "values": {
        "tooltip": "Método de dict que devuelve los valores.",
        "definition_parts": {
            "que_es": "values devuelve los valores de un diccionario",
            "para_que": "para recorrer solo los datos.",
            "ejemplo": "for v in datos.values(): ...",
            "matiz": "puede contener valores duplicados.",
        },
    },
    "update": {
        "tooltip": "Método de dict que fusiona valores.",
        "definition_parts": {
            "que_es": "update agrega o reemplaza claves en un diccionario",
            "para_que": "para combinar configuraciones.",
            "ejemplo": "datos.update({'edad': 30}).",
            "matiz": "sobrescribe valores existentes con la misma clave.",
        },
    },
    "sql": {
        "tooltip": "Lenguaje para consultar y manipular bases de datos relacionales.",
        "definition_parts": {
            "que_es": "SQL es un lenguaje para crear y consultar bases de datos relacionales",
            "para_que": "para seleccionar, insertar o actualizar datos.",
            "ejemplo": "SELECT * FROM usuarios.",
            "matiz": "usar parámetros evita inyección SQL.",
        },
    },
    "cursor": {
        "tooltip": "Objeto que permite recorrer resultados de una consulta.",
        "definition_parts": {
            "que_es": "Un cursor recorre los resultados de una consulta a la base de datos",
            "para_que": "para leer filas una por una o en bloques.",
            "sintaxis": "cursor = conexion.cursor()",
            "ejemplo": "cursor.fetchone().",
            "matiz": "algunos drivers permiten usar cursores en modo servidor para grandes volúmenes.",
            "error_tipico": "olvidar cerrar el cursor y dejar recursos abiertos.",
        },
    },
    "transacción": {
        "tooltip": "Grupo de operaciones que se confirman o revierten juntas.",
        "definition_parts": {
            "que_es": "Una transacción agrupa varias operaciones en una sola unidad",
            "para_que": "para asegurar consistencia en la base de datos.",
            "ejemplo": "transferir saldo entre dos cuentas.",
            "matiz": "si algo falla, se revierte con rollback.",
        },
    },
    "commit": {
        "tooltip": "Acción que confirma los cambios pendientes.",
        "definition_parts": {
            "que_es": "commit confirma de forma permanente los cambios en una transacción",
            "para_que": "cuando todo salió bien.",
            "sintaxis": "conexion.commit()",
            "ejemplo": "conexion.commit().",
            "matiz": "en muchas bases de datos el autocommit puede estar desactivado.",
            "error_tipico": "olvidar commit y perder los cambios.",
        },
    },
    "rollback": {
        "tooltip": "Acción que revierte los cambios pendientes.",
        "definition_parts": {
            "que_es": "rollback revierte los cambios no confirmados en una transacción",
            "para_que": "cuando ocurre un error.",
            "ejemplo": "conexion.rollback().",
            "matiz": "solo revierte cambios desde el último commit.",
        },
    },
    "orm": {
        "tooltip": "Técnica que mapea clases de Python a tablas.",
        "definition_parts": {
            "que_es": "Un ORM mapea clases de Python a tablas de una base de datos",
            "para_que": "para trabajar con datos como objetos.",
            "ejemplo": "Usuario(nombre='Ana') se guarda en la tabla usuarios.",
            "matiz": "sigue habiendo SQL por debajo; hay que entenderlo.",
        },
    },
    "engine": {
        "tooltip": "Componente que gestiona la conexión a la base de datos.",
        "definition_parts": {
            "que_es": "El engine representa la conexión y configuración de acceso a la base",
            "para_que": "para crear sesiones o ejecutar consultas.",
            "ejemplo": "engine = create_engine(url).",
            "matiz": "reutilizar el engine evita abrir conexiones innecesarias.",
        },
    },
    "session": {
        "tooltip": "Unidad de trabajo que gestiona objetos y transacciones.",
        "definition_parts": {
            "que_es": "Una sesión agrupa operaciones y controla el ciclo de vida de objetos ORM",
            "para_que": "para añadir, actualizar o borrar registros.",
            "sintaxis": "session = Session(); session.add(obj)",
            "ejemplo": "session.add(usuario); session.commit().",
            "matiz": "es recomendable usar context managers para cerrar sesiones.",
            "error_tipico": "olvidar cerrar la sesión y mantener conexiones abiertas.",
        },
    },
    "pool": {
        "tooltip": "Conjunto de conexiones reutilizables.",
        "definition_parts": {
            "que_es": "Un pool mantiene conexiones abiertas para reutilizarlas",
            "para_que": "para mejorar rendimiento en bases de datos.",
            "ejemplo": "el pool entrega una conexión disponible al hacer una consulta.",
            "matiz": "si el pool se agota, las consultas esperan.",
        },
    },
    "dsn": {
        "tooltip": "Cadena que describe cómo conectarse a la base de datos.",
        "definition_parts": {
            "que_es": "DSN es un texto con los datos necesarios para conectarse a una base",
            "para_que": "para indicar host, usuario, base y opciones.",
            "sintaxis": "postgres://user:pass@host:5432/db",
            "ejemplo": "postgres://user:pass@localhost/db.",
            "matiz": "usa variables de entorno o secretos para no exponer credenciales.",
            "error_tipico": "exponer el DSN en logs públicos.",
        },
    },
    "sql injection": {
        "tooltip": "Ataque que manipula SQL con datos sin parametrizar.",
        "definition_parts": {
            "que_es": "SQL injection ocurre cuando datos sin filtrar alteran una consulta",
            "para_que": "como ejemplo de qué evitar.",
            "ejemplo": "concatenar texto de usuario en una query.",
            "matiz": "usa parámetros para evitar este riesgo.",
        },
    },
    "señal": {
        "tooltip": "Notificación emitida cuando ocurre un evento en una GUI.",
        "definition_parts": {
            "que_es": "Una señal es un aviso que se emite cuando sucede algo en la interfaz",
            "para_que": "para comunicar eventos a otros componentes.",
            "ejemplo": "button.clicked es una señal.",
            "matiz": "una señal no hace nada si nadie la conecta a un slot.",
        },
    },
    "señales": {
        "tooltip": "Notificaciones emitidas cuando ocurren eventos en una GUI.",
        "definition_parts": {
            "que_es": "Las señales notifican eventos de la interfaz",
            "para_que": "para conectar acciones con respuestas.",
            "ejemplo": "slider.valueChanged se emite al mover el slider.",
            "matiz": "puedes conectar varias funciones a una misma señal.",
        },
    },
    "slot": {
        "tooltip": "Función que responde a una señal en Qt/PySide.",
        "definition_parts": {
            "que_es": "Un slot es la función que se ejecuta cuando llega una señal",
            "para_que": "para definir la reacción a eventos.",
            "ejemplo": "button.clicked.connect(mi_funcion).",
            "matiz": "el slot debe aceptar los argumentos que emite la señal.",
        },
    },
    "slots": {
        "tooltip": "Funciones que responden a señales en Qt/PySide.",
        "definition_parts": {
            "que_es": "Los slots son funciones que reaccionan a señales",
            "para_que": "para organizar lógica de interfaz.",
            "ejemplo": "conectar varias señales a un mismo slot.",
            "matiz": "ayudan a separar la UI de la lógica.",
        },
    },
    "widget": {
        "tooltip": "Componente visual básico de una interfaz gráfica.",
        "definition_parts": {
            "que_es": "Un widget es un elemento visual como botones, inputs o etiquetas",
            "para_que": "para construir la interfaz.",
            "ejemplo": "QLabel muestra texto.",
            "matiz": "todos los widgets tienen un padre para el layout.",
        },
    },
    "widgets": {
        "tooltip": "Componentes visuales básicos de una interfaz gráfica.",
        "definition_parts": {
            "que_es": "Los widgets son piezas visuales de la interfaz",
            "para_que": "para construir ventanas completas.",
            "ejemplo": "QPushButton es un widget de botón.",
            "matiz": "su tamaño puede gestionarse con layouts.",
        },
    },
    "layout": {
        "tooltip": "Distribuidor que organiza widgets en una interfaz.",
        "definition_parts": {
            "que_es": "Un layout organiza widgets en filas, columnas o rejillas",
            "para_que": "para que la interfaz se adapte al tamaño.",
            "sintaxis": "layout = QVBoxLayout(); layout.addWidget(boton)",
            "ejemplo": "QVBoxLayout apila elementos en vertical.",
            "matiz": "un buen layout evita tamaños fijos y mejora la accesibilidad.",
            "error_tipico": "poner widgets sin layout y que no redimensionen bien.",
        },
    },
    "layouts": {
        "tooltip": "Distribuidores que organizan widgets en una interfaz.",
        "definition_parts": {
            "que_es": "Los layouts distribuyen widgets automáticamente",
            "para_que": "para mantener orden y responsividad.",
            "ejemplo": "combinar QHBoxLayout y QVBoxLayout.",
            "matiz": "un widget solo puede pertenecer a un layout.",
        },
    },
    "event loop": {
        "tooltip": "Bucle que procesa eventos y mantiene viva la interfaz.",
        "definition_parts": {
            "que_es": "El event loop es el ciclo que recibe eventos y los distribuye",
            "para_que": "para mantener la app reactiva.",
            "ejemplo": "app.exec() inicia el bucle.",
            "matiz": "bloquear el event loop congela la interfaz.",
        },
    },
    "bucle de eventos": {
        "tooltip": "Bucle que procesa eventos y mantiene viva la interfaz.",
        "definition_parts": {
            "que_es": "El bucle de eventos procesa clics, teclas y actualizaciones",
            "para_que": "para que la GUI responda.",
            "sintaxis": "app.exec()",
            "ejemplo": "eventos de mouse llegan al bucle.",
            "matiz": "tareas pesadas deben ir a hilos o procesos para no bloquearlo.",
            "error_tipico": "usar tareas largas sin hilos y congelar la UI.",
        },
    },
    "qthread": {
        "tooltip": "Clase de Qt para ejecutar tareas en un hilo separado.",
        "definition_parts": {
            "que_es": "QThread permite ejecutar trabajo pesado sin bloquear la interfaz",
            "para_que": "para tareas largas o de fondo.",
            "ejemplo": "mover cálculo pesado a un QThread.",
            "matiz": "nunca actualices la UI desde el hilo secundario.",
        },
    },
    "model/view": {
        "tooltip": "Patrón que separa datos (modelo) y presentación (vista).",
        "definition_parts": {
            "que_es": "Model/View separa los datos de cómo se muestran",
            "para_que": "para interfaces con listas y tablas.",
            "ejemplo": "QListView con un modelo de datos.",
            "matiz": "el modelo notifica cambios a la vista.",
        },
    },
    "modelo/vista": {
        "tooltip": "Patrón que separa datos (modelo) y presentación (vista).",
        "definition_parts": {
            "que_es": "El patrón modelo/vista separa la lógica de datos de la UI",
            "para_que": "para mantener el código organizado.",
            "ejemplo": "QTableView con un modelo.",
            "matiz": "actualizar el modelo actualiza la vista automáticamente.",
        },
    },
    "dataframe": {
        "tooltip": "Tabla de datos bidimensional con filas y columnas en Pandas.",
        "definition_parts": {
            "que_es": "Un DataFrame es una tabla con filas y columnas en Pandas",
            "para_que": "para análisis y limpieza de datos.",
            "ejemplo": "df = pd.DataFrame({'a': [1, 2]}).",
            "matiz": "las columnas pueden tener tipos distintos.",
        },
    },
    "dataframes": {
        "tooltip": "Tablas de datos bidimensionales con filas y columnas en Pandas.",
        "definition_parts": {
            "que_es": "Los DataFrames son tablas con filas y columnas",
            "para_que": "para análisis de datos.",
            "ejemplo": "df[['col1', 'col2']] selecciona columnas.",
            "matiz": "trabajar con copias vs vistas puede afectar cambios.",
        },
    },
    "serie": {
        "tooltip": "Estructura unidimensional de datos en Pandas.",
        "definition_parts": {
            "que_es": "Una Series es una columna con índices en Pandas",
            "para_que": "para trabajar con una sola dimensión.",
            "ejemplo": "s = df['columna'].",
            "matiz": "el índice es parte importante de la Series.",
        },
    },
    "series": {
        "tooltip": "Estructuras unidimensionales de datos en Pandas.",
        "definition_parts": {
            "que_es": "Las Series son estructuras unidimensionales con índice",
            "para_que": "para columnas o datos sueltos.",
            "ejemplo": "pd.Series([1, 2, 3]).",
            "matiz": "operaciones con Series alinean por índice.",
        },
    },
    "groupby": {
        "tooltip": "Operación que agrupa filas para aplicar cálculos por grupo.",
        "definition_parts": {
            "que_es": "groupby agrupa filas para calcular agregados por grupo",
            "para_que": "para resúmenes y estadísticas.",
            "ejemplo": "df.groupby('categoria').mean().",
            "matiz": "tras agrupar, necesitas una agregación.",
        },
    },
    "merge": {
        "tooltip": "Operación para combinar DataFrames por claves comunes.",
        "definition_parts": {
            "que_es": "merge combina DataFrames usando columnas comunes",
            "para_que": "para unir datasets relacionados.",
            "ejemplo": "df1.merge(df2, on='id').",
            "matiz": "el tipo de join cambia qué filas aparecen.",
        },
    },
    "loc": {
        "tooltip": "Acceso por etiquetas de filas/columnas en Pandas.",
        "definition_parts": {
            "que_es": "loc selecciona datos usando etiquetas de filas/columnas",
            "para_que": "cuando el índice tiene nombres.",
            "ejemplo": "df.loc[0, 'col'].",
            "matiz": "incluye el último índice en rangos por etiqueta.",
        },
    },
    "iloc": {
        "tooltip": "Acceso por posiciones numéricas en Pandas.",
        "definition_parts": {
            "que_es": "iloc selecciona datos por posición numérica",
            "para_que": "cuando quieres índices por posición.",
            "ejemplo": "df.iloc[0, 1].",
            "matiz": "los rangos son exclusivos en el final, como en slicing.",
        },
    },
    "nan": {
        "tooltip": "Valor especial que representa datos faltantes.",
        "definition_parts": {
            "que_es": "NaN representa valores faltantes en datos numéricos",
            "para_que": "para indicar ausencia en Pandas o NumPy.",
            "ejemplo": "pd.Series([1, None]).",
            "matiz": "NaN no es igual a sí mismo (NaN != NaN).",
        },
    },
    "dtype": {
        "tooltip": "Tipo de dato almacenado en un array o columna.",
        "definition_parts": {
            "que_es": "dtype indica el tipo de datos de una columna o array",
            "para_que": "para entender cómo se guardan los valores.",
            "ejemplo": "df['col'].dtype.",
            "matiz": "cambiar dtype puede afectar memoria y precisión.",
        },
    },
    "pipeline": {
        "tooltip": "Secuencia encadenada de pasos de procesamiento y modelo.",
        "definition_parts": {
            "que_es": "Un pipeline encadena pasos de preprocesado y modelo",
            "para_que": "para evitar fugas y mantener flujo reproducible.",
            "ejemplo": "Pipeline([('scaler', ...), ('model', ...)]).",
            "matiz": "cada paso debe implementar fit/transform o fit/predict.",
        },
    },
    "leakage": {
        "tooltip": "Uso de información del futuro en entrenamiento, sesga resultados.",
        "definition_parts": {
            "que_es": "Leakage ocurre cuando el modelo ve información que no tendrá en producción",
            "para_que": "como advertencia en ML.",
            "ejemplo": "usar la variable objetivo para normalizar datos.",
            "matiz": "produce métricas falsas y modelos poco fiables.",
        },
    },
    "cross-validation": {
        "tooltip": "Técnica que valida con varias particiones del dataset.",
        "definition_parts": {
            "que_es": "La cross-validation divide los datos en varias particiones para evaluar",
            "para_que": "para medir rendimiento real del modelo.",
            "ejemplo": "K-Fold con 5 particiones.",
            "matiz": "hay que mantener el orden temporal si es series de tiempo.",
        },
    },
    "validación cruzada": {
        "tooltip": "Técnica que valida con varias particiones del dataset.",
        "definition_parts": {
            "que_es": "La validación cruzada evalúa el modelo en varias particiones",
            "para_que": "para reducir el sesgo de una sola división.",
            "ejemplo": "cross_val_score en sklearn.",
            "matiz": "aumenta el costo de cómputo.",
        },
    },
    "estimator": {
        "tooltip": "Objeto en sklearn que aprende parámetros desde datos.",
        "definition_parts": {
            "que_es": "Un estimator es un modelo o transformador en sklearn",
            "para_que": "para ajustar parámetros con fit.",
            "ejemplo": "LinearRegression() es un estimator.",
            "matiz": "algunos estimators también transforman datos.",
        },
    },
    "fit": {
        "tooltip": "Proceso de ajustar un modelo a los datos de entrenamiento.",
        "definition_parts": {
            "que_es": "fit entrena un modelo con datos de entrenamiento",
            "para_que": "para aprender parámetros.",
            "ejemplo": "model.fit(X_train, y_train).",
            "matiz": "no uses datos de test en fit.",
        },
    },
    "transform": {
        "tooltip": "Aplicación de una transformación a los datos.",
        "definition_parts": {
            "que_es": "transform aplica una transformación ya aprendida a nuevos datos",
            "para_que": "después de fit en escaladores o codificadores.",
            "ejemplo": "scaler.transform(X).",
            "matiz": "fit_transform combina ambos pasos en entrenamiento.",
        },
    },
    "predict": {
        "tooltip": "Generación de salidas de un modelo entrenado.",
        "definition_parts": {
            "que_es": "predict genera predicciones usando un modelo entrenado",
            "para_que": "para obtener resultados en datos nuevos.",
            "ejemplo": "model.predict(X_test).",
            "matiz": "la salida depende del tipo de modelo (clase o valor).",
        },
    },
    "tensor": {
        "tooltip": "Estructura n-dimensional para datos numéricos en DL.",
        "definition_parts": {
            "que_es": "Un tensor es una estructura n-dimensional para datos",
            "para_que": "en deep learning para representar matrices y más.",
            "ejemplo": "un batch de imágenes es un tensor 4D.",
            "matiz": "la forma (shape) es clave para operar con tensores.",
        },
    },
    "tensores": {
        "tooltip": "Estructuras n-dimensionales para datos numéricos en DL.",
        "definition_parts": {
            "que_es": "Los tensores son estructuras n-dimensionales de datos",
            "para_que": "en redes neuronales para inputs y pesos.",
            "ejemplo": "pesos de una capa son un tensor.",
            "matiz": "las operaciones requieren dimensiones compatibles.",
        },
    },
    "autograd": {
        "tooltip": "Sistema de cálculo automático de gradientes.",
        "definition_parts": {
            "que_es": "Autograd calcula gradientes automáticamente",
            "para_que": "para entrenar redes neuronales con backpropagation.",
            "ejemplo": "en PyTorch, los tensores con requires_grad.",
            "matiz": "hay que limpiar gradientes entre pasos.",
        },
    },
    "optimizer": {
        "tooltip": "Algoritmo que actualiza pesos para minimizar la pérdida.",
        "definition_parts": {
            "que_es": "Un optimizer ajusta los pesos para minimizar la función de pérdida",
            "para_que": "durante el entrenamiento.",
            "ejemplo": "Adam o SGD.",
            "matiz": "el learning rate influye mucho en el resultado.",
        },
    },
    "optimizador": {
        "tooltip": "Algoritmo que actualiza pesos para minimizar la pérdida.",
        "definition_parts": {
            "que_es": "Un optimizador actualiza los pesos de un modelo",
            "para_que": "para reducir la pérdida durante el entrenamiento.",
            "ejemplo": "optimizador = Adam(model.parameters()).",
            "matiz": "una tasa de aprendizaje muy alta puede divergir.",
        },
    },
    "epoch": {
        "tooltip": "Iteración completa sobre todo el conjunto de entrenamiento.",
        "definition_parts": {
            "que_es": "Una epoch es una pasada completa por el dataset de entrenamiento",
            "para_que": "para medir avance en entrenamiento.",
            "ejemplo": "entrenar 10 epochs.",
            "matiz": "más epochs no siempre significan mejor modelo.",
        },
    },
    "época": {
        "tooltip": "Iteración completa sobre todo el conjunto de entrenamiento.",
        "definition_parts": {
            "que_es": "Época es lo mismo que epoch: una pasada completa por el dataset",
            "para_que": "para contar ciclos de entrenamiento.",
            "ejemplo": "5 épocas de entrenamiento.",
            "matiz": "hay riesgo de overfitting si entrenas demasiado.",
        },
    },
    "batch": {
        "tooltip": "Subconjunto de datos usado en una actualización.",
        "definition_parts": {
            "que_es": "Un batch es un subconjunto de datos usado en una actualización",
            "para_que": "para entrenar por partes en lugar de todo el dataset.",
            "ejemplo": "batch_size = 32.",
            "matiz": "batch muy pequeño puede hacer el entrenamiento inestable.",
        },
    },
    "lote": {
        "tooltip": "Subconjunto de datos usado en una actualización.",
        "definition_parts": {
            "que_es": "Un lote es un grupo de ejemplos usados en cada actualización",
            "para_que": "para controlar memoria y rendimiento.",
            "ejemplo": "entrenar con lotes de 64.",
            "matiz": "lotes grandes pueden requerir más memoria.",
        },
    },
    "gradiente": {
        "tooltip": "Dirección de mayor cambio de la función de pérdida.",
        "definition_parts": {
            "que_es": "El gradiente indica cómo cambiar los pesos para reducir la pérdida",
            "para_que": "en optimización.",
            "ejemplo": "descenso por gradiente ajusta pesos en dirección opuesta.",
            "matiz": "gradientes muy grandes pueden causar explosión.",
        },
    },
    "backpropagation": {
        "tooltip": "Algoritmo que propaga el error para ajustar pesos.",
        "definition_parts": {
            "que_es": "Backpropagation propaga el error hacia atrás para calcular gradientes",
            "para_que": "para entrenar redes neuronales.",
            "ejemplo": "se calcula la pérdida y se propaga por capas.",
            "matiz": "requiere derivadas de las funciones de activación.",
        },
    },
    "loss": {
        "tooltip": "Medida de error que el modelo intenta minimizar.",
        "definition_parts": {
            "que_es": "La loss mide cuánto se equivoca el modelo",
            "para_que": "para guiar el entrenamiento.",
            "ejemplo": "MSE en regresión.",
            "matiz": "una loss baja en entrenamiento no garantiza buen rendimiento.",
        },
    },
    "índice": {
        "tooltip": "Estructura que acelera búsquedas en una tabla de datos.",
        "definition_parts": {
            "que_es": "Un índice acelera la búsqueda de filas en una tabla",
            "para_que": "en bases de datos para consultas rápidas.",
            "ejemplo": "índice en la columna id.",
            "matiz": "mejora lecturas pero puede ralentizar escrituras.",
        },
    },
    "clave primaria": {
        "tooltip": "Columna que identifica de forma única cada fila.",
        "definition_parts": {
            "que_es": "La clave primaria identifica de forma única cada fila",
            "para_que": "para garantizar unicidad en tablas.",
            "ejemplo": "id incremental como clave primaria.",
            "matiz": "no debe repetirse ni ser nula.",
        },
    },
    "clave foránea": {
        "tooltip": "Columna que referencia la clave primaria de otra tabla.",
        "definition_parts": {
            "que_es": "Una clave foránea referencia la clave primaria de otra tabla",
            "para_que": "para relacionar tablas.",
            "ejemplo": "pedidos.usuario_id apunta a usuarios.id.",
            "matiz": "debe existir en la tabla referenciada.",
        },
    },
    "join": {
        "tooltip": "Operación que combina filas de tablas relacionadas.",
        "definition_parts": {
            "que_es": "Un join combina filas de tablas relacionadas por una clave",
            "para_que": "para consultar datos de varias tablas.",
            "ejemplo": "SELECT ... FROM a JOIN b ON a.id = b.a_id.",
            "matiz": "los tipos de join cambian qué filas aparecen.",
        },
    },
    "inner join": {
        "tooltip": "Join que devuelve solo coincidencias entre tablas.",
        "definition_parts": {
            "que_es": "INNER JOIN devuelve solo filas que tienen coincidencia en ambas tablas",
            "para_que": "cuando quieres solo datos relacionados.",
            "ejemplo": "INNER JOIN usuarios y pedidos.",
            "matiz": "filas sin relación se descartan.",
        },
    },
    "left join": {
        "tooltip": "Join que devuelve todas las filas de la tabla izquierda.",
        "definition_parts": {
            "que_es": "LEFT JOIN devuelve todas las filas de la tabla izquierda",
            "para_que": "para mantener datos aunque no haya coincidencia.",
            "ejemplo": "usuarios LEFT JOIN pedidos.",
            "matiz": "las columnas sin coincidencia quedan como NULL.",
        },
    },
    "right join": {
        "tooltip": "Join que devuelve todas las filas de la tabla derecha.",
        "definition_parts": {
            "que_es": "RIGHT JOIN devuelve todas las filas de la tabla derecha",
            "para_que": "cuando quieres preservar la tabla derecha.",
            "ejemplo": "pedidos RIGHT JOIN usuarios.",
            "matiz": "no todos los motores soportan RIGHT JOIN.",
        },
    },
    "full join": {
        "tooltip": "Join que devuelve coincidencias y no coincidencias.",
        "definition_parts": {
            "que_es": "FULL JOIN devuelve filas coincidentes y no coincidentes",
            "para_que": "para ver todo el conjunto de datos.",
            "ejemplo": "FULL JOIN entre clientes y pedidos.",
            "matiz": "algunos motores no lo soportan sin UNION.",
        },
    },
    "tabla": {
        "tooltip": "Estructura que guarda datos en filas y columnas.",
        "definition_parts": {
            "que_es": "Una tabla almacena datos en filas y columnas",
            "para_que": "para organizar información en bases de datos.",
            "ejemplo": "tabla usuarios con columnas id y nombre.",
            "matiz": "un buen diseño evita duplicación de datos.",
        },
    },
    "fila": {
        "tooltip": "Registro horizontal de una tabla.",
        "definition_parts": {
            "que_es": "Una fila es un registro completo dentro de una tabla",
            "para_que": "para representar una entidad.",
            "ejemplo": "una fila de usuarios representa a una persona.",
            "matiz": "cada fila se identifica por la clave primaria.",
        },
    },
    "columna": {
        "tooltip": "Campo vertical que representa un atributo.",
        "definition_parts": {
            "que_es": "Una columna representa un atributo de la tabla",
            "para_que": "para definir el tipo de dato de cada campo.",
            "ejemplo": "columna 'edad' en usuarios.",
            "matiz": "el tipo de columna limita los valores permitidos.",
        },
    },
    "python": {
        "tooltip": "Lenguaje de programación interpretado y multiplataforma.",
        "definition_parts": {
            "que_es": (
                "Python es un lenguaje de alto nivel, interpretado y multiplataforma "
                "con una sintaxis clara enfocada en legibilidad y productividad. "
                "Destaca por su tipado dinámico, gran biblioteca estándar y una "
                "comunidad muy amplia, además de múltiples paradigmas de programación "
                "(imperativo, orientado a objetos y funcional)."
            ),
            "para_que": (
                "Se usa en automatización, desarrollo web, ciencia de datos, scripting, "
                "IA, DevOps, QA y aplicaciones de escritorio, combinando paradigmas "
                "imperativo, orientado a objetos y funcional. También es común en "
                "herramientas de línea de comandos, APIs, ETLs, pipelines de datos y "
                "automatización de infraestructura."
            ),
            "sintaxis": "print('Hola') o def saludar(nombre): return f'Hola {nombre}'",
            "ejemplo": (
                "print('Hola') imprime en consola; con pandas.read_csv() puedes cargar "
                "un CSV, limpiar columnas y generar un análisis rápido o construir un "
                "script que automatice tareas diarias."
            ),
            "matiz": (
                "El ecosistema de paquetes (pip) acelera el desarrollo, pero el "
                "rendimiento puede requerir optimizaciones, tipado o extensiones en C. "
                "El manejo de entornos virtuales es clave para evitar conflictos."
            ),
        },
    },
    "pandas": {
        "tooltip": "Librería de Python para análisis de datos tabulares.",
        "definition_parts": {
            "que_es": (
                "Pandas es una librería de Python para manipular datos estructurados "
                "con DataFrames y Series."
            ),
            "para_que": (
                "Se usa para limpiar, transformar, combinar y analizar datos en tablas, "
                "facilitando operaciones de análisis exploratorio."
            ),
            "sintaxis": "import pandas as pd; df = pd.read_csv('archivo.csv')",
            "ejemplo": (
                "Leer un CSV con pandas.read_csv(), filtrar filas y calcular métricas "
                "por categoría."
            ),
            "matiz": (
                "Funciona en memoria; para volúmenes muy grandes conviene usar "
                "herramientas distribuidas."
            ),
        },
    },
    "numpy": {
        "tooltip": "Librería base de Python para cálculo numérico.",
        "definition_parts": {
            "que_es": (
                "NumPy proporciona arrays n-dimensionales y operaciones vectorizadas "
                "para cálculo científico."
            ),
            "para_que": (
                "Se usa para álgebra lineal, estadísticas básicas, simulaciones y "
                "preprocesamiento numérico eficiente."
            ),
            "sintaxis": "import numpy as np; arreglo = np.array([1, 2, 3])",
            "ejemplo": (
                "Crear un array con numpy.array([1, 2, 3]) y aplicar operaciones "
                "vectorizadas."
            ),
            "matiz": (
                "Muchas librerías científicas dependen de NumPy, por lo que dominar sus "
                "arrays mejora el rendimiento del código."
            ),
        },
    },
    "matplotlib": {
        "tooltip": "Librería de Python para visualización de datos.",
        "definition_parts": {
            "que_es": (
                "Matplotlib es una librería de visualización que permite crear "
                "gráficas 2D y personalizar estilos."
            ),
            "para_que": (
                "Se usa para comunicar resultados, explorar datos y generar reportes "
                "con gráficos reproducibles."
            ),
            "sintaxis": "import matplotlib.pyplot as plt",
            "ejemplo": "plt.plot([1, 2, 3], [2, 4, 6]); plt.show()",
            "matiz": (
                "Aunque tiene una API extensa, el flujo típico es crear la gráfica "
                "y luego mostrarla con plt.show()."
            ),
        },
    },
    "pyplot": {
        "tooltip": "Submódulo de Matplotlib con una API simple para graficar.",
        "definition_parts": {
            "que_es": (
                "pyplot es el submódulo que ofrece funciones como plot, title o show."
            ),
            "para_que": (
                "Permite crear gráficos rápidos con una sintaxis compacta."
            ),
            "sintaxis": "import matplotlib.pyplot as plt",
            "ejemplo": "plt.title('Ventas'); plt.xlabel('Mes')",
            "matiz": (
                "Su API es conveniente para scripts, pero también existe el estilo "
                "orientado a objetos con Figure y Axes."
            ),
        },
    },
    "plt.plot": {
        "tooltip": "Función de pyplot para trazar líneas o puntos.",
        "definition_parts": {
            "que_es": (
                "plt.plot dibuja una serie de datos conectados por una línea."
            ),
            "para_que": (
                "Se usa para visualizar tendencias, comparaciones y cambios en el tiempo."
            ),
            "sintaxis": "plt.plot(x, y, marker='o')",
            "ejemplo": "plt.plot([1, 2], [3, 5])",
            "matiz": (
                "x e y deben tener la misma longitud para evitar errores de dimensión."
            ),
        },
    },
    "plt.show": {
        "tooltip": "Función que muestra la figura en pantalla.",
        "definition_parts": {
            "que_es": (
                "plt.show abre una ventana con la gráfica generada."
            ),
            "para_que": (
                "Permite visualizar el resultado del script de forma interactiva."
            ),
            "sintaxis": "plt.show()",
            "ejemplo": "plt.plot([1, 2, 3], [2, 4, 6]); plt.show()",
            "matiz": (
                "En notebooks suele renderizar automáticamente, pero en scripts es necesario."
            ),
        },
    },
    "plt.title": {
        "tooltip": "Función que define el título de la gráfica.",
        "definition_parts": {
            "que_es": (
                "plt.title asigna un texto descriptivo a la gráfica."
            ),
            "para_que": (
                "Ayuda a interpretar rápidamente lo que representa la figura."
            ),
            "sintaxis": "plt.title('Ventas 2024')",
            "ejemplo": "plt.title('Ventas mensuales')",
            "matiz": "Requiere un texto; llamarla sin argumento lanza TypeError.",
        },
    },
    "plt.xlabel": {
        "tooltip": "Función que define la etiqueta del eje X.",
        "definition_parts": {
            "que_es": "plt.xlabel establece el nombre del eje horizontal.",
            "para_que": "Hace explícita la variable que se grafica en X.",
            "sintaxis": "plt.xlabel('Mes')",
            "ejemplo": "plt.xlabel('Tiempo (s)')",
            "matiz": "Mejora la legibilidad cuando el eje tiene categorías.",
        },
    },
    "plt.ylabel": {
        "tooltip": "Función que define la etiqueta del eje Y.",
        "definition_parts": {
            "que_es": "plt.ylabel establece el nombre del eje vertical.",
            "para_que": "Aclara qué magnitud se está midiendo en Y.",
            "sintaxis": "plt.ylabel('Unidades')",
            "ejemplo": "plt.ylabel('Temperatura (°C)')",
            "matiz": "Es clave cuando comparas series con valores similares.",
        },
    },
    "ndarray": {
        "tooltip": "Tipo de array n-dimensional usado por NumPy.",
        "definition_parts": {
            "que_es": "Estructura de datos central de NumPy para almacenar números.",
            "para_que": (
                "Se usa para representar vectores, matrices y tensores con operaciones "
                "vectorizadas."
            ),
            "sintaxis": "np.array([1, 2, 3]) -> ndarray",
            "ejemplo": "np.array([1, 2, 3]).shape",
            "matiz": "No es lo mismo que una lista: está optimizado para números.",
        },
    },
    "shape": {
        "tooltip": "Tupla que describe las dimensiones de un array.",
        "definition_parts": {
            "que_es": "Atributo que indica filas/columnas o dimensiones de un ndarray.",
            "para_que": "Ayuda a validar tamaños antes de indexar o reestructurar.",
            "sintaxis": "arreglo.shape",
            "ejemplo": "np.array([1, 2, 3]).shape devuelve (3,).",
            "matiz": "No es una función; es un atributo del array.",
        },
    },
    "np.array": {
        "tooltip": "Función de NumPy para crear arrays.",
        "definition_parts": {
            "que_es": "Convierte listas o tuplas en un ndarray.",
            "para_que": "Crear estructuras numéricas para operar de forma vectorizada.",
            "sintaxis": "np.array([1, 2, 3])",
            "ejemplo": "np.array([1, 2, 3]) * 2",
            "matiz": "Si mezclas tipos, NumPy convierte a un tipo común.",
        },
    },
    "np.zeros": {
        "tooltip": "Función de NumPy para crear arrays llenos de ceros.",
        "definition_parts": {
            "que_es": "Genera un ndarray con todos los valores inicializados a 0.",
            "para_que": "Reservar espacio para cálculos numéricos.",
            "sintaxis": "np.zeros(4)",
            "ejemplo": "np.zeros(3) -> array([0., 0., 0.])",
            "matiz": "Acepta dimensiones y dtype opcional.",
        },
    },
    "np.arange": {
        "tooltip": "Función de NumPy para crear secuencias numéricas.",
        "definition_parts": {
            "que_es": "Crea un array con valores equidistantes.",
            "para_que": "Generar rangos numéricos sin bucles.",
            "sintaxis": "np.arange(inicio, fin, paso)",
            "ejemplo": "np.arange(1, 5) -> array([1, 2, 3, 4])",
            "matiz": "El límite final no se incluye.",
        },
    },
    "np.sum": {
        "tooltip": "Función de NumPy que suma elementos de un array.",
        "definition_parts": {
            "que_es": "Reduce un array a un valor sumando sus elementos.",
            "para_que": "Obtener totales de forma rápida.",
            "sintaxis": "np.sum(arreglo)",
            "ejemplo": "np.sum(np.array([1, 2, 3])) -> 6",
            "matiz": "Permite sumar por ejes con axis.",
        },
    },
    "np.mean": {
        "tooltip": "Función de NumPy que calcula la media.",
        "definition_parts": {
            "que_es": "Promedia los valores de un array.",
            "para_que": "Obtener estadísticas descriptivas rápidas.",
            "sintaxis": "np.mean(arreglo)",
            "ejemplo": "np.mean(np.array([10, 20, 30])) -> 20.0",
            "matiz": "Si hay NaN, valida o limpia los datos antes de promediar.",
        },
    },
    "jupyter": {
        "tooltip": "Entorno de notebooks interactivos para código y texto.",
        "definition_parts": {
            "que_es": (
                "Jupyter es un entorno interactivo que permite combinar código, texto, "
                "gráficas y resultados en un mismo documento, normalmente en notebooks "
                "con celdas ejecutables."
            ),
            "para_que": (
                "Se usa para exploración de datos, prototipos rápidos, docencia y "
                "comunicación de análisis reproducibles."
            ),
            "sintaxis": "jupyter lab o jupyter notebook",
            "ejemplo": (
                "Ejecutar un notebook .ipynb para analizar datos con pandas, generar "
                "gráficas con matplotlib y documentar hallazgos paso a paso."
            ),
            "matiz": (
                "Para producción, conviene convertir notebooks en scripts o pipelines "
                "versionados."
            ),
        },
    },
    "jupyter notebook": {
        "tooltip": "Formato y aplicación de notebook interactivo en Jupyter.",
        "definition_parts": {
            "que_es": (
                "Jupyter Notebook es la aplicación y el formato .ipynb para documentos "
                "interactivos con celdas de código y markdown."
            ),
            "para_que": (
                "Se usa para crear análisis reproducibles, demostraciones y reportes "
                "con resultados ejecutables."
            ),
            "sintaxis": "archivo.ipynb abierto con `jupyter notebook`",
            "ejemplo": (
                "Un notebook con celdas que cargan un CSV, limpian datos y generan un "
                "reporte con gráficos."
            ),
            "matiz": (
                "Los notebooks guardan salidas en el archivo JSON, por lo que conviene "
                "limpiar outputs antes de versionar en Git."
            ),
        },
    },
    "jupyterlab": {
        "tooltip": "Interfaz moderna y modular de Jupyter.",
        "definition_parts": {
            "que_es": (
                "JupyterLab es la interfaz moderna de Jupyter con paneles, pestañas y "
                "extensiones para notebooks, terminales y editores."
            ),
            "para_que": (
                "Se usa para trabajar con múltiples notebooks, archivos y recursos en "
                "una experiencia de IDE basada en navegador."
            ),
            "sintaxis": "jupyter lab",
            "ejemplo": (
                "Abrir dos notebooks en paralelo y un editor de scripts en la misma "
                "ventana."
            ),
            "matiz": (
                "Permite extensiones, pero hay que considerar compatibilidad de "
                "versiones y recursos en ambientes compartidos."
            ),
        },
    },
    "json": {
        "tooltip": "Formato de texto para intercambio de datos estructurados.",
        "definition_parts": {
            "que_es": (
                "JSON (JavaScript Object Notation) es un formato de texto para "
                "representar objetos y listas con comillas dobles."
            ),
            "para_que": (
                "Enviar datos entre APIs, guardar configuraciones y serializar "
                "estructuras simples."
            ),
            "sintaxis": "import json",
            "ejemplo": "json.dumps({'ok': True}) produce un string JSON.",
            "matiz": "No acepta sets ni comentarios; todo debe ser JSON válido.",
        },
    },
    "json.dumps": {
        "tooltip": "Función que convierte objetos Python a texto JSON.",
        "definition_parts": {
            "que_es": "Serializa dicts/listas a un string JSON.",
            "para_que": "Enviar datos por red o guardar JSON como texto.",
            "sintaxis": "texto = json.dumps(datos, indent=2)",
            "ejemplo": "json.dumps({'a': 1}) -> '{\"a\": 1}'",
            "matiz": "Solo acepta tipos JSON válidos (dict, list, str, int, float, bool, None).",
        },
    },
    "json.loads": {
        "tooltip": "Función que convierte texto JSON a objetos Python.",
        "definition_parts": {
            "que_es": "Convierte un string JSON en dicts/listas de Python.",
            "para_que": "Leer JSON recibido desde archivos o APIs.",
            "sintaxis": "datos = json.loads(texto)",
            "ejemplo": "json.loads('{\"a\": 1}') -> {'a': 1}",
            "matiz": "Lanza JSONDecodeError si el texto no es JSON válido.",
        },
    },
    "json.dump": {
        "tooltip": "Función que escribe JSON en un archivo abierto.",
        "definition_parts": {
            "que_es": "Serializa datos y los escribe directo en un archivo.",
            "para_que": "Guardar JSON sin llamar a write() manualmente.",
            "sintaxis": "json.dump(datos, archivo, indent=2)",
            "ejemplo": "json.dump({'ok': True}, archivo)",
            "matiz": "El archivo debe estar abierto en modo escritura.",
        },
    },
    "json.load": {
        "tooltip": "Función que lee JSON desde un archivo abierto.",
        "definition_parts": {
            "que_es": "Lee un archivo y devuelve los datos como dict/list.",
            "para_que": "Cargar JSON directo desde archivos.",
            "sintaxis": "datos = json.load(archivo)",
            "ejemplo": "with open('data.json') as f: datos = json.load(f)",
            "matiz": "El archivo debe estar abierto en modo lectura.",
        },
    },
    "kernel": {
        "tooltip": "Proceso que ejecuta el código en un notebook.",
        "definition_parts": {
            "que_es": (
                "Un kernel es el proceso que ejecuta el código de un notebook y "
                "mantiene el estado (variables, imports y resultados)."
            ),
            "para_que": (
                "Se usa para conectar notebooks a distintos lenguajes o entornos, "
                "como Python, R o Julia."
            ),
            "sintaxis": "python3, ipykernel o selección de kernel en Jupyter",
            "ejemplo": (
                "Cambiar el kernel a un entorno con pandas instalado para ejecutar "
                "celdas correctamente."
            ),
            "matiz": (
                "Si el kernel se reinicia, se pierden variables y hay que re-ejecutar "
                "las celdas."
            ),
        },
    },
    "celda": {
        "tooltip": "Unidad básica de ejecución en un notebook.",
        "definition_parts": {
            "que_es": (
                "Una celda es un bloque de contenido en un notebook, ya sea de código "
                "o texto (markdown)."
            ),
            "para_que": (
                "Se usa para ejecutar pasos específicos y documentar cada parte del "
                "análisis de forma incremental."
            ),
            "sintaxis": "Shift+Enter para ejecutar una celda en Jupyter",
            "ejemplo": (
                "Una celda que calcula el promedio de ventas y otra que lo explica en "
                "texto con markdown."
            ),
            "matiz": (
                "El orden de ejecución puede afectar resultados si se re-ejecutan "
                "celdas fuera de secuencia."
            ),
        },
    },
    "scikit-learn": {
        "tooltip": "Librería de machine learning clásica en Python.",
        "definition_parts": {
            "que_es": (
                "Scikit-learn es una librería de Python con algoritmos de ML "
                "supervisado y no supervisado."
            ),
            "para_que": (
                "Se usa para entrenar modelos como regresión, clasificación y clustering, "
                "además de pipelines de preprocesamiento."
            ),
            "sintaxis": "from sklearn.model_selection import train_test_split",
            "ejemplo": (
                "Entrenar un modelo de regresión lineal con train_test_split y evaluar "
                "su error."
            ),
            "matiz": (
                "Es ideal para datasets medianos y prototipos; para deep learning se usan "
                "otras librerías."
            ),
        },
    },
    "tensorflow": {
        "tooltip": "Framework de deep learning de Google.",
        "definition_parts": {
            "que_es": (
                "TensorFlow es un framework para construir y entrenar redes neuronales "
                "y modelos de deep learning."
            ),
            "para_que": (
                "Se usa en visión por computador, NLP y sistemas de recomendación con "
                "aceleración por GPU/TPU."
            ),
            "sintaxis": "import tensorflow as tf; modelo = tf.keras.Sequential([...])",
            "ejemplo": (
                "Entrenar una red neuronal con Keras para clasificar imágenes."
            ),
            "matiz": (
                "Tiene un ecosistema amplio, pero su curva de aprendizaje puede ser "
                "mayor que en librerías más ligeras."
            ),
        },
    },
    "pytorch": {
        "tooltip": "Framework de deep learning con enfoque dinámico.",
        "definition_parts": {
            "que_es": (
                "PyTorch es un framework de deep learning con grafos dinámicos y una "
                "API flexible para investigación."
            ),
            "para_que": (
                "Se usa para prototipar y entrenar modelos de redes neuronales con "
                "gran control sobre el entrenamiento."
            ),
            "sintaxis": "import torch; modelo = torch.nn.Linear(10, 1)",
            "ejemplo": (
                "Definir un modelo con torch.nn.Module y entrenarlo con un loop "
                "personalizado."
            ),
            "matiz": (
                "Su flexibilidad facilita la investigación, pero requiere disciplina "
                "para mantener código consistente en producción."
            ),
        },
    },
    "ciencia de datos": {
        "tooltip": "Disciplina que extrae valor de datos con estadística y programación.",
        "definition_parts": {
            "que_es": (
                "La ciencia de datos combina estadística, programación y conocimiento del "
                "dominio para transformar datos en conocimiento accionable. Abarca "
                "recolección, limpieza, análisis, modelado y comunicación."
            ),
            "para_que": (
                "Se usa para analizar tendencias, construir modelos predictivos, "
                "segmentar clientes, automatizar reportes y apoyar decisiones estratégicas, "
                "combinando análisis descriptivo y predictivo."
            ),
            "sintaxis": "df = pandas.read_csv('ventas.csv')",
            "ejemplo": (
                "Explorar un dataset de ventas con pandas y matplotlib para generar "
                "KPIs, detectar estacionalidad y proponer acciones comerciales."
            ),
            "matiz": (
                "La limpieza, validación y comunicación de resultados son tan importantes "
                "como el modelo en sí. La ética y la privacidad también influyen en "
                "cómo se usan los datos."
            ),
        },
    },
    "data science": {
        "tooltip": "Nombre en inglés de ciencia de datos.",
        "definition_parts": {
            "que_es": (
                "Data science es la disciplina que combina análisis estadístico, "
                "programación, visualización y narrativa para extraer insights y "
                "aplicar modelos predictivos o descriptivos a partir de datos."
            ),
            "para_que": (
                "Se usa para entender fenómenos, detectar patrones, construir modelos "
                "predictivos y comunicar hallazgos al negocio, desde análisis exploratorio "
                "hasta experimentación."
            ),
            "sintaxis": "data science (dos palabras en inglés)",
            "ejemplo": (
                "Analizar churn de clientes, entrenar un modelo de clasificación y "
                "proponer acciones para reducir la pérdida, comunicando resultados con "
                "dashboards."
            ),
            "matiz": (
                "La calidad de datos y el contexto del negocio determinan el valor real "
                "de los resultados. Un buen data science incluye storytelling y métricas "
                "de impacto."
            ),
        },
    },
    "data cience": {
        "tooltip": "Variante común con error de escritura de data science.",
        "definition_parts": {
            "que_es": (
                "Data cience es una escritura incorrecta de data science (ciencia de datos)."
            ),
            "para_que": (
                "Aparece en búsquedas o conversaciones informales, pero el término correcto "
                "es data science."
            ),
            "sintaxis": "data science (forma correcta)",
            "ejemplo": (
                "Escribir \"data cience\" al buscar cursos de ciencia de datos en la web "
                "y corregirlo para encontrar más resultados."
            ),
            "matiz": (
                "Conviene corregirlo en documentación y presentaciones formales para evitar "
                "confusiones y para mejorar la visibilidad de recursos reales."
            ),
        },
    },
    "data engineering": {
        "tooltip": "Disciplina centrada en construir y operar sistemas de datos.",
        "definition_parts": {
            "que_es": (
                "Data engineering se enfoca en diseñar pipelines, arquitecturas y "
                "plataformas que ingieren, transforman y sirven datos confiables."
            ),
            "para_que": (
                "Se usa para habilitar análisis y modelos mediante ETLs/ELTs, "
                "catálogos, calidad de datos, orquestación y gobernanza."
            ),
            "sintaxis": (
                "spark.read.parquet('s3://bucket/datos') o DAGs en Airflow"
            ),
            "ejemplo": (
                "Construir un pipeline que toma logs de una app, los limpia, los "
                "carga en un data warehouse y actualiza dashboards diarios."
            ),
            "matiz": (
                "La confiabilidad depende de monitoreo, tests de calidad y manejo "
                "de backfills, no solo de mover datos."
            ),
        },
    },
    "machine learning": {
        "tooltip": "Rama de la IA que aprende patrones desde datos.",
        "definition_parts": {
            "que_es": (
                "Machine learning es una rama de la inteligencia artificial que aprende "
                "patrones desde datos para predecir, clasificar o recomendar. Incluye "
                "enfoques supervisados, no supervisados y por refuerzo."
            ),
            "para_que": (
                "Se usa en motores de recomendación, detección de fraude, visión por "
                "computador, NLP, pronósticos y mantenimiento predictivo. También se "
                "aplica en scoring de riesgo y personalización."
            ),
            "sintaxis": "modelo.fit(X_train, y_train) y_pred = modelo.predict(X_test)",
            "ejemplo": (
                "Un modelo que predice el precio de una casa a partir de metros cuadrados, "
                "ubicación y antigüedad."
            ),
            "matiz": (
                "Requiere datos representativos, métricas claras, prevención de sobreajuste "
                "y control de sesgos. Sin un buen pipeline de validación, el rendimiento "
                "en producción puede degradarse."
            ),
        },
    },
    "mlops": {
        "tooltip": "Prácticas para operar modelos de ML en producción.",
        "definition_parts": {
            "que_es": (
                "MLOps combina ingeniería de software, data engineering y ML para "
                "desplegar, versionar y monitorear modelos en producción."
            ),
            "para_que": (
                "Se usa para automatizar entrenamiento, despliegue, pruebas, "
                "observabilidad y rollback de modelos."
            ),
            "sintaxis": "mlflow ui o pipeline en Kubeflow/Vertex AI",
            "ejemplo": (
                "Registrar modelos con MLflow, desplegarlos como API y monitorear "
                "drift y métricas de negocio."
            ),
            "matiz": (
                "Sin monitoreo de datos y modelos, el rendimiento puede degradarse "
                "aunque el código esté estable."
            ),
        },
    },
    "full stack": {
        "tooltip": "Desarrollo que cubre frontend y backend.",
        "definition_parts": {
            "que_es": (
                "Full stack describe el desarrollo integral de una aplicación: interfaz "
                "(frontend), servidor (backend), base de datos, integraciones y "
                "despliegue."
            ),
            "para_que": (
                "Se usa cuando se necesita entregar productos end-to-end en equipos pequeños "
                "o proyectos ágiles, integrando autenticación, APIs, CI/CD, monitoreo "
                "y observabilidad."
            ),
            "sintaxis": "frontend + backend + base de datos + despliegue",
            "ejemplo": (
                "Una SPA con React, una API en Python y una base PostgreSQL, todo "
                "desplegado en la nube con un pipeline de CI/CD."
            ),
            "matiz": (
                "Exige comprender integración, seguridad, rendimiento, UX y despliegue, "
                "no solo escribir código. El foco puede variar según el rol en el equipo."
            ),
        },
    },
    "fastapi": {
        "tooltip": "Framework moderno de APIs en Python.",
        "definition_parts": {
            "que_es": (
                "FastAPI es un framework de Python para construir APIs rápidas con "
                "tipado estático y validación automática."
            ),
            "para_que": (
                "Se usa para crear servicios RESTful con documentación interactiva "
                "y alto rendimiento."
            ),
            "ejemplo": (
                "Definir un endpoint con @app.get('/usuarios') y obtener datos en JSON."
            ),
            "matiz": (
                "Aprovecha Pydantic para validación, por lo que un buen diseño de "
                "modelos mejora la calidad de la API."
            ),
        },
    },
    "django": {
        "tooltip": "Framework web completo para Python.",
        "definition_parts": {
            "que_es": (
                "Django es un framework web que incluye ORM, autenticación, panel "
                "de administración y herramientas de seguridad."
            ),
            "para_que": (
                "Se usa para construir aplicaciones web robustas con desarrollo rápido "
                "y buenas prácticas integradas."
            ),
            "ejemplo": (
                "Crear un modelo de base de datos con Django ORM y exponerlo en el admin."
            ),
            "matiz": (
                "Su estructura es opinionada, lo cual acelera proyectos pero puede "
                "limitar personalizaciones profundas."
            ),
        },
    },
    "flask": {
        "tooltip": "Microframework web flexible en Python.",
        "definition_parts": {
            "que_es": (
                "Flask es un microframework para construir aplicaciones web ligeras "
                "y extensibles."
            ),
            "para_que": (
                "Se usa para APIs o apps pequeñas donde se requiere control total "
                "sobre la arquitectura."
            ),
            "ejemplo": (
                "Definir un endpoint con @app.route('/') y devolver HTML simple."
            ),
            "matiz": (
                "Al ser minimalista, muchas funcionalidades se agregan con extensiones."
            ),
        },
    },
    "rest": {
        "tooltip": "Estilo de arquitectura para APIs basadas en HTTP.",
        "definition_parts": {
            "que_es": (
                "REST (Representational State Transfer) define principios para diseñar "
                "APIs basadas en recursos y operaciones HTTP."
            ),
            "para_que": (
                "Se usa para estandarizar endpoints, cachés y códigos de estado en APIs."
            ),
            "sintaxis": "GET /recursos/1, POST /recursos",
            "ejemplo": (
                "GET /productos obtiene recursos, POST /productos crea uno nuevo."
            ),
            "matiz": (
                "REST no es un protocolo; es un estilo de diseño que puede aplicarse "
                "con distintos niveles de rigor."
            ),
        },
    },
    "graphql": {
        "tooltip": "Lenguaje de consultas para APIs.",
        "definition_parts": {
            "que_es": (
                "GraphQL es un lenguaje de consultas y runtime para APIs que permite "
                "pedir exactamente los datos necesarios."
            ),
            "para_que": (
                "Se usa para reducir over-fetching y unificar múltiples fuentes de datos "
                "en una sola API."
            ),
            "sintaxis": "query { usuarios { id nombre } }",
            "ejemplo": (
                "Consultar usuarios { id, nombre, pedidos { total } } en una sola petición."
            ),
            "matiz": (
                "Requiere diseño cuidadoso de esquemas y control de consultas complejas."
            ),
        },
    },
    "pyside": {
        "tooltip": "Bindings de Qt para crear interfaces gráficas en Python.",
        "definition_parts": {
            "que_es": (
                "PySide es el conjunto oficial de bindings de Qt para Python, "
                "incluyendo PySide6 para Qt 6. Permite usar widgets y QML desde Python."
            ),
            "para_que": (
                "Se usa para crear aplicaciones de escritorio con ventanas, formularios, "
                "tablas y componentes interactivos multiplataforma."
            ),
            "sintaxis": (
                "from PySide6.QtWidgets import QApplication, QWidget"
            ),
            "ejemplo": (
                "Diseñar una UI en Qt Designer y cargar el archivo .ui en una app "
                "PySide6 para crear un formulario de captura de datos."
            ),
            "matiz": (
                "Utiliza señales y slots para comunicar widgets de forma desacoplada y "
                "permite integrar temas y recursos del ecosistema Qt. El empaquetado "
                "para distribución suele requerir herramientas como PyInstaller."
            ),
        },
    },
    "aws": {
        "tooltip": "Plataforma cloud de Amazon con múltiples servicios.",
        "definition_parts": {
            "que_es": (
                "AWS (Amazon Web Services) es la plataforma cloud de Amazon con servicios "
                "de cómputo, almacenamiento, redes, datos e IA."
            ),
            "para_que": (
                "Se usa para desplegar aplicaciones, escalar sistemas y operar "
                "infraestructura global con herramientas administradas. Incluye "
                "opciones de serverless, contenedores, redes privadas y analítica."
            ),
            "sintaxis": "aws s3 ls o boto3.client('s3')",
            "ejemplo": (
                "EC2 para servidores, S3 para almacenamiento, RDS para bases de datos y "
                "CloudFront para distribución de contenido, integrados en una arquitectura "
                "con VPC e IAM."
            ),
            "matiz": (
                "El costo es bajo demanda y depende de región, uso, arquitectura y "
                "políticas de optimización. Un buen diseño de IAM y VPC impacta la "
                "seguridad y el mantenimiento."
            ),
        },
    },
    "aws fargate": {
        "tooltip": "Servicio serverless para ejecutar contenedores en AWS.",
        "definition_parts": {
            "que_es": (
                "AWS Fargate es un motor de ejecución para contenedores que elimina la "
                "necesidad de administrar servidores en ECS o EKS."
            ),
            "para_que": (
                "Se usa para ejecutar workloads en contenedores con escalado automático, "
                "pagando por recursos consumidos."
            ),
            "sintaxis": "aws ecs run-task --launch-type FARGATE",
            "ejemplo": (
                "Desplegar un servicio API en ECS sin gestionar instancias EC2."
            ),
            "matiz": (
                "Necesita configurar subredes, roles IAM y límites de recursos para evitar "
                "sobrecostos."
            ),
        },
    },
    "oracle cloud": {
        "tooltip": "Plataforma cloud de Oracle (OCI).",
        "definition_parts": {
            "que_es": (
                "Oracle Cloud Infrastructure (OCI) es la plataforma cloud de Oracle "
                "con servicios de cómputo, bases de datos y redes."
            ),
            "para_que": (
                "Desplegar aplicaciones, usar bases de datos administradas y construir "
                "arquitecturas empresariales en la nube."
            ),
            "sintaxis": "oci os object list --bucket-name mi-bucket",
            "ejemplo": (
                "Usar OCI Compute para instancias y Oracle Autonomous Database para "
                "gestionar datos sin operación manual."
            ),
            "matiz": (
                "Su integración con bases Oracle es un punto fuerte, pero conviene "
                "comparar costos y servicios según región."
            ),
        },
    },
    "ibm cloud": {
        "tooltip": "Plataforma cloud de IBM para servicios empresariales.",
        "definition_parts": {
            "que_es": (
                "IBM Cloud ofrece servicios de cómputo, datos, IA y herramientas "
                "empresariales con enfoque híbrido."
            ),
            "para_que": (
                "Construir soluciones cloud e híbridas, desplegar contenedores y usar "
                "servicios gestionados de datos."
            ),
            "sintaxis": "ibmcloud login y ibmcloud ks cluster ls",
            "ejemplo": (
                "Crear un cluster de Kubernetes con IBM Cloud Kubernetes Service y "
                "conectar servicios de base de datos."
            ),
            "matiz": (
                "Es popular en entornos corporativos y requiere considerar integración "
                "con sistemas legacy."
            ),
        },
    },
    "alibaba cloud": {
        "tooltip": "Plataforma cloud de Alibaba con presencia global.",
        "definition_parts": {
            "que_es": (
                "Alibaba Cloud es la plataforma de nube de Alibaba con servicios de "
                "cómputo, almacenamiento y analítica."
            ),
            "para_que": (
                "Desplegar aplicaciones en mercados asiáticos, usar CDN global y "
                "servicios de datos escalables."
            ),
            "sintaxis": "aliyun oss ls",
            "ejemplo": (
                "Guardar archivos en OSS y distribuirlos con CDN para mejorar la "
                "latencia."
            ),
            "matiz": (
                "Su fortaleza está en Asia, pero conviene revisar la disponibilidad "
                "regional y la documentación."
            ),
        },
    },
    "firebase": {
        "tooltip": "Plataforma cloud de Google para apps móviles y web.",
        "definition_parts": {
            "que_es": (
                "Firebase es una plataforma de Google que ofrece servicios administrados "
                "para autenticación, bases de datos y hosting."
            ),
            "para_que": (
                "Se usa para acelerar el desarrollo de apps móviles y web con backend "
                "serverless, notificaciones y analítica."
            ),
            "sintaxis": "firebase login y firebase deploy",
            "ejemplo": (
                "Usar Firebase Authentication para login con Google y Firestore para "
                "guardar perfiles de usuario."
            ),
            "matiz": (
                "El enfoque serverless reduce la operación, pero puede generar dependencia "
                "del proveedor y costos por lectura/escritura."
            ),
        },
    },
    "supabase": {
        "tooltip": "Backend como servicio basado en PostgreSQL.",
        "definition_parts": {
            "que_es": (
                "Supabase es una plataforma open source que ofrece base de datos "
                "PostgreSQL, autenticación y almacenamiento."
            ),
            "para_que": (
                "Se usa para crear backends rápidos con APIs REST/GraphQL automáticas "
                "y gestión de usuarios."
            ),
            "sintaxis": "supabase init y supabase db push",
            "ejemplo": (
                "Crear una tabla de tareas y consultar datos desde un frontend con "
                "las SDKs de Supabase."
            ),
            "matiz": (
                "Permite autohospedaje, pero el control de permisos y políticas RLS "
                "requiere diseño cuidadoso."
            ),
        },
    },
    "heroku": {
        "tooltip": "Plataforma PaaS para desplegar aplicaciones rápidamente.",
        "definition_parts": {
            "que_es": (
                "Heroku es una plataforma como servicio que simplifica el despliegue de "
                "apps con buildpacks y escalado básico."
            ),
            "para_que": (
                "Se usa para publicar apps web y APIs sin gestionar infraestructura, "
                "ideal para prototipos y MVPs."
            ),
            "sintaxis": "heroku create y git push heroku main",
            "ejemplo": (
                "Hacer push de una app Flask y desplegarla con un Procfile en minutos."
            ),
            "matiz": (
                "Su simplicidad reduce control sobre la infraestructura y puede elevar "
                "costos a gran escala."
            ),
        },
    },
    "render": {
        "tooltip": "Plataforma cloud para desplegar servicios y webs.",
        "definition_parts": {
            "que_es": (
                "Render es un proveedor cloud que facilita despliegues de servicios, "
                "bases de datos y sitios estáticos."
            ),
            "para_que": (
                "Se usa para desplegar apps con pipelines Git, HTTPS automático y "
                "escalado sencillo."
            ),
            "sintaxis": "render.yaml o despliegue conectado a Git",
            "ejemplo": (
                "Desplegar una API FastAPI conectada a PostgreSQL con despliegue continuo."
            ),
            "matiz": (
                "El rendimiento y límites dependen del plan; conviene revisar cuotas y "
                "regiones disponibles."
            ),
        },
    },
    "cloudwatch": {
        "tooltip": "Servicio de monitoreo y métricas en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon CloudWatch es un servicio de observabilidad que recopila métricas, "
                "logs y eventos de recursos en AWS."
            ),
            "para_que": (
                "Se usa para monitorear rendimiento, crear alarmas y visualizar dashboards "
                "de infraestructura y aplicaciones."
            ),
            "sintaxis": "aws cloudwatch put-metric-alarm --alarm-name ...",
            "ejemplo": (
                "Configurar una alarma cuando la CPU de una instancia EC2 supera el 80%."
            ),
            "matiz": (
                "Los costos dependen del volumen de métricas y logs, por lo que conviene "
                "definir retención y filtros."
            ),
        },
    },
    "ecs": {
        "tooltip": "Servicio de orquestación de contenedores en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon ECS (Elastic Container Service) es un orquestador de contenedores "
                "administrado por AWS."
            ),
            "para_que": (
                "Se usa para desplegar y escalar contenedores con integración a servicios "
                "como ALB, IAM y CloudWatch."
            ),
            "sintaxis": "aws ecs create-cluster y aws ecs create-service",
            "ejemplo": (
                "Ejecutar microservicios en contenedores usando Fargate sin administrar "
                "servidores."
            ),
            "matiz": (
                "Ofrece modelos con EC2 o Fargate; la elección impacta costos y control "
                "operativo."
            ),
        },
    },
    "ecr": {
        "tooltip": "Registro de contenedores administrado en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon ECR (Elastic Container Registry) almacena imágenes de contenedores "
                "privadas o públicas."
            ),
            "para_que": (
                "Se usa para versionar y distribuir imágenes Docker dentro de AWS."
            ),
            "sintaxis": "aws ecr create-repository y docker push ...",
            "ejemplo": (
                "Publicar una imagen y luego desplegarla en ECS o EKS."
            ),
            "matiz": (
                "Conviene automatizar el escaneo de vulnerabilidades y la rotación "
                "de versiones."
            ),
        },
    },
    "cloudformation": {
        "tooltip": "Infraestructura como código en AWS.",
        "definition_parts": {
            "que_es": (
                "AWS CloudFormation permite definir infraestructura con plantillas "
                "YAML/JSON."
            ),
            "para_que": (
                "Se usa para crear, actualizar y versionar recursos de forma reproducible."
            ),
            "sintaxis": "aws cloudformation deploy --template-file stack.yaml",
            "ejemplo": (
                "Provisionar una VPC con subredes y una instancia EC2 desde una plantilla."
            ),
            "matiz": (
                "Las plantillas pueden volverse complejas, por lo que modularizar ayuda "
                "a mantenerlas."
            ),
        },
    },
    "route 53": {
        "tooltip": "Servicio DNS administrado de AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon Route 53 es un servicio de DNS y enrutamiento de tráfico global."
            ),
            "para_que": (
                "Se usa para gestionar dominios, balancear tráfico y hacer failover "
                "entre regiones."
            ),
            "sintaxis": "aws route53 change-resource-record-sets --hosted-zone-id ...",
            "ejemplo": (
                "Configurar registros A y CNAME para apuntar un dominio a un balanceador."
            ),
            "matiz": (
                "Incluye políticas de routing avanzadas que requieren pruebas antes de "
                "producción."
            ),
        },
    },
    "s3": {
        "tooltip": "Servicio de almacenamiento de objetos en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon S3 es un servicio de almacenamiento de objetos que organiza "
                "archivos en buckets con alta durabilidad y escalabilidad."
            ),
            "para_que": (
                "Se usa para backups, archivos estáticos, data lakes, logs y "
                "almacenamiento de datasets para análisis y machine learning."
            ),
            "sintaxis": "aws s3 cp archivo.csv s3://mi-bucket/datasets/",
            "ejemplo": (
                "Guardar imágenes de una app web y servirlas vía CloudFront o almacenar "
                "datos crudos de ventas para analítica."
            ),
            "matiz": (
                "No es un sistema de archivos tradicional: su acceso es por objetos y "
                "permite políticas de permisos, versiones y clases de almacenamiento."
            ),
        },
    },
    "ec2": {
        "tooltip": "Servicio de máquinas virtuales en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon EC2 provee instancias virtuales configurables para ejecutar "
                "aplicaciones y servicios en la nube."
            ),
            "para_que": (
                "Se usa cuando necesitas control sobre el sistema operativo, el "
                "runtime o la red, por ejemplo para APIs, workers o workloads legacy."
            ),
            "sintaxis": "aws ec2 describe-instances",
            "ejemplo": (
                "Desplegar una API en Linux con Nginx y autoescalado basado en CPU."
            ),
            "matiz": (
                "Requiere gestionar parches, seguridad, escalado y costos por hora o "
                "por segundo, por lo que conviene automatizar con scripts o IaC."
            ),
        },
    },
    "rds": {
        "tooltip": "Servicio administrado de bases de datos en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon RDS es un servicio administrado de bases de datos relacionales "
                "como PostgreSQL, MySQL o MariaDB."
            ),
            "para_que": (
                "Se usa para tener backups, parches y alta disponibilidad gestionados "
                "por AWS, reduciendo la carga operativa."
            ),
            "sintaxis": "aws rds describe-db-instances",
            "ejemplo": (
                "Base de datos transaccional para una app con réplicas de lectura y "
                "respaldo automático."
            ),
            "matiz": (
                "Simplifica la operación, pero limita ciertas configuraciones y "
                "extensiones dependiendo del motor."
            ),
        },
    },
    "lambda": {
        "tooltip": "Servicio serverless para ejecutar funciones en AWS.",
        "definition_parts": {
            "que_es": (
                "AWS Lambda ejecuta funciones bajo demanda sin gestionar servidores."
            ),
            "para_que": (
                "Se usa para tareas event-driven como procesar archivos, ejecutar "
                "webhooks o automatizar flujos con bajo costo inicial."
            ),
            "sintaxis": "aws lambda invoke --function-name procesar-imagen out.json",
            "ejemplo": (
                "Procesar imágenes cuando se suben a S3 o enviar una alerta al detectar "
                "un error en logs."
            ),
            "matiz": (
                "Tiene límites de tiempo, memoria y cold starts; conviene diseñar "
                "funciones pequeñas y medir latencias."
            ),
        },
    },
    "sagemaker": {
        "tooltip": "Servicio de AWS para construir y desplegar modelos de ML.",
        "definition_parts": {
            "que_es": (
                "Amazon SageMaker es una plataforma administrada para entrenar, "
                "ajustar, desplegar y monitorizar modelos de machine learning."
            ),
            "para_que": (
                "Se usa para acelerar el ciclo de ML con notebooks, jobs de "
                "entrenamiento, pipelines y endpoints de inferencia."
            ),
            "sintaxis": "boto3.client('sagemaker').create_training_job(...)",
            "ejemplo": (
                "Entrenar un modelo de clasificación y desplegarlo como endpoint "
                "para inferencias en tiempo real."
            ),
            "matiz": (
                "Integra monitoreo de drift y pipelines, pero requiere control de "
                "costos y versionado de datos/modelos."
            ),
        },
    },
    "dynamodb": {
        "tooltip": "Base de datos NoSQL administrada de AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon DynamoDB es una base de datos NoSQL key-value y documental, "
                "administrada y altamente escalable."
            ),
            "para_que": (
                "Se usa para aplicaciones con alta lectura/escritura, baja latencia "
                "y necesidades de escalado automático."
            ),
            "sintaxis": "aws dynamodb put-item --table-name sesiones --item ...",
            "ejemplo": (
                "Guardar sesiones de usuarios o catálogos de productos con acceso rápido."
            ),
            "matiz": (
                "El diseño de particiones y claves es crítico para el rendimiento y "
                "evitar hot partitions."
            ),
        },
    },
    "cloudfront": {
        "tooltip": "CDN de AWS para distribución de contenido.",
        "definition_parts": {
            "que_es": (
                "Amazon CloudFront es una red de distribución de contenido (CDN) que "
                "entrega archivos desde ubicaciones globales."
            ),
            "para_que": (
                "Se usa para acelerar sitios web, contenido estático y streaming con "
                "baja latencia y caching."
            ),
            "sintaxis": "aws cloudfront create-distribution --origin-domain-name ...",
            "ejemplo": (
                "Servir imágenes y archivos JS/CSS desde un bucket S3 como origen."
            ),
            "matiz": (
                "Requiere configurar políticas de cache y invalidaciones para balancear "
                "costos y frescura del contenido."
            ),
        },
    },
    "iam": {
        "tooltip": "Servicio de identidades y permisos en AWS.",
        "definition_parts": {
            "que_es": (
                "AWS IAM (Identity and Access Management) gestiona usuarios, roles y "
                "políticas de permisos en AWS."
            ),
            "para_que": (
                "Se usa para controlar quién puede acceder a recursos y acciones, "
                "incluyendo credenciales, roles y políticas."
            ),
            "sintaxis": "aws iam create-role --role-name lectura-s3 --assume-role-policy ...",
            "ejemplo": (
                "Un rol que permite a una Lambda leer un bucket S3 sin exponer claves."
            ),
            "matiz": (
                "Las políticas deben seguir el principio de menor privilegio y "
                "auditarse regularmente."
            ),
        },
    },
    "vpc": {
        "tooltip": "Red virtual aislada dentro de AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon VPC (Virtual Private Cloud) crea redes virtuales con subredes, "
                "tablas de rutas y controles de seguridad."
            ),
            "para_que": (
                "Se usa para aislar servicios, controlar tráfico y definir "
                "arquitecturas con redes públicas y privadas."
            ),
            "sintaxis": "aws ec2 create-vpc --cidr-block 10.0.0.0/16",
            "ejemplo": (
                "Subred privada para bases de datos y subred pública para una API."
            ),
            "matiz": (
                "Una mala configuración de rutas o security groups puede exponer "
                "recursos sensibles."
            ),
        },
    },
    "sqs": {
        "tooltip": "Cola de mensajes administrada de AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon SQS es un servicio de colas de mensajes para desacoplar "
                "componentes y procesar tareas asíncronas."
            ),
            "para_que": (
                "Se usa para absorber picos de tráfico, distribuir trabajo y "
                "controlar reintentos."
            ),
            "sintaxis": "aws sqs send-message --queue-url ... --message-body \"pedido\"",
            "ejemplo": (
                "Encolar pedidos para que workers los procesen posteriormente."
            ),
            "matiz": (
                "Garantiza entrega al menos una vez, por lo que hay que manejar "
                "duplicados en el consumidor."
            ),
        },
    },
    "sns": {
        "tooltip": "Servicio de notificaciones y pub/sub de AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon SNS es un servicio de pub/sub para publicar mensajes y "
                "distribuirlos a múltiples destinos."
            ),
            "para_que": (
                "Se usa para notificaciones, alertas y flujos event-driven hacia email, "
                "HTTP, SQS o Lambda."
            ),
            "sintaxis": "aws sns publish --topic-arn ... --message \"Alerta\"",
            "ejemplo": (
                "Enviar alertas cuando falla un proceso de datos y notificar a varios "
                "suscriptores."
            ),
            "matiz": (
                "Se integra bien con SQS y Lambda, pero requiere gobernar permisos "
                "y seguridad de los temas."
            ),
        },
    },
    "eks": {
        "tooltip": "Servicio administrado de Kubernetes en AWS.",
        "definition_parts": {
            "que_es": (
                "Amazon EKS ofrece clusters de Kubernetes gestionados con el plano "
                "de control administrado."
            ),
            "para_que": (
                "Se usa para orquestar contenedores, microservicios y workloads "
                "de larga duración con autoescalado."
            ),
            "sintaxis": "eksctl create cluster --name mi-cluster",
            "ejemplo": (
                "Desplegar microservicios en un cluster con HPA y balanceo de carga."
            ),
            "matiz": (
                "Hay costos por el control plane y requiere gestionar nodos, redes "
                "y permisos de Kubernetes."
            ),
        },
    },
    "cloud": {
        "tooltip": "Modelo de computación con recursos bajo demanda.",
        "definition_parts": {
            "que_es": (
                "La computación en la nube ofrece recursos de cómputo, almacenamiento y "
                "red bajo demanda con pago por uso."
            ),
            "para_que": (
                "Se usa para escalar sin comprar hardware, desplegar rápido en múltiples "
                "regiones y aprovechar servicios administrados."
            ),
            "sintaxis": "proveedor + servicio (ej: AWS + S3, Azure + Functions)",
            "ejemplo": (
                "Publicar una app en un proveedor cloud con balanceo y backups automáticos."
            ),
            "matiz": (
                "Los modelos IaaS, PaaS y SaaS definen el nivel de control y las "
                "responsabilidades compartidas."
            ),
        },
    },
    "iaas": {
        "tooltip": "Infraestructura como servicio.",
        "definition_parts": {
            "que_es": (
                "IaaS ofrece infraestructura virtualizada como servidores, redes y "
                "almacenamiento."
            ),
            "para_que": (
                "Se usa cuando necesitas controlar el sistema operativo, la red y el "
                "software instalado."
            ),
            "sintaxis": "VM + red + almacenamiento",
            "ejemplo": (
                "Instancias virtuales en AWS EC2 o Azure Virtual Machines."
            ),
            "matiz": (
                "El usuario administra sistema, seguridad y parches; el proveedor gestiona "
                "el hardware."
            ),
        },
    },
    "paas": {
        "tooltip": "Plataforma como servicio.",
        "definition_parts": {
            "que_es": (
                "PaaS ofrece una plataforma administrada para ejecutar aplicaciones con "
                "runtime, escalado y servicios integrados."
            ),
            "para_que": (
                "Se usa para enfocarse en el código sin administrar servidores ni "
                "infraestructura base."
            ),
            "sintaxis": "deploy app + buildpack/runtime",
            "ejemplo": "Heroku, Google App Engine o Azure App Service.",
            "matiz": (
                "Limita ciertas configuraciones, pero acelera despliegues y reduce "
                "operación."
            ),
        },
    },
    "saas": {
        "tooltip": "Software como servicio.",
        "definition_parts": {
            "que_es": (
                "SaaS es software accesible vía web sin instalación local."
            ),
            "para_que": (
                "Se usa para consumir aplicaciones listas para usar con pagos por "
                "suscripción o uso."
            ),
            "sintaxis": "login + uso desde navegador",
            "ejemplo": "Gmail, Slack o Notion.",
            "matiz": (
                "El proveedor gestiona infraestructura y actualizaciones; el usuario "
                "se centra en la configuración y uso."
            ),
        },
    },
    "azure": {
        "tooltip": "Plataforma cloud de Microsoft.",
        "definition_parts": {
            "que_es": (
                "Azure es la plataforma cloud de Microsoft con servicios de cómputo, "
                "almacenamiento, datos, IA y soluciones empresariales."
            ),
            "para_que": (
                "Se usa para cargas híbridas, integración con entornos Windows y "
                "despliegues a escala empresarial."
            ),
            "sintaxis": "az login y az webapp up",
            "ejemplo": (
                "Azure Functions para serverless y Azure SQL Database para datos."
            ),
            "matiz": (
                "Integra servicios como Active Directory y herramientas del ecosistema "
                "Microsoft."
            ),
        },
    },
    "azure devops": {
        "tooltip": "Suite de herramientas DevOps de Microsoft.",
        "definition_parts": {
            "que_es": (
                "Azure DevOps es una plataforma que integra repositorios, pipelines, "
                "tableros y gestión de artefactos."
            ),
            "para_que": (
                "Se usa para automatizar CI/CD, planificar trabajo y coordinar equipos "
                "de desarrollo."
            ),
            "sintaxis": "az devops login y az pipelines create",
            "ejemplo": (
                "Configurar un pipeline que ejecute tests y despliegue a Azure App Service."
            ),
            "matiz": (
                "Puede integrarse con GitHub, pero requiere definir bien permisos y "
                "flujos de aprobación."
            ),
        },
    },
    "azure functions": {
        "tooltip": "Servicio serverless de Azure para ejecutar funciones.",
        "definition_parts": {
            "que_es": (
                "Azure Functions permite ejecutar código bajo demanda sin gestionar "
                "servidores."
            ),
            "para_que": (
                "Se usa para automatizaciones, APIs ligeras y flujos basados en eventos."
            ),
            "sintaxis": "func init && func start",
            "ejemplo": (
                "Procesar eventos de cola o disparar tareas programadas."
            ),
            "matiz": (
                "Ofrece distintos planes de escalado y límites por ejecución."
            ),
        },
    },
    "azure app service": {
        "tooltip": "Plataforma PaaS de Azure para desplegar aplicaciones web.",
        "definition_parts": {
            "que_es": (
                "Azure App Service es un servicio administrado para alojar aplicaciones "
                "web, APIs y backends sin gestionar servidores."
            ),
            "para_que": (
                "Se usa para desplegar apps con escalado automático, certificados SSL y "
                "slots de despliegue."
            ),
            "sintaxis": "az webapp up --name mi-app --resource-group mi-grupo",
            "ejemplo": (
                "Publicar una API en Flask con un pipeline de CI/CD y un dominio propio."
            ),
            "matiz": (
                "El rendimiento y el costo dependen del plan de servicio elegido."
            ),
        },
    },
    "azure blob storage": {
        "tooltip": "Servicio de almacenamiento de objetos en Azure.",
        "definition_parts": {
            "que_es": "Azure Blob Storage almacena datos como objetos en contenedores",
            "para_que": "para archivos estáticos, backups y data lakes.",
            "sintaxis": "az storage blob upload --container-name datos --file archivo.csv",
            "ejemplo": "guardar imágenes de una app o archivos de analítica.",
            "matiz": "ofrece niveles de acceso (hot, cool, archive) según costo.",
        },
    },
    "azure sql": {
        "tooltip": "Base de datos relacional administrada en Azure.",
        "definition_parts": {
            "que_es": (
                "Azure SQL Database es un servicio administrado de bases relacionales basado en SQL "
                "Server"
            ),
            "para_que": "para aplicaciones transaccionales.",
            "sintaxis": "az sql db create --name mi-db --server mi-servidor",
            "ejemplo": "base de datos para un ERP con alta disponibilidad.",
            "matiz": "ofrece escalado elástico y backups automáticos.",
        },
    },
    "gcp": {
        "tooltip": "Google Cloud Platform para servicios en la nube.",
        "definition_parts": {
            "que_es": (
                "GCP es la plataforma cloud de Google con servicios de cómputo, datos y "
                "machine learning."
            ),
            "para_que": (
                "Se usa para análisis a gran escala, procesamiento de eventos y "
                "despliegues rápidos."
            ),
            "sintaxis": "gcloud auth login y gcloud run deploy",
            "ejemplo": (
                "BigQuery para análisis y Cloud Run para contenedores."
            ),
            "matiz": (
                "Destaca por sus herramientas de datos y analítica."
            ),
        },
    },
    "vertex ai": {
        "tooltip": "Plataforma de ML administrado en Google Cloud.",
        "definition_parts": {
            "que_es": (
                "Vertex AI es la suite de Google Cloud para construir, entrenar y "
                "desplegar modelos de machine learning de forma administrada."
            ),
            "para_que": (
                "Se usa para MLOps, pipelines de entrenamiento, despliegue de endpoints "
                "y monitoreo de modelos."
            ),
            "sintaxis": "gcloud ai models list",
            "ejemplo": (
                "Entrenar un modelo de clasificación y exponerlo como endpoint para una API."
            ),
            "matiz": (
                "Integra servicios como BigQuery y AutoML, pero requiere gobernanza de datos."
            ),
        },
    },
    "cloudflare": {
        "tooltip": "Plataforma de CDN y seguridad para aplicaciones web.",
        "definition_parts": {
            "que_es": (
                "Cloudflare es una plataforma de CDN, DNS y seguridad que protege "
                "y acelera sitios web."
            ),
            "para_que": (
                "Se usa para reducir latencia, mitigar ataques DDoS y gestionar "
                "reglas de firewall en el borde."
            ),
            "sintaxis": "configurar DNS en el panel de Cloudflare",
            "ejemplo": (
                "Activar caché global y WAF para un sitio que recibe tráfico internacional."
            ),
            "matiz": (
                "El rendimiento depende de una correcta configuración de caché y "
                "políticas de seguridad."
            ),
        },
    },
    "vercel": {
        "tooltip": "Plataforma cloud para frontends y deployments rápidos.",
        "definition_parts": {
            "que_es": (
                "Vercel es una plataforma que despliega aplicaciones frontend y "
                "serverless con enfoque en frameworks como Next.js."
            ),
            "para_que": (
                "Se usa para publicar sitios estáticos y apps web con CI/CD automático "
                "y previews por cada rama."
            ),
            "sintaxis": "vercel deploy o integración con Git",
            "ejemplo": (
                "Desplegar una app Next.js con preview URLs por pull request."
            ),
            "matiz": (
                "Es muy cómoda para frontends, pero para backends complejos se suele "
                "combinar con otros servicios."
            ),
        },
    },
    "netlify": {
        "tooltip": "Plataforma cloud para sitios estáticos y funciones.",
        "definition_parts": {
            "que_es": (
                "Netlify es una plataforma para desplegar sitios estáticos y funciones "
                "serverless con integración a Git."
            ),
            "para_que": (
                "Se usa para publicar landing pages, documentación y SPAs con "
                "despliegues automáticos."
            ),
            "sintaxis": "netlify deploy o integración con Git",
            "ejemplo": (
                "Conectar un repositorio y desplegar automáticamente cada commit."
            ),
            "matiz": (
                "Las funciones serverless tienen límites de ejecución que hay que "
                "considerar en apps más complejas."
            ),
        },
    },
    "digitalocean": {
        "tooltip": "Proveedor cloud con enfoque simple para desarrolladores.",
        "definition_parts": {
            "que_es": (
                "DigitalOcean ofrece infraestructura cloud con un enfoque sencillo y "
                "planes predecibles."
            ),
            "para_que": (
                "Se usa para desplegar VPS, bases de datos administradas y "
                "contenedores con baja complejidad."
            ),
            "sintaxis": "doctl compute droplet create mi-droplet",
            "ejemplo": (
                "Crear un droplet para alojar una API con Docker y Nginx."
            ),
            "matiz": (
                "Es más simple que hiperescalares, pero tiene menos servicios avanzados."
            ),
        },
    },
    "cloud storage": {
        "tooltip": "Almacenamiento de objetos en Google Cloud.",
        "definition_parts": {
            "que_es": "Google Cloud Storage almacena objetos en buckets con alta durabilidad",
            "para_que": "para datos estáticos, backups y data lakes.",
            "sintaxis": "gsutil cp archivo.csv gs://mi-bucket/datos/",
            "ejemplo": "guardar archivos de un sistema de analítica.",
            "matiz": "permite definir clases de almacenamiento según costo y acceso.",
        },
    },
    "cloud run": {
        "tooltip": "Servicio de GCP para ejecutar contenedores.",
        "definition_parts": {
            "que_es": "Cloud Run ejecuta contenedores HTTP de forma serverless",
            "para_que": "para desplegar APIs y servicios sin administrar servidores.",
            "sintaxis": "gcloud run deploy mi-servicio --source .",
            "ejemplo": "publicar un contenedor con FastAPI en GCP.",
            "matiz": "escala a cero y se cobra por uso real.",
        },
    },
    "bigquery": {
        "tooltip": "Data warehouse administrado de Google Cloud.",
        "definition_parts": {
            "que_es": "BigQuery es un data warehouse serverless para consultas SQL a gran escala",
            "para_que": "para analítica de grandes volúmenes de datos.",
            "sintaxis": "bq query --use_legacy_sql=false \"SELECT ...\"",
            "ejemplo": "consultas sobre terabytes de logs en segundos.",
            "matiz": "cobra por almacenamiento y por volumen de datos consultados.",
        },
    },
    "cloud sql": {
        "tooltip": "Base de datos relacional administrada en GCP.",
        "definition_parts": {
            "que_es": "Cloud SQL es el servicio de bases de datos relacionales gestionadas de GCP",
            "para_que": "para ejecutar PostgreSQL, MySQL o SQL Server sin administrar servidores.",
            "sintaxis": "gcloud sql instances create mi-db --database-version=POSTGRES_15",
            "ejemplo": "base transaccional para un backend web.",
            "matiz": "ofrece backups automáticos y alta disponibilidad.",
        },
    },
    "cloud functions": {
        "tooltip": "Servicio serverless de GCP para ejecutar funciones.",
        "definition_parts": {
            "que_es": "Cloud Functions permite ejecutar funciones bajo demanda en Google Cloud",
            "para_que": "para responder a eventos de almacenamiento, pub/sub o HTTP.",
            "sintaxis": "gcloud functions deploy procesar --runtime python311 --trigger-http",
            "ejemplo": "procesar un archivo al subirlo a Cloud Storage.",
            "matiz": "escala automáticamente y se cobra por invocación.",
        },
    },
    "pub/sub": {
        "tooltip": "Mensajería pub/sub en Google Cloud.",
        "definition_parts": {
            "que_es": "Pub/Sub es un servicio de mensajería asíncrona con productores y suscriptores",
            "para_que": "para desacoplar sistemas y procesar eventos.",
            "sintaxis": "gcloud pubsub topics create eventos",
            "ejemplo": "un servicio publica eventos y varios consumidores los procesan.",
            "matiz": "soporta reintentos y ordenamiento según configuración.",
        },
    },
    "serverless": {
        "tooltip": "Ejecución de código sin gestionar servidores.",
        "definition_parts": {
            "que_es": "Serverless es un modelo donde ejecutas funciones bajo demanda sin administrar servidores",
            "para_que": "para tareas event-driven y escalado automático.",
            "sintaxis": "función + trigger (HTTP, cola, storage)",
            "ejemplo": "AWS Lambda o Azure Functions.",
            "matiz": "suele tener límites de tiempo y recursos.",
        },
    },
    "data lake": {
        "tooltip": "Repositorio de datos crudos a gran escala.",
        "definition_parts": {
            "que_es": (
                "Un data lake es un repositorio que almacena datos en su formato original para análisis "
                "futuro"
            ),
            "para_que": "para centralizar datos heterogéneos.",
            "ejemplo": "almacenar archivos parquet y JSON en S3 para analítica.",
            "matiz": "requiere gobernanza para evitar convertirse en un \"data swamp\".",
        },
    },
    "data warehouse": {
        "tooltip": "Almacén de datos optimizado para analítica.",
        "definition_parts": {
            "que_es": "Un data warehouse organiza datos estructurados para consultas analíticas",
            "para_que": "para reportes, BI y métricas de negocio.",
            "ejemplo": "consolidar ventas en BigQuery o Snowflake.",
            "matiz": "suele incluir modelos dimensionales y procesos ETL/ELT.",
        },
    },
    "etl": {
        "tooltip": "Proceso de extraer, transformar y cargar datos.",
        "definition_parts": {
            "que_es": (
                "ETL (Extract, Transform, Load) es un flujo para mover datos desde fuentes a un destino "
                "analítico"
            ),
            "para_que": "para limpiar y estructurar información.",
            "ejemplo": "extraer CSVs, transformar columnas y cargar a un data warehouse.",
            "matiz": "en ELT se carga primero y se transforma después.",
        },
    },
    "feature engineering": {
        "tooltip": "Creación de variables útiles para modelos de ML.",
        "definition_parts": {
            "que_es": (
                "Feature engineering es el proceso de crear o transformar variables para mejorar el "
                "rendimiento de un modelo"
            ),
            "para_que": "para capturar patrones relevantes del dominio.",
            "ejemplo": "convertir fechas en día de la semana o crear la variable ingreso_por_persona.",
            "matiz": "debe evitar fugas de información (data leakage).",
        },
    },
    "api": {
        "tooltip": "Interfaz para que sistemas se comuniquen.",
        "definition_parts": {
            "que_es": "Una API (Application Programming Interface) define cómo dos sistemas intercambian datos",
            "para_que": "para exponer funcionalidades de un servicio.",
            "ejemplo": "una API REST que devuelve JSON con pedidos de clientes.",
            "matiz": "requiere versionado y autenticación para ser estable y segura.",
        },
    },
    "frontend": {
        "tooltip": "Parte visual e interactiva de una aplicación.",
        "definition_parts": {
            "que_es": (
                "Frontend es la capa que interactúa con el usuario: UI, estilos y lógica en el navegador "
                "o cliente"
            ),
            "para_que": "para presentar datos y capturar acciones.",
            "ejemplo": "una interfaz React que consume una API.",
            "matiz": "rendimiento y accesibilidad impactan directamente en la UX.",
        },
    },
    "backend": {
        "tooltip": "Lógica del servidor y acceso a datos.",
        "definition_parts": {
            "que_es": (
                "Backend es la capa que procesa solicitudes, aplica reglas de negocio y gestiona bases de "
                "datos"
            ),
            "para_que": "para implementar APIs y servicios internos.",
            "ejemplo": "un servicio FastAPI que valida usuarios y consulta una base.",
            "matiz": "seguridad, escalabilidad y observabilidad son claves.",
        },
    },
    "docker": {
        "tooltip": "Herramienta para crear y ejecutar contenedores.",
        "definition_parts": {
            "que_es": "Docker permite empaquetar aplicaciones con sus dependencias en contenedores",
            "para_que": "para reproducir entornos y facilitar despliegues.",
            "ejemplo": "ejecutar una API en un contenedor con Dockerfile.",
            "matiz": "los contenedores comparten el kernel del host.",
        },
    },
    "kubernetes": {
        "tooltip": "Orquestador de contenedores.",
        "definition_parts": {
            "que_es": "Kubernetes (K8s) es un sistema para orquestar contenedores",
            "para_que": "para desplegar, escalar y recuperar aplicaciones en clústeres.",
            "ejemplo": "definir Deployments y Services para una app.",
            "matiz": "requiere configuración y observabilidad para operar bien.",
        },
    },
    "logging": {
        "tooltip": "Módulo estándar para registrar eventos en una app.",
        "definition_parts": {
            "que_es": "Librería estándar de Python para registrar mensajes y errores.",
            "para_que": "para observar el comportamiento del programa sin depender de prints.",
            "sintaxis": "import logging",
            "ejemplo": "logging.basicConfig(level=logging.INFO)",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logging.basicconfig": {
        "tooltip": "Configura el logging global básico.",
        "definition_parts": {
            "que_es": "Función que define nivel y formato global del logging.",
            "para_que": "para establecer una configuración inicial sencilla.",
            "sintaxis": "logging.basicConfig(level=logging.INFO, format='...')",
            "ejemplo": "logging.basicConfig(level=logging.INFO)",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logging.getlogger": {
        "tooltip": "Obtiene un logger con nombre.",
        "definition_parts": {
            "que_es": "Función que devuelve un logger identificado por nombre.",
            "para_que": "para agrupar mensajes por módulo o dominio.",
            "sintaxis": "logger = logging.getLogger('app')",
            "ejemplo": "logger = logging.getLogger('ventas')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.info": {
        "tooltip": "Registra un mensaje informativo.",
        "definition_parts": {
            "que_es": "Método del logger para mensajes de nivel INFO.",
            "para_que": "para registrar pasos esperados del flujo.",
            "sintaxis": "logger.info('mensaje')",
            "ejemplo": "logger.info('Inicio')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.error": {
        "tooltip": "Registra un mensaje de error.",
        "definition_parts": {
            "que_es": "Método del logger para mensajes de nivel ERROR.",
            "para_que": "para registrar fallos que requieren atención.",
            "sintaxis": "logger.error('mensaje')",
            "ejemplo": "logger.error('Falló la conexión')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.exception": {
        "tooltip": "Registra un error con traceback.",
        "definition_parts": {
            "que_es": "Método del logger que incluye el traceback de la excepción actual.",
            "para_que": "para depurar errores con contexto completo.",
            "sintaxis": "logger.exception('mensaje')",
            "ejemplo": "logger.exception('Error al calcular')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.debug": {
        "tooltip": "Registra un mensaje de depuración.",
        "definition_parts": {
            "que_es": "Método del logger para mensajes de nivel DEBUG.",
            "para_que": "para inspeccionar detalles durante el desarrollo.",
            "sintaxis": "logger.debug('detalle')",
            "ejemplo": "logger.debug('Payload recibido')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.warning": {
        "tooltip": "Registra un aviso (WARNING).",
        "definition_parts": {
            "que_es": "Método del logger para mensajes de nivel WARNING.",
            "para_que": "para advertencias que no detienen la ejecución.",
            "sintaxis": "logger.warning('mensaje')",
            "ejemplo": "logger.warning('Saldo bajo')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logger.propagate": {
        "tooltip": "Controla si un logger propaga mensajes.",
        "definition_parts": {
            "que_es": "Propiedad booleana que decide si el logger envía mensajes al padre.",
            "para_que": "para evitar duplicados cuando hay handlers en la jerarquía.",
            "sintaxis": "logger.propagate = False",
            "ejemplo": "logger.propagate = True",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logging.filehandler": {
        "tooltip": "Handler que escribe logs en un archivo.",
        "definition_parts": {
            "que_es": "Clase que envía mensajes de logging a un archivo.",
            "para_que": "para guardar trazas y auditorías persistentes.",
            "sintaxis": "handler = logging.FileHandler('app.log')",
            "ejemplo": "logging.FileHandler('app.log', encoding='utf-8')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logging.streamhandler": {
        "tooltip": "Handler que envía logs a consola o stream.",
        "definition_parts": {
            "que_es": "Clase que escribe logs en stdout/stderr u otro stream.",
            "para_que": "para ver mensajes en consola o redirigirlos.",
            "sintaxis": "handler = logging.StreamHandler()",
            "ejemplo": "logging.StreamHandler()",
            "matiz": "pendiente de ampliar.",
        },
    },
    "logging.formatter": {
        "tooltip": "Define el formato de los mensajes de logging.",
        "definition_parts": {
            "que_es": "Clase que aplica formato a cada registro de log.",
            "para_que": "para controlar nivel, nombre y mensaje en la salida.",
            "sintaxis": "logging.Formatter('%(levelname)s:%(message)s')",
            "ejemplo": "logging.Formatter('%(levelname)s:%(name)s:%(message)s')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "typer": {
        "tooltip": "Librería para construir CLIs tipadas.",
        "definition_parts": {
            "que_es": "Typer es una librería basada en typer/click para crear CLIs con anotaciones.",
            "para_que": "para generar comandos, ayuda automática y validación de tipos.",
            "sintaxis": "import typer",
            "ejemplo": "app = typer.Typer()",
            "matiz": "pendiente de ampliar.",
        },
    },
    "typer.typer": {
        "tooltip": "Crea una app CLI con Typer.",
        "definition_parts": {
            "que_es": "Clase principal para agrupar comandos.",
            "para_que": "para definir subcomandos y opciones en una CLI.",
            "sintaxis": "app = typer.Typer()",
            "ejemplo": "app = typer.Typer(add_completion=False)",
            "matiz": "pendiente de ampliar.",
        },
    },
    "typer.argument": {
        "tooltip": "Define un argumento posicional.",
        "definition_parts": {
            "que_es": "Función que configura argumentos obligatorios o con validación.",
            "para_que": "para declarar parámetros posicionales con reglas.",
            "sintaxis": "typer.Argument(..., min=1)",
            "ejemplo": "personas: int = typer.Argument(..., min=1)",
            "matiz": "pendiente de ampliar.",
        },
    },
    "typer.option": {
        "tooltip": "Define una opción de línea de comando.",
        "definition_parts": {
            "que_es": "Función que declara una opción con valor por defecto y flags.",
            "para_que": "para crear parámetros opcionales con `--banderas`.",
            "sintaxis": "typer.Option(False, '--verbose')",
            "ejemplo": "ciudad: str = typer.Option('Lima', '--ciudad')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "typer.echo": {
        "tooltip": "Imprime texto con soporte CLI.",
        "definition_parts": {
            "que_es": "Función para imprimir mensajes con soporte adicional de consola.",
            "para_que": "para emitir salida coherente en apps CLI.",
            "sintaxis": "typer.echo('mensaje')",
            "ejemplo": "typer.echo('Proceso terminado')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "rich": {
        "tooltip": "Librería para imprimir texto con estilo en terminal.",
        "definition_parts": {
            "que_es": "Rich es una librería de Python para texto con colores y layouts.",
            "para_que": "para mejorar la legibilidad de CLIs con estilos y paneles.",
            "sintaxis": "from rich import print",
            "ejemplo": "print('[bold green]OK[/]')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "rich.print": {
        "tooltip": "Imprime texto con estilos de Rich.",
        "definition_parts": {
            "que_es": "Función de Rich que interpreta markup en la salida.",
            "para_que": "para imprimir texto con colores y estilos rápidos.",
            "sintaxis": "from rich import print; print('[bold]texto[/]')",
            "ejemplo": "print('[cyan]Proceso[/]')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "rich.console.console": {
        "tooltip": "Clase Console para salida avanzada en terminal.",
        "definition_parts": {
            "que_es": "Clase principal de Rich para imprimir objetos estilizados.",
            "para_que": "para controlar salida, estilos y objetos Rich.",
            "sintaxis": "from rich.console import Console; console = Console()",
            "ejemplo": "console = Console()",
            "matiz": "pendiente de ampliar.",
        },
    },
    "console.print": {
        "tooltip": "Imprime usando una instancia de Console.",
        "definition_parts": {
            "que_es": "Método de Console que imprime texto u objetos Rich.",
            "para_que": "para renderizar paneles, tablas y texto con estilo.",
            "sintaxis": "console.print('mensaje')",
            "ejemplo": "console.print('OK')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "rich.panel.panel": {
        "tooltip": "Panel para destacar texto con un recuadro.",
        "definition_parts": {
            "que_es": "Clase de Rich que envuelve texto en un panel con borde.",
            "para_que": "para resaltar mensajes o estados en la terminal.",
            "sintaxis": "from rich.panel import Panel; Panel('texto', title='Estado')",
            "ejemplo": "Panel('Listo', title='OK')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "regex": {
        "tooltip": "Patrones para buscar y validar texto.",
        "definition_parts": {
            "que_es": "Regex (expresión regular) es un patrón que describe texto.",
            "para_que": "para buscar, validar formatos y extraer partes de cadenas.",
            "sintaxis": "re.search(r'patron', texto)",
            "ejemplo": "re.search(r'\\d+', 'Pedido 123')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "expresión regular": {
        "tooltip": "Patrón que describe texto (regex).",
        "definition_parts": {
            "que_es": "Una expresión regular es un patrón para texto.",
            "para_que": "para validar, buscar y extraer información en cadenas.",
            "sintaxis": "re.findall(r'[A-Z]\\d+', texto)",
            "ejemplo": "re.findall(r'#\\w+', 'Hola #python')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "re": {
        "tooltip": "Módulo estándar para expresiones regulares.",
        "definition_parts": {
            "que_es": "Librería estándar de Python para trabajar con regex.",
            "para_que": "para buscar y extraer patrones en texto.",
            "sintaxis": "import re",
            "ejemplo": "re.search(r'\\d+', 'ID 42')",
            "matiz": "pendiente de ampliar.",
        },
    },
    "re.search": {
        "tooltip": "Busca una coincidencia en el texto.",
        "definition_parts": {
            "que_es": "Función que encuentra la primera coincidencia de un patrón.",
            "para_que": "para validar o localizar un fragmento en una cadena.",
            "sintaxis": "re.search(patron, texto)",
            "ejemplo": "re.search(r'\\d+', 'ID 42')",
            "matiz": "devuelve None si no hay coincidencia.",
        },
    },
    "re.findall": {
        "tooltip": "Devuelve todas las coincidencias del patrón.",
        "definition_parts": {
            "que_es": "Función que obtiene todas las coincidencias en una lista.",
            "para_que": "para extraer todos los fragmentos que cumplen un patrón.",
            "sintaxis": "re.findall(patron, texto)",
            "ejemplo": "re.findall(r'[A-Z]\\d+', 'A12 B34')",
            "matiz": "si hay grupos, devuelve tuplas por coincidencia.",
        },
    },
    "re.compile": {
        "tooltip": "Compila un patrón regex para reutilizarlo.",
        "definition_parts": {
            "que_es": "Función que precompila un patrón regex.",
            "para_que": "para reutilizar el patrón muchas veces con mejor rendimiento.",
            "sintaxis": "patron = re.compile(r'\\w+')",
            "ejemplo": "patron = re.compile(r'\\b\\w+\\b')",
            "matiz": "el resultado es un patrón con métodos como findall.",
        },
    },
    "pattern.findall": {
        "tooltip": "Busca todas las coincidencias con un patrón compilado.",
        "definition_parts": {
            "que_es": "Método del patrón compilado que devuelve todas las coincidencias.",
            "para_que": "para reutilizar un patrón sin recompilarlo cada vez.",
            "sintaxis": "patron.findall(texto)",
            "ejemplo": "patron.findall('hola mundo')",
            "matiz": "requiere pasar el texto como argumento.",
        },
    },
    "match.group": {
        "tooltip": "Devuelve un grupo capturado en una coincidencia.",
        "definition_parts": {
            "que_es": "Método del objeto match para obtener grupos por índice.",
            "para_que": "para extraer partes específicas del texto coincidente.",
            "sintaxis": "coincidencia.group(1)",
            "ejemplo": "re.search(r'(\\d+)', 'ID 42').group(1)",
            "matiz": "lanza error si la coincidencia es None.",
        },
    },
    "re.dotall": {
        "tooltip": "Hace que . incluya saltos de línea.",
        "definition_parts": {
            "que_es": "Bandera de regex que permite que '.' coincida con '\\n'.",
            "para_que": "para buscar texto multilínea sin perder saltos de línea.",
            "sintaxis": "re.search(patron, texto, re.DOTALL)",
            "ejemplo": "re.search(r'a.*b', 'a\\n b', re.DOTALL)",
            "matiz": "se pasa como flag a las funciones re.",
        },
    },
    "pip": {
        "tooltip": "Gestor de paquetes estándar de Python.",
        "definition_parts": {
            "que_es": "Herramienta que instala, actualiza y desinstala paquetes desde PyPI.",
            "para_que": "para gestionar dependencias de proyectos de Python.",
            "sintaxis": "python -m pip install paquete",
            "ejemplo": "python -m pip install requests",
            "matiz": "usar python -m pip asegura usar el pip del entorno activo.",
        },
    },
    "pypi": {
        "tooltip": "Repositorio oficial de paquetes de Python.",
        "definition_parts": {
            "que_es": "Python Package Index, el repositorio público de paquetes.",
            "para_que": "para encontrar e instalar librerías con pip.",
            "sintaxis": "python -m pip install paquete",
            "ejemplo": "pip instala paquetes desde PyPI por defecto.",
            "matiz": "también existen índices privados para empresas.",
        },
    },
    "python -m pip": {
        "tooltip": "Ejecuta pip usando el intérprete activo.",
        "definition_parts": {
            "que_es": "Forma recomendada de invocar pip con el Python correcto.",
            "para_que": "para evitar instalar en el Python equivocado.",
            "sintaxis": "python -m pip <comando>",
            "ejemplo": "python -m pip list",
            "matiz": "funciona igual en Windows, macOS y Linux.",
        },
    },
    "pip install": {
        "tooltip": "Instala un paquete desde PyPI.",
        "definition_parts": {
            "que_es": "Subcomando que descarga e instala paquetes.",
            "para_que": "para agregar dependencias al entorno actual.",
            "sintaxis": "python -m pip install paquete",
            "ejemplo": "python -m pip install pandas",
            "matiz": "puedes fijar versiones con ==, >= o <=.",
        },
    },
    "requests": {
        "tooltip": "Librería popular para hacer requests HTTP.",
        "definition_parts": {
            "que_es": "Biblioteca que simplifica solicitudes HTTP en Python.",
            "para_que": "para consumir APIs y descargar recursos web.",
            "sintaxis": "import requests; requests.get('https://api.example.com')",
            "ejemplo": "requests.get('https://httpbin.org/get')",
            "matiz": "en producción conviene manejar timeouts y errores de red.",
        },
    },
    "pip install -r": {
        "tooltip": "Instala dependencias desde un archivo requirements.",
        "definition_parts": {
            "que_es": "Subcomando que lee un archivo de requisitos.",
            "para_que": "para recrear un entorno con las mismas versiones.",
            "sintaxis": "python -m pip install -r requirements.txt",
            "ejemplo": "python -m pip install -r requirements.txt",
            "matiz": "fallará si el archivo no existe o la ruta es incorrecta.",
        },
    },
    "pip install --upgrade": {
        "tooltip": "Actualiza un paquete a una versión más reciente.",
        "definition_parts": {
            "que_es": "Bandera para instalar o actualizar paquetes.",
            "para_que": "para mejorar la versión de una dependencia.",
            "sintaxis": "python -m pip install --upgrade paquete",
            "ejemplo": "python -m pip install --upgrade pip",
            "matiz": "útil cuando pip está desactualizado en el entorno.",
        },
    },
    "pip list": {
        "tooltip": "Lista los paquetes instalados en el entorno.",
        "definition_parts": {
            "que_es": "Subcomando que muestra paquetes y versiones.",
            "para_que": "para inspeccionar el estado actual del entorno.",
            "sintaxis": "python -m pip list",
            "ejemplo": "python -m pip list",
            "matiz": "útil para verificar si una dependencia está instalada.",
        },
    },
    "pip freeze": {
        "tooltip": "Exporta dependencias con versiones exactas.",
        "definition_parts": {
            "que_es": "Subcomando que genera una lista reproducible.",
            "para_que": "para crear un requirements.txt.",
            "sintaxis": "python -m pip freeze > requirements.txt",
            "ejemplo": "python -m pip freeze > requirements.txt",
            "matiz": "incluye paquetes instalados de forma indirecta.",
        },
    },
    "requirements.txt": {
        "tooltip": "Archivo estándar de dependencias para pip.",
        "definition_parts": {
            "que_es": "Archivo de texto con paquetes y versiones.",
            "para_que": "para instalar dependencias de forma reproducible.",
            "sintaxis": "python -m pip install -r requirements.txt",
            "ejemplo": "requests==2.32.3",
            "matiz": "se suele regenerar con pip freeze cuando cambia el entorno.",
        },
    },
    "entorno virtual": {
        "tooltip": "Carpeta aislada con su propio Python y paquetes.",
        "definition_parts": {
            "que_es": "Un entorno independiente con dependencias propias.",
            "para_que": "para evitar conflictos entre proyectos.",
            "sintaxis": "python -m venv .venv",
            "ejemplo": "source .venv/bin/activate",
            "matiz": "debe activarse para que pip instale dentro del entorno.",
        },
    },
    "venv": {
        "tooltip": "Módulo estándar para crear entornos virtuales.",
        "definition_parts": {
            "que_es": "Módulo incluido con Python para crear entornos aislados.",
            "para_que": "para gestionar dependencias por proyecto.",
            "sintaxis": "python -m venv .venv",
            "ejemplo": "python -m venv .venv",
            "matiz": "crea la carpeta del entorno con su propio pip.",
        },
    },
    "python -m venv": {
        "tooltip": "Comando para crear un entorno virtual.",
        "definition_parts": {
            "que_es": "Invocación del módulo venv desde la terminal.",
            "para_que": "para crear un entorno aislado dentro del proyecto.",
            "sintaxis": "python -m venv nombre_entorno",
            "ejemplo": "python -m venv .venv",
            "matiz": "requiere indicar la carpeta de destino.",
        },
    },
}

def definition_text(data: dict[str, object]) -> str:
    definition = data.get("definition")
    if isinstance(definition, str) and definition.strip():
        cleaned = definition.strip()
        for label in ("Ejemplo:", "Matiz:", "Error típico:", "Ver también:", "Sintaxis:"):
            cleaned = cleaned.replace(f" {label}", f"\n{label}")
        return cleaned.strip()
    parts = data.get("definition_parts")
    if not isinstance(parts, dict):
        return ""
    parts = dict(parts)
    if not parts.get("sintaxis") and parts.get("ejemplo"):
        parts["sintaxis"] = "Ver ejemplo (forma típica)."

    def _flatten(value: object) -> str:
        if isinstance(value, list):
            return " ".join(str(item).strip() for item in value if str(item).strip())
        return str(value).strip()

    labels = {
        "que_es": "Qué es:",
        "para_que": "Para qué:",
        "sintaxis": "Sintaxis:",
        "ejemplo": "Ejemplo:",
        "matiz": "Matiz:",
        "error_tipico": "Error típico:",
        "ver_tambien": "Ver también:",
    }
    ordered_keys = [
        "que_es",
        "para_que",
        "sintaxis",
        "ejemplo",
        "matiz",
        "error_tipico",
        "ver_tambien",
    ]
    lines = []
    for key in ordered_keys:
        value = parts.get(key)
        if value:
            text = _flatten(value)
            if text:
                if key == "para_que":
                    cleaned = text.strip()
                    lower = cleaned.lower()
                    if lower.startswith("para "):
                        cleaned = cleaned[5:].strip()
                    text = cleaned
                lines.append(f"{labels.get(key, key)} {text}")
    return "\n".join(lines).strip()


def glossary_tooltip(term: str, data: dict[str, object]) -> str:
    if isinstance(data.get("tooltip"), str) and data.get("tooltip"):
        return str(data["tooltip"]).strip()
    definition = definition_text(data)
    if definition:
        return definition.splitlines()[0]
    return term


def merge_glossary(auto_terms: dict[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    merged = dict(GLOSSARY)
    for term, data in auto_terms.items():
        if term not in merged:
            merged[term] = data
    return merged


def register_auto_terms(auto_terms: dict[str, dict[str, object]]) -> None:
    for term, data in auto_terms.items():
        if term not in GLOSSARY:
            GLOSSARY[term] = data
    for term, data in auto_terms.items():
        TERMS.setdefault(term, definition_text(GLOSSARY[term]))


TERMS = {term: definition_text(data) for term, data in GLOSSARY.items()}
KEYWORDS: list[str] = list(GLOSSARY.keys())
