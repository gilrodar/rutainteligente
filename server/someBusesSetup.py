from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Station, Bus
#Connect to Database and create database session
engine = create_engine('sqlite:///stationsandbuses.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

latitudes = [19.4929466,19.4783194,19.4632962,19.4474636,19.4559315,19.4673904,19.4658558,19.4654416]
longitudes = [-99.1203114,-99.13127,-99.1438015,-99.153182,-99.1504059,-99.1398673,-99.1415141,-99.1413561]
siguientes = [2,4,6,8,8,5,5,5]
previas = [1,3,5,9,9,6,6,6]
rooms = [43,65,40,65,20,60,38,44]
etas = [228, 226, 232, 428, 29, 14, 323, 38]

for i in range( 0, 8 ):
	bus=Bus(longitude = longitudes[i], latitude = latitudes[i], next_station = siguientes[i], prev_station  = previas[i], time_to_next_station = etas[i], room = rooms[i])
	session.add(bus)
        session.commit()

print "Loaded 8 new buses to the database"

