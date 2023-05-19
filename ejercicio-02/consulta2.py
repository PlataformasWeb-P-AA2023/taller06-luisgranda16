from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import country

from genera_base import engine

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países de Asía, ordenados por el atributo Dial.
segundo = session.query(country).filter(country.continent=="AS").order_by(country.dial).all()
print(segundo) 