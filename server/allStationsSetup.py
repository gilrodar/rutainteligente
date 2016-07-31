
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
urls = [
        "http://3.bp.blogspot.com/-GUayYNNMLYM/TglkJaXmR7I/AAAAAAAABEo/EvAno18rYZg/s400/mb-indiosverdes.png",
        "http://1.bp.blogspot.com/_XXpvlSXUPdU/TQMmDQXiy_I/AAAAAAAAApA/_XeO0Q5Gs7E/s400/mb-18marzo.png",
        "http://4.bp.blogspot.com/-ci4pEm1Untc/TYl3mzppBfI/AAAAAAAAA48/8DNPNJghtIE/s400/mb-euzkaro.png",
        "http://3.bp.blogspot.com/-BpbYjDmpc0k/Tj-A8seLceI/AAAAAAAABUI/yiPHWd5N2U8/s400/mb-potrero.png",
        "http://3.bp.blogspot.com/-LGGdFFx46Cc/TWiul15ZxJI/AAAAAAAAAzg/pw2nIEd4PIQ/s400/mb-laraza.png",
        "http://1.bp.blogspot.com/_XXpvlSXUPdU/TOS-LiIsj8I/AAAAAAAAAeo/Oa0_JXrf_4w/s400/mb-circuito.png",
        "http://4.bp.blogspot.com/-ZlgbfnCe_98/T0r4PjbtgjI/AAAAAAAACX0/5lfhwVgXsmg/s400/mb-sansimon.png",
        "http://4.bp.blogspot.com/-RGCLj4rbBiI/TmrkVbzWKGI/AAAAAAAABiE/O4-1mlqhzR4/s1600/mb-manuelgonzalez.png",
        "http://lh3.ggpht.com/_XXpvlSXUPdU/TODg-7JLnRI/AAAAAAAAAbg/rdSFDi-icgU/s400/mb-buenavista.png"
        ]

for i in range(0,9):
    station = Station(longitude = float(longitudes[i]),
            latitude = float(latitudes[i]),
            name = names[i],
            url_img  = urls[i])
    session.add(station)
    session.commit()

print "Finish loading defalut stations"
