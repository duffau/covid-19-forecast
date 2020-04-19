PIPENV_RUN := pipenv run python
all : get-data data-prep calc-forecast plot-forecast make-content deploy-github
from-data-prep: data-prep calc-forecast plot-forecast make-content deploy-github
from-calc-forecast: calc-forecast plot-forecast make-content deploy-github
from-plot: plot-forecast make-content deploy-github
from-readme: make-content deploy-github

to-plot-forecast: get-data data-prep calc-forecast plot-forecast


get-data :
	${PIPENV_RUN} scripts/download_cssegi_sand_data.py
	${PIPENV_RUN} scripts/download_population_world_bank.py
	${PIPENV_RUN} scripts/download_hospital_beds_world_bank.py

data-prep :
	${PIPENV_RUN} scripts/run_data_prep.py

calc-forecast:
	${PIPENV_RUN} scripts/make_new_forecast.py

plot-forecast:
	${PIPENV_RUN} scripts/remove_forecast_plots.py
	${PIPENV_RUN} scripts/make_forecast_plots.py

make-content:
	${PIPENV_RUN} scripts/make_content.py

deploy-github:
	${PIPENV_RUN} scripts/deploy.py
