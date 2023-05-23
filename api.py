

import requests
from pprint import pprint
def weather(city):
    token="7311aa89429bc363d47d76b65ae85633"
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?&q={city}&appid={token}")
    info=res.json()
    return info

pprint(weather("Gulistan"))





