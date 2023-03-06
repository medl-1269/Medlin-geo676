# Lauren Medlin     Spring 2023     GEOG 676 Lab 8 ePortfolio

## Introduction
Coastal dunes are essential to help protect development from extreme weather events, high winds, storm surges, and sea level rise. These coastal environments are constantly shifting and moving due to rain, wind, and tides. Extreme weather events such as hurricanes cause rapid reduction of coastal sand dunes and leave development vulnerable to damage and beach erosion. Beach erosion is costly, and the absence of sand dunes leaves coastal communities more susceptible to damage from extreme weather events, which can cost millions of dollars. Understanding the impacts hurricanes have on coastal environments will aid in the protection of sand dunes and coastal communities from hurricane events.

## Project Problem
This Project will try to solve the problem of identifying the sand volume loss on the Texas Gulf Coast after Hurricane Harvey. This project will primarily focus on creating a tool simultaneously run surface volume tool and cutfill tool to evaluate the sand volume loss in Galveston Island and San Jose Island. The goal of this project is to utilize tools in ArcGIS Pro to help identify the sand volume loss before and after Hurricane Harvey as well as identify the areas of net gain or loss. The tools that will be utilize include 1) Conversion of Laz to DEM, 2) ModelBuilder, 3) Surface Volume, and 4) Cutfill.

## Tools Utilized
This project will allow users to utilize tools such as Visual Studio Code and ArcGIS Pro to design, build, and modify the tool fitting their needs. 

## Data Sources
The data used to in this project would include digital elevation lidar data, acquired from the National Ocean and Atmospheric Administration Digital Coast Data Access Viewer [website](https://www.coast.noaa.gov/dataviewer). The lidar DEM data can be downloaded from the data viewer for various location on the coast and at the range to fit the user's needs. This project will use ground data extracted by the lidar data to assess the surface volume within the study area. In order to calculate the sand volume loss before and after Hurricane Harvey lidar data collected in 2016 (before Harvey) and in 2018 (After Harvey) must be used. However, the San Jose elevation data was a .laz files. In order to use the necessary tools, conversion from .laz to DEM must be completed prior. 

## Methods
The San Jose Island elevation data is available in .laz files in order for the data to be used in ArcGIS pro, the files must be converted to raster format. Using **laz2las** located in the las toolbox (downloaded from online)[website](https://rapidlasso.com/lastools/) will convert .laz files to .las files.

After Converting the .laz files to .las, a geodatabase to store the converted data and las tools needs to be created. The following steps outlined in [Lab4](https://github.com/medl-1269/Medlin-geo676/tree/main/lab4) the user can create a geodatabase to fit their needs.  

 After conversion, associate the .las file in the catalog and define the xy coordinate system and vertical datum. Using the **LAS dataset to TIN** the las datasets will be converted to a TIN file (after the conversion users should open up the properties to filter out the ground results). Lastly, using **Model Builder** convert the TIN to raster (to create the DEM files). Using the iterator within Module Builder allows the conversion of multiple TIN files to be done simultaneously. 

The **Extract by Mask** tool can be used to clip the raster data by a feature class or shapfile (a shapefile of the users choice can be used or one can be created using the editor tool)[website](https://pro.arcgis.com/en/pro-app/latest/help/editing/a-quick-tour-of-editing.htm).

In order to create a tool, the user can create a geodatabase to hold the users data. The user can create a geodatabase by following the steps outlined in [Lab 4](https://github.com/medl-1269/Medlin-geo676/blob/03374e6b86c87dc0ee2fbcbc8a91aaa8d1b85725/lab4). The raster data the user obtains from the lidar data can be compiled into one csv fule with the XY coordinates along with using the **arcpy.MakeXYEventLayer_management** and **arcpy.FeatureClassToGeodatabase_conversion** tools. To copy the spatial reference data of the feature class to the geodatabase the following tools will be utilize: **arcpy.Copy_management**, **arcpy.Describe(layer).spatialReference**, and **arcpy.Project_management**. However, To create a raster geodatabase the **arcpy.management.CreateRasterDataset** tool will need to be used instead since the user will be using raster data for this analysis. 

Finally the tool can be created by using the methods outlined in [Lab 5](https://github.com/medl-1269/Medlin-geo676/blob/03374e6b86c87dc0ee2fbcbc8a91aaa8d1b85725/lab5) and [Lab 6](https://github.com/medl-1269/Medlin-geo676/blob/03374e6b86c87dc0ee2fbcbc8a91aaa8d1b85725/lab6). This tool will have parameters that use the information from the **Surface Volume** tool with inputs of the 2016 raster and the 2018 raster data to get the surface volume for each year. This will produce a table with the total surface volume of the users specified study area. Additionally, using **CutFill** tool with the same 2016 and 2018 raster data will give a map containing the net gain, net loss, and unchange surface volume in the users study area [website](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/cut-fill.htm).

## Outputs
**Surface Volume**
This tool will produce a table with the total surface volume for the users specified study area for the input raster's year. To get the total san volume loss, the user will need to take the difference between the two years (aka - use subtraction). This method can be done through code if the user wishes by following the methods outlined in Lab 2.

**CutFill**
This will give a map containing the net gain, net loss, and unchanged surface volume areas in the users study area. 

This tool will also give you an attribute table containing positive values that represent regions in the study area before the raster surface had been cut. Then negative values indicating regions of the study area had been filled. 

## References
ESRI. (n.d.). Cut fill (3D analyst). Cut Fill (3D Analyst)-ArcGIS Pro | Documentation. Retrieved from https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/cut-fill.htm 

Sloss, C. R., Shepherd, M., &amp; Hesp, P. (2012). Coastal Dunes: Geomorphology. Nature news. Retrieved December 8, 2021, from https://www.nature.com/scitable/knowledge/library/coastal-dunes-geomorphology-25822000/.

US Department of Commerce, N. O. A. A. (2021, September 30). Tropical Weather. USA.gov. Retrieved December 9, 2021, from https://www.weather.gov/lch/2017harvey