import os.path as op
import glob
from datetime import datetime

FORECAST_PLOT_FOLDER = '../forecast_plots'
README_FILE = '../README.md'

readme_markdown_template = '''
# Forecasting COVID-19 cases

Attempt to forecast the number of cases of COVID-19 around the world using the simple SIR model.

## Forecasts updated: {date}

Forecast are based on the simple [SIR model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model) which assumes
an individual can be one of three states:

- Susceptible: Part of the population not immune to the disease 
- Infected: Are currently infected.
- Removed: Are immune after a recovery or dead.

The model is governed by two parameters, the rate at which individuals contract the disease 𝛽 (beta), and the rate at which they are removed from the infected group 𝛾 (gamma). 

{plots}
'''

def extract_country(plot_filename):
    base, _ = op.splitext(plot_filename)
    country, _ = base.split('_')
    return country.capitalize()


plot_img_markdown_template = "![country](./forecast_plots/{plot_filename})"

forecast_plots = glob.glob(op.join(FORECAST_PLOT_FOLDER, '*.png'))

readme_plot_makdowns = []

for forecast_plot in forecast_plots:
    plot_filename = op.basename(forecast_plot)
    country = extract_country(plot_filename)
    plot_img_markdown = plot_img_markdown_template.format(country=country, plot_filename=plot_filename)
    readme_plot_makdowns.append(plot_img_markdown)

readme_markdown = readme_markdown_template.format(
    date=datetime.now().strftime("%d-%m-%Y"),
    plots='\n\n'.join(readme_plot_makdowns)
)

with open(README_FILE,'w') as readme_file:
    readme_file.write(readme_markdown)


