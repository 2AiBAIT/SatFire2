import shapefile
from pyproj import Proj, transform
from haversine import haversine
from epsg_ident import EpsgIdent

path = "AA2017\AA2017.shp"

sf = shapefile.Reader(path)

print(len(sf))

ident = EpsgIdent()
prj_file = path.replace('.shp', '.prj')
ident.read_prj_from_file(prj_file)
# epsg = ident.get_epsg()
# inProj="EPSG:" + str(epsg)
inProj="EPSG:3763"
outProj = Proj(init='epsg:4326')

for shape in sf.iterShapeRecords():
    xmin = shape.shape.bbox[0]
    xmax = shape.shape.bbox[2]
    ymin = shape.shape.bbox[1]
    ymax = shape.shape.bbox[3]

    x_minpoint = transform(inProj, outProj, xmin, ymin)
    x_maxpoint = transform(inProj, outProj, xmax, ymin)
    y_minpoint = transform(inProj, outProj, xmin, ymin)
    y_maxpoint = transform(inProj, outProj, xmin, ymax)

    x_dist = haversine(x_minpoint, x_maxpoint)
    y_dist = haversine(y_minpoint, y_maxpoint)
