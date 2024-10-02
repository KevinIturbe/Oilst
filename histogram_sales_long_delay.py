# %% [markdown]
# Desarrolla un programa ("histogram_sales_long_delay.py")que construya el histograma de frecuencias de la variable total_sales, junto con los intervalos que define la regla empírica débil para encontrar el 88.88% de los datos alrededor del promedio, restringiendo el análisis a las órdenes que tienen status completo. El resultado de este script deberá ser una figura denominada “histogram_sales_long_delay.png”.

# %%
#Preparando el ambiente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Lectura de datos
datos = pd.read_csv("oilst_processed.csv")

# %%
datos = datos[datos['order_status'] == 'delivered']

# %%
media = datos.total_sales.mean() #Media
dist_std = datos.total_sales.std() #Distribución estándar
lim_superior = media + dist_std*3
lim_inferior = 0

# %%
media

# %%
#Creando la figura y construyendo el gráfico
plt.figure(figsize=(15,10))
sns.histplot(data=datos, x='total_sales', bins=50)

#Limitar el eje x para mejorar la visualización
plt.xlim(0, 2300)

#Agregando títulos
plt.title("Histograma de ventas con retraso largo")
plt.xlabel("Total de ventas")
plt.ylabel("Frecuencias")

plt.axvline(lim_inferior, label=f'Límite Inferior: {lim_inferior:.2f}', color='orange', linestyle='--')
plt.axvline(lim_superior, label=f'Límite Superior: {lim_superior:.2f}', color='orange', linestyle='--')
plt.axvline(media, label=f'Media: {media:.2f}', color='red', )

plt.legend()

#Guardar la figura
plt.savefig("histogram_sales_long_delay.png")

#mostrar la figura
plt.show()


