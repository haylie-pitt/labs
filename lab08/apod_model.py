# apod_model.py
import requests
from datetime import date

API_KEY = "gQPyttUpTyNH1hrThDjHxeTN4qLEBrwcMUAMiJPM"
BASE_URL = "https://api.nasa.gov/planetary/apod"

def get_apod_data(apod_date=None):
    params = {"api_key": API_KEY}
    if apod_date:
        params["date"] = apod_date
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

def is_valid_date(input_date):
    earliest_date = date(1995, 6, 16)
    current_date = date.today()
    return earliest_date <= input_date <= current_date
