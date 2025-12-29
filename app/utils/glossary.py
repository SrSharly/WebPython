from __future__ import annotations

GLOSSARY = {
    "variable": {
        "tooltip": "Espacio de memoria con un nombre que guarda un valor.",
        "definition": (
            "Una variable es un nombre que referencia un valor guardado en memoria. "
            "Se usa para reutilizar datos, hacer el código legible y expresar intención. "
            "Ejemplo: x = 5 guarda el 5 en la variable x. "
            "Matiz: el nombre puede reasignarse y apuntar a otro valor, por lo que su "
            "contenido puede cambiar durante la ejecución."
        ),
    },
    "función": {
        "tooltip": "Bloque reutilizable de código que realiza una tarea específica.",
        "definition": (
            "Una función agrupa instrucciones bajo un nombre para reutilizarlas. "
            "Se usa para evitar repetir lógica, organizar el programa y encapsular "
            "comportamiento. "
            "Ejemplo: def saludar(): print('Hola'). "
            "Matiz: puede devolver un valor con return o no devolver nada (None)."
        ),
    },
    "método": {
        "tooltip": "Función asociada a un objeto o clase.",
        "definition": (
            "Un método es una función que pertenece a un objeto o clase y actúa sobre sus datos. "
            "Se usa para definir comportamientos del objeto. "
            "Ejemplo: 'hola'.upper() llama al método upper del string. "
            "Error típico: olvidar los paréntesis y no ejecutar el método."
        ),
    },
    "clase": {
        "tooltip": "Molde que define atributos y comportamientos para crear objetos.",
        "definition": (
            "Una clase es un molde que describe datos (atributos) y acciones (métodos). "
            "Se usa para modelar entidades con estado y comportamiento. "
            "Ejemplo: class Perro: def ladrar(self): print('guau'). "
            "Matiz: definir la clase no crea objetos; hay que instanciarla con Perro()."
        ),
    },
    "objeto": {
        "tooltip": "Instancia de una clase con estado y comportamiento.",
        "definition": (
            "Un objeto es una instancia concreta creada a partir de una clase. "
            "Se usa para trabajar con datos reales siguiendo el molde de la clase. "
            "Ejemplo: perro = Perro() crea un objeto Perro. "
            "Error típico: confundir la clase (molde) con el objeto (instancia)."
        ),
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
        "definition": (
            "Python es un lenguaje de programación de alto nivel con una sintaxis "
            "clara que prioriza la legibilidad. Se usa en automatización, desarrollo "
            "web, ciencia de datos, scripting y aplicaciones de escritorio. "
            "Ejemplo: print('Hola') imprime texto en la consola. "
            "Matiz: su ecosistema de paquetes (pip) y su comunidad facilitan resolver "
            "problemas comunes rápidamente."
        ),
    },
    "ciencia de datos": {
        "tooltip": "Disciplina que extrae valor de datos con estadística y programación.",
        "definition": (
            "La ciencia de datos combina estadística, programación y conocimiento del "
            "dominio para obtener conclusiones a partir de datos. Se usa para analizar "
            "tendencias, construir modelos predictivos y apoyar decisiones. "
            "Ejemplo: usar pandas y matplotlib para explorar un dataset de ventas. "
            "Matiz: requiere limpieza de datos, validación de resultados y comunicación "
            "clara de los hallazgos."
        ),
    },
    "data science": {
        "tooltip": "Nombre en inglés de ciencia de datos.",
        "definition": (
            "Data science aplica estadística, programación y comunicación para "
            "extraer conocimiento de datos. Se usa para entender fenómenos, detectar "
            "patrones, construir modelos y comunicar insights a negocio. "
            "Ejemplo: analizar el churn de clientes y proponer acciones para reducirlo. "
            "Matiz: la limpieza y la calidad de los datos son el punto de partida del "
            "valor generado."
        ),
    },
    "data cience": {
        "tooltip": "Variante común con error de escritura de data science.",
        "definition": (
            "Data cience es una escritura incorrecta de data science (ciencia de datos). "
            "Se usa en búsquedas o conversaciones informales, pero el término correcto "
            "es data science. Ejemplo: preparar datos, analizar tendencias y crear modelos. "
            "Matiz: conviene corregirlo en documentación y presentaciones formales."
        ),
    },
    "machine learning": {
        "tooltip": "Rama de la IA que aprende patrones desde datos.",
        "definition": (
            "Machine learning es una rama de la inteligencia artificial que aprende "
            "patrones desde datos para predecir, clasificar o recomendar. "
            "Se usa en motores de recomendación, detección de fraude, visión y NLP. "
            "Ejemplo: un modelo que predice el precio de una casa a partir de variables. "
            "Matiz: requiere datos representativos, métricas claras y control de sesgos."
        ),
    },
    "full stack": {
        "tooltip": "Desarrollo que cubre frontend y backend.",
        "definition": (
            "Full stack describe a quien desarrolla toda la aplicación: interfaz "
            "(frontend), servidor (backend) y base de datos. Se usa cuando se necesita "
            "entregar un producto end-to-end en equipos pequeños o proyectos ágiles. "
            "Ejemplo: una SPA con React, una API con Python y una base en PostgreSQL. "
            "Matiz: exige entender integración, seguridad, rendimiento y despliegue."
        ),
    },
    "pyside": {
        "tooltip": "Bindings de Qt para crear interfaces gráficas en Python.",
        "definition": (
            "PySide es el conjunto oficial de bindings de Qt para Python. "
            "Se usa para crear aplicaciones de escritorio con ventanas, formularios, "
            "tablas y componentes interactivos. "
            "Ejemplo: PySide6 para construir una GUI multiplataforma con Qt Designer. "
            "Matiz: usa señales y slots para comunicar widgets de forma desacoplada."
        ),
    },
    "aws": {
        "tooltip": "Plataforma cloud de Amazon con múltiples servicios.",
        "definition": (
            "AWS (Amazon Web Services) es la plataforma cloud de Amazon con servicios "
            "de cómputo, almacenamiento, redes, datos e IA. Se usa para desplegar apps, "
            "escalar sistemas y operar infraestructuras globales. "
            "Ejemplo: EC2 para servidores, S3 para almacenamiento, RDS para bases. "
            "Matiz: el costo es bajo demanda y depende de región, uso y arquitectura."
        ),
    },
    "s3": {
        "tooltip": "Servicio de almacenamiento de objetos en AWS.",
        "definition": (
            "Amazon S3 almacena archivos como objetos en buckets y está pensado para "
            "durabilidad y escalabilidad. Se usa para backups, archivos estáticos y "
            "data lakes. Ejemplo: guardar imágenes de una aplicación web. "
            "Matiz: organiza por buckets y permisos; no es un sistema de archivos clásico."
        ),
    },
    "ec2": {
        "tooltip": "Servicio de máquinas virtuales en AWS.",
        "definition": (
            "Amazon EC2 ofrece instancias virtuales para ejecutar servidores. "
            "Se usa cuando necesitas control total del sistema operativo. "
            "Ejemplo: desplegar una API en una instancia Linux. "
            "Matiz: hay que gestionar parches, escalado y seguridad."
        ),
    },
    "rds": {
        "tooltip": "Servicio administrado de bases de datos en AWS.",
        "definition": (
            "Amazon RDS provee bases de datos relacionales gestionadas (PostgreSQL, "
            "MySQL, etc.). Se usa para evitar tareas de mantenimiento como backups. "
            "Ejemplo: una base de datos transaccional para una app. "
            "Matiz: simplifica la operación, pero limita ciertas configuraciones."
        ),
    },
    "lambda": {
        "tooltip": "Servicio serverless para ejecutar funciones en AWS.",
        "definition": (
            "AWS Lambda ejecuta funciones bajo demanda sin servidores visibles. "
            "Se usa para tareas event-driven como procesar archivos o enviar notificaciones. "
            "Ejemplo: procesar imágenes cuando se suben a S3. "
            "Matiz: tiene límites de tiempo y memoria por ejecución."
        ),
    },
    "sagemaker": {
        "tooltip": "Servicio de AWS para construir y desplegar modelos de ML.",
        "definition": (
            "Amazon SageMaker es una plataforma administrada para entrenar, ajustar y "
            "desplegar modelos de machine learning. Se usa para acelerar el ciclo de ML. "
            "Ejemplo: entrenamiento distribuido de modelos y despliegue como endpoint. "
            "Matiz: integra notebooks, pipelines y monitoreo del rendimiento."
        ),
    },
    "cloud": {
        "tooltip": "Modelo de computación con recursos bajo demanda.",
        "definition": (
            "La computación en la nube ofrece recursos (cómputo, almacenamiento, red) "
            "bajo demanda y con pago por uso. Se usa para escalar sin comprar hardware "
            "y para desplegar rápido en múltiples regiones. "
            "Ejemplo: publicar una app en un proveedor cloud con balanceo y backups. "
            "Matiz: los modelos IaaS, PaaS y SaaS definen el nivel de control."
        ),
    },
    "iaas": {
        "tooltip": "Infraestructura como servicio.",
        "definition": (
            "IaaS ofrece infraestructura virtualizada como servidores y redes. "
            "Se usa cuando necesitas control del sistema operativo y configuración. "
            "Ejemplo: instancias virtuales en AWS EC2 o Azure Virtual Machines. "
            "Matiz: el usuario administra el sistema y la seguridad del servidor."
        ),
    },
    "paas": {
        "tooltip": "Plataforma como servicio.",
        "definition": (
            "PaaS ofrece una plataforma administrada para ejecutar aplicaciones. "
            "Se usa para enfocarse en el código sin administrar servidores. "
            "Ejemplo: Heroku, Google App Engine o Azure App Service. "
            "Matiz: limita ciertas configuraciones del entorno."
        ),
    },
    "saas": {
        "tooltip": "Software como servicio.",
        "definition": (
            "SaaS es software accesible vía web sin instalarlo localmente. "
            "Se usa para consumir aplicaciones listas para usar. "
            "Ejemplo: Gmail, Slack o Notion. "
            "Matiz: el proveedor gestiona la infraestructura y actualizaciones."
        ),
    },
    "azure": {
        "tooltip": "Plataforma cloud de Microsoft.",
        "definition": (
            "Azure es la plataforma cloud de Microsoft con servicios de cómputo, "
            "almacenamiento, datos, IA y soluciones empresariales. "
            "Se usa para cargas híbridas, integración con entornos Windows y despliegues "
            "a escala. Ejemplo: Azure Functions para serverless y Azure SQL Database. "
            "Matiz: integra servicios como Active Directory y herramientas de Microsoft."
        ),
    },
    "azure functions": {
        "tooltip": "Servicio serverless de Azure para ejecutar funciones.",
        "definition": (
            "Azure Functions permite ejecutar código bajo demanda sin gestionar servidores. "
            "Se usa para automatizaciones, APIs ligeras y flujos basados en eventos. "
            "Ejemplo: procesar eventos de cola o disparar tareas programadas. "
            "Matiz: ofrece distintos planes de escalado y límites por ejecución."
        ),
    },
    "gcp": {
        "tooltip": "Google Cloud Platform para servicios en la nube.",
        "definition": (
            "GCP es la plataforma cloud de Google con servicios de cómputo, datos y "
            "machine learning. Se usa para análisis a gran escala, procesamiento de "
            "eventos y despliegues rápidos. "
            "Ejemplo: BigQuery para análisis y Cloud Run para contenedores. "
            "Matiz: destaca por sus herramientas de datos y analítica."
        ),
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
    "serverless": {
        "tooltip": "Ejecución de código sin gestionar servidores.",
        "definition": (
            "Serverless es un modelo donde ejecutas funciones bajo demanda sin "
            "administrar servidores. Se usa para tareas event-driven y escalado "
            "automático. Ejemplo: AWS Lambda o Azure Functions. "
            "Matiz: suele tener límites de tiempo y recursos."
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

TERMS = {term: data["definition"] for term, data in GLOSSARY.items()}
KEYWORDS = list(GLOSSARY.keys())
