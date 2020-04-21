from data_prep.data_prep.cssegi_prep import run as run_cssegi_prep
from data_prep.data_prep.world_bank_pop_prep import run as run_pop_prep
from data_prep.data_prep.world_bank_hosp_beds_prep import run as run_hosp_beds_prep

import os.path as op
import os
import logging

logger = logging.getLogger(__name__)


def main():
    from glob import glob
    import scripts.config as config

    world_pop_df = op.join(config.WORLD_BANK_PREPROC_DATA_DIR, config.POP_FILENAME_PICKLE)
    world_hosp_beds_df = op.join(config.WORLD_BANK_PREPROC_DATA_DIR, config.HOSP_BEDS_FILENAME_PICKLE)
    confirmed_csv_file_path = op.join(config.CSSEGI_RAW_DATA_DIR, config.CONFIRMED_FILENAME_CSV)
    deaths_csv_file_path = op.join(config.CSSEGI_RAW_DATA_DIR, config.DEATHS_FILENAME_CSV)
    recovered_csv_file_path = op.join(config.CSSEGI_RAW_DATA_DIR, config.RECOVERED_FILENAME_CSV)

    cssegi_preproc_file_path = config.CSSEGI_PREPROC_DATA_FILE
    os.makedirs(os.path.dirname(cssegi_preproc_file_path), exist_ok=True)
    world_bank_preproc_data_dir = config.WORLD_BANK_PREPROC_DATA_DIR
    os.makedirs(world_bank_preproc_data_dir, exist_ok=True)

    csv_hosp_beds_pattern = op.join(config.WORLD_BANK_RAW_DATA_DIR, 'hospital_beds/API_SH.MED.BEDS.ZS*.csv')
    csv_pop_pattern = op.join(config.WORLD_BANK_RAW_DATA_DIR, 'population/API_SP.POP.TOTL*.csv')

    logger.info('Running data prep of World Bank population data ...')
    csv_filenames = glob(csv_pop_pattern)
    assert len(csv_filenames) == 1, f'len(csv_filenames) = {len(csv_filenames)} != 1'
    run_pop_prep(csv_filenames[0], output_folder=world_bank_preproc_data_dir)

    logger.info('Running data prep of World Bank hospital beds data ...')
    csv_filenames = glob(csv_hosp_beds_pattern)
    assert len(csv_filenames) == 1, f'len(csv_filenames) = {len(csv_filenames)} != 1'
    run_hosp_beds_prep(csv_filenames[0], output_folder=world_bank_preproc_data_dir)

    logger.info('Running data prep of CSSEGI data ...')
    run_cssegi_prep(
        csv_file_paths=[confirmed_csv_file_path, deaths_csv_file_path, recovered_csv_file_path],
        known_errors=None,
        world_pop_file=world_pop_df,
        world_hosp_beds_file=world_hosp_beds_df,
        output_file=cssegi_preproc_file_path
    )


if __name__ == '__main__':
    main()
