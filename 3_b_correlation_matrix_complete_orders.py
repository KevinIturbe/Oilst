# %% [markdown]
# Diseña un programa (“3_b_correlation_matrix_complete_orders.py”) que genere una visualización de la matriz de correlación de delta_days junto con el resto de variables numéricas, para las órdenes en las que se concretó su entrega. La figura resultante del programa deberá llamarse “3_b_correlation_matrix_complete_orders.png”.

# %%
#Preparando el ambiente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
datos = pd.read_csv("oilst_processed.csv")

# %%
#Filtrando los datos
datos = datos.query("order_status == 'delivered'")

# %%
#Buscando las variables numéricas
datos.dtypes

# %%
datos = datos[['delta_days', 'distance_distribution_center', 'total_products', 'total_sales', 'year', 'month', 'geolocation_lng', 'geolocation_lat']].corr()

# %%
plt.figure(figsize=(20,20))
sns.heatmap(datos, annot=True,  cmap='coolwarm')

#Añadiendo titulo
plt.title("Matriz de correlación de órdenes completas", fontsize=20)

plt.savefig("3_b_correlation_matrix_complete_orders.png")
plt.show()
plt.close()


