from osgeo import gdal, ogr
pts = ogr.Open('../files/shp/IA_FullState.shp',0)
layer = pts.GetLayer()
raster = gdal.Open('../files/tif/IA_FullState.tif')

gt = raster.GetGeoTransform()
ulx = gt[0]
uly = gt[3]
res = gt[5]

xsize = raster.RasterXSize
ysize = raster.RasterYSize

lrx = ulx + xsize * res
lry = uly - ysize * res

pts = layer = None
nn = gdal.Grid('../files/tif/IA_FullState2.tif','../files/shp/IA_FullState.shp',zfield="elevation"
,algorithm="nearest",outputBounds = [ulx,uly,lrx,lry],width=xsize,height=ysize)