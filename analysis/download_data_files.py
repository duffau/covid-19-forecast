import requests
import os
import datetime

DATA_FOLDER = 'data'


def timestamp_filename(filename):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M")
    basename, extension = os.path.splitext(filename)
    return f"{basename}_{timestamp}{extension}"


total_case_url = "https://cowid.netlify.com/data/all_data.csv"

response = requests.get(total_case_url)
filename = os.path.basename(response.url)
filename = timestamp_filename(filename)
filepath = os.path.join(DATA_FOLDER, filename)
os.makedirs(filepath)
with open(filepath, 'wb') as file:
    file.write(response.content)
    print(f"Downloaded to file: '{filename}'")
