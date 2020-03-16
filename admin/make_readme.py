import os.path as op
import glob
from datetime import datetime

FORECAST_PLOT_FOLDER = '../forecast_plots'
README_FILE = '../_README.md'

readme_markdown_template = '''
# Forecasting COVID-19 cases

Attempt to forecast the number of cases of COVID-19 around the world using the simple SIR model.

## Forecasts updated: {date}

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


