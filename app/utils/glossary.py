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
        "definition": (
            "Un módulo es un archivo .py que contiene funciones, clases y variables. "
            "Se usa para organizar el código y reutilizarlo con import. "
            "Ejemplo: import math permite usar math.sqrt(9). "
            "Error típico: crear un archivo con el mismo nombre que un módulo estándar "
            "y bloquear la importación correcta."
        ),
    },
    "paquete": {
        "tooltip": "Carpeta con módulos y un __init__.py para organizar código.",
        "definition": (
            "Un paquete es una carpeta que agrupa módulos relacionados. "
            "Se usa para estructurar proyectos grandes y jerarquizar imports. "
            "Ejemplo: from mi_paquete import utilidades. "
            "Matiz: en Python clásico necesita un __init__.py para ser importable "
            "como paquete."
        ),
    },
    "parámetro": {
        "tooltip": "Nombre definido en la función para recibir valores.",
        "definition": (
            "Un parámetro es el nombre dentro de una función que recibirá un valor. "
            "Se usa para hacer funciones flexibles. "
            "Ejemplo: def sumar(a, b): return a + b. "
            "Error típico: confundir parámetro (nombre) con argumento (valor real)."
        ),
    },
    "argumento": {
        "tooltip": "Valor real que se envía a una función al llamarla.",
        "definition": (
            "Un argumento es el valor que pasas cuando llamas a una función. "
            "Se usa para alimentar los parámetros de la función. "
            "Ejemplo: sumar(2, 3) usa 2 y 3 como argumentos. "
            "Matiz: los argumentos pueden ser posicionales o con nombre."
        ),
    },
    "return": {
        "tooltip": "Palabra clave que devuelve un valor desde una función.",
        "definition": (
            "return finaliza una función y devuelve un valor al lugar donde se llamó. "
            "Se usa para producir resultados reutilizables. "
            "Ejemplo: return a + b devuelve la suma. "
            "Error típico: usar return sin valor pensando que devuelve un string vacío."
        ),
    },
    "none": {
        "tooltip": "Objeto especial que representa ausencia de valor.",
        "definition": (
            "None representa que no hay un valor válido. "
            "Se usa para indicar ausencia o resultado vacío. "
            "Ejemplo: resultado = None antes de calcular. "
            "Matiz: None no es lo mismo que 0, '' o False."
        ),
    },
    "bool": {
        "tooltip": "Tipo de dato lógico con valores True o False.",
        "definition": (
            "bool es el tipo lógico con dos valores: True o False. "
            "Se usa en condiciones y controles de flujo. "
            "Ejemplo: es_mayor = edad > 18. "
            "Error típico: comparar con 'True' en vez de evaluar la condición directa."
        ),
    },
    "int": {
        "tooltip": "Tipo numérico para enteros.",
        "definition": (
            "int representa números enteros sin decimales. "
            "Se usa para contar, indexar o iterar. "
            "Ejemplo: cantidad = 42. "
            "Matiz: dividir con / produce float aunque uses ints."
        ),
    },
    "float": {
        "tooltip": "Tipo numérico para decimales.",
        "definition": (
            "float representa números con decimales. "
            "Se usa para cálculos con precisión aproximada. "
            "Ejemplo: precio = 19.99. "
            "Error típico: comparar floats con == por problemas de precisión."
        ),
    },
    "str": {
        "tooltip": "Tipo de texto (cadena de caracteres).",
        "definition": (
            "str es el tipo de dato para texto en Python. "
            "Se usa para almacenar palabras, frases o datos formateados. "
            "Ejemplo: nombre = 'Ana'. "
            "Matiz: los strings son inmutables; no se pueden cambiar en sitio."
        ),
    },
    "list": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition": (
            "Una lista es una colección ordenada que puede cambiarse. "
            "Se usa para guardar varios elementos en un solo lugar. "
            "Ejemplo: numeros = [1, 2, 3]. "
            "Error típico: compartir la misma lista entre variables sin copiarla."
        ),
    },
    "lista": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition": (
            "Una lista es una colección ordenada que puede cambiarse. "
            "Se usa para guardar varios elementos en un solo lugar. "
            "Ejemplo: numeros = [1, 2, 3]. "
            "Error típico: modificarla mientras la recorres con un for."
        ),
    },
    "listas": {
        "tooltip": "Colección ordenada y mutable de elementos.",
        "definition": (
            "Las listas guardan elementos en orden y se pueden modificar. "
            "Se usan para agrupar datos relacionados. "
            "Ejemplo: frutas = ['manzana', 'pera']. "
            "Matiz: los índices empiezan en 0."
        ),
    },
    "tuple": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition": (
            "Una tupla es una colección ordenada que no se puede modificar. "
            "Se usa para agrupar datos fijos. "
            "Ejemplo: punto = (3, 4). "
            "Error típico: intentar hacer punto[0] = 5."
        ),
    },
    "tupla": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition": (
            "Una tupla es una colección ordenada que no se puede modificar. "
            "Se usa para datos que no deberían cambiar. "
            "Ejemplo: dimensiones = (1920, 1080). "
            "Matiz: una tupla de un solo elemento lleva coma: (5,)."
        ),
    },
    "tuplas": {
        "tooltip": "Colección ordenada e inmutable de elementos.",
        "definition": (
            "Las tuplas son colecciones ordenadas e inmutables. "
            "Se usan para registrar datos fijos. "
            "Ejemplo: colores = ('rojo', 'azul'). "
            "Error típico: pensar que son listas y tratar de modificar elementos."
        ),
    },
    "dict": {
        "tooltip": "Colección de pares clave-valor.",
        "definition": (
            "Un diccionario guarda pares clave-valor para buscar datos rápido. "
            "Se usa para mapas, configuraciones o datos estructurados. "
            "Ejemplo: edades = {'Ana': 20}. "
            "Matiz: las claves deben ser únicas e inmutables, y las búsquedas son "
            "rápidas gracias a tablas hash."
        ),
    },
    "diccionario": {
        "tooltip": "Colección de pares clave-valor.",
        "definition": (
            "Un diccionario relaciona claves con valores. "
            "Se usa para acceder a información por nombre. "
            "Ejemplo: colores = {'rojo': '#ff0000'}. "
            "Error típico: acceder a una clave inexistente y provocar KeyError."
        ),
    },
    "diccionarios": {
        "tooltip": "Colección de pares clave-valor.",
        "definition": (
            "Los diccionarios organizan datos en pares clave-valor. "
            "Se usan para búsquedas rápidas por clave. "
            "Ejemplo: precios = {'pan': 1.2, 'leche': 0.9}. "
            "Matiz: usa get para evitar errores si no existe la clave."
        ),
    },
    "set": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition": (
            "Un set es una colección sin orden y sin elementos repetidos. "
            "Se usa para eliminar duplicados o hacer operaciones de conjuntos. "
            "Ejemplo: unicos = {1, 2, 3}. "
            "Error típico: esperar un orden fijo al iterar."
        ),
    },
    "conjunto": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition": (
            "Un conjunto guarda valores únicos y no garantiza orden. "
            "Se usa para comprobar pertenencia rápidamente. "
            "Ejemplo: vistos = {'ana', 'luis'}. "
            "Matiz: no puedes indexar un set con [0]."
        ),
    },
    "conjuntos": {
        "tooltip": "Colección de elementos únicos sin orden.",
        "definition": (
            "Los conjuntos almacenan elementos únicos sin orden. "
            "Se usan para eliminar duplicados o comparar colecciones. "
            "Ejemplo: set([1, 1, 2]) produce {1, 2}. "
            "Error típico: pensar que mantienen el orden de inserción."
        ),
    },
    "mutable": {
        "tooltip": "Se puede modificar después de ser creado.",
        "definition": (
            "Un objeto mutable puede cambiar su contenido después de crearse. "
            "Se usa cuando necesitas actualizar datos en sitio. "
            "Ejemplo: una lista es mutable, puedes hacer lista.append(4). "
            "Matiz: mutar un objeto compartido afecta a todas las referencias."
        ),
    },
    "inmutable": {
        "tooltip": "No se puede modificar después de ser creado.",
        "definition": (
            "Un objeto inmutable no puede cambiarse; si lo 'modificas' creas otro. "
            "Se usa para valores fijos o claves de diccionario. "
            "Ejemplo: strings y tuplas son inmutables. "
            "Error típico: intentar modificar un string con asignación por índice."
        ),
    },
    "iterador": {
        "tooltip": "Objeto que permite recorrer elementos uno a uno.",
        "definition": (
            "Un iterador devuelve elementos de una colección uno a uno. "
            "Se usa con for o next() para recorrer datos. "
            "Ejemplo: iter([1, 2]) crea un iterador. "
            "Matiz: un iterador se agota cuando llegas al final."
        ),
    },
    "generador": {
        "tooltip": "Función o expresión que produce valores bajo demanda.",
        "definition": (
            "Un generador produce valores uno por uno sin guardar todos en memoria. "
            "Se usa para secuencias grandes o infinitas. "
            "Ejemplo: (x * 2 for x in range(3)) crea un generador. "
            "Error típico: intentar indexarlo como si fuera una lista."
        ),
    },
    "excepción": {
        "tooltip": "Evento que interrumpe el flujo normal por un error.",
        "definition": (
            "Una excepción es un error que interrumpe el flujo normal del programa. "
            "Se usa para señalar fallos y tratarlos con try/except. "
            "Ejemplo: int('a') lanza ValueError. "
            "Matiz: si no la manejas, el programa se detiene."
        ),
    },
    "try": {
        "tooltip": "Bloque para capturar errores potenciales.",
        "definition": (
            "try delimita el código que podría fallar. "
            "Se usa junto con except para manejar errores. "
            "Ejemplo: try: abrir_archivo() except FileNotFoundError: ... "
            "Error típico: poner demasiado código dentro y ocultar bugs."
        ),
    },
    "except": {
        "tooltip": "Bloque que maneja una excepción específica.",
        "definition": (
            "except captura una excepción y ejecuta código alternativo. "
            "Se usa para manejar errores esperables. "
            "Ejemplo: except ZeroDivisionError: print('No dividir entre 0'). "
            "Matiz: evita usar except sin tipo porque oculta errores reales."
        ),
    },
    "finally": {
        "tooltip": "Bloque que se ejecuta siempre al finalizar un try.",
        "definition": (
            "finally se ejecuta siempre, haya error o no. "
            "Se usa para liberar recursos. "
            "Ejemplo: finally: archivo.close(). "
            "Matiz: no reemplaza el manejo de errores, solo asegura limpieza."
        ),
    },
    "with": {
        "tooltip": "Bloque que gestiona recursos con context manager.",
        "definition": (
            "with abre un bloque que administra recursos automáticamente. "
            "Se usa para abrir archivos o conexiones y cerrarlas al final. "
            "Ejemplo: with open('a.txt') as f: leer = f.read(). "
            "Error típico: olvidar usar with y dejar recursos abiertos."
        ),
    },
    "context manager": {
        "tooltip": "Objeto que controla la entrada y salida de un bloque with.",
        "definition": (
            "Un context manager define qué hacer al entrar y salir de un with. "
            "Se usa para gestionar recursos de forma segura. "
            "Ejemplo: open() es un context manager para archivos. "
            "Matiz: implementa __enter__ y __exit__."
        ),
    },
    "scope": {
        "tooltip": "Alcance donde una variable es visible y válida.",
        "definition": (
            "El scope indica dónde una variable puede ser usada. "
            "Se usa para entender por qué un nombre existe o no existe en un bloque. "
            "Ejemplo: una variable creada en una función no existe fuera. "
            "Error típico: intentar leer una variable local fuera de su función."
        ),
    },
    "global": {
        "tooltip": "Palabra clave para usar una variable del ámbito global.",
        "definition": (
            "global permite modificar una variable definida fuera de una función. "
            "Se usa con cuidado cuando necesitas cambiar un valor global. "
            "Ejemplo: global contador dentro de una función. "
            "Matiz: su abuso hace el código más difícil de mantener."
        ),
    },
    "local": {
        "tooltip": "Variable definida dentro de un bloque o función.",
        "definition": (
            "Una variable local existe solo dentro de la función o bloque donde se crea. "
            "Se usa para mantener datos temporales. "
            "Ejemplo: dentro de una función, temp = 5. "
            "Error típico: intentar usarla fuera de su alcance."
        ),
    },
    "snake_case": {
        "tooltip": "Convención de nombres con minúsculas y guiones bajos.",
        "definition": (
            "snake_case es una forma de nombrar variables con minúsculas y guiones bajos. "
            "Se usa en Python para nombres de variables y funciones. "
            "Ejemplo: total_ventas = 10. "
            "Matiz: ayuda a la legibilidad y sigue PEP 8."
        ),
    },
    "pascalcase": {
        "tooltip": "Convención de nombres con cada palabra en mayúscula.",
        "definition": (
            "PascalCase escribe cada palabra con inicial en mayúscula. "
            "Se usa en Python sobre todo para nombres de clases. "
            "Ejemplo: class UsuarioPremium. "
            "Error típico: usarlo para variables en lugar de snake_case."
        ),
    },
    "pep8": {
        "tooltip": "Guía de estilo oficial para escribir código Python.",
        "definition": (
            "PEP 8 es la guía de estilo oficial para escribir Python legible. "
            "Se usa para nombrar, espaciar y organizar el código. "
            "Ejemplo: 4 espacios por indentación. "
            "Matiz: seguirla facilita trabajar en equipo."
        ),
    },
    "indentación": {
        "tooltip": "Espacios o tabulaciones que delimitan bloques de código.",
        "definition": (
            "La indentación en Python define bloques de código. "
            "Se usa para delimitar if, for, funciones, etc. "
            "Ejemplo: cuatro espacios antes de una línea dentro de una función. "
            "Error típico: mezclar tabs y espacios y provocar errores de indentación."
        ),
    },
    "f-string": {
        "tooltip": "Cadena con interpolación usando prefijo f.",
        "definition": (
            "Una f-string permite insertar variables en un string con { }. "
            "Se usa para crear textos dinámicos de forma clara. "
            "Ejemplo: f'Hola {nombre}'. "
            "Matiz: las expresiones dentro de { } se evalúan al momento."
        ),
    },
    "slice": {
        "tooltip": "Subsección de una secuencia usando índices y rango.",
        "definition": (
            "Un slice extrae una parte de una secuencia usando inicio y fin. "
            "Se usa con listas, strings o tuplas. "
            "Ejemplo: texto[0:3] devuelve los primeros 3 caracteres. "
            "Error típico: olvidar que el índice final no se incluye."
        ),
    },
    "comprehension": {
        "tooltip": "Sintaxis compacta para construir colecciones.",
        "definition": (
            "Una comprehension crea listas, sets o dicts en una sola línea. "
            "Se usa para transformar datos de forma concisa. "
            "Ejemplo: [x * 2 for x in numeros]. "
            "Matiz: si se vuelve muy larga, pierde legibilidad."
        ),
    },
    "append": {
        "tooltip": "Método de listas que agrega un elemento al final.",
        "definition": (
            "append añade un elemento al final de una lista. "
            "Se usa para crecer listas paso a paso. "
            "Ejemplo: lista.append(10). "
            "Error típico: asignar lista = lista.append(10) y perder la lista."
        ),
    },
    "extend": {
        "tooltip": "Método de listas que agrega varios elementos.",
        "definition": (
            "extend añade varios elementos de otra colección a una lista. "
            "Se usa para concatenar listas. "
            "Ejemplo: lista.extend([4, 5]). "
            "Matiz: extend recibe una colección, append recibiría la lista completa."
        ),
    },
    "insert": {
        "tooltip": "Método de listas que agrega en una posición específica.",
        "definition": (
            "insert agrega un elemento en una posición específica de la lista. "
            "Se usa para insertar sin reemplazar. "
            "Ejemplo: lista.insert(1, 'nuevo'). "
            "Error típico: usar índices fuera del rango sin entender el resultado."
        ),
    },
    "pop": {
        "tooltip": "Método que extrae y devuelve un elemento.",
        "definition": (
            "pop elimina y devuelve un elemento de una lista (por defecto el último). "
            "Se usa para procesar elementos y quitarlos. "
            "Ejemplo: ultimo = lista.pop(). "
            "Matiz: si la lista está vacía, lanza IndexError."
        ),
    },
    "remove": {
        "tooltip": "Método que elimina la primera coincidencia.",
        "definition": (
            "remove elimina la primera aparición de un valor en una lista. "
            "Se usa para borrar por valor. "
            "Ejemplo: lista.remove('a'). "
            "Error típico: si el valor no existe, lanza ValueError."
        ),
    },
    "sort": {
        "tooltip": "Método que ordena los elementos en su lugar.",
        "definition": (
            "sort ordena una lista en el mismo lugar. "
            "Se usa para ordenar sin crear otra lista. "
            "Ejemplo: numeros.sort(). "
            "Matiz: sort no devuelve la lista; devuelve None."
        ),
    },
    "upper": {
        "tooltip": "Método de strings que convierte a mayúsculas.",
        "definition": (
            "upper crea una versión en mayúsculas del string. "
            "Se usa para normalizar texto. "
            "Ejemplo: 'hola'.upper() -> 'HOLA'. "
            "Matiz: no modifica el string original."
        ),
    },
    "lower": {
        "tooltip": "Método de strings que convierte a minúsculas.",
        "definition": (
            "lower crea una versión en minúsculas del string. "
            "Se usa para comparar sin importar el caso. "
            "Ejemplo: 'Hola'.lower() -> 'hola'. "
            "Matiz: devuelve un nuevo string, no modifica el original."
        ),
    },
    "strip": {
        "tooltip": "Método que quita espacios al inicio y final.",
        "definition": (
            "strip elimina espacios (u otros caracteres) al inicio y final. "
            "Se usa para limpiar entradas de usuario. "
            "Ejemplo: '  hola  '.strip() -> 'hola'. "
            "Matiz: no quita espacios del medio."
        ),
    },
    "split": {
        "tooltip": "Método que separa un string en partes.",
        "definition": (
            "split divide un string en una lista usando un separador. "
            "Se usa para procesar texto. "
            "Ejemplo: 'a,b'.split(',') -> ['a', 'b']. "
            "Matiz: si no das separador, usa espacios en blanco."
        ),
    },
    "join": {
        "tooltip": "Método que une una lista de strings.",
        "definition": (
            "join une una colección de strings usando un separador. "
            "Se usa para construir textos. "
            "Ejemplo: ','.join(['a', 'b']) -> 'a,b'. "
            "Error típico: incluir elementos que no son strings."
        ),
    },
    "replace": {
        "tooltip": "Método que reemplaza subcadenas.",
        "definition": (
            "replace sustituye una subcadena por otra. "
            "Se usa para limpiar o cambiar texto. "
            "Ejemplo: 'hola'.replace('h', 'H') -> 'Hola'. "
            "Matiz: reemplaza todas las apariciones por defecto."
        ),
    },
    "startswith": {
        "tooltip": "Método que comprueba el prefijo.",
        "definition": (
            "startswith verifica si un string comienza con un prefijo. "
            "Se usa para validar formatos. "
            "Ejemplo: 'https://'.startswith('http') -> True. "
            "Matiz: distingue mayúsculas y minúsculas."
        ),
    },
    "endswith": {
        "tooltip": "Método que comprueba el sufijo.",
        "definition": (
            "endswith verifica si un string termina con un sufijo. "
            "Se usa para validar extensiones. "
            "Ejemplo: 'archivo.txt'.endswith('.txt') -> True. "
            "Matiz: también distingue mayúsculas y minúsculas."
        ),
    },
    "get": {
        "tooltip": "Método de dict que devuelve un valor con clave.",
        "definition": (
            "get obtiene el valor de una clave en un diccionario. "
            "Se usa para evitar errores si la clave no existe. "
            "Ejemplo: datos.get('edad', 0). "
            "Matiz: puedes dar un valor por defecto."
        ),
    },
    "items": {
        "tooltip": "Método de dict que devuelve pares clave-valor.",
        "definition": (
            "items devuelve pares clave-valor como tuplas. "
            "Se usa para recorrer diccionarios. "
            "Ejemplo: for k, v in datos.items(): ... "
            "Matiz: el resultado es una vista, no una lista real."
        ),
    },
    "keys": {
        "tooltip": "Método de dict que devuelve las claves.",
        "definition": (
            "keys devuelve todas las claves de un diccionario. "
            "Se usa para iterar o verificar claves. "
            "Ejemplo: 'nombre' in datos.keys(). "
            "Matiz: también es una vista dinámica."
        ),
    },
    "values": {
        "tooltip": "Método de dict que devuelve los valores.",
        "definition": (
            "values devuelve los valores de un diccionario. "
            "Se usa para recorrer solo los datos. "
            "Ejemplo: for v in datos.values(): ... "
            "Matiz: puede contener valores duplicados."
        ),
    },
    "update": {
        "tooltip": "Método de dict que fusiona valores.",
        "definition": (
            "update agrega o reemplaza claves en un diccionario. "
            "Se usa para combinar configuraciones. "
            "Ejemplo: datos.update({'edad': 30}). "
            "Matiz: sobrescribe valores existentes con la misma clave."
        ),
    },
    "sql": {
        "tooltip": "Lenguaje para consultar y manipular bases de datos relacionales.",
        "definition": (
            "SQL es un lenguaje para crear y consultar bases de datos relacionales. "
            "Se usa para seleccionar, insertar o actualizar datos. "
            "Ejemplo: SELECT * FROM usuarios. "
            "Matiz: usar parámetros evita inyección SQL."
        ),
    },
    "cursor": {
        "tooltip": "Objeto que permite recorrer resultados de una consulta.",
        "definition": (
            "Un cursor recorre los resultados de una consulta a la base de datos. "
            "Se usa para leer filas una por una o en bloques. "
            "Ejemplo: cursor.fetchone(). "
            "Error típico: olvidar cerrar el cursor y dejar recursos abiertos."
        ),
    },
    "transacción": {
        "tooltip": "Grupo de operaciones que se confirman o revierten juntas.",
        "definition": (
            "Una transacción agrupa varias operaciones en una sola unidad. "
            "Se usa para asegurar consistencia en la base de datos. "
            "Ejemplo: transferir saldo entre dos cuentas. "
            "Matiz: si algo falla, se revierte con rollback."
        ),
    },
    "commit": {
        "tooltip": "Acción que confirma los cambios pendientes.",
        "definition": (
            "commit confirma de forma permanente los cambios en una transacción. "
            "Se usa cuando todo salió bien. "
            "Ejemplo: conexion.commit(). "
            "Error típico: olvidar commit y perder los cambios."
        ),
    },
    "rollback": {
        "tooltip": "Acción que revierte los cambios pendientes.",
        "definition": (
            "rollback revierte los cambios no confirmados en una transacción. "
            "Se usa cuando ocurre un error. "
            "Ejemplo: conexion.rollback(). "
            "Matiz: solo revierte cambios desde el último commit."
        ),
    },
    "orm": {
        "tooltip": "Técnica que mapea clases de Python a tablas.",
        "definition": (
            "Un ORM mapea clases de Python a tablas de una base de datos. "
            "Se usa para trabajar con datos como objetos. "
            "Ejemplo: Usuario(nombre='Ana') se guarda en la tabla usuarios. "
            "Matiz: sigue habiendo SQL por debajo; hay que entenderlo."
        ),
    },
    "engine": {
        "tooltip": "Componente que gestiona la conexión a la base de datos.",
        "definition": (
            "El engine representa la conexión y configuración de acceso a la base. "
            "Se usa para crear sesiones o ejecutar consultas. "
            "Ejemplo: engine = create_engine(url). "
            "Matiz: reutilizar el engine evita abrir conexiones innecesarias."
        ),
    },
    "session": {
        "tooltip": "Unidad de trabajo que gestiona objetos y transacciones.",
        "definition": (
            "Una sesión agrupa operaciones y controla el ciclo de vida de objetos ORM. "
            "Se usa para añadir, actualizar o borrar registros. "
            "Ejemplo: session.add(usuario); session.commit(). "
            "Error típico: olvidar cerrar la sesión y mantener conexiones abiertas."
        ),
    },
    "pool": {
        "tooltip": "Conjunto de conexiones reutilizables.",
        "definition": (
            "Un pool mantiene conexiones abiertas para reutilizarlas. "
            "Se usa para mejorar rendimiento en bases de datos. "
            "Ejemplo: el pool entrega una conexión disponible al hacer una consulta. "
            "Matiz: si el pool se agota, las consultas esperan."
        ),
    },
    "dsn": {
        "tooltip": "Cadena que describe cómo conectarse a la base de datos.",
        "definition": (
            "DSN es un texto con los datos necesarios para conectarse a una base. "
            "Se usa para indicar host, usuario, base y opciones. "
            "Ejemplo: postgres://user:pass@localhost/db. "
            "Error típico: exponer el DSN en logs públicos."
        ),
    },
    "sql injection": {
        "tooltip": "Ataque que manipula SQL con datos sin parametrizar.",
        "definition": (
            "SQL injection ocurre cuando datos sin filtrar alteran una consulta. "
            "Se usa como ejemplo de qué evitar. "
            "Ejemplo: concatenar texto de usuario en una query. "
            "Matiz: usa parámetros para evitar este riesgo."
        ),
    },
    "señal": {
        "tooltip": "Notificación emitida cuando ocurre un evento en una GUI.",
        "definition": (
            "Una señal es un aviso que se emite cuando sucede algo en la interfaz. "
            "Se usa para comunicar eventos a otros componentes. "
            "Ejemplo: button.clicked es una señal. "
            "Matiz: una señal no hace nada si nadie la conecta a un slot."
        ),
    },
    "señales": {
        "tooltip": "Notificaciones emitidas cuando ocurren eventos en una GUI.",
        "definition": (
            "Las señales notifican eventos de la interfaz. "
            "Se usan para conectar acciones con respuestas. "
            "Ejemplo: slider.valueChanged se emite al mover el slider. "
            "Matiz: puedes conectar varias funciones a una misma señal."
        ),
    },
    "slot": {
        "tooltip": "Función que responde a una señal en Qt/PySide.",
        "definition": (
            "Un slot es la función que se ejecuta cuando llega una señal. "
            "Se usa para definir la reacción a eventos. "
            "Ejemplo: button.clicked.connect(mi_funcion). "
            "Matiz: el slot debe aceptar los argumentos que emite la señal."
        ),
    },
    "slots": {
        "tooltip": "Funciones que responden a señales en Qt/PySide.",
        "definition": (
            "Los slots son funciones que reaccionan a señales. "
            "Se usan para organizar lógica de interfaz. "
            "Ejemplo: conectar varias señales a un mismo slot. "
            "Matiz: ayudan a separar la UI de la lógica."
        ),
    },
    "widget": {
        "tooltip": "Componente visual básico de una interfaz gráfica.",
        "definition": (
            "Un widget es un elemento visual como botones, inputs o etiquetas. "
            "Se usa para construir la interfaz. "
            "Ejemplo: QLabel muestra texto. "
            "Matiz: todos los widgets tienen un padre para el layout."
        ),
    },
    "widgets": {
        "tooltip": "Componentes visuales básicos de una interfaz gráfica.",
        "definition": (
            "Los widgets son piezas visuales de la interfaz. "
            "Se usan para construir ventanas completas. "
            "Ejemplo: QPushButton es un widget de botón. "
            "Matiz: su tamaño puede gestionarse con layouts."
        ),
    },
    "layout": {
        "tooltip": "Distribuidor que organiza widgets en una interfaz.",
        "definition": (
            "Un layout organiza widgets en filas, columnas o rejillas. "
            "Se usa para que la interfaz se adapte al tamaño. "
            "Ejemplo: QVBoxLayout apila elementos en vertical. "
            "Error típico: poner widgets sin layout y que no redimensionen bien."
        ),
    },
    "layouts": {
        "tooltip": "Distribuidores que organizan widgets en una interfaz.",
        "definition": (
            "Los layouts distribuyen widgets automáticamente. "
            "Se usan para mantener orden y responsividad. "
            "Ejemplo: combinar QHBoxLayout y QVBoxLayout. "
            "Matiz: un widget solo puede pertenecer a un layout."
        ),
    },
    "event loop": {
        "tooltip": "Bucle que procesa eventos y mantiene viva la interfaz.",
        "definition": (
            "El event loop es el ciclo que recibe eventos y los distribuye. "
            "Se usa para mantener la app reactiva. "
            "Ejemplo: app.exec() inicia el bucle. "
            "Matiz: bloquear el event loop congela la interfaz."
        ),
    },
    "bucle de eventos": {
        "tooltip": "Bucle que procesa eventos y mantiene viva la interfaz.",
        "definition": (
            "El bucle de eventos procesa clics, teclas y actualizaciones. "
            "Se usa para que la GUI responda. "
            "Ejemplo: eventos de mouse llegan al bucle. "
            "Error típico: usar tareas largas sin hilos y congelar la UI."
        ),
    },
    "qthread": {
        "tooltip": "Clase de Qt para ejecutar tareas en un hilo separado.",
        "definition": (
            "QThread permite ejecutar trabajo pesado sin bloquear la interfaz. "
            "Se usa para tareas largas o de fondo. "
            "Ejemplo: mover cálculo pesado a un QThread. "
            "Matiz: nunca actualices la UI desde el hilo secundario."
        ),
    },
    "model/view": {
        "tooltip": "Patrón que separa datos (modelo) y presentación (vista).",
        "definition": (
            "Model/View separa los datos de cómo se muestran. "
            "Se usa para interfaces con listas y tablas. "
            "Ejemplo: QListView con un modelo de datos. "
            "Matiz: el modelo notifica cambios a la vista."
        ),
    },
    "modelo/vista": {
        "tooltip": "Patrón que separa datos (modelo) y presentación (vista).",
        "definition": (
            "El patrón modelo/vista separa la lógica de datos de la UI. "
            "Se usa para mantener el código organizado. "
            "Ejemplo: QTableView con un modelo. "
            "Matiz: actualizar el modelo actualiza la vista automáticamente."
        ),
    },
    "dataframe": {
        "tooltip": "Tabla de datos bidimensional con filas y columnas en Pandas.",
        "definition": (
            "Un DataFrame es una tabla con filas y columnas en Pandas. "
            "Se usa para análisis y limpieza de datos. "
            "Ejemplo: df = pd.DataFrame({'a': [1, 2]}). "
            "Matiz: las columnas pueden tener tipos distintos."
        ),
    },
    "dataframes": {
        "tooltip": "Tablas de datos bidimensionales con filas y columnas en Pandas.",
        "definition": (
            "Los DataFrames son tablas con filas y columnas. "
            "Se usan para análisis de datos. "
            "Ejemplo: df[['col1', 'col2']] selecciona columnas. "
            "Matiz: trabajar con copias vs vistas puede afectar cambios."
        ),
    },
    "serie": {
        "tooltip": "Estructura unidimensional de datos en Pandas.",
        "definition": (
            "Una Series es una columna con índices en Pandas. "
            "Se usa para trabajar con una sola dimensión. "
            "Ejemplo: s = df['columna']. "
            "Matiz: el índice es parte importante de la Series."
        ),
    },
    "series": {
        "tooltip": "Estructuras unidimensionales de datos en Pandas.",
        "definition": (
            "Las Series son estructuras unidimensionales con índice. "
            "Se usan para columnas o datos sueltos. "
            "Ejemplo: pd.Series([1, 2, 3]). "
            "Matiz: operaciones con Series alinean por índice."
        ),
    },
    "groupby": {
        "tooltip": "Operación que agrupa filas para aplicar cálculos por grupo.",
        "definition": (
            "groupby agrupa filas para calcular agregados por grupo. "
            "Se usa para resúmenes y estadísticas. "
            "Ejemplo: df.groupby('categoria').mean(). "
            "Matiz: tras agrupar, necesitas una agregación."
        ),
    },
    "merge": {
        "tooltip": "Operación para combinar DataFrames por claves comunes.",
        "definition": (
            "merge combina DataFrames usando columnas comunes. "
            "Se usa para unir datasets relacionados. "
            "Ejemplo: df1.merge(df2, on='id'). "
            "Matiz: el tipo de join cambia qué filas aparecen."
        ),
    },
    "loc": {
        "tooltip": "Acceso por etiquetas de filas/columnas en Pandas.",
        "definition": (
            "loc selecciona datos usando etiquetas de filas/columnas. "
            "Se usa cuando el índice tiene nombres. "
            "Ejemplo: df.loc[0, 'col']. "
            "Matiz: incluye el último índice en rangos por etiqueta."
        ),
    },
    "iloc": {
        "tooltip": "Acceso por posiciones numéricas en Pandas.",
        "definition": (
            "iloc selecciona datos por posición numérica. "
            "Se usa cuando quieres índices por posición. "
            "Ejemplo: df.iloc[0, 1]. "
            "Matiz: los rangos son exclusivos en el final, como en slicing."
        ),
    },
    "nan": {
        "tooltip": "Valor especial que representa datos faltantes.",
        "definition": (
            "NaN representa valores faltantes en datos numéricos. "
            "Se usa para indicar ausencia en Pandas o NumPy. "
            "Ejemplo: pd.Series([1, None]). "
            "Matiz: NaN no es igual a sí mismo (NaN != NaN)."
        ),
    },
    "dtype": {
        "tooltip": "Tipo de dato almacenado en un array o columna.",
        "definition": (
            "dtype indica el tipo de datos de una columna o array. "
            "Se usa para entender cómo se guardan los valores. "
            "Ejemplo: df['col'].dtype. "
            "Matiz: cambiar dtype puede afectar memoria y precisión."
        ),
    },
    "pipeline": {
        "tooltip": "Secuencia encadenada de pasos de procesamiento y modelo.",
        "definition": (
            "Un pipeline encadena pasos de preprocesado y modelo. "
            "Se usa para evitar fugas y mantener flujo reproducible. "
            "Ejemplo: Pipeline([('scaler', ...), ('model', ...)]). "
            "Matiz: cada paso debe implementar fit/transform o fit/predict."
        ),
    },
    "leakage": {
        "tooltip": "Uso de información del futuro en entrenamiento, sesga resultados.",
        "definition": (
            "Leakage ocurre cuando el modelo ve información que no tendrá en producción. "
            "Se usa como advertencia en ML. "
            "Ejemplo: usar la variable objetivo para normalizar datos. "
            "Matiz: produce métricas falsas y modelos poco fiables."
        ),
    },
    "cross-validation": {
        "tooltip": "Técnica que valida con varias particiones del dataset.",
        "definition": (
            "La cross-validation divide los datos en varias particiones para evaluar. "
            "Se usa para medir rendimiento real del modelo. "
            "Ejemplo: K-Fold con 5 particiones. "
            "Matiz: hay que mantener el orden temporal si es series de tiempo."
        ),
    },
    "validación cruzada": {
        "tooltip": "Técnica que valida con varias particiones del dataset.",
        "definition": (
            "La validación cruzada evalúa el modelo en varias particiones. "
            "Se usa para reducir el sesgo de una sola división. "
            "Ejemplo: cross_val_score en sklearn. "
            "Matiz: aumenta el costo de cómputo."
        ),
    },
    "estimator": {
        "tooltip": "Objeto en sklearn que aprende parámetros desde datos.",
        "definition": (
            "Un estimator es un modelo o transformador en sklearn. "
            "Se usa para ajustar parámetros con fit. "
            "Ejemplo: LinearRegression() es un estimator. "
            "Matiz: algunos estimators también transforman datos."
        ),
    },
    "fit": {
        "tooltip": "Proceso de ajustar un modelo a los datos de entrenamiento.",
        "definition": (
            "fit entrena un modelo con datos de entrenamiento. "
            "Se usa para aprender parámetros. "
            "Ejemplo: model.fit(X_train, y_train). "
            "Matiz: no uses datos de test en fit."
        ),
    },
    "transform": {
        "tooltip": "Aplicación de una transformación a los datos.",
        "definition": (
            "transform aplica una transformación ya aprendida a nuevos datos. "
            "Se usa después de fit en escaladores o codificadores. "
            "Ejemplo: scaler.transform(X). "
            "Matiz: fit_transform combina ambos pasos en entrenamiento."
        ),
    },
    "predict": {
        "tooltip": "Generación de salidas de un modelo entrenado.",
        "definition": (
            "predict genera predicciones usando un modelo entrenado. "
            "Se usa para obtener resultados en datos nuevos. "
            "Ejemplo: model.predict(X_test). "
            "Matiz: la salida depende del tipo de modelo (clase o valor)."
        ),
    },
    "tensor": {
        "tooltip": "Estructura n-dimensional para datos numéricos en DL.",
        "definition": (
            "Un tensor es una estructura n-dimensional para datos. "
            "Se usa en deep learning para representar matrices y más. "
            "Ejemplo: un batch de imágenes es un tensor 4D. "
            "Matiz: la forma (shape) es clave para operar con tensores."
        ),
    },
    "tensores": {
        "tooltip": "Estructuras n-dimensionales para datos numéricos en DL.",
        "definition": (
            "Los tensores son estructuras n-dimensionales de datos. "
            "Se usan en redes neuronales para inputs y pesos. "
            "Ejemplo: pesos de una capa son un tensor. "
            "Matiz: las operaciones requieren dimensiones compatibles."
        ),
    },
    "autograd": {
        "tooltip": "Sistema de cálculo automático de gradientes.",
        "definition": (
            "Autograd calcula gradientes automáticamente. "
            "Se usa para entrenar redes neuronales con backpropagation. "
            "Ejemplo: en PyTorch, los tensores con requires_grad. "
            "Matiz: hay que limpiar gradientes entre pasos."
        ),
    },
    "optimizer": {
        "tooltip": "Algoritmo que actualiza pesos para minimizar la pérdida.",
        "definition": (
            "Un optimizer ajusta los pesos para minimizar la función de pérdida. "
            "Se usa durante el entrenamiento. "
            "Ejemplo: Adam o SGD. "
            "Matiz: el learning rate influye mucho en el resultado."
        ),
    },
    "optimizador": {
        "tooltip": "Algoritmo que actualiza pesos para minimizar la pérdida.",
        "definition": (
            "Un optimizador actualiza los pesos de un modelo. "
            "Se usa para reducir la pérdida durante el entrenamiento. "
            "Ejemplo: optimizador = Adam(model.parameters()). "
            "Matiz: una tasa de aprendizaje muy alta puede divergir."
        ),
    },
    "epoch": {
        "tooltip": "Iteración completa sobre todo el conjunto de entrenamiento.",
        "definition": (
            "Una epoch es una pasada completa por el dataset de entrenamiento. "
            "Se usa para medir avance en entrenamiento. "
            "Ejemplo: entrenar 10 epochs. "
            "Matiz: más epochs no siempre significan mejor modelo."
        ),
    },
    "época": {
        "tooltip": "Iteración completa sobre todo el conjunto de entrenamiento.",
        "definition": (
            "Época es lo mismo que epoch: una pasada completa por el dataset. "
            "Se usa para contar ciclos de entrenamiento. "
            "Ejemplo: 5 épocas de entrenamiento. "
            "Matiz: hay riesgo de overfitting si entrenas demasiado."
        ),
    },
    "batch": {
        "tooltip": "Subconjunto de datos usado en una actualización.",
        "definition": (
            "Un batch es un subconjunto de datos usado en una actualización. "
            "Se usa para entrenar por partes en lugar de todo el dataset. "
            "Ejemplo: batch_size = 32. "
            "Matiz: batch muy pequeño puede hacer el entrenamiento inestable."
        ),
    },
    "lote": {
        "tooltip": "Subconjunto de datos usado en una actualización.",
        "definition": (
            "Un lote es un grupo de ejemplos usados en cada actualización. "
            "Se usa para controlar memoria y rendimiento. "
            "Ejemplo: entrenar con lotes de 64. "
            "Matiz: lotes grandes pueden requerir más memoria."
        ),
    },
    "gradiente": {
        "tooltip": "Dirección de mayor cambio de la función de pérdida.",
        "definition": (
            "El gradiente indica cómo cambiar los pesos para reducir la pérdida. "
            "Se usa en optimización. "
            "Ejemplo: descenso por gradiente ajusta pesos en dirección opuesta. "
            "Matiz: gradientes muy grandes pueden causar explosión."
        ),
    },
    "backpropagation": {
        "tooltip": "Algoritmo que propaga el error para ajustar pesos.",
        "definition": (
            "Backpropagation propaga el error hacia atrás para calcular gradientes. "
            "Se usa para entrenar redes neuronales. "
            "Ejemplo: se calcula la pérdida y se propaga por capas. "
            "Matiz: requiere derivadas de las funciones de activación."
        ),
    },
    "loss": {
        "tooltip": "Medida de error que el modelo intenta minimizar.",
        "definition": (
            "La loss mide cuánto se equivoca el modelo. "
            "Se usa para guiar el entrenamiento. "
            "Ejemplo: MSE en regresión. "
            "Matiz: una loss baja en entrenamiento no garantiza buen rendimiento."
        ),
    },
    "índice": {
        "tooltip": "Estructura que acelera búsquedas en una tabla de datos.",
        "definition": (
            "Un índice acelera la búsqueda de filas en una tabla. "
            "Se usa en bases de datos para consultas rápidas. "
            "Ejemplo: índice en la columna id. "
            "Matiz: mejora lecturas pero puede ralentizar escrituras."
        ),
    },
    "clave primaria": {
        "tooltip": "Columna que identifica de forma única cada fila.",
        "definition": (
            "La clave primaria identifica de forma única cada fila. "
            "Se usa para garantizar unicidad en tablas. "
            "Ejemplo: id incremental como clave primaria. "
            "Matiz: no debe repetirse ni ser nula."
        ),
    },
    "clave foránea": {
        "tooltip": "Columna que referencia la clave primaria de otra tabla.",
        "definition": (
            "Una clave foránea referencia la clave primaria de otra tabla. "
            "Se usa para relacionar tablas. "
            "Ejemplo: pedidos.usuario_id apunta a usuarios.id. "
            "Matiz: debe existir en la tabla referenciada."
        ),
    },
    "join": {
        "tooltip": "Operación que combina filas de tablas relacionadas.",
        "definition": (
            "Un join combina filas de tablas relacionadas por una clave. "
            "Se usa para consultar datos de varias tablas. "
            "Ejemplo: SELECT ... FROM a JOIN b ON a.id = b.a_id. "
            "Matiz: los tipos de join cambian qué filas aparecen."
        ),
    },
    "inner join": {
        "tooltip": "Join que devuelve solo coincidencias entre tablas.",
        "definition": (
            "INNER JOIN devuelve solo filas que tienen coincidencia en ambas tablas. "
            "Se usa cuando quieres solo datos relacionados. "
            "Ejemplo: INNER JOIN usuarios y pedidos. "
            "Matiz: filas sin relación se descartan."
        ),
    },
    "left join": {
        "tooltip": "Join que devuelve todas las filas de la tabla izquierda.",
        "definition": (
            "LEFT JOIN devuelve todas las filas de la tabla izquierda. "
            "Se usa para mantener datos aunque no haya coincidencia. "
            "Ejemplo: usuarios LEFT JOIN pedidos. "
            "Matiz: las columnas sin coincidencia quedan como NULL."
        ),
    },
    "right join": {
        "tooltip": "Join que devuelve todas las filas de la tabla derecha.",
        "definition": (
            "RIGHT JOIN devuelve todas las filas de la tabla derecha. "
            "Se usa cuando quieres preservar la tabla derecha. "
            "Ejemplo: pedidos RIGHT JOIN usuarios. "
            "Matiz: no todos los motores soportan RIGHT JOIN."
        ),
    },
    "full join": {
        "tooltip": "Join que devuelve coincidencias y no coincidencias.",
        "definition": (
            "FULL JOIN devuelve filas coincidentes y no coincidentes. "
            "Se usa para ver todo el conjunto de datos. "
            "Ejemplo: FULL JOIN entre clientes y pedidos. "
            "Matiz: algunos motores no lo soportan sin UNION."
        ),
    },
    "tabla": {
        "tooltip": "Estructura que guarda datos en filas y columnas.",
        "definition": (
            "Una tabla almacena datos en filas y columnas. "
            "Se usa para organizar información en bases de datos. "
            "Ejemplo: tabla usuarios con columnas id y nombre. "
            "Matiz: un buen diseño evita duplicación de datos."
        ),
    },
    "fila": {
        "tooltip": "Registro horizontal de una tabla.",
        "definition": (
            "Una fila es un registro completo dentro de una tabla. "
            "Se usa para representar una entidad. "
            "Ejemplo: una fila de usuarios representa a una persona. "
            "Matiz: cada fila se identifica por la clave primaria."
        ),
    },
    "columna": {
        "tooltip": "Campo vertical que representa un atributo.",
        "definition": (
            "Una columna representa un atributo de la tabla. "
            "Se usa para definir el tipo de dato de cada campo. "
            "Ejemplo: columna 'edad' en usuarios. "
            "Matiz: el tipo de columna limita los valores permitidos."
        ),
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
        "definition": (
            "Azure Blob Storage almacena datos como objetos en contenedores. "
            "Se usa para archivos estáticos, backups y data lakes. "
            "Ejemplo: guardar imágenes de una app o archivos de analítica. "
            "Matiz: ofrece niveles de acceso (hot, cool, archive) según costo."
        ),
    },
    "azure sql": {
        "tooltip": "Base de datos relacional administrada en Azure.",
        "definition": (
            "Azure SQL Database es un servicio administrado de bases relacionales "
            "basado en SQL Server. Se usa para aplicaciones transaccionales. "
            "Ejemplo: base de datos para un ERP con alta disponibilidad. "
            "Matiz: ofrece escalado elástico y backups automáticos."
        ),
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
        "definition": (
            "Google Cloud Storage almacena objetos en buckets con alta durabilidad. "
            "Se usa para datos estáticos, backups y data lakes. "
            "Ejemplo: guardar archivos de un sistema de analítica. "
            "Matiz: permite definir clases de almacenamiento según costo y acceso."
        ),
    },
    "cloud run": {
        "tooltip": "Servicio de GCP para ejecutar contenedores.",
        "definition": (
            "Cloud Run ejecuta contenedores HTTP de forma serverless. "
            "Se usa para desplegar APIs y servicios sin administrar servidores. "
            "Ejemplo: publicar un contenedor con FastAPI en GCP. "
            "Matiz: escala a cero y se cobra por uso real."
        ),
    },
    "bigquery": {
        "tooltip": "Data warehouse administrado de Google Cloud.",
        "definition": (
            "BigQuery es un data warehouse serverless para consultas SQL a gran escala. "
            "Se usa para analítica de grandes volúmenes de datos. "
            "Ejemplo: consultas sobre terabytes de logs en segundos. "
            "Matiz: cobra por almacenamiento y por volumen de datos consultados."
        ),
    },
    "cloud sql": {
        "tooltip": "Base de datos relacional administrada en GCP.",
        "definition": (
            "Cloud SQL es el servicio de bases de datos relacionales gestionadas de GCP. "
            "Se usa para ejecutar PostgreSQL, MySQL o SQL Server sin administrar servidores. "
            "Ejemplo: base transaccional para un backend web. "
            "Matiz: ofrece backups automáticos y alta disponibilidad."
        ),
    },
    "cloud functions": {
        "tooltip": "Servicio serverless de GCP para ejecutar funciones.",
        "definition": (
            "Cloud Functions permite ejecutar funciones bajo demanda en Google Cloud. "
            "Se usa para responder a eventos de almacenamiento, pub/sub o HTTP. "
            "Ejemplo: procesar un archivo al subirlo a Cloud Storage. "
            "Matiz: escala automáticamente y se cobra por invocación."
        ),
    },
    "pub/sub": {
        "tooltip": "Mensajería pub/sub en Google Cloud.",
        "definition": (
            "Pub/Sub es un servicio de mensajería asíncrona con productores y suscriptores. "
            "Se usa para desacoplar sistemas y procesar eventos. "
            "Ejemplo: un servicio publica eventos y varios consumidores los procesan. "
            "Matiz: soporta reintentos y ordenamiento según configuración."
        ),
    },
    "serverless": {
        "tooltip": "Ejecución de código sin gestionar servidores.",
        "definition": (
            "Serverless es un modelo donde ejecutas funciones bajo demanda sin "
            "administrar servidores. Se usa para tareas event-driven y escalado "
            "automático. Ejemplo: AWS Lambda o Azure Functions. "
            "Matiz: suele tener límites de tiempo y recursos."
        ),
    },
    "data lake": {
        "tooltip": "Repositorio de datos crudos a gran escala.",
        "definition": (
            "Un data lake es un repositorio que almacena datos en su formato original "
            "para análisis futuro. Se usa para centralizar datos heterogéneos. "
            "Ejemplo: almacenar archivos parquet y JSON en S3 para analítica. "
            "Matiz: requiere gobernanza para evitar convertirse en un \"data swamp\"."
        ),
    },
    "data warehouse": {
        "tooltip": "Almacén de datos optimizado para analítica.",
        "definition": (
            "Un data warehouse organiza datos estructurados para consultas analíticas. "
            "Se usa para reportes, BI y métricas de negocio. "
            "Ejemplo: consolidar ventas en BigQuery o Snowflake. "
            "Matiz: suele incluir modelos dimensionales y procesos ETL/ELT."
        ),
    },
    "etl": {
        "tooltip": "Proceso de extraer, transformar y cargar datos.",
        "definition": (
            "ETL (Extract, Transform, Load) es un flujo para mover datos desde fuentes "
            "a un destino analítico. Se usa para limpiar y estructurar información. "
            "Ejemplo: extraer CSVs, transformar columnas y cargar a un data warehouse. "
            "Matiz: en ELT se carga primero y se transforma después."
        ),
    },
    "feature engineering": {
        "tooltip": "Creación de variables útiles para modelos de ML.",
        "definition": (
            "Feature engineering es el proceso de crear o transformar variables para "
            "mejorar el rendimiento de un modelo. Se usa para capturar patrones "
            "relevantes del dominio. "
            "Ejemplo: convertir fechas en día de la semana o crear la variable "
            "ingreso_por_persona. "
            "Matiz: debe evitar fugas de información (data leakage)."
        ),
    },
    "api": {
        "tooltip": "Interfaz para que sistemas se comuniquen.",
        "definition": (
            "Una API (Application Programming Interface) define cómo dos sistemas "
            "intercambian datos. Se usa para exponer funcionalidades de un servicio. "
            "Ejemplo: una API REST que devuelve JSON con pedidos de clientes. "
            "Matiz: requiere versionado y autenticación para ser estable y segura."
        ),
    },
    "frontend": {
        "tooltip": "Parte visual e interactiva de una aplicación.",
        "definition": (
            "Frontend es la capa que interactúa con el usuario: UI, estilos y lógica "
            "en el navegador o cliente. Se usa para presentar datos y capturar acciones. "
            "Ejemplo: una interfaz React que consume una API. "
            "Matiz: rendimiento y accesibilidad impactan directamente en la UX."
        ),
    },
    "backend": {
        "tooltip": "Lógica del servidor y acceso a datos.",
        "definition": (
            "Backend es la capa que procesa solicitudes, aplica reglas de negocio y "
            "gestiona bases de datos. Se usa para implementar APIs y servicios internos. "
            "Ejemplo: un servicio FastAPI que valida usuarios y consulta una base. "
            "Matiz: seguridad, escalabilidad y observabilidad son claves."
        ),
    },
    "docker": {
        "tooltip": "Herramienta para crear y ejecutar contenedores.",
        "definition": (
            "Docker permite empaquetar aplicaciones con sus dependencias en contenedores. "
            "Se usa para reproducir entornos y facilitar despliegues. "
            "Ejemplo: ejecutar una API en un contenedor con Dockerfile. "
            "Matiz: los contenedores comparten el kernel del host."
        ),
    },
    "kubernetes": {
        "tooltip": "Orquestador de contenedores.",
        "definition": (
            "Kubernetes (K8s) es un sistema para orquestar contenedores. "
            "Se usa para desplegar, escalar y recuperar aplicaciones en clústeres. "
            "Ejemplo: definir Deployments y Services para una app. "
            "Matiz: requiere configuración y observabilidad para operar bien."
        ),
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
                lines.append(f"{labels.get(key, key)} {text}")
    return "\n".join(lines).strip()


TERMS = {term: definition_text(data) for term, data in GLOSSARY.items()}
KEYWORDS = list(GLOSSARY.keys())
