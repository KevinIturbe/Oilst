# %% [markdown]
# Crea un programa (“3_a_histogram_sales_short_long_delays.py”) que construya una visualización que permita comparar los histogramas de las ventas de órdenes completas que tuvieron retrasos moderados y prolongados. La imagen resultante del programa deberá denominarse “3_a_histogram_sales_short_long_delays.png”.

# %%
#Preparando el ambiente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Leyendo los datos
datos = pd.read_csv("oilst_processed.csv")

# %%
pd.set_option('display.max_columns', None)
datos.head()

# %%
datos.delay_status.unique()

# %%
#Filtrando datos
datos = datos[datos['order_status'] == 'delivered']
datos = datos[(datos['delay_status']== 'long_delay') | (datos['delay_status'] == 'short_delay')]

# %%
#Creando el gráfico

plt.figure(figsize=(20,15))
sns.histplot(data=datos, x='total_sales', hue='delay_status', kde =True)

#Se establece un límite para mejorar la visualización
plt.xlim(0,1000)

#Agregando etiquetas y título
plt.xlabel("Ventas", fontsize=20)
plt.ylabel("Total", fontsize=20)
plt.title("Histogramas de venta por retraso", fontsize=20)

#Guardando la figura
plt.savefig("3_a_histogram_sales_short_long_delays.png")
plt.show()


