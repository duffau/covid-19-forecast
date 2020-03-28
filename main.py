#! .venv/bin/python
from scripts.download_cssegi_sand_data import main as get_data
from scripts.run_data_prep import main as data_prep
from scripts.make_new_forecast import main as calc_forecast
from scripts.make_forecast_plots import main as plot_forecast
from scripts.make_readme import main as make_readme
from scripts.deploy import deploy
import logging

logging.basicConfig(level=logging.INFO)

get_data()
data_prep()
update_time = calc_forecast()
plot_forecast(update_time)
make_readme()
deploy()
