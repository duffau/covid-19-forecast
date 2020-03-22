from get_data.download_cssegi_sand_data import main as get_data
from data_prep.cssegi_prep import main as data_prep
from admin.make_new_forecast import main as calc_forecast
from admin.make_forecast_plots import main as plot_forecast
from admin.make_readme import main as make_readme
import logging

logging.basicConfig(level=logging.INFO)

get_data()
data_prep()
update_time = calc_forecast()
plot_forecast(update_time)
make_readme()
