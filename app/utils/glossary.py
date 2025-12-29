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
            "ejemplo": "dimensiones = (1920, 1080).",
            "matiz": "una tupla de un solo elemento lleva coma: (5,).",
        },
    },
    "tuplas": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition_parts": {
            "que_es": "Las tuplas son colecciones ordenadas e inmutables",
            "para_que": "para registrar datos fijos.",
            "ejemplo": "colores = ('rojo', 'azul').",
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
            "ejemplo": "vistos = {'ana', 'luis'}.",
            "matiz": "no puedes indexar un set con [0].",
        },
    },
    "conjuntos": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition_parts": {
            "que_es": "Los conjuntos almacenan elementos únicos sin orden",
            "para_que": "para eliminar duplicados o comparar colecciones.",
            "ejemplo": "set([1, 1, 2]) produce {1, 2}.",
            "error_tipico": "pensar que mantienen el orden de inserción.",
        },
    },
    "mutable": {
        "tooltip": "Se puede modificar después de ser creado.",
        "definition_parts": {
            "que_es": "Un objeto mutable puede cambiar su contenido después de crearse",
            "para_que": "cuando necesitas actualizar datos en sitio.",
            "ejemplo": "una lista es mutable, puedes hacer lista.append(4).",
            "matiz": "mutar un objeto compartido afecta a todas las referencias.",
        },
    },
    "inmutable": {
        "tooltip": "No se puede modificar después de ser creado.",
        "definition_parts": {
            "que_es": "Un objeto inmutable no puede cambiarse; si lo 'modificas' creas otro",
            "para_que": "para valores fijos o claves de diccionario.",
            "ejemplo": "strings y tuplas son inmutables.",
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
            "ejemplo": "(x * 2 for x in range(3)) crea un generador.",
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
    "try": {
        "tooltip": "Bloque para capturar errores potenciales.",
        "definition_parts": {
            "que_es": "try delimita el código que podría fallar",
            "para_que": "junto con except para manejar errores.",
            "ejemplo": "try: abrir_archivo() except FileNotFoundError: ...",
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
            "ejemplo": "with open('a.txt') as f: leer = f.read().",
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
            "ejemplo": "una variable creada en una función no existe fuera.",
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
            "ejemplo": "dentro de una función, temp = 5.",
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
            "ejemplo": "class UsuarioPremium.",
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
            "ejemplo": "cuatro espacios antes de una línea dentro de una función.",
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
            "ejemplo": "texto[0:3] devuelve los primeros 3 caracteres.",
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
            "ejemplo": "lista.append(10).",
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
            "ejemplo": "lista.insert(1, 'nuevo').",
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
            "ejemplo": "lista.remove('a').",
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
            "ejemplo": "cursor.fetchone().",
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
            "ejemplo": "conexion.commit().",
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
            "ejemplo": "session.add(usuario); session.commit().",
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
            "ejemplo": "postgres://user:pass@localhost/db.",
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
            "ejemplo": "QVBoxLayout apila elementos en vertical.",
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
            "ejemplo": "eventos de mouse llegan al bucle.",
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
                "comunidad muy amplia."
            ),
            "para_que": (
                "Se usa en automatización, desarrollo web, ciencia de datos, scripting, "
                "IA, DevOps, QA y aplicaciones de escritorio, combinando paradigmas "
                "imperativo, orientado a objetos y funcional. También es común en "
                "herramientas de línea de comandos, APIs, ETLs y pipelines de datos."
            ),
            "sintaxis": "print('Hola') o def saludar(nombre): return f'Hola {nombre}'",
            "ejemplo": (
                "print('Hola') imprime en consola; con pandas.read_csv() puedes cargar "
                "un CSV, limpiar columnas y generar un análisis rápido."
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
    "jupyter": {
        "tooltip": "Entorno de notebooks interactivos para código y texto.",
        "definition_parts": {
            "que_es": (
                "Jupyter es un entorno interactivo que permite combinar código, texto, "
                "gráficas y resultados en un mismo documento."
            ),
            "para_que": (
                "Se usa para exploración de datos, prototipos rápidos, docencia y "
                "comunicación de análisis reproducibles."
            ),
            "ejemplo": (
                "Ejecutar un notebook .ipynb para analizar datos y visualizar gráficos "
                "paso a paso."
            ),
            "matiz": (
                "Para producción, conviene convertir notebooks en scripts o pipelines "
                "versionados."
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
                "programación, visualización y narrativa para extraer insights."
            ),
            "para_que": (
                "Se usa para entender fenómenos, detectar patrones, construir modelos "
                "predictivos y comunicar hallazgos al negocio, desde análisis exploratorio "
                "hasta experimentación."
            ),
            "sintaxis": "data science (dos palabras en inglés)",
            "ejemplo": (
                "Analizar churn de clientes, entrenar un modelo de clasificación y "
                "proponer acciones para reducir la pérdida."
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
                "Escribir \"data cience\" al buscar cursos de ciencia de datos en la web."
            ),
            "matiz": (
                "Conviene corregirlo en documentación y presentaciones formales para evitar "
                "confusiones."
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
                "(frontend), servidor (backend), base de datos y despliegue."
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
                "PySide6."
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
                "CloudFront para distribución de contenido."
            ),
            "matiz": (
                "El costo es bajo demanda y depende de región, uso, arquitectura y "
                "políticas de optimización. Un buen diseño de IAM y VPC impacta la "
                "seguridad y el mantenimiento."
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
    "azure blob storage": {
        "tooltip": "Servicio de almacenamiento de objetos en Azure.",
        "definition_parts": {
            "que_es": "Azure Blob Storage almacena datos como objetos en contenedores",
            "para_que": "para archivos estáticos, backups y data lakes.",
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
            "ejemplo": "guardar archivos de un sistema de analítica.",
            "matiz": "permite definir clases de almacenamiento según costo y acceso.",
        },
    },
    "cloud run": {
        "tooltip": "Servicio de GCP para ejecutar contenedores.",
        "definition_parts": {
            "que_es": "Cloud Run ejecuta contenedores HTTP de forma serverless",
            "para_que": "para desplegar APIs y servicios sin administrar servidores.",
            "ejemplo": "publicar un contenedor con FastAPI en GCP.",
            "matiz": "escala a cero y se cobra por uso real.",
        },
    },
    "bigquery": {
        "tooltip": "Data warehouse administrado de Google Cloud.",
        "definition_parts": {
            "que_es": "BigQuery es un data warehouse serverless para consultas SQL a gran escala",
            "para_que": "para analítica de grandes volúmenes de datos.",
            "ejemplo": "consultas sobre terabytes de logs en segundos.",
            "matiz": "cobra por almacenamiento y por volumen de datos consultados.",
        },
    },
    "cloud sql": {
        "tooltip": "Base de datos relacional administrada en GCP.",
        "definition_parts": {
            "que_es": "Cloud SQL es el servicio de bases de datos relacionales gestionadas de GCP",
            "para_que": "para ejecutar PostgreSQL, MySQL o SQL Server sin administrar servidores.",
            "ejemplo": "base transaccional para un backend web.",
            "matiz": "ofrece backups automáticos y alta disponibilidad.",
        },
    },
    "cloud functions": {
        "tooltip": "Servicio serverless de GCP para ejecutar funciones.",
        "definition_parts": {
            "que_es": "Cloud Functions permite ejecutar funciones bajo demanda en Google Cloud",
            "para_que": "para responder a eventos de almacenamiento, pub/sub o HTTP.",
            "ejemplo": "procesar un archivo al subirlo a Cloud Storage.",
            "matiz": "escala automáticamente y se cobra por invocación.",
        },
    },
    "pub/sub": {
        "tooltip": "Mensajería pub/sub en Google Cloud.",
        "definition_parts": {
            "que_es": "Pub/Sub es un servicio de mensajería asíncrona con productores y suscriptores",
            "para_que": "para desacoplar sistemas y procesar eventos.",
            "ejemplo": "un servicio publica eventos y varios consumidores los procesan.",
            "matiz": "soporta reintentos y ordenamiento según configuración.",
        },
    },
    "serverless": {
        "tooltip": "Ejecución de código sin gestionar servidores.",
        "definition_parts": {
            "que_es": "Serverless es un modelo donde ejecutas funciones bajo demanda sin administrar servidores",
            "para_que": "para tareas event-driven y escalado automático.",
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
            "matiz": "requiere gobernanza para evitar convertirse en un "data swamp".",
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


TERMS = {term: definition_text(data) for term, data in GLOSSARY.items()}
KEYWORDS = list(GLOSSARY.keys())
