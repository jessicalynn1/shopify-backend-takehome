import os
import json
import requests
from pprint import pprint

import model
import server



CITIES = ["Denver", "San Jose", "Philadelphia", "Atlanta", "Chicago"]

for city in CITIES:
    c = model.Warehouse(name=city)
    model.db.session.add(c)
    model.db.session.commit()


#This is the weather API that I'm trying to connect to, needs to be included in description of inventory
# res = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={93b423527d6806d147c30e1558064431}')
# response = res.json()



