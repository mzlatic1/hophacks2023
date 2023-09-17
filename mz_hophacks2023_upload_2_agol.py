# load packages
from arcgis import GIS
import os

# locate shapefile
folder = os.path.split(os.getcwd())[0]
datasets = os.path.join(folder, 'datasets')

pred_shp = os.path.join(datasets, 'mz_hophacks_2023_influenza_global_predictions.shp')

# log into the ArcGIS Python API
gis = GIS(url='usually is https://arcgis.com', username='', password='')

# brief example on how to populate metadata information
item_prop = {
    'title': 'MZ HopHacks 2023 - Influenza Global Predictions',
    'description': 'This shapefile file contains predictions of global influenza infections from 2023 - 2028'
}

# upload and publish content!
upload_pred = gis.content.add(item_prop, data=pred_shp, folder='hophacks')
upload_pred.publish()
