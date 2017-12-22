#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:46:35 2017

@author: serenewizard
"""

import os
import glob
import pandas as pd
import geopandas as gpd
import psycopg2

infname = glob.glob('vector/*.shp')[0]
gdf = gpd.read_file(infname)


connection = psycopg2.connect(database="evenstar", 
                              user="gandalf", 
                              password="dejavu", 
                              host="localhost")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS mytable")
cursor.execute("""
               CREATE TABLE mytable 
               (id SERIAL PRIMARY KEY, 
               COUNTY_NAM VARCHAR NOT NULL, 
               CO_FIPS BIGINT NOT NULL, 
               geometry GEOMETRY)""")
connection.commit()

for i in range(gdf.shape[0]):
    a = gdf.loc[i,:]
    b = a['COUNTY_NAM']
    c = a['CO_FIPS']
    d = a['geometry'].wkt
    cursor.execute("""
                   INSERT INTO mytable (COUNTY_NAM, CO_FIPS, geometry)
                   VALUES ('{}', {}, ST_GeomFromText('{}'))
                   """.format(b, c, d))
connection.commit()
cursor.execute("select UpdateGeometrySRID('mytable', 'geometry', 4269);")
connection.commit()
connection.close()
    


