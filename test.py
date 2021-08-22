from geosome.fetch import geo_fetch
from geosome.elevate import geo_shp, geo_elevation
from geosome.plot import geo_plot_terrain

#geo_fetch outputs the tif file and creates shp file path from bounds and region 
tif_file, shp_file = geo_fetch("([-93.756155, 41.918015], [-93.747334, 41.921429])","IA_FullState/")

#geo_shp generates the actual shp file
shp_file = geo_shp(shp_file)

#return geopandas dataframe with elevation and geometry as output
gpd_df = geo_elevation(shp_file)

#plot of elevation files
geo_plot_terrain(tif_file)