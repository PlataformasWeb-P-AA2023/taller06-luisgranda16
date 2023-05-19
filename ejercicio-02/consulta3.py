from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import country

from genera_base import engine

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los lenguajes de cada país.
tercero = session.query(country.npais,country.languages).all()
print(tercero)