# %% [markdown]
# Implementa un script ("3_f_map_monetary_value_long_delays_by_state.py") que genere una visualización que permita analizar el valor monetario que representan los retrasos prolongados que ocurrieron en cada estado. La imagen interactiva resultante deberá denominarse como "3_f_map_monetary_value_long_delays_by_state.html".

# %%
#preparando el ambiente
import pandas as pd
import plotly.express as px

# %%
#Leyendo los datos
datos = pd.read_csv("oilst_processed.csv")

# %%
#Filtrando los retrasos prolongados
datos = datos.query("order_status == 'delivered' and delay_status == 'long_delay'")

# %%
datos = datos.groupby('customer_state')['total_sales'].sum().reset_index(name="Total")

# %%
geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'

# %%
fig = px.choropleth(
    datos,
    geojson=geojson_url, 
    locationmode= 'geojson-id',
    featureidkey="properties.sigla",
    locations='customer_state',
    color='Total',
    title='Valor de ventas con retraso por Estado'
)
fig.show()
fig.write_html("3_f_map_monetary_value_long_delays_by_state.html")


