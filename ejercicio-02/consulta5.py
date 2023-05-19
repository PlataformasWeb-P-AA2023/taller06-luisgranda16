from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import country

from genera_base import engine

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
quinto = session.query(country).filter(or_(country.npais.like("%uador"), country.capital.like("%ito"))).all()
print(quinto)