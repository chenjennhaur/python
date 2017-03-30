import requests
import json
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Singapore+238359&key='+api)
data = json.loads(r.text)
data['results'][0]['geometry']['location']
# lat or lng
