# %% [markdown]
# Crea un script ("correlation_matrix_10_days_delay.py") que calcule la matriz de correlación entre las variables total_sales, total_products, delta_days y distance_distribution_center para órdenes completadas que cuya fecha de entrega sobrepasa los 10 días de la fecha estimada para la entrega. El resultado de este script deberá ser una figura denominada “correlation_matrix_10_days_delay.png”.

# %%
#Preparando el ambiente
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
datos = pd.read_csv("oilst_processed.csv")

# %%
datos.dtypes

# %%
#Se filtran las entregas realizadas 10 días después de la fecha de entrega.
datos = datos[datos.delta_days > 10]

# %%
#Se filtran los datos. Se seleccionan las ordenes completadas
datos =datos[datos['order_status'] =='delivered' ]

# %%
#Se seleccionan columnas de interés 
datos = datos[['total_sales', 'total_products', 'delta_days', 'distance_distribution_center']]

# %%
matriz = datos.corr()

# %%
#Se crea el mapa de calor
plt.figure(figsize=(12,10))
sns.heatmap(matriz, annot=True,   fmt=".2f", cmap='coolwarm', square=True)

plt.title("Matriz de correlación para órdenes con retraso mayor a 10 días")
plt.savefig("correlation_matrix_10_days_delay.png")
plt.show()
plt.close()


