from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import country

from genera_base import engine

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países del continente americano
primero = session.query(country).filter(country.continent.in_(['NA','SA'])).order_by(country.npais).all()
print(primero)