from sqlalchemy import create_engine

engine = create_engine('sqlite:///country.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class country(Base):
    __tablename__="country_codes"

    id = Column(Integer, primary_key=True)
    npais = Column(String)
    capital = Column(String)
    continent = Column(String)
    dial = Column(String)
    geoname = Column(Integer)
    itu = Column(String)
    languages = Column(String)
    independiente = Column(String)

Base.metadata.create_all(engine)