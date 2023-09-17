# hophacks2023
**This repository contains the source code for the Influenza Predictions WebApp engineered dataset web application code.**<br/><br/>

The Python code int he main branch is used to output a shapefile (.shp) file containing the resulting predictions of influenza infections for 180 countries from 2023 to 2028. The primary machine learning model used was the XGBoost regressor from the XGBoost API. Due to the robust data manipulation of the parent dataset, there was no hyperparameter tuning as the resulting R-Squared and RMSE values are considered ideal. Once when the production ready prediction shapefile is created, a supplementary Python script (mz_hophacks2023_upload_2_agol.py) was created to automate the process to upload and publish content in ArcGIS Online (AGOL).

The source dataset used to produce the predictions is from the World Heath Organization's (WHO) FluNet Database containing the records of several virus infections for severl countries from 1997 to 2023, found [here]("https://www.who.int/tools/flunet").

The primary feature layer enabling this web application can be found [here]("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/MS_HopHacks_2023_Influenza_Global_Predictions_2023_to_2028/FeatureServer").

The file geodatabase (gdb) that contains the global country geopolitical boundaries used to generate the final shapefile is from Esri's ArcGIS Hub, found [here]("https://hub.arcgis.com/datasets/esri::world-countries-generalized/explore").

The web application rendering the results can be found in [GitHub]("https://github.com/mzlatic1/hophacks2023") for the source code and can also be viewed from the JSbin hosted link [here]("https://jsbin.com/diyihurola").

Author Info:<br/>
Name: Marko Zlatic<br/>
Date: September 17, 2023<br/>
Purpose: HopHacks 2023<br/>
Student Status: Graduate<br/>
Program: MSc. Geographic Information Systems<br/>
University: Johns Hopkins University<br/><br/>

The Infuenza Prediction WebApp is a web application that was primarily built with the ArcGIS Maps SDK for JavaScript and jQuery, for the purpose of illustrating results of an XGBoost Regressor model predicting the number of infuenza infections for 180 countries from 2023 to 2028.
<br/><br/>
For more information regarding the machine learning model that was used, please click on the GitHub link on the bottom right of the webapp (a Jupyter notebook was used to illustrate the process of developing and training the XGBoost regressor model, the code being written in Python).
<br/><br/>
To utilize the web application is as follows:
Time Slider (very bottom of webapp): This widget effectively queries the hosted dataset based on the year of predicted influenza infections for each country. Due to the sample size comprising of 180 countries, there might be some years in which some countries do not render (ie visualize); this means that there is no data present for the given year.
<br/><br/>
Select Symbology by Type Widget (far middle right): This widget sends a request to the ArcGIS Online (AGOL) REST endpoint to adjust the symbology currently being visualized for the user.<br/>
The Random Color Default option is a simple random generated color symbology for each of the available countries that was able to properly query (every time the webapp reloads or this option is reselected, a new generated array of colors are created to symbolize the web map.
The Gradient Flu Count option is a gradient-based symbology renderer that darkens the map (with dark red being the max extreme and white being the minimum extreme) based on the number of infuenza infections there are per country (this symbology isnt influenced by the size of the country, rather the total count of infections (in comparison to other countries globally)<br/>
The Standard Deviation Breaks option is a class-break-style symbology that classifies an array of values based on pre-defined values. The pre-defined values selected was the standard deviation of the total dataset. This means, if a country has a darker red color, then the number of infections is far greater when compared to the observed mean; the opposite is said with countries that are classified with a dark green color (indicating the number of infections are far less when compared to the observed mean)<br/>
The Infection Density Analysis option is a spatially-defined dot density symbology that can be used to help predict where infections are the highest (within a countries boarders). Since the analysis was done using strictly tabular information (ie lacking geospatial components), there is no way to properly predict where on the map the infections are occurring (and at what rate). As a result, a dot-density methodology randomly generates a fixed number of points based on the size of the countries respected land area and number of infections; estimating potential locations for infection 'hot spots'.
<br/><br/>
Basemap Gallery Widget (far bottom left): This widget can be used to change the current basemap (default is the light-gray canvas) displayed on the web map.
<br/><br/>
Legend Widget (far top right): This widget assists with displaying the render options that are returned from the AGOL REST endpoint.
<br/><br/>
Query Results (far top left): This widget is a read-only dynamic text widget that renders the resulting query that is returned from the AGOL REST endpoint.
<br/><br/>
Sources (far bottom right): Web links to several sources (source code, parent dataset used to generate predicted results, and the final-engineered product that powers the Influenza Prediction WebApp).

