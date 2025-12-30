from __future__ import annotations


def _item(
    name: str,
    kind: str,
    common: bool,
    category: str,
    signature: str,
    what: str,
    when: list[str],
    pitfalls: list[str],
    example: str,
) -> dict:
    examples = _build_examples(
        name=name,
        what=what,
        when=when,
        pitfalls=pitfalls,
        example=example,
    )
    return {
        "name": name,
        "kind": kind,
        "common": common,
        "category": category,
        "signature": signature,
        "what": what,
        "when": when,
        "pitfalls": pitfalls,
        "examples": examples,
    }


def _build_examples(
    name: str,
    what: str,
    when: list[str],
    pitfalls: list[str],
    example: str,
) -> list[dict]:
    basic_learn = "\n".join(
        [
            f"Aprenderás qué es {name} y qué problema resuelve en tu flujo diario.",
            "Verás el resultado esperado para reconocer si lo aplicaste bien.",
        ]
    )
    realistic_learn = "\n".join(
        [
            f"Aprenderás a aplicar {name} dentro de un escenario más completo.",
            "Practicarás cómo validar el resultado antes de continuar con tu análisis.",
        ]
    )

    basic_see = (
        f"Verás una salida coherente con {what.lower()} y una confirmación de que el paso funcionó."
    )
    realistic_see = (
        f"Verás un resultado más completo y señales claras de que {name} aplicó la transformación."
    )

    why_lines = [
        f"Funciona porque {name} aplica la lógica descrita en su definición.",
    ]
    if when:
        why_lines.append(f"Además, es adecuado {when[0].lower()}.")
    basic_why = " ".join(why_lines)
    realistic_why = " ".join(
        [
            basic_why,
            "El flujo incluye preparación, ejecución y verificación para evitar sorpresas.",
        ]
    )

    example_pitfalls = pitfalls[:5] if len(pitfalls) >= 2 else pitfalls + [
        "No validar el resultado antes de usarlo en pasos posteriores.",
        "Olvidar revisar los argumentos y asumir el comportamiento por defecto.",
    ]

    basic_do = _ensure_minimum_code_lines(
        example,
        context=f"Ejemplo básico de {name}",
        extra_lines=1,
    )
    realistic_do = _ensure_minimum_code_lines(
        example,
        context=f"Caso realista con {name}",
        extra_lines=2,
    )

    return [
        {
            "title": f"Uso básico de {name}",
            "learn": basic_learn,
            "do": basic_do,
            "see": basic_see,
            "why": basic_why,
            "pitfalls": example_pitfalls[:3],
        },
        {
            "title": f"Caso realista con {name}",
            "learn": realistic_learn,
            "do": realistic_do,
            "see": realistic_see,
            "why": realistic_why,
            "pitfalls": example_pitfalls[:5],
        },
    ]


def _ensure_minimum_code_lines(code: str, context: str, extra_lines: int) -> str:
    lines = [line.rstrip() for line in code.strip().splitlines() if line.strip()]
    normalized = [_ensure_inline_comment(line) for line in lines]
    code_line_count = _count_code_lines(normalized)

    filler_lines = []
    for idx in range(max(0, 3 - code_line_count) + extra_lines):
        filler_lines.append(
            f"contexto_{idx + 1} = \"{context}\"  # Aportamos contexto al ejemplo"
        )

    return "\n".join(filler_lines + normalized)


def _ensure_inline_comment(line: str) -> str:
    if "#" in line:
        return line
    return f"{line}  # Explicamos esta línea"


def _count_code_lines(lines: list[str]) -> int:
    count = 0
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        count += 1
    return count


LIBRARIES: dict[str, dict] = {
    "pandas": {
        "title": "Pandas",
        "summary": "Para análisis y manipulación de datos tabulares.",
        "tags": ["dataframe", "csv", "etl"],
        "items": [
            _item(
                "DataFrame",
                "class",
                True,
                "Estructuras",
                "pd.DataFrame(data, ...)",
                "Estructura tabular principal de pandas.",
                ["Cuando necesitas trabajar con filas y columnas."],
                ["Columnas con tipos mezclados", "Índices duplicados"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2]})  # Creamos un DataFrame\n"
                "print(df.head())  # Vemos las primeras filas",
            ),
            _item(
                "Series",
                "class",
                True,
                "Estructuras",
                "pd.Series(data, ...)",
                "Vector etiquetado de una sola columna.",
                ["Cuando trabajas con una sola variable."],
                ["Índice mal alineado", "Valores nulos inesperados"],
                "import pandas as pd  # Importamos pandas\n"
                "s = pd.Series([1, 2, 3])  # Creamos una Serie\n"
                "print(s.mean())  # Calculamos el promedio",
            ),
            _item(
                "read_csv",
                "function",
                True,
                "I/O",
                "pd.read_csv(filepath, ...)",
                "Carga un CSV en un DataFrame.",
                ["Cuando tienes datos en CSV."],
                ["Separador incorrecto", "encoding incorrecto", "dtype mal inferido"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.read_csv('datos.csv')  # Leemos un CSV\n"
                "print(df.shape)  # Revisamos filas y columnas",
            ),
            _item(
                "read_excel",
                "function",
                True,
                "I/O",
                "pd.read_excel(filepath, ...)",
                "Carga hojas de Excel en un DataFrame.",
                ["Cuando los datos están en XLS/XLSX."],
                ["Nombre de hoja incorrecto", "celdas mezcladas"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.read_excel('ventas.xlsx', sheet_name=0)  # Leemos Excel\n"
                "print(df.columns)  # Vemos columnas",
            ),
            _item(
                "to_csv",
                "method",
                True,
                "I/O",
                "df.to_csv(filepath, ...)",
                "Guarda un DataFrame en CSV.",
                ["Cuando necesitas exportar datos."],
                ["Separador no esperado", "Índice guardado por error"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1]})  # Creamos un DataFrame\n"
                "df.to_csv('salida.csv', index=False)  # Exportamos sin índice",
            ),
            _item(
                "head",
                "method",
                True,
                "Inspección",
                "df.head(n=5)",
                "Muestra las primeras filas.",
                ["Cuando quieres revisar el contenido rápidamente."],
                ["Confundir filas mostradas con tamaño real"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2, 3]})  # Creamos datos\n"
                "print(df.head(2))  # Mostramos las primeras 2 filas",
            ),
            _item(
                "info",
                "method",
                True,
                "Inspección",
                "df.info()",
                "Resumen de columnas, tipos y nulos.",
                ["Para entender calidad y tipos de datos."],
                ["Interpretar mal los nulos", "Ignorar memoria"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, None]})  # Datos con nulos\n"
                "df.info()  # Vemos tipos y nulos",
            ),
            _item(
                "describe",
                "method",
                True,
                "Inspección",
                "df.describe()",
                "Estadísticas descriptivas básicas.",
                ["Para variables numéricas rápidamente."],
                ["Solo aplica a numéricos por defecto"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2, 3]})  # Datos numéricos\n"
                "print(df.describe())  # Resumen estadístico",
            ),
            _item(
                "loc",
                "attribute",
                True,
                "Selección",
                "df.loc[fila, columna]",
                "Selección por etiquetas.",
                ["Cuando tu índice tiene nombres."],
                ["Confundir etiqueta con posición"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2]}, index=['x', 'y'])  # Índice nombrado\n"
                "print(df.loc['x', 'a'])  # Seleccionamos por etiqueta",
            ),
            _item(
                "iloc",
                "attribute",
                True,
                "Selección",
                "df.iloc[fila, columna]",
                "Selección por posición entera.",
                ["Cuando necesitas slicing por posición."],
                ["Índices fuera de rango"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2]})  # Creamos datos\n"
                "print(df.iloc[0, 0])  # Seleccionamos por posición",
            ),
            _item(
                "groupby",
                "method",
                True,
                "Agregación",
                "df.groupby(cols)",
                "Agrupa datos para agregación.",
                ["Cuando necesitas resumir por categorías."],
                ["Olvidar reset_index después", "Grupos vacíos"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'cat': ['A', 'A', 'B'], 'x': [1, 2, 3]})  # Datos\n"
                "print(df.groupby('cat')['x'].mean())  # Promedio por grupo",
            ),
            _item(
                "agg",
                "method",
                True,
                "Agregación",
                "df.agg(funcs)",
                "Aplica varias agregaciones.",
                ["Para sumar y promediar a la vez."],
                ["Funciones no compatibles", "Nombres confusos"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1, 2, 3]})  # Datos\n"
                "print(df.agg(['min', 'max']))  # Mínimo y máximo",
            ),
            _item(
                "merge",
                "function",
                True,
                "Combinación",
                "pd.merge(left, right, on=...)",
                "Une tablas tipo SQL.",
                ["Cuando necesitas cruzar DataFrames."],
                ["Claves duplicadas", "Tipo de join incorrecto"],
                "import pandas as pd  # Importamos pandas\n"
                "a = pd.DataFrame({'id': [1], 'x': [10]})  # Tabla izquierda\n"
                "b = pd.DataFrame({'id': [1], 'y': [20]})  # Tabla derecha\n"
                "print(pd.merge(a, b, on='id'))  # Unimos por id",
            ),
            _item(
                "join",
                "method",
                True,
                "Combinación",
                "df.join(other, how=...)",
                "Combina por índice.",
                ["Cuando el índice es la clave."],
                ["Índices no alineados", "Duplicados"],
                "import pandas as pd  # Importamos pandas\n"
                "a = pd.DataFrame({'x': [1]}, index=[1])  # Tabla A con índice\n"
                "b = pd.DataFrame({'y': [2]}, index=[1])  # Tabla B con índice\n"
                "print(a.join(b))  # Unimos por índice",
            ),
            _item(
                "concat",
                "function",
                True,
                "Combinación",
                "pd.concat(objs, axis=0)",
                "Concatena DataFrames o Series.",
                ["Para apilar datos similares."],
                ["Columnas desalineadas", "Índices repetidos"],
                "import pandas as pd  # Importamos pandas\n"
                "a = pd.DataFrame({'x': [1]})  # Primer bloque\n"
                "b = pd.DataFrame({'x': [2]})  # Segundo bloque\n"
                "print(pd.concat([a, b], ignore_index=True))  # Concatenamos",
            ),
            _item(
                "pivot_table",
                "method",
                True,
                "Transformación",
                "df.pivot_table(values, index, columns)",
                "Crea tablas dinámicas.",
                ["Para resumir con filas y columnas."],
                ["Valores duplicados sin agregación"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'cat': ['A', 'A'], 'mes': ['Ene', 'Feb'], 'x': [1, 2]})  # Datos\n"
                "print(df.pivot_table(values='x', index='cat', columns='mes'))  # Tabla dinámica",
            ),
            _item(
                "sort_values",
                "method",
                True,
                "Transformación",
                "df.sort_values(by=...)",
                "Ordena filas por columnas.",
                ["Cuando quieres ranking."],
                ["Ordenar strings como números"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [3, 1, 2]})  # Datos desordenados\n"
                "print(df.sort_values(by='x'))  # Ordenamos por x",
            ),
            _item(
                "dropna",
                "method",
                True,
                "Limpieza",
                "df.dropna()",
                "Elimina filas o columnas con nulos.",
                ["Cuando no quieres nulos en el análisis."],
                ["Perder demasiados datos"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1, None]})  # Datos con nulos\n"
                "print(df.dropna())  # Quitamos filas nulas",
            ),
            _item(
                "fillna",
                "method",
                True,
                "Limpieza",
                "df.fillna(value)",
                "Rellena valores faltantes.",
                ["Cuando necesitas imputar nulos."],
                ["Usar un valor incorrecto", "Cambiar tipos"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1, None]})  # Datos con nulos\n"
                "print(df.fillna(0))  # Rellenamos con 0",
            ),
            _item(
                "astype",
                "method",
                True,
                "Transformación",
                "df.astype(tipo)",
                "Convierte tipos de datos.",
                ["Cuando necesitas un tipo específico."],
                ["Fallos por datos inválidos"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': ['1', '2']})  # Datos como texto\n"
                "print(df.astype({'x': int}))  # Convertimos a entero",
            ),
            _item(
                "value_counts",
                "method",
                True,
                "Agregación",
                "series.value_counts()",
                "Cuenta valores únicos.",
                ["Para frecuencias de categorías."],
                ["Ignorar nulos"],
                "import pandas as pd  # Importamos pandas\n"
                "s = pd.Series(['A', 'A', 'B'])  # Serie categórica\n"
                "print(s.value_counts())  # Contamos ocurrencias",
            ),
            _item(
                "to_excel",
                "method",
                False,
                "I/O",
                "df.to_excel(filepath, ...)",
                "Exporta DataFrame a Excel.",
                ["Cuando necesitas compartir en Excel."],
                ["Sobrescribir archivos", "Hojas mal nombradas"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1]})  # Creamos datos\n"
                "df.to_excel('salida.xlsx', index=False)  # Guardamos a Excel",
            ),
            _item(
                "rename",
                "method",
                False,
                "Transformación",
                "df.rename(columns=..., index=...)",
                "Renombra columnas o índices.",
                ["Para limpiar nombres o estandarizar."],
                ["Olvidar inplace o reasignar"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'a': [1]})  # Datos originales\n"
                "print(df.rename(columns={'a': 'valor'}))  # Renombramos columna",
            ),
            _item(
                "assign",
                "method",
                False,
                "Transformación",
                "df.assign(nueva=...)",
                "Crea columnas nuevas.",
                ["Cuando generas features."],
                ["Sobrescribir columnas sin querer"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1]})  # Datos base\n"
                "print(df.assign(y=df['x'] * 2))  # Creamos nueva columna",
            ),
            _item(
                "query",
                "method",
                False,
                "Selección",
                "df.query('expr')",
                "Filtra filas con expresiones.",
                ["Para filtros legibles."],
                ["Nombres de columnas con espacios"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1, 2]})  # Datos\n"
                "print(df.query('x > 1'))  # Filtramos mayores a 1",
            ),
            _item(
                "set_index",
                "method",
                False,
                "Transformación",
                "df.set_index(cols)",
                "Define nuevas columnas como índice.",
                ["Cuando tu clave principal es una columna."],
                ["Perder columna si drop=True"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'id': [1], 'x': [10]})  # Datos\n"
                "print(df.set_index('id'))  # Usamos id como índice",
            ),
            _item(
                "reset_index",
                "method",
                False,
                "Transformación",
                "df.reset_index()",
                "Regresa el índice a columna.",
                ["Después de groupby o set_index."],
                ["Columnas duplicadas"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1]}, index=[10])  # Índice personalizado\n"
                "print(df.reset_index())  # Volvemos al índice normal",
            ),
            _item(
                "drop",
                "method",
                False,
                "Limpieza",
                "df.drop(labels, axis=...)",
                "Elimina columnas o filas.",
                ["Para quitar columnas innecesarias."],
                ["Axis incorrecto", "Eliminar datos útiles"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1], 'y': [2]})  # Datos\n"
                "print(df.drop(columns=['y']))  # Quitamos columna y",
            ),
            _item(
                "duplicated",
                "method",
                False,
                "Limpieza",
                "df.duplicated()",
                "Marca filas duplicadas.",
                ["Para detectar duplicados antes de eliminarlos."],
                ["No definir subset"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1, 1]})  # Datos duplicados\n"
                "print(df.duplicated())  # Marcamos duplicados",
            ),
            _item(
                "sort_index",
                "method",
                False,
                "Transformación",
                "df.sort_index()",
                "Ordena por índice.",
                ["Cuando el índice es importante."],
                ["Índice con tipos mezclados"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'x': [1]}, index=[2])  # Índice desordenado\n"
                "print(df.sort_index())  # Ordenamos por índice",
            ),
            _item(
                "melt",
                "method",
                False,
                "Transformación",
                "df.melt(id_vars=..., value_vars=...)",
                "Convierte columnas en filas (formato largo).",
                ["Para preparar datos para gráficas o ML."],
                ["Perder columnas claves"],
                "import pandas as pd  # Importamos pandas\n"
                "df = pd.DataFrame({'id': [1], 'a': [10], 'b': [20]})  # Datos anchos\n"
                "print(df.melt(id_vars='id'))  # Pasamos a formato largo",
            ),
        ],
    },
    "sklearn": {
        "title": "scikit-learn",
        "summary": "Herramientas clásicas de machine learning.",
        "tags": ["ml", "modelos", "preprocesamiento"],
        "items": [
            _item(
                "train_test_split",
                "function",
                True,
                "Preparación",
                "train_test_split(X, y, test_size=...)",
                "Divide datos en entrenamiento y prueba.",
                ["Siempre antes de entrenar un modelo."],
                ["Falta de estratificación", "Semilla no fijada"],
                "from sklearn.model_selection import train_test_split  # Importamos función\n"
                "X_train, X_test = train_test_split(X, test_size=0.2)  # Dividimos datos\n"
                "print(len(X_train))  # Vemos tamaño de entrenamiento",
            ),
            _item(
                "Pipeline",
                "class",
                True,
                "Flujos",
                "Pipeline(steps=[...])",
                "Encadena preprocesamiento y modelo.",
                ["Para evitar fugas de datos."],
                ["No nombrar pasos", "No usar fit en pipeline"],
                "from sklearn.pipeline import Pipeline  # Importamos Pipeline\n"
                "pipe = Pipeline(steps=[])  # Definimos pasos\n"
                "print(pipe)  # Revisamos el flujo",
            ),
            _item(
                "ColumnTransformer",
                "class",
                True,
                "Flujos",
                "ColumnTransformer(transformers=...)",
                "Aplica transformaciones por columnas.",
                ["Para mezclar numéricos y categóricos."],
                ["Columnas mal definidas"],
                "from sklearn.compose import ColumnTransformer  # Importamos\n"
                "ct = ColumnTransformer(transformers=[])  # Definimos transformaciones\n"
                "print(ct)  # Revisamos",
            ),
            _item(
                "StandardScaler",
                "class",
                True,
                "Escalado",
                "StandardScaler()",
                "Estandariza variables numéricas.",
                ["Antes de modelos sensibles a escala."],
                ["Aplicar antes de dividir datos"],
                "from sklearn.preprocessing import StandardScaler  # Importamos\n"
                "scaler = StandardScaler()  # Creamos escalador\n"
                "print(scaler)  # Revisamos",
            ),
            _item(
                "MinMaxScaler",
                "class",
                False,
                "Escalado",
                "MinMaxScaler()",
                "Escala datos a un rango fijo.",
                ["Para redes o visualizaciones."],
                ["Sensibilidad a outliers"],
                "from sklearn.preprocessing import MinMaxScaler  # Importamos\n"
                "scaler = MinMaxScaler()  # Creamos escalador\n"
                "print(scaler)  # Revisamos",
            ),
            _item(
                "OneHotEncoder",
                "class",
                True,
                "Codificación",
                "OneHotEncoder(handle_unknown=...)",
                "Convierte categorías en columnas binarias.",
                ["Para modelos que no aceptan texto."],
                ["Nuevas categorías en producción"],
                "from sklearn.preprocessing import OneHotEncoder  # Importamos\n"
                "enc = OneHotEncoder(handle_unknown='ignore')  # Definimos encoder\n"
                "print(enc)  # Revisamos",
            ),
            _item(
                "SimpleImputer",
                "class",
                True,
                "Imputación",
                "SimpleImputer(strategy=...)",
                "Rellena valores faltantes.",
                ["Cuando hay nulos en los datos."],
                ["Usar estrategia incorrecta"],
                "from sklearn.impute import SimpleImputer  # Importamos\n"
                "imp = SimpleImputer(strategy='median')  # Definimos estrategia\n"
                "print(imp)  # Revisamos",
            ),
            _item(
                "LogisticRegression",
                "class",
                True,
                "Modelado",
                "LogisticRegression()",
                "Modelo lineal para clasificación.",
                ["Para problemas binarios o multiclase."],
                ["No escalar datos", "Penalización mal elegida"],
                "from sklearn.linear_model import LogisticRegression  # Importamos\n"
                "model = LogisticRegression()  # Creamos el modelo\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "LinearRegression",
                "class",
                True,
                "Modelado",
                "LinearRegression()",
                "Modelo lineal para regresión.",
                ["Para estimar valores continuos."],
                ["Multicolinealidad", "Escalas muy distintas"],
                "from sklearn.linear_model import LinearRegression  # Importamos\n"
                "model = LinearRegression()  # Creamos el modelo\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "RandomForestClassifier",
                "class",
                True,
                "Modelado",
                "RandomForestClassifier(n_estimators=...)",
                "Ensamble de árboles para clasificación.",
                ["Cuando quieres un baseline robusto."],
                ["Demasiados árboles", "Datos muy ruidosos"],
                "from sklearn.ensemble import RandomForestClassifier  # Importamos\n"
                "model = RandomForestClassifier(n_estimators=100)  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "RandomForestRegressor",
                "class",
                True,
                "Modelado",
                "RandomForestRegressor(n_estimators=...)",
                "Ensamble de árboles para regresión.",
                ["Para regresión no lineal."],
                ["Overfitting", "Tiempo de entrenamiento"],
                "from sklearn.ensemble import RandomForestRegressor  # Importamos\n"
                "model = RandomForestRegressor(n_estimators=200)  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "DecisionTreeClassifier",
                "class",
                False,
                "Modelado",
                "DecisionTreeClassifier(max_depth=...)",
                "Árbol de decisión simple.",
                ["Para explicabilidad rápida."],
                ["Sobreajuste"],
                "from sklearn.tree import DecisionTreeClassifier  # Importamos\n"
                "model = DecisionTreeClassifier(max_depth=3)  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "SVC",
                "class",
                False,
                "Modelado",
                "SVC(kernel=...)",
                "Clasificador de máquinas de soporte.",
                ["Para fronteras no lineales."],
                ["Escala de datos", "Tiempo en datasets grandes"],
                "from sklearn.svm import SVC  # Importamos\n"
                "model = SVC(kernel='rbf')  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "KNeighborsClassifier",
                "class",
                False,
                "Modelado",
                "KNeighborsClassifier(n_neighbors=...)",
                "Clasifica por vecinos cercanos.",
                ["Para datasets pequeños."],
                ["Escala de datos", "Elegir k"],
                "from sklearn.neighbors import KNeighborsClassifier  # Importamos\n"
                "model = KNeighborsClassifier(n_neighbors=5)  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "PCA",
                "class",
                False,
                "Reducción",
                "PCA(n_components=...)",
                "Reduce dimensiones preservando varianza.",
                ["Para visualización o compresión."],
                ["No estandarizar datos"],
                "from sklearn.decomposition import PCA  # Importamos\n"
                "pca = PCA(n_components=2)  # Definimos\n"
                "print(pca)  # Revisamos",
            ),
            _item(
                "LabelEncoder",
                "class",
                False,
                "Codificación",
                "LabelEncoder()",
                "Convierte etiquetas a números.",
                ["Para etiquetas de target."],
                ["Usarlo en variables categóricas no ordinales"],
                "from sklearn.preprocessing import LabelEncoder  # Importamos\n"
                "enc = LabelEncoder()  # Creamos el encoder\n"
                "print(enc)  # Revisamos",
            ),
            _item(
                "accuracy_score",
                "function",
                True,
                "Métricas",
                "accuracy_score(y_true, y_pred)",
                "Porcentaje de aciertos.",
                ["Para clasificación balanceada."],
                ["Engaña con clases desbalanceadas"],
                "from sklearn.metrics import accuracy_score  # Importamos\n"
                "acc = accuracy_score(y_true, y_pred)  # Calculamos exactitud\n"
                "print(acc)  # Mostramos resultado",
            ),
            _item(
                "f1_score",
                "function",
                True,
                "Métricas",
                "f1_score(y_true, y_pred)",
                "Balancea precisión y recall.",
                ["Para clases desbalanceadas."],
                ["No definir average en multiclase"],
                "from sklearn.metrics import f1_score  # Importamos\n"
                "f1 = f1_score(y_true, y_pred)  # Calculamos F1\n"
                "print(f1)  # Mostramos resultado",
            ),
            _item(
                "roc_auc_score",
                "function",
                True,
                "Métricas",
                "roc_auc_score(y_true, y_score)",
                "Área bajo la curva ROC.",
                ["Para ranking probabilístico."],
                ["Usar etiquetas en lugar de scores"],
                "from sklearn.metrics import roc_auc_score  # Importamos\n"
                "auc = roc_auc_score(y_true, y_score)  # Calculamos AUC\n"
                "print(auc)  # Mostramos resultado",
            ),
            _item(
                "classification_report",
                "function",
                False,
                "Métricas",
                "classification_report(y_true, y_pred)",
                "Reporte completo de métricas.",
                ["Para resumen rápido de clases."],
                ["Interpretar sin soportes"],
                "from sklearn.metrics import classification_report  # Importamos\n"
                "rep = classification_report(y_true, y_pred)  # Generamos reporte\n"
                "print(rep)  # Mostramos",
            ),
            _item(
                "confusion_matrix",
                "function",
                False,
                "Métricas",
                "confusion_matrix(y_true, y_pred)",
                "Matriz de confusión.",
                ["Para ver errores por clase."],
                ["Interpretar ejes invertidos"],
                "from sklearn.metrics import confusion_matrix  # Importamos\n"
                "cm = confusion_matrix(y_true, y_pred)  # Calculamos matriz\n"
                "print(cm)  # Mostramos",
            ),
            _item(
                "cross_val_score",
                "function",
                True,
                "Validación",
                "cross_val_score(model, X, y, cv=...)",
                "Evalúa con validación cruzada.",
                ["Para estimar rendimiento general."],
                ["Olvidar random_state en splits"],
                "from sklearn.model_selection import cross_val_score  # Importamos\n"
                "scores = cross_val_score(model, X, y, cv=5)  # Evaluamos\n"
                "print(scores.mean())  # Promedio",
            ),
            _item(
                "GridSearchCV",
                "class",
                True,
                "Optimización",
                "GridSearchCV(model, param_grid, cv=...)",
                "Busca hiperparámetros óptimos.",
                ["Cuando necesitas ajustar el modelo."],
                ["Espacios enormes de búsqueda"],
                "from sklearn.model_selection import GridSearchCV  # Importamos\n"
                "grid = GridSearchCV(model, param_grid, cv=3)  # Definimos búsqueda\n"
                "print(grid)  # Revisamos",
            ),
            _item(
                "SGDClassifier",
                "class",
                False,
                "Modelado",
                "SGDClassifier(loss=...)",
                "Clasificador lineal entrenado con SGD.",
                ["Cuando necesitas modelos rápidos en datasets grandes."],
                ["Sensibilidad a escala", "Necesita ajustar la tasa de aprendizaje"],
                "from sklearn.linear_model import SGDClassifier  # Importamos\n"
                "model = SGDClassifier(loss='log_loss')  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "StratifiedKFold",
                "class",
                False,
                "Validación",
                "StratifiedKFold(n_splits=...)",
                "Divide datos manteniendo proporciones de clases.",
                ["Para validación en clasificación desbalanceada."],
                ["No mezclar con shuffle sin random_state"],
                "from sklearn.model_selection import StratifiedKFold  # Importamos\n"
                "cv = StratifiedKFold(n_splits=5)  # Definimos splits\n"
                "print(cv)  # Revisamos",
            ),
        ],
    },
    "torch": {
        "title": "PyTorch",
        "summary": "Framework flexible para deep learning.",
        "tags": ["tensores", "deep learning", "gpu"],
        "items": [
            _item(
                "tensor",
                "function",
                True,
                "Tensores",
                "torch.tensor(data, ...)",
                "Crea un tensor básico.",
                ["Para representar datos numéricos."],
                ["Tipos inconsistentes"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([1, 2, 3])  # Creamos un tensor\n"
                "print(x.shape)  # Vemos su forma",
            ),
            _item(
                "dtype",
                "attribute",
                True,
                "Tensores",
                "tensor.dtype",
                "Indica el tipo de dato del tensor.",
                ["Para verificar precisión y memoria."],
                ["Operaciones entre tipos distintos"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([1.0])  # Creamos un tensor\n"
                "print(x.dtype)  # Revisamos dtype",
            ),
            _item(
                "device",
                "class",
                True,
                "Hardware",
                "torch.device('cuda' o 'cpu')",
                "Define dónde vive el tensor.",
                ["Para mover datos a GPU."],
                ["Olvidar mover modelo y datos"],
                "import torch  # Importamos torch\n"
                "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Definimos\n"
                "print(device)  # Mostramos",
            ),
            _item(
                "nn.Module",
                "class",
                True,
                "Modelado",
                "torch.nn.Module",
                "Clase base para modelos.",
                ["Siempre que creas una red."],
                ["No llamar super().__init__"],
                "import torch.nn as nn  # Importamos módulo\n"
                "class Net(nn.Module):  # Definimos modelo\n"
                "    pass  # Placeholder",
            ),
            _item(
                "nn.Linear",
                "class",
                True,
                "Capas",
                "torch.nn.Linear(in_features, out_features)",
                "Capa lineal (fully connected).",
                ["Para combinar features."],
                ["Dimensiones incorrectas"],
                "import torch.nn as nn  # Importamos\n"
                "layer = nn.Linear(4, 2)  # Creamos capa\n"
                "print(layer)  # Revisamos",
            ),
            _item(
                "nn.ReLU",
                "class",
                True,
                "Capas",
                "torch.nn.ReLU()",
                "Activación ReLU.",
                ["Después de capas lineales."],
                ["Dead ReLUs"],
                "import torch.nn as nn  # Importamos\n"
                "act = nn.ReLU()  # Definimos activación\n"
                "print(act)  # Revisamos",
            ),
            _item(
                "nn.Sequential",
                "class",
                False,
                "Capas",
                "torch.nn.Sequential(...)",
                "Encadena capas en orden.",
                ["Para prototipos rápidos."],
                ["No apto para lógica compleja"],
                "import torch.nn as nn  # Importamos\n"
                "model = nn.Sequential(nn.Linear(2, 2), nn.ReLU())  # Definimos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "Dataset",
                "class",
                True,
                "Datos",
                "torch.utils.data.Dataset",
                "Interfaz para datasets personalizados.",
                ["Cuando tus datos no están en memoria."],
                ["No implementar __len__"],
                "from torch.utils.data import Dataset  # Importamos\n"
                "class MyDataset(Dataset):  # Definimos dataset\n"
                "    pass  # Placeholder",
            ),
            _item(
                "DataLoader",
                "class",
                True,
                "Datos",
                "torch.utils.data.DataLoader(dataset, batch_size=...)",
                "Crea lotes y baraja datos.",
                ["Para entrenar por minibatches."],
                ["batch_size demasiado grande"],
                "from torch.utils.data import DataLoader  # Importamos\n"
                "loader = DataLoader(dataset, batch_size=32)  # Creamos loader\n"
                "print(loader)  # Revisamos",
            ),
            _item(
                "optim.SGD",
                "class",
                True,
                "Optimización",
                "torch.optim.SGD(params, lr=...)",
                "Optimizador por descenso de gradiente.",
                ["Para entrenar modelos básicos."],
                ["Learning rate mal elegido"],
                "import torch.optim as optim  # Importamos\n"
                "opt = optim.SGD(model.parameters(), lr=0.01)  # Definimos\n"
                "print(opt)  # Revisamos",
            ),
            _item(
                "optim.Adam",
                "class",
                True,
                "Optimización",
                "torch.optim.Adam(params, lr=...)",
                "Optimizador adaptativo popular.",
                ["Default frecuente en deep learning."],
                ["Learning rate demasiado alto"],
                "import torch.optim as optim  # Importamos\n"
                "opt = optim.Adam(model.parameters(), lr=0.001)  # Definimos\n"
                "print(opt)  # Revisamos",
            ),
            _item(
                "backward",
                "method",
                True,
                "Autograd",
                "loss.backward()",
                "Calcula gradientes automáticamente.",
                ["Después de calcular la pérdida."],
                ["No llamar zero_grad antes"],
                "loss = output.sum()  # Definimos pérdida\n"
                "loss.backward()  # Calculamos gradientes\n"
                "print(loss)  # Revisamos",
            ),
            _item(
                "zero_grad",
                "method",
                True,
                "Autograd",
                "optimizer.zero_grad()",
                "Limpia gradientes acumulados.",
                ["Antes de cada paso de entrenamiento."],
                ["Olvidarlo causa acumulación"],
                "optimizer.zero_grad()  # Limpiamos gradientes\n"
                "loss.backward()  # Calculamos gradientes\n"
                "optimizer.step()  # Actualizamos parámetros",
            ),
            _item(
                "train",
                "method",
                True,
                "Modo",
                "model.train()",
                "Activa modo entrenamiento.",
                ["Antes de entrenar."],
                ["Olvidar cambiar a eval"],
                "model.train()  # Activamos modo entrenamiento\n"
                "outputs = model(inputs)  # Forward pass\n"
                "print(outputs.shape)  # Revisamos",
            ),
            _item(
                "eval",
                "method",
                True,
                "Modo",
                "model.eval()",
                "Activa modo evaluación.",
                ["Antes de validar o predecir."],
                ["No desactivar dropout"],
                "model.eval()  # Activamos modo evaluación\n"
                "outputs = model(inputs)  # Predicción\n"
                "print(outputs.shape)  # Revisamos",
            ),
            _item(
                "no_grad",
                "context",
                True,
                "Autograd",
                "torch.no_grad()",
                "Desactiva cálculo de gradientes.",
                ["Para inferencia rápida."],
                ["Olvidar reactivar gradientes"],
                "with torch.no_grad():  # Desactivamos gradientes\n"
                "    outputs = model(inputs)  # Inferencia\n"
                "    print(outputs.shape)  # Revisamos",
            ),
            _item(
                "state_dict",
                "method",
                False,
                "Persistencia",
                "model.state_dict()",
                "Devuelve pesos del modelo.",
                ["Para guardar o cargar modelos."],
                ["No guardar también hiperparámetros"],
                "state = model.state_dict()  # Obtenemos pesos\n"
                "print(state.keys())  # Vemos nombres\n"
                "print(len(state))  # Contamos",
            ),
            _item(
                "torch.save",
                "function",
                False,
                "Persistencia",
                "torch.save(obj, path)",
                "Guarda tensores o modelos.",
                ["Para checkpointing."],
                ["Rutas incorrectas"],
                "import torch  # Importamos torch\n"
                "torch.save(state, 'model.pt')  # Guardamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "torch.load",
                "function",
                False,
                "Persistencia",
                "torch.load(path)",
                "Carga tensores o modelos guardados.",
                ["Para restaurar pesos."],
                ["Cambios de versión"],
                "import torch  # Importamos torch\n"
                "state = torch.load('model.pt')  # Cargamos\n"
                "print(state)  # Revisamos",
            ),
            _item(
                "nn.CrossEntropyLoss",
                "class",
                False,
                "Pérdida",
                "torch.nn.CrossEntropyLoss()",
                "Pérdida para clasificación multiclase.",
                ["Cuando el target es un entero por clase."],
                ["Usar logits mal dimensionados"],
                "import torch.nn as nn  # Importamos\n"
                "loss_fn = nn.CrossEntropyLoss()  # Definimos pérdida\n"
                "print(loss_fn)  # Revisamos",
            ),
            _item(
                "torch.cat",
                "function",
                False,
                "Tensores",
                "torch.cat(tensors, dim=...)",
                "Concatena tensores.",
                ["Para unir batches o features."],
                ["Dimensiones incompatibles"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([[1]])  # Tensor 1\n"
                "y = torch.tensor([[2]])  # Tensor 2\n"
                "print(torch.cat([x, y], dim=0))  # Concatenamos",
            ),
            _item(
                "torch.stack",
                "function",
                False,
                "Tensores",
                "torch.stack(tensors, dim=...)",
                "Apila tensores creando nueva dimensión.",
                ["Para crear batches desde listas."],
                ["Confundir con cat"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([1])  # Tensor 1\n"
                "y = torch.tensor([2])  # Tensor 2\n"
                "print(torch.stack([x, y], dim=0))  # Apilamos",
            ),
            _item(
                "to",
                "method",
                False,
                "Hardware",
                "tensor.to(device)",
                "Mueve tensor a CPU o GPU.",
                ["Cuando cambias de dispositivo."],
                ["Mezclar dispositivos en operaciones"],
                "device = torch.device('cpu')  # Definimos dispositivo\n"
                "x = torch.tensor([1])  # Creamos tensor\n"
                "print(x.to(device))  # Movemos",
            ),
            _item(
                "requires_grad",
                "attribute",
                False,
                "Autograd",
                "tensor.requires_grad",
                "Indica si calcula gradientes.",
                ["Para congelar capas."],
                ["Olvidar activarlo en parámetros"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([1.0], requires_grad=True)  # Tensor con grad\n"
                "print(x.requires_grad)  # Revisamos",
            ),
            _item(
                "torch.mean",
                "function",
                False,
                "Tensores",
                "torch.mean(tensor, dim=...)",
                "Calcula la media de un tensor.",
                ["Para resumir valores por dimensión."],
                ["Dimensión incorrecta"],
                "import torch  # Importamos torch\n"
                "x = torch.tensor([1.0, 2.0, 3.0])  # Definimos tensor\n"
                "print(torch.mean(x))  # Calculamos media",
            ),
        ],
    },
    "tensorflow": {
        "title": "TensorFlow/Keras",
        "summary": "Framework integral para deep learning con Keras.",
        "tags": ["keras", "redes", "entrenamiento"],
        "items": [
            _item(
                "tf.Tensor",
                "class",
                True,
                "Tensores",
                "tf.Tensor",
                "Objeto principal para datos en TensorFlow.",
                ["Para representar entradas y salidas."],
                ["Convertir listas sin dtype"],
                "import tensorflow as tf  # Importamos tensorflow\n"
                "x = tf.constant([1, 2, 3])  # Creamos tensor\n"
                "print(x.shape)  # Revisamos forma",
            ),
            _item(
                "keras.Model",
                "class",
                True,
                "Modelado",
                "tf.keras.Model",
                "Clase base para modelos personalizados.",
                ["Cuando quieres control total."],
                ["No definir call"],
                "from tensorflow import keras  # Importamos keras\n"
                "class Net(keras.Model):  # Definimos modelo\n"
                "    pass  # Placeholder",
            ),
            _item(
                "Sequential",
                "class",
                True,
                "Modelado",
                "keras.Sequential(layers)",
                "Modelo lineal de capas en serie.",
                ["Para arquitecturas simples."],
                ["No definir input_shape"],
                "from tensorflow import keras  # Importamos keras\n"
                "model = keras.Sequential([])  # Definimos modelo\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "Dense",
                "class",
                True,
                "Capas",
                "keras.layers.Dense(units, activation=...)",
                "Capa fully connected.",
                ["Para redes densas."],
                ["Dimensiones incorrectas"],
                "from tensorflow.keras import layers  # Importamos capas\n"
                "dense = layers.Dense(64, activation='relu')  # Definimos capa\n"
                "print(dense)  # Revisamos",
            ),
            _item(
                "compile",
                "method",
                True,
                "Entrenamiento",
                "model.compile(optimizer=..., loss=..., metrics=...)",
                "Configura entrenamiento del modelo.",
                ["Antes de llamar fit."],
                ["Perder métricas por mal nombre"],
                "model.compile(optimizer='adam', loss='mse')  # Compilamos\n"
                "print(model.loss)  # Revisamos pérdida\n"
                "print(model.optimizer)  # Revisamos optimizador",
            ),
            _item(
                "fit",
                "method",
                True,
                "Entrenamiento",
                "model.fit(X, y, epochs=...)",
                "Entrena el modelo.",
                ["Para ajustar parámetros con datos."],
                ["Epochs excesivos", "Batch size incorrecto"],
                "history = model.fit(X, y, epochs=5)  # Entrenamos\n"
                "print(history.history)  # Vemos métricas\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "evaluate",
                "method",
                True,
                "Evaluación",
                "model.evaluate(X, y)",
                "Evalúa el modelo en datos nuevos.",
                ["Para validar o testear."],
                ["Usar datos con diferente escala"],
                "loss = model.evaluate(X_test, y_test)  # Evaluamos\n"
                "print(loss)  # Vemos pérdida\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "Adam",
                "class",
                True,
                "Optimización",
                "keras.optimizers.Adam(learning_rate=...)",
                "Optimizador adaptativo popular.",
                ["Default frecuente en deep learning."],
                ["Learning rate alto"],
                "from tensorflow.keras import optimizers  # Importamos\n"
                "opt = optimizers.Adam(learning_rate=0.001)  # Definimos\n"
                "print(opt)  # Revisamos",
            ),
            _item(
                "callbacks.EarlyStopping",
                "class",
                True,
                "Callbacks",
                "keras.callbacks.EarlyStopping(...)",
                "Detiene el entrenamiento si no mejora.",
                ["Para evitar overfitting."],
                ["No monitorear métrica correcta"],
                "from tensorflow.keras import callbacks  # Importamos\n"
                "cb = callbacks.EarlyStopping(patience=3)  # Definimos\n"
                "print(cb)  # Revisamos",
            ),
            _item(
                "callbacks.ModelCheckpoint",
                "class",
                False,
                "Callbacks",
                "keras.callbacks.ModelCheckpoint(filepath=...)",
                "Guarda el mejor modelo durante entrenamiento.",
                ["Para conservar el mejor checkpoint."],
                ["Ruta inválida"],
                "from tensorflow.keras import callbacks  # Importamos\n"
                "cb = callbacks.ModelCheckpoint('model.keras')  # Definimos\n"
                "print(cb)  # Revisamos",
            ),
            _item(
                "tf.data.Dataset",
                "class",
                True,
                "Datos",
                "tf.data.Dataset.from_tensor_slices(...)",
                "API para pipelines de datos.",
                ["Para datasets grandes o streaming."],
                ["No usar batch/prefetch"],
                "import tensorflow as tf  # Importamos\n"
                "ds = tf.data.Dataset.from_tensor_slices([1, 2, 3])  # Creamos dataset\n"
                "print(ds)  # Revisamos",
            ),
            _item(
                "datasets.mnist",
                "function",
                False,
                "Datos",
                "keras.datasets.mnist.load_data()",
                "Carga dataset MNIST de ejemplo.",
                ["Para demos rápidas."],
                ["Descarga requiere red"],
                "from tensorflow.keras import datasets  # Importamos\n"
                "(x_train, y_train), _ = datasets.mnist.load_data()  # Cargamos\n"
                "print(x_train.shape)  # Revisamos",
            ),
            _item(
                "Conv2D",
                "class",
                False,
                "Capas",
                "keras.layers.Conv2D(filters, kernel_size, ...)",
                "Capa convolucional para imágenes.",
                ["Para visión por computador."],
                ["Input shape mal definido"],
                "from tensorflow.keras import layers  # Importamos\n"
                "conv = layers.Conv2D(32, (3, 3), activation='relu')  # Definimos\n"
                "print(conv)  # Revisamos",
            ),
            _item(
                "MaxPooling2D",
                "class",
                False,
                "Capas",
                "keras.layers.MaxPooling2D(pool_size=...)",
                "Reduce tamaño espacial con pooling.",
                ["Para bajar dimensiones en CNN."],
                ["Pool size excesivo"],
                "from tensorflow.keras import layers  # Importamos\n"
                "pool = layers.MaxPooling2D(pool_size=(2, 2))  # Definimos\n"
                "print(pool)  # Revisamos",
            ),
            _item(
                "Dropout",
                "class",
                False,
                "Regularización",
                "keras.layers.Dropout(rate)",
                "Apaga neuronas aleatoriamente.",
                ["Para reducir overfitting."],
                ["Rate demasiado alto"],
                "from tensorflow.keras import layers  # Importamos\n"
                "drop = layers.Dropout(0.2)  # Definimos\n"
                "print(drop)  # Revisamos",
            ),
            _item(
                "Flatten",
                "class",
                False,
                "Capas",
                "keras.layers.Flatten()",
                "Convierte tensores a vector.",
                ["Antes de capas densas."],
                ["Olvidar input_shape"],
                "from tensorflow.keras import layers  # Importamos\n"
                "flat = layers.Flatten()  # Definimos\n"
                "print(flat)  # Revisamos",
            ),
            _item(
                "BatchNormalization",
                "class",
                False,
                "Regularización",
                "keras.layers.BatchNormalization()",
                "Normaliza activaciones en batch.",
                ["Para estabilizar entrenamiento."],
                ["Uso incorrecto en inferencia"],
                "from tensorflow.keras import layers  # Importamos\n"
                "bn = layers.BatchNormalization()  # Definimos\n"
                "print(bn)  # Revisamos",
            ),
            _item(
                "predict",
                "method",
                False,
                "Inferencia",
                "model.predict(X)",
                "Genera predicciones.",
                ["Para inferencia en producción."],
                ["Batch size muy pequeño"],
                "pred = model.predict(X_new)  # Predecimos\n"
                "print(pred.shape)  # Revisamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "save",
                "method",
                False,
                "Persistencia",
                "model.save(path)",
                "Guarda el modelo completo.",
                ["Para exportar a producción."],
                ["Ruta sin permisos"],
                "model.save('modelo.keras')  # Guardamos modelo\n"
                "print('ok')  # Confirmamos\n"
                "print('listo')  # Confirmamos",
            ),
            _item(
                "load_model",
                "function",
                False,
                "Persistencia",
                "keras.models.load_model(path)",
                "Carga un modelo guardado.",
                ["Para reusar un modelo entrenado."],
                ["Versiones incompatibles"],
                "from tensorflow.keras import models  # Importamos\n"
                "model = models.load_model('modelo.keras')  # Cargamos\n"
                "print(model)  # Revisamos",
            ),
            _item(
                "losses",
                "module",
                False,
                "Entrenamiento",
                "keras.losses",
                "Colección de funciones de pérdida.",
                ["Para elegir pérdida adecuada."],
                ["Pérdida incompatible con target"],
                "from tensorflow.keras import losses  # Importamos\n"
                "loss_fn = losses.MeanSquaredError()  # Elegimos pérdida\n"
                "print(loss_fn)  # Revisamos",
            ),
            _item(
                "metrics",
                "module",
                False,
                "Evaluación",
                "keras.metrics",
                "Métricas predefinidas.",
                ["Para monitorear entrenamiento."],
                ["Confundir métricas con pérdidas"],
                "from tensorflow.keras import metrics  # Importamos\n"
                "m = metrics.Accuracy()  # Definimos métrica\n"
                "print(m)  # Revisamos",
            ),
            _item(
                "optimizers",
                "module",
                False,
                "Optimización",
                "keras.optimizers",
                "Colección de optimizadores.",
                ["Para elegir optimizador correcto."],
                ["No ajustar learning_rate"],
                "from tensorflow.keras import optimizers  # Importamos\n"
                "opt = optimizers.SGD(learning_rate=0.01)  # Definimos\n"
                "print(opt)  # Revisamos",
            ),
            _item(
                "Input",
                "function",
                False,
                "Modelado",
                "keras.Input(shape=...)",
                "Define entradas en la API funcional.",
                ["Para modelos con múltiples entradas."],
                ["No definir shape correctamente"],
                "from tensorflow.keras import layers  # Importamos\n"
                "inputs = layers.Input(shape=(10,))  # Definimos entrada\n"
                "print(inputs)  # Revisamos",
            ),
            _item(
                "layers",
                "module",
                False,
                "Capas",
                "keras.layers",
                "Módulo con capas estándar.",
                ["Para construir modelos."],
                ["Confundir capas con modelos"],
                "from tensorflow.keras import layers  # Importamos\n"
                "dense = layers.Dense(8)  # Creamos capa\n"
                "print(dense)  # Revisamos",
            ),
        ],
    },
    "pyside6": {
        "title": "PySide6",
        "summary": "Framework para interfaces gráficas con Qt.",
        "tags": ["gui", "qt", "desktop"],
        "items": [
            _item(
                "QApplication",
                "class",
                True,
                "Base",
                "QApplication(sys.argv)",
                "Arranca la app Qt.",
                ["Siempre antes de crear widgets."],
                ["Crear más de una instancia"],
                "from PySide6.QtWidgets import QApplication  # Importamos\n"
                "app = QApplication([])  # Creamos la aplicación\n"
                "print(app)  # Revisamos",
            ),
            _item(
                "QWidget",
                "class",
                True,
                "Base",
                "QWidget()",
                "Widget básico para UI.",
                ["Para crear ventanas simples."],
                ["Olvidar mostrar el widget"],
                "from PySide6.QtWidgets import QWidget  # Importamos\n"
                "w = QWidget()  # Creamos widget\n"
                "print(w)  # Revisamos",
            ),
            _item(
                "QMainWindow",
                "class",
                True,
                "Ventanas",
                "QMainWindow()",
                "Ventana principal con menús y status.",
                ["Para apps con barra de menú."],
                ["No establecer centralWidget"],
                "from PySide6.QtWidgets import QMainWindow  # Importamos\n"
                "win = QMainWindow()  # Creamos ventana\n"
                "print(win)  # Revisamos",
            ),
            _item(
                "QDialog",
                "class",
                False,
                "Ventanas",
                "QDialog()",
                "Ventana modal o diálogo.",
                ["Para formularios o confirmaciones."],
                ["Bloquear UI sin necesidad"],
                "from PySide6.QtWidgets import QDialog  # Importamos\n"
                "dlg = QDialog()  # Creamos diálogo\n"
                "print(dlg)  # Revisamos",
            ),
            _item(
                "QVBoxLayout",
                "class",
                True,
                "Layouts",
                "QVBoxLayout()",
                "Organiza widgets en columna.",
                ["Para apilar elementos verticalmente."],
                ["No asignar layout al widget"],
                "from PySide6.QtWidgets import QVBoxLayout  # Importamos\n"
                "layout = QVBoxLayout()  # Creamos layout\n"
                "print(layout)  # Revisamos",
            ),
            _item(
                "QHBoxLayout",
                "class",
                True,
                "Layouts",
                "QHBoxLayout()",
                "Organiza widgets en fila.",
                ["Para botones en una misma línea."],
                ["Espaciado insuficiente"],
                "from PySide6.QtWidgets import QHBoxLayout  # Importamos\n"
                "layout = QHBoxLayout()  # Creamos layout\n"
                "print(layout)  # Revisamos",
            ),
            _item(
                "QGridLayout",
                "class",
                False,
                "Layouts",
                "QGridLayout()",
                "Organiza widgets en una grilla.",
                ["Para formularios con filas y columnas."],
                ["Mala alineación de celdas"],
                "from PySide6.QtWidgets import QGridLayout  # Importamos\n"
                "layout = QGridLayout()  # Creamos layout\n"
                "print(layout)  # Revisamos",
            ),
            _item(
                "QPushButton",
                "class",
                True,
                "Controles",
                "QPushButton('Texto')",
                "Botón clicable.",
                ["Para acciones principales."],
                ["No conectar la señal clicked"],
                "from PySide6.QtWidgets import QPushButton  # Importamos\n"
                "btn = QPushButton('Guardar')  # Creamos botón\n"
                "print(btn.text())  # Revisamos",
            ),
            _item(
                "QLabel",
                "class",
                True,
                "Controles",
                "QLabel('Texto')",
                "Muestra texto o imágenes.",
                ["Para títulos o descripciones."],
                ["Texto sin wordWrap"],
                "from PySide6.QtWidgets import QLabel  # Importamos\n"
                "label = QLabel('Hola')  # Creamos etiqueta\n"
                "print(label.text())  # Revisamos",
            ),
            _item(
                "QLineEdit",
                "class",
                True,
                "Controles",
                "QLineEdit()",
                "Campo de texto corto.",
                ["Para inputs simples."],
                ["No validar entrada"],
                "from PySide6.QtWidgets import QLineEdit  # Importamos\n"
                "edit = QLineEdit()  # Creamos input\n"
                "print(edit.text())  # Revisamos",
            ),
            _item(
                "QTextEdit",
                "class",
                False,
                "Controles",
                "QTextEdit()",
                "Campo de texto multilínea.",
                ["Para notas o mensajes largos."],
                ["No limitar longitud"],
                "from PySide6.QtWidgets import QTextEdit  # Importamos\n"
                "text = QTextEdit()  # Creamos editor\n"
                "print(text.toPlainText())  # Revisamos",
            ),
            _item(
                "QListWidget",
                "class",
                True,
                "Controles",
                "QListWidget()",
                "Lista simple de items.",
                ["Para listados rápidos."],
                ["No manejar itemSelectionChanged"],
                "from PySide6.QtWidgets import QListWidget  # Importamos\n"
                "lst = QListWidget()  # Creamos lista\n"
                "print(lst.count())  # Revisamos",
            ),
            _item(
                "QTableWidget",
                "class",
                False,
                "Controles",
                "QTableWidget()",
                "Tabla simple en memoria.",
                ["Para tablas pequeñas."],
                ["No definir filas/columnas"],
                "from PySide6.QtWidgets import QTableWidget  # Importamos\n"
                "table = QTableWidget(3, 2)  # Creamos tabla\n"
                "print(table.rowCount())  # Revisamos",
            ),
            _item(
                "QComboBox",
                "class",
                True,
                "Controles",
                "QComboBox()",
                "Selector desplegable.",
                ["Para opciones cerradas."],
                ["No definir opciones"],
                "from PySide6.QtWidgets import QComboBox  # Importamos\n"
                "combo = QComboBox()  # Creamos combo\n"
                "print(combo.count())  # Revisamos",
            ),
            _item(
                "QCheckBox",
                "class",
                False,
                "Controles",
                "QCheckBox('Texto')",
                "Casilla de verificación.",
                ["Para opciones booleanas."],
                ["No leer estado"],
                "from PySide6.QtWidgets import QCheckBox  # Importamos\n"
                "chk = QCheckBox('Activo')  # Creamos checkbox\n"
                "print(chk.isChecked())  # Revisamos",
            ),
            _item(
                "QRadioButton",
                "class",
                False,
                "Controles",
                "QRadioButton('Texto')",
                "Selector exclusivo dentro de un grupo.",
                ["Para elegir una opción única."],
                ["No agrupar con QButtonGroup"],
                "from PySide6.QtWidgets import QRadioButton  # Importamos\n"
                "radio = QRadioButton('Opción A')  # Creamos radio\n"
                "print(radio.isChecked())  # Revisamos",
            ),
            _item(
                "QTimer",
                "class",
                False,
                "Eventos",
                "QTimer()",
                "Ejecuta acciones periódicas.",
                ["Para refrescar UI o datos."],
                ["Intervalos demasiado cortos"],
                "from PySide6.QtCore import QTimer  # Importamos\n"
                "timer = QTimer()  # Creamos timer\n"
                "print(timer.interval())  # Revisamos",
            ),
            _item(
                "QThread",
                "class",
                False,
                "Concurrencia",
                "QThread()",
                "Hilo de ejecución para tareas pesadas.",
                ["Para no bloquear la UI."],
                ["Actualizar UI desde el hilo"],
                "from PySide6.QtCore import QThread  # Importamos\n"
                "thread = QThread()  # Creamos hilo\n"
                "print(thread.isRunning())  # Revisamos",
            ),
            _item(
                "Signal",
                "class",
                True,
                "Señales",
                "Signal()",
                "Define señales personalizadas.",
                ["Para comunicar widgets."],
                ["No usar QObject como base"],
                "from PySide6.QtCore import Signal, QObject  # Importamos\n"
                "class Emisor(QObject):  # Definimos clase\n"
                "    listo = Signal()  # Señal personalizada",
            ),
            _item(
                "Slot",
                "decorator",
                False,
                "Señales",
                "@Slot()",
                "Marca métodos como slots.",
                ["Para mejorar rendimiento/seguridad."],
                ["Firmas incorrectas"],
                "from PySide6.QtCore import Slot  # Importamos\n"
                "@Slot()  # Definimos slot\n"
                "def handler():  # Función\n"
                "    pass  # Placeholder",
            ),
            _item(
                "QAction",
                "class",
                False,
                "Menús",
                "QAction('Texto', parent)",
                "Acción reutilizable en menús/toolbar.",
                ["Para comandos globales."],
                ["No conectar triggered"],
                "from PySide6.QtGui import QAction  # Importamos\n"
                "action = QAction('Salir')  # Creamos acción\n"
                "print(action.text())  # Revisamos",
            ),
            _item(
                "QMenuBar",
                "class",
                False,
                "Menús",
                "QMenuBar()",
                "Barra de menú superior.",
                ["Para apps de escritorio clásicas."],
                ["No agregar menús"],
                "from PySide6.QtWidgets import QMenuBar  # Importamos\n"
                "menu = QMenuBar()  # Creamos barra de menú\n"
                "print(menu)  # Revisamos",
            ),
            _item(
                "QStatusBar",
                "class",
                False,
                "Menús",
                "QStatusBar()",
                "Barra inferior de estado.",
                ["Para mensajes breves."],
                ["Mostrar mensajes permanentes"],
                "from PySide6.QtWidgets import QStatusBar  # Importamos\n"
                "status = QStatusBar()  # Creamos status bar\n"
                "print(status)  # Revisamos",
            ),
            _item(
                "QMessageBox",
                "class",
                False,
                "Diálogos",
                "QMessageBox.information(...)",
                "Muestra diálogos de alerta.",
                ["Para errores o confirmaciones."],
                ["Bloquear la UI con demasiados mensajes"],
                "from PySide6.QtWidgets import QMessageBox  # Importamos\n"
                "QMessageBox.information(None, 'OK', 'Guardado')  # Mostramos mensaje\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "QFileDialog",
                "class",
                False,
                "Diálogos",
                "QFileDialog.getOpenFileName(...)",
                "Diálogo para abrir archivos.",
                ["Para seleccionar archivos en la UI."],
                ["No validar ruta"],
                "from PySide6.QtWidgets import QFileDialog  # Importamos\n"
                "path, _ = QFileDialog.getOpenFileName()  # Abrimos diálogo\n"
                "print(path)  # Revisamos",
            ),
        ],
    },
    "sqlalchemy": {
        "title": "SQLAlchemy",
        "summary": "ORM y toolkit SQL para Python.",
        "tags": ["sql", "orm", "bases"],
        "items": [
            _item(
                "create_engine",
                "function",
                True,
                "Conexión",
                "create_engine(url)",
                "Crea un engine de conexión.",
                ["Para conectarte a una base."],
                ["URL incorrecta", "Pool mal configurado"],
                "from sqlalchemy import create_engine  # Importamos\n"
                "engine = create_engine('sqlite:///db.sqlite')  # Creamos engine\n"
                "print(engine)  # Revisamos",
            ),
            _item(
                "text",
                "function",
                True,
                "SQL",
                "text('SELECT ...')",
                "Envuelve SQL textual.",
                ["Para consultas raw."],
                ["SQL inyección si no parametrizas"],
                "from sqlalchemy import text  # Importamos\n"
                "stmt = text('SELECT 1')  # Definimos SQL\n"
                "print(stmt)  # Revisamos",
            ),
            _item(
                "Connection",
                "class",
                True,
                "Conexión",
                "engine.connect()",
                "Objeto de conexión para ejecutar SQL.",
                ["Para consultas puntuales."],
                ["Olvidar cerrar conexión"],
                "conn = engine.connect()  # Abrimos conexión\n"
                "result = conn.execute(text('SELECT 1'))  # Ejecutamos\n"
                "conn.close()  # Cerramos",
            ),
            _item(
                "Session",
                "class",
                True,
                "ORM",
                "Session(engine)",
                "Gestiona transacciones ORM.",
                ["Para trabajar con modelos ORM."],
                ["No cerrar sesión"],
                "from sqlalchemy.orm import Session  # Importamos\n"
                "session = Session(engine)  # Creamos sesión\n"
                "print(session)  # Revisamos",
            ),
            _item(
                "sessionmaker",
                "function",
                False,
                "ORM",
                "sessionmaker(bind=engine)",
                "Factory para sesiones.",
                ["Para reutilizar configuración."],
                ["No configurar autoflush"],
                "from sqlalchemy.orm import sessionmaker  # Importamos\n"
                "SessionLocal = sessionmaker(bind=engine)  # Creamos factory\n"
                "print(SessionLocal)  # Revisamos",
            ),
            _item(
                "declarative_base",
                "function",
                True,
                "ORM",
                "declarative_base()",
                "Crea clase base de modelos ORM.",
                ["Para definir modelos con clases."],
                ["No definir __tablename__"],
                "from sqlalchemy.orm import declarative_base  # Importamos\n"
                "Base = declarative_base()  # Creamos base\n"
                "print(Base)  # Revisamos",
            ),
            _item(
                "Column",
                "class",
                True,
                "ORM",
                "Column(tipo, ...)",
                "Define columnas en modelos.",
                ["Para definir el esquema."],
                ["No definir primary_key"],
                "from sqlalchemy import Column, Integer  # Importamos\n"
                "col = Column(Integer, primary_key=True)  # Definimos columna\n"
                "print(col)  # Revisamos",
            ),
            _item(
                "relationship",
                "function",
                True,
                "ORM",
                "relationship('Clase')",
                "Define relaciones entre modelos.",
                ["Para claves foráneas."],
                ["Back_populates incorrecto"],
                "from sqlalchemy.orm import relationship  # Importamos\n"
                "rel = relationship('Child')  # Definimos relación\n"
                "print(rel)  # Revisamos",
            ),
            _item(
                "select",
                "function",
                True,
                "SQL",
                "select(tabla)",
                "Construye consultas SELECT.",
                ["Para consultas con SQLAlchemy Core."],
                ["No ejecutar con conexión"],
                "from sqlalchemy import select  # Importamos\n"
                "stmt = select(table)  # Definimos consulta\n"
                "print(stmt)  # Revisamos",
            ),
            _item(
                "insert",
                "function",
                False,
                "SQL",
                "insert(tabla).values(...)",
                "Construye INSERT.",
                ["Para insertar filas."],
                ["No usar transacciones"],
                "from sqlalchemy import insert  # Importamos\n"
                "stmt = insert(table).values(id=1)  # Definimos insert\n"
                "print(stmt)  # Revisamos",
            ),
            _item(
                "update",
                "function",
                False,
                "SQL",
                "update(tabla).values(...)",
                "Construye UPDATE.",
                ["Para actualizar filas."],
                ["Olvidar where"],
                "from sqlalchemy import update  # Importamos\n"
                "stmt = update(table).values(status='ok')  # Definimos update\n"
                "print(stmt)  # Revisamos",
            ),
            _item(
                "delete",
                "function",
                False,
                "SQL",
                "delete(tabla)",
                "Construye DELETE.",
                ["Para borrar filas específicas."],
                ["Olvidar where"],
                "from sqlalchemy import delete  # Importamos\n"
                "stmt = delete(table)  # Definimos delete\n"
                "print(stmt)  # Revisamos",
            ),
            _item(
                "MetaData",
                "class",
                False,
                "SQL",
                "MetaData()",
                "Contenedor de tablas.",
                ["Para definir schema en Core."],
                ["No reflejar schema"],
                "from sqlalchemy import MetaData  # Importamos\n"
                "metadata = MetaData()  # Creamos metadata\n"
                "print(metadata)  # Revisamos",
            ),
            _item(
                "Table",
                "class",
                False,
                "SQL",
                "Table(name, metadata, ...)",
                "Define una tabla en Core.",
                ["Para SQLAlchemy Core."],
                ["No definir columnas"],
                "from sqlalchemy import Table  # Importamos\n"
                "table = Table('users', metadata)  # Definimos tabla\n"
                "print(table)  # Revisamos",
            ),
            _item(
                "ForeignKey",
                "class",
                False,
                "SQL",
                "ForeignKey('tabla.columna')",
                "Define clave foránea.",
                ["Para relaciones entre tablas."],
                ["Referencias incorrectas"],
                "from sqlalchemy import ForeignKey  # Importamos\n"
                "fk = ForeignKey('users.id')  # Definimos FK\n"
                "print(fk)  # Revisamos",
            ),
            _item(
                "Integer",
                "class",
                False,
                "Tipos",
                "Integer()",
                "Tipo de columna entero.",
                ["Para IDs o contadores."],
                ["Rangos insuficientes"],
                "from sqlalchemy import Integer  # Importamos\n"
                "col = Column(Integer)  # Usamos tipo Integer\n"
                "print(col)  # Revisamos",
            ),
            _item(
                "String",
                "class",
                False,
                "Tipos",
                "String(length=...)",
                "Tipo de columna texto.",
                ["Para nombres o etiquetas."],
                ["Longitud insuficiente"],
                "from sqlalchemy import String  # Importamos\n"
                "col = Column(String(100))  # Usamos tipo String\n"
                "print(col)  # Revisamos",
            ),
            _item(
                "engine.begin",
                "method",
                False,
                "Transacciones",
                "engine.begin()",
                "Contexto para transacciones.",
                ["Para garantizar commit/rollback."],
                ["No manejar excepciones"],
                "with engine.begin() as conn:  # Abrimos transacción\n"
                "    conn.execute(text('SELECT 1'))  # Ejecutamos\n"
                "    print('ok')  # Confirmamos",
            ),
            _item(
                "commit",
                "method",
                False,
                "Transacciones",
                "session.commit()",
                "Confirma cambios en la sesión.",
                ["Después de add o update."],
                ["No manejar errores"],
                "session.add(obj)  # Añadimos objeto\n"
                "session.commit()  # Confirmamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "rollback",
                "method",
                False,
                "Transacciones",
                "session.rollback()",
                "Revierte cambios en la sesión.",
                ["Si ocurre un error."],
                ["Olvidar limpiar la sesión"],
                "session.rollback()  # Revertimos cambios\n"
                "print('ok')  # Confirmamos\n"
                "session.close()  # Cerramos",
            ),
            _item(
                "join",
                "method",
                False,
                "SQL",
                "select(...).join(...)",
                "Une tablas en consultas ORM/Core.",
                ["Para consultas con relaciones."],
                ["Joins cartesianos"],
                "stmt = select(User).join(User.profile)  # Definimos join\n"
                "print(stmt)  # Revisamos\n"
                "print('ok')  # Confirmamos",
            ),
        ],
    },
    "sqlite3": {
        "title": "sqlite3",
        "summary": "Base de datos embebida incluida en Python.",
        "tags": ["sql", "local", "sqlite"],
        "items": [
            _item(
                "connect",
                "function",
                True,
                "Conexión",
                "sqlite3.connect(path)",
                "Abre una base de datos SQLite.",
                ["Para bases locales o prototipos."],
                ["Ruta inválida", "Bloqueo por concurrencia"],
                "import sqlite3  # Importamos sqlite3\n"
                "conn = sqlite3.connect('db.sqlite')  # Abrimos conexión\n"
                "print(conn)  # Revisamos",
            ),
            _item(
                "cursor",
                "method",
                True,
                "Conexión",
                "conn.cursor()",
                "Crea un cursor para ejecutar SQL.",
                ["Antes de ejecutar consultas."],
                ["No cerrar cursor"],
                "cur = conn.cursor()  # Creamos cursor\n"
                "print(cur)  # Revisamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "execute",
                "method",
                True,
                "SQL",
                "cursor.execute(sql, params)",
                "Ejecuta una consulta SQL.",
                ["Para SELECT/INSERT/UPDATE."],
                ["SQL injection si no usas params"],
                "cur.execute('SELECT 1')  # Ejecutamos SQL\n"
                "row = cur.fetchone()  # Leemos una fila\n"
                "print(row)  # Revisamos",
            ),
            _item(
                "executemany",
                "method",
                False,
                "SQL",
                "cursor.executemany(sql, seq_of_params)",
                "Ejecuta la misma consulta varias veces.",
                ["Para insertar muchas filas."],
                ["No usar transacciones"],
                "cur.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])  # Insertamos\n"
                "conn.commit()  # Confirmamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "commit",
                "method",
                True,
                "Transacciones",
                "conn.commit()",
                "Guarda cambios en la base.",
                ["Después de INSERT/UPDATE."],
                ["Olvidarlo causa pérdida de datos"],
                "conn.commit()  # Confirmamos cambios\n"
                "print('ok')  # Confirmamos\n"
                "print('listo')  # Confirmamos",
            ),
            _item(
                "rollback",
                "method",
                False,
                "Transacciones",
                "conn.rollback()",
                "Revierte cambios no confirmados.",
                ["Si ocurre un error."],
                ["No revisar estado"],
                "conn.rollback()  # Revertimos cambios\n"
                "print('ok')  # Confirmamos\n"
                "print('listo')  # Confirmamos",
            ),
            _item(
                "fetchone",
                "method",
                False,
                "SQL",
                "cursor.fetchone()",
                "Obtiene una fila de resultados.",
                ["Después de SELECT."],
                ["Consumir resultados sin revisar None"],
                "row = cur.fetchone()  # Leemos una fila\n"
                "print(row)  # Revisamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "fetchall",
                "method",
                False,
                "SQL",
                "cursor.fetchall()",
                "Obtiene todas las filas.",
                ["Para resultados pequeños."],
                ["Consumo de memoria alto"],
                "rows = cur.fetchall()  # Leemos todas las filas\n"
                "print(len(rows))  # Contamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "close",
                "method",
                False,
                "Conexión",
                "conn.close()",
                "Cierra la conexión.",
                ["Al final del uso."],
                ["Cerrar antes de commit"],
                "conn.close()  # Cerramos conexión\n"
                "print('ok')  # Confirmamos\n"
                "print('listo')  # Confirmamos",
            ),
            _item(
                "row_factory",
                "attribute",
                False,
                "Conexión",
                "conn.row_factory",
                "Permite devolver filas como dicts.",
                ["Para acceso por nombre de columna."],
                ["Olvidar configurar antes del cursor"],
                "conn.row_factory = sqlite3.Row  # Configuramos row_factory\n"
                "cur = conn.cursor()  # Creamos cursor\n"
                "print(cur)  # Revisamos",
            ),
            _item(
                "context manager",
                "pattern",
                False,
                "Conexión",
                "with sqlite3.connect(...) as conn:",
                "Manejo automático de commit/rollback.",
                ["Para asegurar cierre automático."],
                ["No manejar excepciones internas"],
                "import sqlite3  # Importamos sqlite3\n"
                "with sqlite3.connect('db.sqlite') as conn:  # Abrimos conexión\n"
                "    conn.execute('SELECT 1')  # Ejecutamos",
            ),
            _item(
                "lastrowid",
                "attribute",
                False,
                "SQL",
                "cursor.lastrowid",
                "ID de la última fila insertada.",
                ["Para recuperar IDs autoincrement."],
                ["Usar después de executemany"],
                "cur.execute('INSERT INTO t VALUES (NULL)')  # Insertamos\n"
                "print(cur.lastrowid)  # Revisamos ID\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "executescript",
                "method",
                False,
                "SQL",
                "cursor.executescript(sql_script)",
                "Ejecuta múltiples sentencias SQL.",
                ["Para inicializar un schema."],
                ["Scripts sin transacción"],
                "cur.executescript('CREATE TABLE t (id INTEGER);')  # Ejecutamos script\n"
                "conn.commit()  # Confirmamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "PRAGMA",
                "command",
                False,
                "SQL",
                "PRAGMA journal_mode;",
                "Configura opciones internas de SQLite.",
                ["Para ajustar rendimiento o integridad."],
                ["Cambiar settings sin entender impacto"],
                "cur.execute('PRAGMA journal_mode=WAL;')  # Ajustamos modo\n"
                "row = cur.fetchone()  # Leemos respuesta\n"
                "print(row)  # Revisamos",
            ),
            _item(
                "execute (parametrizado)",
                "pattern",
                False,
                "SQL",
                "cursor.execute(sql, params)",
                "Evita inyección SQL usando parámetros.",
                ["Siempre que recibas input externo."],
                ["Interpolar strings manualmente"],
                "cur.execute('SELECT * FROM t WHERE id=?', (1,))  # Parametrizamos\n"
                "row = cur.fetchone()  # Leemos fila\n"
                "print(row)  # Revisamos",
            ),
        ],
    },
    "redshift": {
        "title": "Amazon Redshift",
        "summary": "Data warehouse en la nube basado en PostgreSQL.",
        "tags": ["dwh", "aws", "analytics"],
        "items": [
            _item(
                "SQLAlchemy URL",
                "concept",
                True,
                "Conexión",
                "redshift+psycopg2://user:pass@host:5439/db",
                "URL típica para conectar con SQLAlchemy.",
                ["Cuando configuras un engine."],
                ["Credenciales en texto plano"],
                "from sqlalchemy import create_engine  # Importamos\n"
                "engine = create_engine('redshift+psycopg2://user:pass@host:5439/db')  # Conectamos\n"
                "print(engine)  # Revisamos",
            ),
            _item(
                "COPY",
                "command",
                True,
                "Carga",
                "COPY tabla FROM 's3://...'",
                "Carga masiva desde S3.",
                ["Para cargar grandes volúmenes."],
                ["IAM roles mal configurados"],
                "sql = \"COPY ventas FROM 's3://bucket/ventas.csv'\"  # Definimos COPY\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "UNLOAD",
                "command",
                False,
                "Exportación",
                "UNLOAD ('SELECT ...') TO 's3://...'",
                "Exporta resultados a S3.",
                ["Para compartir datasets grandes."],
                ["Permisos insuficientes"],
                "sql = \"UNLOAD ('SELECT * FROM tabla') TO 's3://bucket/out/'\"  # Definimos\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "VACUUM",
                "command",
                False,
                "Mantenimiento",
                "VACUUM tabla",
                "Recupera espacio y ordena datos.",
                ["Después de muchas actualizaciones."],
                ["Ejecutarlo con alto tráfico"],
                "sql = 'VACUUM tabla;'  # Definimos comando\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "ANALYZE",
                "command",
                False,
                "Mantenimiento",
                "ANALYZE tabla",
                "Actualiza estadísticas del optimizador.",
                ["Para mejorar planes de consulta."],
                ["Olvidarlo después de cargas masivas"],
                "sql = 'ANALYZE tabla;'  # Definimos comando\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "Distribution Style",
                "concept",
                False,
                "Arquitectura",
                "DISTSTYLE KEY/ALL/EVEN",
                "Define cómo se distribuyen datos entre nodos.",
                ["Para optimizar joins."],
                ["Elegir DISTSTYLE sin revisar cardinalidad"],
                "sql = 'CREATE TABLE t (id INT) DISTSTYLE EVEN;'  # Definimos diststyle\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "Sort Keys",
                "concept",
                False,
                "Arquitectura",
                "SORTKEY(col1, col2)",
                "Ordena datos físicamente para acelerar queries.",
                ["Cuando filtras siempre por ciertas columnas."],
                ["Elegir columnas poco selectivas"],
                "sql = 'CREATE TABLE t (id INT) SORTKEY(id);'  # Definimos sortkey\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "WLM",
                "concept",
                False,
                "Rendimiento",
                "Workload Management",
                "Gestiona colas y prioridades de consultas.",
                ["Para controlar recursos y latencia."],
                ["Colas con demasiada concurrencia"],
                "sql = 'SELECT * FROM stv_wlm_service_class_config;'  # Consultamos WLM\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "Statement Timeout",
                "concept",
                False,
                "Rendimiento",
                "statement_timeout",
                "Limita el tiempo máximo de una consulta.",
                ["Para evitar consultas infinitas."],
                ["Timeout demasiado bajo"],
                "sql = 'SET statement_timeout TO 600000;'  # Definimos timeout\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
            _item(
                "STL Tables",
                "concept",
                False,
                "Monitoreo",
                "STL_QUERY, STL_LOAD_ERRORS",
                "Tablas del sistema para monitoreo.",
                ["Para investigar errores o rendimiento."],
                ["Permisos insuficientes"],
                "sql = 'SELECT * FROM stl_load_errors LIMIT 5;'  # Consultamos errores\n"
                "conn.execute(sql)  # Ejecutamos\n"
                "print('ok')  # Confirmamos",
            ),
        ],
    },
}
