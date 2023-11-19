
# Transport Strikes in Italy


In this data analysis and visualization project, using the DataSet made available by the Ministry of Infrastructure and Transport (https://dati.mit.gov.it/catalog/dataset), 4 graphs will be created on the problem of worker strikes transport in Italy, in particular:
- A histogram on the number of transport strikes from 2014 to 2020
- A bar chart and pie chart on the number of sectors where strikes occurred
- Visualization of a choropleth map on the number of strikes in Italy by region

### Requirements
Install the python packages present in the `requirements.txt` file

    pip3 install -r requirements.txt

## Number of transport strikes 2014-2020
The `histogram.py` file creates a histogram where the X axis is the year
while the Y axis is the number of transport strikes that occurred in that year.  This python script also use the `strikes_number_per_year.py` present in the module directory.

## Transport sectors where strikes occurred
The `bar_chart.py` and `pie_chart.py` files creates the two graphs about the numbers of strikes occured in	various sectors of transport. This python script also use the `strikes_number_per_sectors.py` present in the module directory.

## Strikes in Italy by region
The `choropleth_map.py` file create an choropleth map about of the number of strikes occured in every region of Italy. This python script also use the `strikes_number_by_region.py` present in the module directory.
