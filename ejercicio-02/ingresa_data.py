from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Contry

import json
import requests

engine = create_engine('sqlite:///country.db')

Session = sessionmaker(bind=engine)
session = Session()

resp = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos_json =  resp.json()

for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Country(npais=d['CLDR display name'], capital=d['Capital'], continent=d['Continent'], \
            dial=d['Dial'],geoname=d['Geoname ID'],itu=d['ITU'],languages=d['Languages'],independiente=d['is_independent'] )
    session.add(p)

# confirmar transacciones

session.commit()