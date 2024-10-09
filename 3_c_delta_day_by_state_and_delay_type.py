# %% [markdown]
# Implementa un programa que construya una visualización que permite observar la distribución de la variable delta_days a lo largo de los estados de Brasil. Dicha visualización deberá segmentarse o aperturarse de forma que permita revisar la variación a través diferentes valores del campo delay_status. Dicho script se llamarán “3_c_delta_day_by_state_and_delay_type.py” y la figura resultante del mismo se denominará “3_c_delta_day_by_state_and_delay_type.png”.

# %%
#Preparando el ambiente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Leyendo los datos
datos = pd.read_csv("oilst_processed.csv")

# %%
#Se seleccionan las columnas importantes
datos = datos[['delta_days', 'customer_state', 'delay_status']]


# %%
#Se eliminan valores nulos
datos.dropna(subset=['delta_days'], inplace=True)

# %%
#Se crea el gráfico 
plt.figure(figsize=(20,15))
sns.boxplot(data=datos, x='customer_state', y='delta_days', hue='delay_status')

plt.title("Distribución por Estado y Delta days", fontsize=20)
plt.xlabel("Estado", fontsize=18)
plt.ylabel("Delta Days", fontsize=18)
plt.tight_layout()
plt.savefig("3_c_delta_day_by_state_and_delay_type.png")
plt.show()