from project import db
from geoalchemy2 import Raster


class Elevation(db.Model):
    __tablename__ ='elevation'
    __table_args__ = {"schema":"rasters"}
    rid = db.Column(db.Integer, primary_key=True)
    rast = db.Column(Raster)
    filename = db.Column(db.String(200))
    
# class Precipitation(db.Model):
#     __tablename__ ='precipitation'
#     __table_args__ = {"schema":"rasters"}
#     rid = db.Column(db.Integer, primary_key=True)
#     rast = db.Column(Raster)
#     filename = db.Column(db.String(200))

# class Soil_Texture(db.Model):
#     __tablename__ ='soil_texture'
#     __table_args__ = {"schema":"rasters"}
#     rid = db.Column(db.Integer, primary_key=True)
#     rast = db.Column(Raster)
#     filename = db.Column(db.String(200))

# class Topo_Slope(db.Model):
#     __tablename__ ='topo_slope'
#     __table_args__ = {"schema":"rasters"}
#     rid = db.Column(db.Integer, primary_key=True)
#     rast = db.Column(Raster)
#     filename = db.Column(db.String(200))