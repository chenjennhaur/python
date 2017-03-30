import requests
import json
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Singapore+238359&key='+api)
data = json.loads(r.text)
