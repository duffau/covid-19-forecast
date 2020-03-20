
# Forecasting COVID-19 cases

Attempt to forecast the number of cases of COVID-19 around the world using the simple SIR model.

## Forecasts
*Updated: 20-03-2020*

Forecasts are based on the simple [SIR model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model) which assumes
an individual can be in one of three states,

- Susceptible: Part of the population not immune to the disease, 
- Infected: Is currently infected,
- Removed: Is immune after a recovery or death.

The model is governed by two parameters, the rate at which individuals contract the disease 𝛽 (beta), and the rate at which they are removed from the infected group 𝛾 (gamma). 

Data is downloaded from *Johns Hopkins University Center for Systems Science and Engineering* COVID-19 [data repository](](https://github.com/CSSEGISandData/COVID-19)), used by their 
[dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) app.

|![Spain](forecast_plots/spain_sir.png)|
|:----------------------------------------:|
| *Latest data point: 20-03-2020*|

|![Italy](forecast_plots/italy_sir.png)|
|:----------------------------------------:|
| *Latest data point: 20-03-2020*|

|![Iran](forecast_plots/iran_sir.png)|
|:----------------------------------------:|
| *Latest data point: 20-03-2020*|

|![Sweden](forecast_plots/sweden_sir.png)|
|:----------------------------------------:|
| *Latest data point: 20-03-2020*|

|![Denmark](forecast_plots/denmark_sir.png)|
|:----------------------------------------:|
| *Latest data point: 20-03-2020*|
