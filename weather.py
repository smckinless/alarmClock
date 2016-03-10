import urllib2
import json
import os

def say_weather():
	key = 'f1b1b60b5ac7f727'

	zip = '07605'

	url = 'http://api.wunderground.com/api/' + key + '/geolookup/forecast/q/' + zip + '.json'

	data = urllib2.urlopen(url)

	json_data = data.read()

	parsed_data = json.loads(json_data)

	forecasts = parsed_data['forecast']['txt_forecast']['forecastday']

	for forecast in forecasts:
		if forecast['period'] == 1:
			os.system("say -v"+'Agnes'+' Today will be '+forecast['fcttext'])
				
