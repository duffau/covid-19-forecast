"""
Downloading historical data from Network Systems Science and Advanced Computing (NSSAC)
of the University of Virginia, dashboard API.
The dasboard can be found here: http://nssac.bii.virginia.edu/covid-19/dashboard/.
The CSV files contain on Confirmed cases, Deaths and Recovered cases from over 100
countries (at the time of writing).
"""
from datetime import datetime, timedelta
import time
import requests
import get_data.utils as utils
from get_data.url_cache import URLCache

base_url = "http://nssac.bii.virginia.edu/covid-19/dashboard/data/nssac-ncov-sd-{date}.csv"

DATA_FOLDER = '../data/raw/historical'
URL_CACHE_FILE = '.url_cache'
DATE_FORMAT = "%m-%d-%Y"
SLEEP_SEC = 3
start_date = datetime.strptime("01-23-2020", DATE_FORMAT)
end_date = datetime.now()
with open(URL_CACHE_FILE, 'r') as cache_file:
    try:
        url_cache = URLCache(cache_file)
    except EOFError:
        url_cache = URLCache()

# Downloading summary data
csv_url = base_url.format(date="summary")
response = requests.get(csv_url)
response.raise_for_status()
utils.save(response, DATA_FOLDER)
url_cache.add(csv_url)


# Downloading historical CSV's
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


for date in daterange(start_date, end_date + timedelta(1)):
    date_string = date.strftime(DATE_FORMAT)
    csv_url = base_url.format(date=date_string)
    if csv_url in url_cache:
        continue
    print(f"Downaloading data from {csv_url} ...")
    try:
        response = requests.get(csv_url)
        response.raise_for_status()
        utils.save(response, DATA_FOLDER)
        url_cache.add(csv_url)
    except requests.HTTPError as e:
        print(f"Failed downloading {csv_url}. Exception: {e}")
        print(f"Sleeping {SLEEP_SEC} seconds ...")
        time.sleep(SLEEP_SEC)

with open(URL_CACHE_FILE, 'w') as cache_file:
    url_cache.save(cache_file)
