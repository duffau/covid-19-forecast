import requests
import os
import os.path as op
import time
import logging

logger = logging.getLogger(__name__)


def main():
    import scripts.config as config
    confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    confirmed_filename = config.CONFIRMED_FILENAME_CSV
    deaths_filename = config.DEATHS_FILENAME_CSV
    recovered_filename = config.RECOVERED_FILENAME_CSV
    out_dir = config.CSSEGI_RAW_DATA_DIR

    os.makedirs(out_dir, exist_ok=True)

    for url, filename in [(confirmed_url, confirmed_filename),
                          (deaths_url, deaths_filename),
                          (recovered_url, recovered_filename)]:
        logger.info(f'Downloading data: {op.basename(url)} ...')
        resp = requests.get(url)
        resp.raise_for_status()
        csv_file_path = op.join(out_dir, filename)
        with open(csv_file_path, 'wb') as csv_file:
            csv_file.write(resp.content)
        time.sleep(1)


if __name__ == '__main__':
    main()
