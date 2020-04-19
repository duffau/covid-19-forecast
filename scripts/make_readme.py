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

README_TEMPLATE = '''
<h1 align="center">Forecasting COVID-19 cases</h1>

Attempt to forecast the number of cases of COVID-19 around the world using the simple [SIR model][sir_model_wiki].

The development of the estimation method is documented in the [CHANGELOG of the analysis section](analysis/CHANGELOG.md).

The site is hosted here: https://duffau.github.io/covid-19-forecast/.

## Forecasts
*Updated: {date}*

Forecasts are based on a variation of the simple [SIR model][sir_model_wiki] found 
in the article of [Bohner et al (2018)].

In the model an individual can be in one of three states,

- Susceptible: Part of the population not immune to the disease, 
- Infected: Is currently infected,
- Removed: Is immune after a recovery or death.

The model is governed by two parameters, the rate at which individuals contract the disease, 
and the rate at which they are removed from the infected group. 

The current model is only fitted on the number of infected using the closed form solution
from [Bohner et al (2018)]. The fitted equation is given by,

$$
\begin{{equation}}
I(t) = I_0 (1 + \kappa)^{{b/(b-c)}} \left(1 + \kappa e^{{(b-c)(t-t_0)}}\right)^{{-b/(b-c)}}e^{{(b-c)(t-t_0)}}.
\end{{equation}}
$$

where $b$ and $c$ are free parameters governing the rate of transmission and recovery, respectively, 
$I_0$ is the number of infected at time $t_0$ and $\kappa = I_0/S_0$.

Data is downloaded from *Johns Hopkins University Center for Systems Science and Engineering* 
COVID-19 [data repository][csse-data-repo], used in their [dashboard][john-hopkins-dashboard] app.

### Plots
{plots}

[sir_model_wiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model
[csse-data-repo]: https://github.com/CSSEGISandData/COVID-19
[john-hopkins-dashboard]: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
[Bohner et al (2018)]: https://arxiv.org/abs/1812.09759
[Bailey (1975)]: https://www.amazon.com/Mathematical-Theory-Infectious-Diseases-2nd/dp/0852642318 

'''

README_PLOT_TEMPLATE = '''|![{country}]({file_path})|\n|:----------------------------------------:|\n| *Latest data point: {latest_data_point}*|'''


def make_plots_markdown(plot_paths: List[str], latest_data_point_dates: List[datetime]):
    readme_plot_makdowns = []
    for plot_path, latest_data_point in zip(plot_paths, latest_data_point_dates):
        country = extract_country(plot_path)
        forecast_plot_rel_path = op.relpath(plot_path, README_FOLDER)
        plot_img_markdown = README_PLOT_TEMPLATE.format(country=country,
                                                        file_path=forecast_plot_rel_path,
                                                        latest_data_point=latest_data_point.strftime(OUTPUT_DATE_FORMAT))
        readme_plot_makdowns.append(plot_img_markdown)
    return readme_plot_makdowns


def make_readme_markdown(plots_md: List[str], update_date: datetime):
    readme_markdown = README_TEMPLATE.format(
        date=update_date.strftime(OUTPUT_DATE_FORMAT),
        plots='\n\n'.join(plots_md)
    )
    return readme_markdown


def extract_country(plot_filepath):
    base, _ = op.splitext(op.basename(plot_filepath))
    country, _ = base.split('_')
    return country.capitalize()


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
    readme_markdown = make_readme_markdown(plots_md, update_date)
    with open(README_FILE, 'w') as file:
        file.write(readme_markdown)
    with open(INDEX_MD_FILE, 'w') as file:
        file.write(readme_markdown)


if __name__ == '__main__':
    main()
