# %% [markdown]
# Crea un script ("prop_sales_delay_status_by_quarte.py") que calcule la proporción que han representado las ventas de órdenes completas de Oilst dentro de los categorías de delay_status y a los largo de los trimestres de 2016 a 2018. El resultado de este script deberá ser un tabla denominada “prop_sales_delay_status_by_quarte.csv”.

# %%
import pandas as pd

# %%
oilst = pd.read_csv("oilst_processed.csv")

# %%
oilst.head()

# %%
oilst.columns

# %%
#Filtrando solo las ordenes completadas
datos = oilst[oilst["order_status"] == "delivered"]

# %%
datos = datos[["order_status", "delay_status", "quarter"]]

# %%
datos.head()

# %%
#Se agrupan por situación y trimestre y se calcula cuantas veces aparece esa combinación
datos_agrupados = datos.groupby(["delay_status", "quarter"]).size().reset_index(name="conteo")

# %%
datos_agrupados

# %%
total_trimestre = datos_agrupados.groupby("quarter")['conteo'].transform('sum')

# %%
datos_agrupados['proporcion']= ( datos_agrupados['conteo'] / total_trimestre)  * 100

# %%
resultado = datos_agrupados[["quarter", "delay_status", "proporcion"]].sort_values("quarter")

# %%
resultado.to_csv("prop_sales_delay_status_by_quarte.csv")


