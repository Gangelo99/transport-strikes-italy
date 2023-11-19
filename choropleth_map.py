import json
import pandas as pd
import plotly.express as px

with open('data/limits_IT_regions.geojson', encoding='utf-8') as response:
    polygons = json.load(response)

df = pd.read_csv('data/strikes_number_by_region.csv', index_col=0, dtype={"NumeroScioperi": int})

fig = px.choropleth_mapbox(
    df,
    geojson=polygons,
    locations='nome_regione',
    featureidkey='properties.reg_name',
    center=dict(lat=41.871941, lon=12.567380),
    color="NumeroScioperi",
    color_continuous_scale="Jet",
    mapbox_style="white-bg",
    zoom=4.9,
    range_color=(0, 600)
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()