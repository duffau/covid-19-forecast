from typing import List
import os.path as op
from datetime import datetime
from dateutil import parser as dateparser
import glob
from configparser import ConfigParser
import logging
import scripts.config as config

logger = logging.getLogger(__name__)

FORECAST_PLOT_FOLDER = config.FORECAST_PLOT_FOLDER
README_FILE = config.README_FILE
INDEX_MD_FILE = config.INDEX_MD_FILE
README_FOLDER = op.dirname(README_FILE)
OUTPUT_DATE_FORMAT = "%d-%m-%Y"

BASE_TEMPLATE = '''
{_header}
{_forecast}
{_plots}

{_refs}
'''
PLOT_TOC_ENTRY_TEMPLATE = '- [{country}](#{country_link})'
PLOT_CELL_TEMPLATE = '''### {country}\n\n|![{country}]({file_path})|\n|:----------------------------------------:|\n| *Latest data point: {latest_data_point}*|'''


def make_plots_markdown(plot_paths: List[str], latest_data_point_dates: List[datetime]):
    plot_cells = []
    for plot_path, latest_data_point in zip(plot_paths, latest_data_point_dates):
        country = extract_country(plot_path)
        forecast_plot_rel_path = op.relpath(plot_path, README_FOLDER)
        plot_cell = PLOT_CELL_TEMPLATE.format(country=country,
                                              file_path=forecast_plot_rel_path,
                                              latest_data_point=latest_data_point.strftime(OUTPUT_DATE_FORMAT))
        plot_cells.append(plot_cell)
    return plot_cells


def make_plot_toc(plot_paths: List[str]):
    plot_toc_entries = []
    for plot_path in plot_paths:
        country = extract_country(plot_path)
        plot_toc_entries.append(PLOT_TOC_ENTRY_TEMPLATE.format(
            country=country,
            country_link=country.lower().replace(' ', '-')
        ))
    return plot_toc_entries


def make_full_markdown(header_tmp,
                       forecast_tmp,
                       plots_tmp,
                       refs_tmp,
                       plot_cells: List[str],
                       plots_toc: List[str],
                       update_date: datetime):
    template = BASE_TEMPLATE.format(
        _header=header_tmp,
        _forecast=forecast_tmp,
        _plots=plots_tmp,
        _refs=refs_tmp
    )

    readme_markdown = template.format(
        date=update_date.strftime(OUTPUT_DATE_FORMAT),
        plots_toc='\n'.join(plots_toc),
        plots='\n\n'.join(plot_cells)
    )
    return readme_markdown


def extract_country(plot_filepath):
    base, _ = op.splitext(op.basename(plot_filepath))
    country, _ = base.split('_')
    return country.capitalize()


def make_readme(plot_cells, plot_toc, update_date):
    with open(config.README_HEADER_TEMPLATE) as file:
        header_template = file.read()

    with open(config.README_FORECAST_TEMPLATE) as file:
        forecast_template = file.read()

    with open(config.README_PLOT_TEMPLATE) as file:
        plot_template = file.read()

    with open(config.README_REFS_TEMPLATE) as file:
        refs_template = file.read()

    return make_full_markdown(
        header_tmp=header_template,
        forecast_tmp=forecast_template,
        plots_tmp=plot_template,
        refs_tmp=refs_template,
        plots_toc=plot_toc,
        plot_cells=plot_cells,
        update_date=update_date
    )


def make_pages_index(plot_cells, plot_toc, update_date):
    with open(config.PAGES_HEADER_TEMPLATE) as file:
        header_template = file.read()

    with open(config.PAGES_FORECAST_TEMPLATE) as file:
        forecast_template = file.read()

    with open(config.PAGES_PLOT_TEMPLATE) as file:
        plot_template = file.read()

    with open(config.PAGES_REFS_TEMPLATE) as file:
        refs_template = file.read()

    return make_full_markdown(
        header_tmp=header_template,
        forecast_tmp=forecast_template,
        plots_tmp=plot_template,
        refs_tmp=refs_template,
        plots_toc=plot_toc,
        plot_cells=plot_cells,
        update_date=update_date
    )


def main():
    logger.info('Compiling README ...')
    config = ConfigParser()
    forecast_plots_paths = sorted(glob.glob(op.join(FORECAST_PLOT_FOLDER, '*.png')))
    forecast_info_paths = sorted(glob.glob(op.join(FORECAST_PLOT_FOLDER, '*.ini')))
    assert len(forecast_plots_paths) == len(forecast_info_paths), f'len(forecast_plots_paths) = {len(forecast_plots_paths)} != len(forecast_info_paths) = {len(forecast_info_paths)}'

    forecast_infos = []
    for forecast_info_path in forecast_info_paths:
        config.read(forecast_info_path)
        forecast_infos.append(config._sections['forecast-info'].copy())
    latest_data_points = [dateparser.parse(forecast_info['latest_data_point'].strip('"')) for forecast_info in forecast_infos]
    update_date = dateparser.parse(forecast_infos[0]['forecast_time'].strip('"'))
    plots_md = make_plots_markdown(forecast_plots_paths, latest_data_points)
    plots_toc = make_plot_toc(forecast_plots_paths)

    readme_markdown = make_readme(plots_md, plots_toc, update_date)
    pages_markdown = make_pages_index(plots_md, plots_toc, update_date)
    with open(README_FILE, 'w') as file:
        file.write(readme_markdown)
    with open(INDEX_MD_FILE, 'w') as file:
        file.write(pages_markdown)


if __name__ == '__main__':
    main()
