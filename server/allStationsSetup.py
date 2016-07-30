
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Station, Bus
#Connect to Database and create database session
engine = create_engine('sqlite:///stationsandbuses.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



names = ["Indios Verdes","Deportivo 18 De Marzo","Euzkaro","Potrero","La Raza","Circuito","San Simon","Manuel Gonzalez","Buenavista"]
latitudes = [19.4966275,19.48636,19.48247,19.47661,19.46883,19.46244,19.45966,19.45688,19.44695]
longitudes = [-99.1197621,-99.12432,-99.12774,-99.13247,-99.1388,-99.14403,-99.14651,-99.14915,-99.15302]

for i in range(0,9):
	station = Station(longitude = longitudes[i],
                latitude = latitudes[i],
                name = names[i],
                url_img  = "")
	session.add(station)
	session.commit()

print "Finish loading defalut stations"



