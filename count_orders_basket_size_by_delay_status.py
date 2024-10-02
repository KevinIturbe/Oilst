# %% [markdown]
# Elabora un programa ("count_orders_basket_size_by_delay_status.py") que construya una tabla que muestre el número de órdenes que existieron por cantidad de productos dentro de la orden y el tipo de retraso de las categorías delay_status. El resultado de este script deberá ser un tabla denominada “count_orders_basket_size_by_delay_status.csv.”

# %%
#Preparando el ambiente
import pandas as pd
oilst = pd.read_csv("oilst_processed.csv")

# %%
#Se seleccionan los atributos de interés, se utiliza reset_index() para convertir el resultado a DF y value_counts() para contar el número de casos
num_productos_estado = oilst[["delay_status", "total_products"]].value_counts().reset_index(name="total")

# %%
#Se crea el archivo csv
num_productos_estado.to_csv("count_orders_basket_size_by_delay_status.csv")


