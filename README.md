<h1> AgriTech USGS-LIDAR Challenge </h2>

The goal of this challenge was to write a python modular code to fetch and visualize LIDAR high definition elevation data - [USGS 3DEP](https://www.usgs.gov/core-science-systems/ngp/3dep)
The USGS recently released high resolution elevation data as a lidar point cloud in a [public dataset on Amazon](https://registry.opendata.aws/usgs-lidar/). 

<h2> Libraries Used </h2>

* PDAL
* GDAL
* Shapely
* Geopandas

<h2>Setting up the module</h2>

1. Initialise git in a folder
  ```
  git init
  ```
2. Clone the github repo 
  ```
  git clone https://github.com/katenjoki/AgriTech_USGS.git
  ```
3. Open your Anaconda prompt and point the directory to the AgriTech_USGS folder which contains the cloned git repo e.g.
  ```
  cd C:\Users\user\Desktop\agritech\AgriTech_USGS
  ```
4. Create a conda environment, activate it and configure the channels 
  ```
  conda create --name geovenv
  conda activate geovenv
  conda config --append channels conda-forge
  ```
5. Install the packages in the requirements.txt file
  ```
  conda install --file requirements.txt
  
  ```
  
  <h3> Tutorial</h3>
  
  * To test it out, run the [geotest notebook](https://github.com/katenjoki/AgriTech_USGS/blob/master/agritech_tutorial/geotest.ipynb)
  * Fetch the data
  ```
  geo_fetch(df,"IA_FullState/")
  ```
  The geo_fetch function outputs a geopandas dataframe with elevation and geometry as columns
  
|    | elevation | geometry|
| -- | :---------:| --------:|
| 0 |	306.51519775390625 |	POINT (-10436886.930 5149216.890)|
| 1 |	306.44091796875 |	POINT (-10436885.930 5149216.890)|
| 2 |	306.41668701171875 |	POINT (-10436884.930 5149216.890)|
| 3 |	306.449859619140625 |	POINT (-10436883.930 5149216.890)|
| 4 |	306.4075927734375 |	POINT (-10436882.930 5149216.890)|

* Visualize the terrain
  ```
  geo_plot(gdf)
  ```
  The geo_plot function returns the elevation files as a 3D plot 
  
