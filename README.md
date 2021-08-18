<h1> AgriTech USGS-LIDAR Challenge </h2>
AgriTech, is very interested in how water flows through a maize farm field. This knowledge will help them improve their research on new agricultural products being tested on farms.

<h2> Business Objective </h2>
AgriTech would like to be able to better understand which parts of the farm are likely to produce more or less maize.

**Why?**
So that if they try a new fertilizer on part of this farm, they have more confidence that any differences in the maize harvest are due mostly to the new fertilizer changes, and not just random effects due to other environmental factors.  

* Water is very important for crop growth and health, hence AfriTech believe that they can better predict maize harvest if they understand how water flows through a field, and which parts are likely to be flooded or too dry. 
* One important ingredient to understanding water flow in a field is by measuring the elevation of the field at many points.

<h2> Overiew of data source and formats </h2>

* The USGS recently released high resolution elevation data as a lidar point cloud called **USGS 3DEP** in a [public dataset on Amazon.](https://registry.opendata.aws/usgs-lidar/) This dataset is essential to build models of water flow and predict plant health and maize harvest. 
* The 3DEP point cloud data was compressed using the LASzip compression encoding in the us-west-2 region. The data was then organised as Entwine Point Tile (EPT) resources

<h2> Python packages to build on </h2>

<hh3> PDAL </h3>
* Point Data Abstraction Library (PDAL) is open source software for translating, extracting, filtering, and exploiting geospatial point cloud data.
* PDAL will be used to build a pipeline over specific bounds and region which will be used to load and fetch 
