# %% [markdown]
# ![title](./images/logo_nao_digital.png)

# %% [markdown]
# # Tema 1: Conocimientos sobre Pandas
# 
# ## 1. Objetivo
# 
# Procesar en Python la información entregada por el equipo de Ingeniería de datos de Oilst de forma funcional para el análisis de los retrasos en las órdenes de los clientes.
# 
# ## Datos de Oilst
# 
# Cómo se ha mencionado en el Anexo A, se ha provisto la siguiente información al equipo de `Brasil BI Consulting:`
# 
# | Archivo                      	| Descripción                                                                                                                                     	| Formato 	|
# |------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------	|---------	|
# | olist_customers_dataset      	| Datos de identificación de los clientes y la ubicación del domicilio que tienen registrado con Olist para recibir pedidos.                      	| xlsx    	|
# | olist_orders_dataset         	| Datos de identificación de las órdenes realizadas por los clientes, su estatus de envío y la cronología de entrega en el domicilio del cliente. 	| csv     	|
# | olist_geolocation_dataset    	| Datos de geolocalización de códigos postales de zonas de Brasil.                                                                                	| csv     	|
# | olist_order_items_dataset    	| Contiene la relación de artículos contenidos en las órdenes de los clientes                                                                     	| csv     	|
# | olist_order_payments_dataset 	| Contiene la relación de pagos que cada cliente hizo en sus órdenes por medio de pago                                                            	| csv     	|
# | states_abreviations          	| Contiene la relación de nombres de los estados de Brasil y sus abreviaciones.                                                                   	| json    	|
# 
# 
# Adicionalmente, también se tiene el diagrama de relación entre las tablas:
# 
# ![title](../images/oilst_diagram.png)
# 
# 

# %% [markdown]
# Este documento se desarrollarán scripts en Python que permitan procesar la  la información de Oilst para realizar posteriormente el análisis de sus datos

# %% [markdown]
# ## 2. Librerias de trabajo

# %%
import os
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# %% [markdown]
# ## 3. Lectura de datos
# 
# Primero nos encargaremos de leer los datos, indicando a Python donde se encuentra la carpeta que contiene los datos y los nombres de los archivos relevantes para el análisis.

# %%
#  Indicamos la ruta a la carpeta de de tu computadora 
# donde se ubican los datos del E-commerce
# Ejemplo: "C:\Usuarios\[tu nombre]\Descargas"

DATA_PATH=r"C:\Users\Kevin\Documents\NAO\Reto 1\datos"

# %% [markdown]
# Ahora procederemos a definir variables que indiquen el nombre de los archivos junto con su extensión (por ejemplo, `.csv`, `.json` u otra).

# %%
FILE_CUSTOMERS = 'olist_customers_dataset.xlsx'
FILE_GEOLOCATIONS = 'olist_geolocation_dataset.csv'

# completa los nombres del resto de los archivos con su extesion (ejemplo .csv) ...
FILE_ITEMS = 'olist_order_items_dataset.csv' 
FILE_PAYMENTS = 'olist_order_payments_dataset.csv'
FILE_ORDERS =  'olist_orders_dataset.csv'
FILE_STATES_ABBREVIATIONS = 'states_abbreviations.json'

# %% [markdown]
# Echaremos mano de la utilidad `os.path.join` de Python que indicar rutas en tu computadora donde se ubican archivos, así Pandas encontrá los archivos de datos.
# 
# 
# **Ejemplo**
# 
# A continuación mostraremos un ejemplo leyendo el archivo `olist_geolocation_dataset.csv`:

# %%
# Ejemplo
print(f"Ruta del archivo: {FILE_GEOLOCATIONS}")
print(os.path.join(DATA_PATH, FILE_GEOLOCATIONS))

# %%
# Leemos con pandas
geolocations = pd.read_csv(
    os.path.join(DATA_PATH, FILE_GEOLOCATIONS),
    dtype={'geolocation_zip_code_prefix': 'str'}
    )

# %% [markdown]
# Podemos explorar el archivo con los comandos `.head(), .info(), .describe()`

# %% [markdown]
# **Función .head()**
# 
# Este comando nos brinda información de los primeros renglones de la tabla:

# %%
geolocations.head()

# %% [markdown]
# **Función .describe()**
# 
# Este comando nos ayuda obtener información estadística de las variables de la tabla, entre ellas el conteo de los elementos no nulos de una columnas, la media, su desviación estándar (que es una medida de que tan dispersa se encuentra la información a partir de su media), el primer, segundo y tercer cuartil de los datos 
# que se refiere a que valor de los datos ocupar el 25%, 50% y 75% de la distribución de los datos si se ordenan de menor a mayor y que se denotan, respectivamente como, denotado Q1, Q2 y Q3. Además provee información del mínimo y máximo presentes en la columna.

# %%
geolocations .describe()

# %% [markdown]
# **Función .info()**
# 
# Este comando nos ayuda obtener información de cuantas entradas tiene una tabla, el tipo de dato en que se representarn sus columnas y el tamaño que ocupa en la memoria de nuestra computadora.

# %%
geolocations.info()

# %% [markdown]
# Ahora estamos en posición de completar el código para el resto de conjuntos de datos:
# 
# ### 3.1 Archivo olist_customers_dataset
# 
# **Hint:** 
# 
# 1. Pandas necesita instalar una libreria extrar para leer éste tipo de archivos (`openpyxl`).
# 2. Se debe expecificar el tipo de dato de `customer_zip_code_prefix` (ver Anexo A)

# %%
customers = pd.read_excel(
    os.path.join(DATA_PATH, FILE_CUSTOMERS),
    # Especificar el tipo de dato de customer_zip_code_prefix
    dtype={'customer_zip_code_prefix': str}
    )

# %% [markdown]
# Verificamos que `customer_zip_code_prefix` tenga el formato correcto (Ojo: !no es un número, sino un código postal!)

# %%
customers.info()

# %% [markdown]
# También podemos visualizar una muestra aleatoria con el método `.sample(numero_entero)`

# %%
# Revisamos 10 renglones al azar
customers.sample(10)

# %% [markdown]
# ### 3.2 Archivo olist_order_items_dataset

# %%
items = pd.read_csv(
    # Completa la ubicacion usando os.path.join, DATA_PATH y
    # el nombre del archivo FILE_ITEMS
    os.path.join(DATA_PATH, FILE_ITEMS)
    )

# %% [markdown]
# Como sabemos, este conjunto contiene datos de los productos que contiene cada orden. Por ello, para el análisis nos interesará saber cual es la cantidad de productos en cada orden y el precio total de las mismas.
# 
# Esto se puede calcular mediante agregaciones de Pandas (https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.core.groupby.DataFrameGroupBy.agg.html), que basicamente nos permite hacer cálculos para un grupo en especial. En el ejemplo de inferior se muestra para cada `order_id` se cuenta la cantidad de productos (items) y el precio agregado de todos los artículos en las órdenes:

# %%
items_agg = items.groupby(
    ['order_id']).agg(
        # conteo de producto
        {'order_item_id': 'count',
        # suma de los precios de los artículos
        'price': 'sum'}
                      ).reset_index() 

# %%
items_agg.head()

# %% [markdown]
# Vamos a renombrar las columnas anteriores, para que sea más intuitivo su significado.

# %%
# Nota: el parámetro inplace sobre escribe los cambios
# en el dataframe
items_agg.rename(
    columns={'order_item_id': 'total_products', 'price': 'total_sales'},
    inplace=True
    )

# %%
items_agg

# %% [markdown]
# Vamos a repetir el proceso anterior para el resto de tablas:

# %% [markdown]
# ### 3.3 olist_order_payments_dataset

# %%
payments = pd.read_csv(
    # Completa la ubicacion usando os.path.join, DATA_PATH y
    # el nombre del archivo correspondiente a los pagos
    os.path.join(DATA_PATH,FILE_PAYMENTS)
    )

# %% [markdown]
# ### 3.4 states_abbreviations

# %%
states_abbreviations = pd.read_json(
    # Completa la ubicacion usando os.path.join, DATA_PATH y
    # el nombre del archivo correspondiente a las abreviaciones de los estados
    os.path.join(DATA_PATH,FILE_STATES_ABBREVIATIONS)
    )

# %% [markdown]
# ### 3.5 olist_orders_dataset

# %%
orders = pd.read_csv(
    # Completa la ubicacion usando os.path.join, DATA_PATH y
    # el nombre del archivo correspondiente a las ordenes de Oislt
    os.path.join(DATA_PATH,FILE_ORDERS)
    )

# %% [markdown]
# Si revisamos el formato que Pandas ha otorgado a las columnas que contienen fecha encontraremos algo extraño, no se ha interpretado correctamente:

# %%
orders.info()

# %% [markdown]
# Por lo tanto es necesario convertir las columnas al formato de fecha `datetime` (Ver: https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587).
# 
# Emplearemos la función `to_datetime` de Pandas para modificar las columnas para que se interpreten como fechas:

# %%
# Convierte a formato fecha completando los campos apropiados

## convierte order_purchase_timestamp
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'] , errors='coerce' )

# order_approved_at
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'], errors = 'coerce')

# order_delivered_carrier_date
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'], errors = 'coerce')

# order_delivered_customer_date
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors = 'coerce')

# order_estimated_delivery_date
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'], errors = 'coerce')

# %% [markdown]
# Ahora podemos ver como ha cambiado el formato:

# %%
orders.info()

# %% [markdown]
# Una vez corregido el tema de las fecha definiremos también algunas variables auxiliares que nos serviran posteriormente en el análisis.
# 
# Por ejemplo, es de interés conocer en que mes, año y trimestre del año sucedieron las compras, usando la columna `order_purchase_timestamp`:

# %%
# Define una columna con el año en que sucedió la orden
orders['year'] = orders['order_purchase_timestamp'].dt.year

# Define una columna con el mes en que sucedió la orden
orders['month'] = orders['order_purchase_timestamp'].dt.month

# Define una columna con trimestre con el que paso la orden (ej. Q12018)
# https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html
orders['quarter'] = orders['order_purchase_timestamp'].dt.to_period('Q')

# Define una columna con mes y año con el que paso la orden (ej. 02-2018)
# Hint: ¿que hace el metodo ...to_period('M')?
orders['year_month'] = orders['order_purchase_timestamp'].dt.to_period('M')

# %% [markdown]
# Por otro lado, también necesitamos identificar las órdenes que tuvieron retrasos prolongados. Recordemos que de acuerdo a la documentación del `Anexo A`:
# * Oilst notifica el usuario de cuando llegará su pedido con el valor de la columna `order_estimated_delivery_date`,
# * Además la fecha real en que se llevó la entrega se encuentra en el campo `order_delivered_customer_date`
# 
# A continuación calcularemos distancia (en días) entre ambas fecha definiendo a la variable `delta_days`:

# %%
# Nota: tenemos que realizar la conversion de
# segundos a días

orders['delta_days'] = (
    orders['order_delivered_customer_date'] -
    orders['order_estimated_delivery_date']
    ).dt.total_seconds()/ 60 / 60 / 24

# %% [markdown]
# **Pregunta:**
# 
# * ¿Porqué para convertir lo anterior a días tenemos que dividir entre 60, después entre 60 y luego entre 24?

# %% [markdown]
# Podemos explorar ahora los valores de dicha variables con el método `.descri be()`

# %%
orders['delta_days'].describe()

# %% [markdown]
# En el contexto del problema, los valores de `delta_days` tiene el significado:
# 
# * Un valor negativo en `delta_days` significa que el pedido llego antes de lo esperado; es decir, no existió retraso.
# * Un valor de `delta_days`, mayor a 0 días pero menor a 3 días, significa que es un retrazo aceptable,
# * Sin embargo, si `delta_days` es más grande que 3 días esto significa que tenemos un retrazo prolongado.
# 
# Crearemos una variable `delay_status` para indicar la discusión anterior usando el operador `where` de Numpy (https://towardsdatascience.com/creating-conditional-columns-on-pandas-with-numpy-select-and-where-methods-8ee6e2dbd5d5).
# 
# Esencialmente, el operador `where` de Numpy permite definir variables siguiendo reglas lógicas de manera condicional, similar al `if ... else ...` de Python:

# %%
# Define 
orders['delay_status']  = np.where(
    orders['delta_days'] > 3, 'long_delay',
    np.where(orders['delta_days'] <= 0, 'on_time','short_delay')
    )

# %% [markdown]
# Para ver el efecto de lo anterior podemos extraer un muestra con la función `.sample`

# %%
orders['delay_status'].sample(10)

# %% [markdown]
# **Pregunta:**
# 
# * ¿Las categorías anteriores en que se han clasificado los estatus de entrega de las órdenes se pueden inteserctar?
# 

# %% [markdown]
# ### 3.5 olist_geolocation_dataset
# 
# Aunque anteriormente hemos leído este archivo, debemos notar que contiene información redudante de muchos codigos postales, como en el caso del valor `24220`:
# 

# %%
geolocations.query("geolocation_zip_code_prefix == 24220")

# %% [markdown]
# Para el análisis tendremos que eliminar esta duplicaciones. Esto se puede lograr con el método `drop_duplicates`

# %%
unique_geolocations = geolocations.drop_duplicates(
    subset = ['geolocation_zip_code_prefix']
    )

# %% [markdown]
# Como se aprecia a continuación, ahora el dataframe `unique_geolocations` corrige el error:

# %%
unique_geolocations.query(
    "geolocation_zip_code_prefix == 24220"
    )

# %% [markdown]
# ## 4. Procesamiento global
# 
# Ahora que hemos cargado a Pandas los datos del E-commerce, debemos **consolidar toda la información** en una sola tabla, lo que nos permitirá centralizar el análisis y hacer comparativos.
# 
# Para ello, nos proponemos lo siguiente:
# 1. A los datos de clientes le añadiremos los datos de geolocalización. **(Clientes + geolocalización)**
# 2. Tales datos se complementarán añadiendo los datos del nombre del estado de Brasil en que se localizan. (**Clientes + geolocalización + nombre del estado donde viven**)
# 3. Posteriormente archivo de órdenes, agregaremos los datos del precio y cantidad de artículos. **(Órdenes + total de artículos y precios)**
# 4. Finalmente, uniremos toda la información de los pasos 2 y 3 en una sola tabla.

# %% [markdown]
# ### 4.1 Clientes + geolocalización

# %% [markdown]
# Para unir dos fuentes de datos, podemos usar la función `.merge` (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html). En el siguiente ejemplo se unes los datos de los clientes junto sus geolocalizaciones.
# 
# **Nota:** Los códigos postales deben tener el formato texto.

# %%
customers_geolocation = customers.merge(
    unique_geolocations,
    left_on='customer_zip_code_prefix',
    right_on='geolocation_zip_code_prefix',
    how='left'
)

# %%
customers_geolocation.head()

# %% [markdown]
# ### 4.2 Clientes + geolocalización + nombre del estado donde viven
# 
# Ahora repetiremos un proceso análogo pero con los nombres del estado donde viven los customers

# %%
# Une los dataframe customers_geolocation y states_abbreviations

customers_geolocation_estado = customers_geolocation.merge(
    states_abbreviations,
    left_on='geolocation_state',
    right_on='abbreviation',
    how='left'
)

# %%
customers_geolocation_estado

# %% [markdown]
# ### 4.3 Órdenes + total de artículos y precios

# %%
# une los dataframe orders y items_agg por order_id
orders_totals = orders.merge(
    items_agg,
    on=['order_id'],
    how='left'
    )

# %% [markdown]
# ### 4.4 Clientes + geolocalización + nombre del estado donde viven + Órdenes + total de artículos y precios

# %%
results = orders_totals.merge(
    customers_geolocation_estado,
    on=['customer_id'],
    how='left'
    )

# %%
len(results.columns)

# %%
#Se consolida la información en un archivo csv
oilst = results.to_csv("oilst_processed.csv")

# %%
#Se verifica el archivo
print(os.path.exists("oilst_processed.csv"))


