from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package that outputs elevation and geometry'
LONG_DESCRIPTION = 'Python package that inputs the bounds and region and outputs the elevation and geometry of that region'

#Setting up
setup(name = 'geosome',
     version = VERSION,
     author = 'Kate Njoki',
     author_email = 'katenjoki98@gmail.com',
     description = DESCRIPTION,
     long_description = LONG_DESCRIPTION,
     packages = find_packages(),
     install_requires = ['json','pdal'],
     keywords = ['python','geospatial package'],
     classifiers = [
     "Development Status :: 3-Alpha",
     "Intended Audience :: Geospatial",
     "Programming Language :: Python :: 3",
     "Operating System :: Microsoft :: Windows"]
     )