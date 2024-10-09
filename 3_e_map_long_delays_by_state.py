# %% [markdown]
# Desarrolla un programa ("3_e_map_long_delays_by_state.py") que construya un mapa interactivo que indique con una escala de colores a la cantidad de casos de órdenes con retrasos prolongados que ocurrieron en cada estado. La imagen interactiva generada deberá tener el nombre “3_e_map_long_delays_by_state.html”.

# %%
#Preparando el ambiente
import pandas as pd
import plotly.express as px

# %%
#Leyendo los datos
datos = pd.read_csv("oilst_processed.csv")

# %%
#Filtrando los datos
datos = datos.query("delay_status == 'long_delay'")
datos = datos.query("order_status == 'delivered'")

# %%
datos = datos.groupby('customer_state').size().reset_index(name="conteo")

# %%
geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'

# %%
fig = px.choropleth(datos,
                    locations='customer_state',
                    geojson=geojson_url,  
                    featureidkey="properties.sigla",
                    locationmode='geojson-id',
                    color='conteo',
                    hover_name='customer_state',
                    title='Pedidos con retraso por Estado'
)

fig.show()
fig.write_html("3_e_map_long_delays_by_state.html")
# %%
datos


