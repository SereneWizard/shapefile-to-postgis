# Shapefile to PostGIS table

This repository shows how to upload a shapefile into PostGIS table using Python.
The required python libraries are:
* glob
* fiona
* shapely
* psycopg2

This code uses the library *fiona* for lazy evaluation of the shapefile features and *psycopg2* for uploading each shapefile feature as Postgres table records.
Lazy evaluation is useful in the sense that we don't have to upload the whole file in the memory in the beginning, and therefore, has its utility in working with large shapefiles.
