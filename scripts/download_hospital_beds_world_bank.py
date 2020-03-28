import requests
import os
import os.path as op
import io
from zipfile import ZipFile
import logging
import scripts.config as config

logger = logging.getLogger(__name__)


def main():
    url = 'http://api.worldbank.org/v2/country/all/indicator/SH.MED.BEDS.ZS'
    params = {
        'downloadformat': 'csv',
        'mrnev': 1,    # most recent non-empty values
        'footnote': 'n'
    }
    FOLDER = op.join(config.WORLD_BANK_RAW_DATA_DIR, 'hospital_beds')
    os.makedirs(FOLDER, exist_ok=True)

    logger.info(f'Downloading data: {op.basename(url)} ...')
    resp = requests.get(url, params=params)
    zip = ZipFile(io.BytesIO(resp.content))
    zip.extractall(FOLDER)


if __name__ == '__main__':
    main()
