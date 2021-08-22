import matplotlib.pyplot as plt
import numpy as np
import gdal 

def geo_plot_terrain(tif_path:str) ->None:
    filename = tif_path
    gdal_data = gdal.Open(filename)
    gdal_band = gdal_data.GetRasterBand(1)
    nodataval = gdal_band.GetNoDataValue()

    # convert to a numpy array
    data_array = gdal_data.ReadAsArray().astype(np.float)
    data_array

    # replace missing values if necessary
    if np.any(data_array == nodataval):
        data_array[data_array == nodataval] = np.nan
    #Plot elevations with Matplotlib's 'contourf'
    fig = plt.figure(figsize = (12, 8))
    ax = fig.add_subplot(111)
    plt.contourf(data_array, cmap = "gist_rainbow_r'", 
                levels = list(range(0, 500, 100)))
    plt.title("Elevation Terrain Visualisation")
    cbar = plt.colorbar()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()