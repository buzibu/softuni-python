import requests
import json
valuta = input("Въведете валута: ")
sumata = input("Въведете сума: ")

response = requests.get('http://api.fixer.io/latest', params={'symbols': 'BGN','base': valuta.upper()})

json_data = json.loads(response.text)
print("Равностойност в BGN: {}".format(float(sumata)*float(json_data['rates']['BGN'])))