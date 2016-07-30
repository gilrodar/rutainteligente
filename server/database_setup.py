


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True)
    longitude = Column(Double, nullable=False)
    latitude = Column(Double, nullable=False)
    next_station = Column(Double, nullable=False)
    prev_station = Column(Double, nullable=False)
    time_to_next_station = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'capacity'                 : self.capacity,
           'timetonextstation'        : self.time_to_next_station,
           'prevstation'              : self.prev_station,
           'nextstation'              : self.next_station,
           'latitude'                 : self.latitude,
           'longitude'                : self.longitude,
           'id'                       : self.id,
       }


class Station(Base):
    __tablename__ = 'station'

    id = Column(Integer, primary_key=True)
    longitude = Column(Double, nullable=False)
    latitude = Column(Double,  nullable=False)
    name = Column(String(50), nullable=False)
    url_img  = Column(String(150), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'urlimg'         : self.url_img,
           'name'           : self.name,
           'latitude'       : self.latitude,
           'longitude'      : self.longitude,
           'id'             : self.id,
       }



engine = create_engine('sqlite:///stationsandbuses.db')


Base.metadata.create_all(engine)
