import requests
import json

r = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure")
                 
data = r.json()

with open("data/json/data.json", "w") as file:
    json.dump(data, file) 
