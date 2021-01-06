from flask import Flask, render_template
from apod import APOD
import random
import datetime

app = Flask(__name__)
api = APOD()

@app.route('/')
def index():
    
    #GENERAMOS UNA FECHA ALEATORIA ENTRE UN RANGO DE 2 FECHAS ESTABLECIDAS
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2020, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    apod = api.getPicture(random_date)
    return render_template('index.html', apod = apod)

    
if __name__=="__main__":
    app.run(host="0.0.0.0")
