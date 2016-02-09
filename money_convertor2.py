import requests
import json
valuta = input("Въведете валута: ")
sumata = input("Въведете сума: ")
da_konvertira = input("Въведете валута, към която да се конвертира: ")

response = requests.get('http://api.fixer.io/latest', params={'symbols': da_konvertira.upper(),'base': valuta.upper()})

json_data = json.loads(response.text)
print("Равностойност в {}: {}".format(da_konvertira.upper(),float(sumata)*float(json_data['rates'][da_konvertira.upper()])))

