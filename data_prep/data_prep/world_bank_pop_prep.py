import pandas as pd
import os
import os.path as op
import scripts.config as config


def run(csv_file: str, output_folder: str):
    df = pd.read_csv(csv_file, skiprows=4, usecols=range(6))
    os.makedirs(output_folder, exist_ok=True)
    df.to_pickle(op.join(output_folder, config.POP_FILENAME_PICKLE))
    df.to_csv(op.join(output_folder, config.POP_FILENAME_CSV))

