import requests
import json
import pandas as pd


# Access the website https://open-meteo.com/en/docs and generate historical hourly data on Minais Gerais (lat: -21.72,  long: -45.39) from Jan 1 2022 to Dec 31 2023. Generate data on `temperature`, `relative humidity`, `precipitation`, and `surface pressure`.

r = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure")
         
data = r.json() 


# Use this URL to pull your JSON data programmatically into your Python program, and save this object into the path `data/json`.  

file_path = "data/json/data.json"

with open(file_path, "w") as file:
    json.dump(data, file, indent=4) 


# Remove all the meta-data from this resultant JSON file and keep only the data that describes the time and the variables listed above. Convert this modified JSON file into a CSV file and save it to the path `data/CSV/`. 


# filtered_data = pd.DataFrame({
#     "time": df["time"].iloc[0],  
#     "temperature": df["temperature"].iloc[0],
#     "relative humidity": df["relative humidity"].iloc[0],
#     "precipitation": df["precipitation"].iloc[0],
#     "surface pressure": df["surface pressure"].iloc[0]
# })

df = pd.DataFrame(data)

columns_to_keep = ["time", "temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure"]
filtered_data = pd.DataFrame(data["hourly"])[columns_to_keep]

filtered_data.to_csv("data/csv/data.csv", index=False)

