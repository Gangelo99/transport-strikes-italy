import json
import pandas as pd
import plotly.express as px

with open('data/limits_IT_regions.geojson', encoding='utf-8') as response:
    polygons = json.load(response)

df = pd.read_csv('data/strikes_number_by_region.csv', index_col=0, dtype={"NumeroScioperi": int})
# df['classificazione'] = df['classificazione'].astype(str)

fig = px.choropleth_mapbox(
    df,
    geojson=polygons,
    locations='nome_regione',
    featureidkey='properties.reg_name',
    center=dict(lat=41.871941, lon=12.567380),
    color="NumeroScioperi",
    color_continuous_scale="Jet",
    # color_discrete_sequence=4,
    # color_discrete_map={'4': 'Green',
    #                     '3': 'Yellow',
    #                     '2': 'Orange',
    #                     '1': 'red'},
    mapbox_style="carto-positron",
    zoom=6,
    range_color=(0, 600),
    labels={"Classificazione sismica sicilia"},
)


fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()