from qgis.core import *

# supply path to qgis install location
QgsApplication.sexPrefixPath("/Users/ColeThorpen/Desktop", True)

# create a reference to the QgsApplication
# setting the second argument to False disables the GUI
qgs = QgsApplication([], False)

#load providers
qgs.initQgis()

# write coder here to load layers, processing, algs, etc.


# remove provider and layer registeries from memory
qgs.exitQgis()