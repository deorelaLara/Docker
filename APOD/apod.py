import requests
import json
import random
import datetime

class APOD(object):
    def __init__(self):
        self.ENDPOINT = 'https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP'

    def getPicture(self, x):
        uri = f'{self.ENDPOINT}&date={x}'
        req = requests.get(uri)
        data = req.json()

        return {
            'title' : data.get('title'),
            'url' : data.get('url'),
            'explanation': data.get('explanation'),
        }


'''
#GENERAMOS UNA FECHA ALEATORIA DADO UN RANGO DE 2 FECHAS ESTABLECIDAS
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
#print(random_date)

#Clase con funciones para hacer nuestro request
api = APOD()

#date = input('Insert date: ')
#print(json.dumps(api.getPicture(date), indent=2))
print(json.dumps(api.getPicture(random_date), indent=2))
'''