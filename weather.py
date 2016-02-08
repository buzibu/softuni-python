import requests
import json
import datetime
import pytz
sofia_zone = pytz.timezone('Europe/Sofia')

place = input("Въведете град: ")

response = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q': place,'APPID':'965acdac1ae64cf06761bb563ad34d96','units':'metric'})
#print(response.text)
json_data = json.loads(response.text)
weather_time = datetime.datetime.fromtimestamp((int(json_data['dt']))).strftime('%Y-%m-%d %H:%M:%S')
#local_time = sofia_zone.localize(datetime.datetime.fromtimestamp(int(json_data['dt']))).strftime('%Y-%m-%d %H:%M:%S')
print("Информация към: {} ".format(weather_time))
#print("Информация към: {} Local Time".format(local_time))
print("Температура: {} C".format(json_data['main']['temp']))
print("Налягане: {} hPa".format(json_data['main']['pressure']))
print("Влажност: {} %".format(json_data['main']['humidity']))
print("Вятър: {} meter/sec".format(json_data['wind']['speed']))


