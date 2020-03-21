from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  text
from flask_migrate import Migrate
import rasterio as ras

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

from project.models import Elevation
# , Precipitation, Soil_Texture, Topo_Slope

migrate = Migrate(app, db)
@app.route("/")
def hello_world():
    return jsonify(hello="world")
    

@app.route("/list")
def list():
    sql = text("select filename from rasters.elevation") 
    result = db.engine.execute(sql).fetchall()
    return str(result)

@app.route('/add_rast')
def add():
    from osgeo import gdal, osr
    import psycopg2
    import subprocess
    fileName='Example_Tiffs/ex.tiff' #tiff_file_name and location
    raster = gdal.Open(fileName)
    proj = osr.SpatialReference(wkt=raster.GetProjection())
    projection=str(proj.GetAttrValue('AUTHORITY',1))
    gt =raster.GetGeoTransform()
    pixelSizeX =str(round(gt[1]))
    pixelSizeY =str(round(-gt[5]))
    # -t  +pixelSizeX+'x'+pixelSizeY
    cmds = "raster2pgsql -a -s 4326 " + fileName + " -F rasters.elevation " + \
           "| PGPASSWORD=test psql -d test -U test -h db -p 5432"
    print(cmds)
    code = subprocess.call(cmds, shell=True)
    if(code == 0): return str("Wiw")
    return "Something went wrong"
