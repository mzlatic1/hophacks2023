# load packages
from arcgis import GIS
import arcpy # note ArcPy is a propitiatory Python package, built by Esri, and requires an ArcGIS Pro License
import os

# locate recently updated shapefile
folder = os.path.split(os.getcwd())[0]
datasets = os.path.join(folder, 'datasets')

pred_shp = os.path.join(datasets, 'mz_hophacks_2023_influenza_global_predictions.shp')

# log into ArcGIS Online (AGOL)
gis = GIS('Pro')

# locate the REST endpoint of the production dataset using the itemid
prod_itemid = gis.content.search('fac915ebefcb40f6bd86b21df1d07dee')[0]

# load the dataset
dataset = prod_itemid.layers[0]

# delete all rows from production dataset
dataset.delete_features(where='OBJECTID >= 0')

# append new data
arcpy.Append_management(pred_shp, dataset.url, 'NO_TEST')
