# Sport master planning basis from open data

![Python Logo](./python_logo.png)

## Description

A lib version of the sports master planning code.

Aimed a producing sport overviews for certain cities. Demoes of reports for [Sedan](examples\outputs\rapports_8409.docx) and the [Kremlin Bicetre](examples\outputs\rapports_94043.docx).

## Repository Ownership
* **Practice**: Sport
* **Sector**: Asset management
* **Original Author(s)**: Luc Jonveaux
* **Contact Details for Current Repository Owner(s)**: luc.jonveaux@mottmac.com

## Data

* Données équipements sportifs: https://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/ 
* Données éducation: https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/ 
* Découpage communal: https://www.data.gouv.fr/fr/datasets/*decoupage-administratif-communal-francais-issu-d-openstreetmap/ 
* Licenses sportives 2015: https://www.data.gouv.fr/fr/datasets/donnees-geocodees-issues-du-recensement-des-licences-et-clubs-aupres-des-federations-sportives-agreees-par-le-ministere-charge-des-sports/ 


## Running the Code

Relatively straightforward

```python
import gpdSport

data = gpdSport.dataSets()
DATA = data.CreateDF("data/)

data.CreateVille(8409); #produces the an analysis for SEDAN
fig = data.CreateMap(ZOOM=12) # creates a map, with a basemap zoom at 12
data.createReport(); #produces the report

```

It produces [this report](examples\outputs\rapports_8409.docx), and this map:

![](examples\outputs\8409_terrain.png)