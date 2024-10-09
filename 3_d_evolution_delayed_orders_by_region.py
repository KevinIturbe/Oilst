# %% [markdown]
# Crea un programa ("3_d_evolution_delayed_orders_by_region.py") que cree una visualización interactiva de un gráfico de barras que por cada mes y años, donde la altura de cada barra cuente la cantidad de órdenes con retraso prolongado que sucedieron en dicho periodo. Además, dentro cada barra se deberá tener un desglose de la cantidad de órdenes que tuvieron retraso en cada uno de los periodos. La imagen interactiva generada deberá nombrase como "3_d_evolution_delayed_orders_by_region.html"

# %%
#Preparando el ambiente
import pandas as pd
import plotly.express as px

# %%
#Leyendo los datos
datos = pd.read_csv("oilst_processed.csv")

# %%
#Se filtran las órdenes con retraso prolongado 
datos = datos.query("delay_status == 'long_delay'")

# %%
datos['month'] = pd.to_datetime(datos['month'], format='%m').dt.month_name()

# %%

datos = datos.groupby(['year', 'month']).size().reset_index(name="Número de registros")

# %%
fig = px.bar(datos,
             x= 'year',
             y= 'Número de registros',
             color='month',
             title='Ordenes con retraso por Región'
            )

fig.update_layout(xaxis_title='Año')

fig.show()

fig.write_html("3_d_evolution_delayed_orders_by_region.html")


