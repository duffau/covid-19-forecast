import requests
import os
import os.path as op

confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"

FOLDER = '../data/raw/cssegi_sand_data'
os.makedirs(FOLDER, exist_ok=True)

for url in [confirmed_url, deaths_url, recovered_url]:
    resp = requests.get(url)
    filename = op.basename(url)
    csv_file_path = op.join(FOLDER, filename)
    with open(csv_file_path, 'wb') as csv_file:
        csv_file.write(resp.content)
