import requests
import os
import os.path as op
import io
from zipfile import ZipFile
import logging

logger = logging.getLogger(__name__)


def main():
    url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL'
    params = {
        'downloadformat': 'csv',
        'mrnev': 1,    # most recent non-empty values
        'footnote': 'n'
    }
    FOLDER = '../data/raw/world_bank/population'
    os.makedirs(FOLDER, exist_ok=True)

    logger.info(f'Downloading data: {op.basename(url)} ...')
    resp = requests.get(url, params=params)
    zip = ZipFile(io.BytesIO(resp.content))
    zip.extractall(FOLDER)


if __name__ == '__main__':
    main()
