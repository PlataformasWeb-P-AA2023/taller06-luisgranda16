from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import country

from genera_base import engine

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
cuarta = session.query(country.npais,country.capital).filter(country.continent=='EU').order_by(country.capital).all()
print(cuarta)