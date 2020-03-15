import preproc.utils as utils


def run(csv_file, world_pop_csv, output_folder):
    df = utils.read_data(csv_file)
    df_world_pop = utils.read_data(world_pop_csv)
    df = utils.add_constant_variables(
        df,
        names=['total_population'],
        values=[utils.get_population_size(df_world_pop, "World")]
    )
    df = utils.rename_variables(df)
    df = utils.preprocess(df)
    utils.save(df, csv_file, output_folder)


if __name__ == '__main__':
    CSV_WORLD_POP = '../data/raw/world_population.csv'
    CSV_FILE = '../data/raw/historical/nssac-ncov-sd-summary.csv'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/historical'
    run(CSV_FILE, CSV_WORLD_POP, PRE_PROCESSED_DATA_FOLDER)
