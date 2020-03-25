import pandas as pd
import os
import os.path as op


def run(csv_file: str, output_folder: str):
    df = pd.read_csv(csv_file, skiprows=4, usecols=range(6))
    df.info()
    os.makedirs(output_folder, exist_ok=True)
    df.to_pickle(op.join(output_folder, 'hospital_beds.pickle'))
    df.to_csv(op.join(output_folder, 'hospital_beds.csv'))


def main():
    from glob import glob

    CSV_POP_PATTERN = '../data/raw/world_bank/hospital_beds/API_SH.MED.BEDS.ZS*.csv'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/world_bank'

    csv_filenames = glob(CSV_POP_PATTERN)
    assert len(csv_filenames) == 1, f'len(csv_filenames) = {len(csv_filenames)} != 1'
    run(csv_filenames[0], output_folder=PRE_PROCESSED_DATA_FOLDER)


if __name__ == '__main__':
    main()
