
<h1 align="center">Forecasting COVID-19 cases</h1>

Attempt to forecast the number of cases of COVID-19 around the world using the simple [SIR model][sir_model_wiki].

The development of the estimation method is documented in the [CHANGELOG of the analysis section](analysis/CHANGELOG.md).

The site is hosted here: https://duffau.github.io/covid-19-forecast/.

## Forecasts
*Updated: 19-04-2020*

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

```python
I_t = I_0 * (1 + kappa)**(b/(b-c))*(1 + kappa*exp((b-c)(t-t_0)))**(-b/(b-c)) * exp((b-c)*(t-t_0)).
```

where `b` and `c` are free parameters governing the rate of transmission and recovery, respectively, 
`I_0` is the number of infected at time `t_0` and `kappa = I_0/S_0`.

Data is downloaded from *Johns Hopkins University Center for Systems Science and Engineering* 
COVID-19 [data repository][csse-data-repo], used in their [dashboard][john-hopkins-dashboard] app.

### Plots

|![Afghanistan](forecast_plots/afghanistan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Albania](forecast_plots/albania_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Algeria](forecast_plots/algeria_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Andorra](forecast_plots/andorra_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Angola](forecast_plots/angola_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Antigua and barbuda](forecast_plots/antigua and barbuda_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Argentina](forecast_plots/argentina_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Armenia](forecast_plots/armenia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Australia](forecast_plots/australia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Austria](forecast_plots/austria_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Azerbaijan](forecast_plots/azerbaijan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bahamas](forecast_plots/bahamas_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bahrain](forecast_plots/bahrain_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bangladesh](forecast_plots/bangladesh_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Barbados](forecast_plots/barbados_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Belarus](forecast_plots/belarus_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Belgium](forecast_plots/belgium_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Belize](forecast_plots/belize_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Benin](forecast_plots/benin_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bhutan](forecast_plots/bhutan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bolivia](forecast_plots/bolivia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bosnia and herzegovina](forecast_plots/bosnia and herzegovina_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Botswana](forecast_plots/botswana_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Brazil](forecast_plots/brazil_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Brunei](forecast_plots/brunei_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Bulgaria](forecast_plots/bulgaria_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Burkina faso](forecast_plots/burkina faso_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Burma](forecast_plots/burma_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Burundi](forecast_plots/burundi_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cabo verde](forecast_plots/cabo verde_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cambodia](forecast_plots/cambodia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cameroon](forecast_plots/cameroon_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Canada](forecast_plots/canada_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Central african republic](forecast_plots/central african republic_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Chad](forecast_plots/chad_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Chile](forecast_plots/chile_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![China](forecast_plots/china_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Colombia](forecast_plots/colombia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Congo (brazzaville)](forecast_plots/congo (brazzaville)_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Congo (kinshasa)](forecast_plots/congo (kinshasa)_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Costa rica](forecast_plots/costa rica_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cote d'ivoire](forecast_plots/cote d'ivoire_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Croatia](forecast_plots/croatia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cuba](forecast_plots/cuba_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Cyprus](forecast_plots/cyprus_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Czechia](forecast_plots/czechia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Denmark](forecast_plots/denmark_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Diamond princess](forecast_plots/diamond princess_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Djibouti](forecast_plots/djibouti_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Dominica](forecast_plots/dominica_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Dominican republic](forecast_plots/dominican republic_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ecuador](forecast_plots/ecuador_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Egypt](forecast_plots/egypt_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![El salvador](forecast_plots/el salvador_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Equatorial guinea](forecast_plots/equatorial guinea_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Eritrea](forecast_plots/eritrea_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Estonia](forecast_plots/estonia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Eswatini](forecast_plots/eswatini_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ethiopia](forecast_plots/ethiopia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Fiji](forecast_plots/fiji_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Finland](forecast_plots/finland_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![France](forecast_plots/france_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Gabon](forecast_plots/gabon_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Gambia](forecast_plots/gambia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Georgia](forecast_plots/georgia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Germany](forecast_plots/germany_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ghana](forecast_plots/ghana_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Greece](forecast_plots/greece_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Grenada](forecast_plots/grenada_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Guatemala](forecast_plots/guatemala_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Guinea-bissau](forecast_plots/guinea-bissau_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Guinea](forecast_plots/guinea_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Guyana](forecast_plots/guyana_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Haiti](forecast_plots/haiti_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Holy see](forecast_plots/holy see_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Honduras](forecast_plots/honduras_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Hungary](forecast_plots/hungary_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Iceland](forecast_plots/iceland_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![India](forecast_plots/india_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Indonesia](forecast_plots/indonesia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Iran](forecast_plots/iran_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Iraq](forecast_plots/iraq_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ireland](forecast_plots/ireland_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Israel](forecast_plots/israel_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Italy](forecast_plots/italy_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Jamaica](forecast_plots/jamaica_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Japan](forecast_plots/japan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Jordan](forecast_plots/jordan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Kazakhstan](forecast_plots/kazakhstan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Kenya](forecast_plots/kenya_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Korea, south](forecast_plots/korea, south_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Kosovo](forecast_plots/kosovo_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Kuwait](forecast_plots/kuwait_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Kyrgyzstan](forecast_plots/kyrgyzstan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Laos](forecast_plots/laos_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Latvia](forecast_plots/latvia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Lebanon](forecast_plots/lebanon_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Liberia](forecast_plots/liberia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Libya](forecast_plots/libya_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Liechtenstein](forecast_plots/liechtenstein_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Lithuania](forecast_plots/lithuania_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Luxembourg](forecast_plots/luxembourg_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Madagascar](forecast_plots/madagascar_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Malawi](forecast_plots/malawi_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Malaysia](forecast_plots/malaysia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Maldives](forecast_plots/maldives_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mali](forecast_plots/mali_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Malta](forecast_plots/malta_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mauritania](forecast_plots/mauritania_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mauritius](forecast_plots/mauritius_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mexico](forecast_plots/mexico_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Moldova](forecast_plots/moldova_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Monaco](forecast_plots/monaco_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mongolia](forecast_plots/mongolia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Montenegro](forecast_plots/montenegro_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Morocco](forecast_plots/morocco_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Mozambique](forecast_plots/mozambique_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ms zaandam](forecast_plots/ms zaandam_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Namibia](forecast_plots/namibia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Nepal](forecast_plots/nepal_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Netherlands](forecast_plots/netherlands_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![New zealand](forecast_plots/new zealand_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Nicaragua](forecast_plots/nicaragua_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Niger](forecast_plots/niger_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Nigeria](forecast_plots/nigeria_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![North macedonia](forecast_plots/north macedonia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Norway](forecast_plots/norway_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Oman](forecast_plots/oman_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Pakistan](forecast_plots/pakistan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Panama](forecast_plots/panama_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Papua new guinea](forecast_plots/papua new guinea_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Paraguay](forecast_plots/paraguay_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Peru](forecast_plots/peru_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Philippines](forecast_plots/philippines_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Poland](forecast_plots/poland_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Portugal](forecast_plots/portugal_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Qatar](forecast_plots/qatar_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Romania](forecast_plots/romania_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Russia](forecast_plots/russia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Rwanda](forecast_plots/rwanda_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Saint kitts and nevis](forecast_plots/saint kitts and nevis_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Saint lucia](forecast_plots/saint lucia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Saint vincent and the grenadines](forecast_plots/saint vincent and the grenadines_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![San marino](forecast_plots/san marino_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Sao tome and principe](forecast_plots/sao tome and principe_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Saudi arabia](forecast_plots/saudi arabia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Senegal](forecast_plots/senegal_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Serbia](forecast_plots/serbia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Seychelles](forecast_plots/seychelles_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Sierra leone](forecast_plots/sierra leone_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Singapore](forecast_plots/singapore_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Slovakia](forecast_plots/slovakia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Slovenia](forecast_plots/slovenia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Somalia](forecast_plots/somalia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![South africa](forecast_plots/south africa_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![South sudan](forecast_plots/south sudan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Spain](forecast_plots/spain_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Sri lanka](forecast_plots/sri lanka_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Sudan](forecast_plots/sudan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Suriname](forecast_plots/suriname_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Sweden](forecast_plots/sweden_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Switzerland](forecast_plots/switzerland_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Syria](forecast_plots/syria_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Taiwan*](forecast_plots/taiwan*_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Tanzania](forecast_plots/tanzania_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Thailand](forecast_plots/thailand_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Timor-leste](forecast_plots/timor-leste_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Togo](forecast_plots/togo_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Trinidad and tobago](forecast_plots/trinidad and tobago_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Tunisia](forecast_plots/tunisia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Turkey](forecast_plots/turkey_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Uganda](forecast_plots/uganda_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Ukraine](forecast_plots/ukraine_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![United arab emirates](forecast_plots/united arab emirates_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![United kingdom](forecast_plots/united kingdom_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![United states](forecast_plots/united states_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Uruguay](forecast_plots/uruguay_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Uzbekistan](forecast_plots/uzbekistan_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Venezuela](forecast_plots/venezuela_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Vietnam](forecast_plots/vietnam_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![West bank and gaza](forecast_plots/west bank and gaza_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Western sahara](forecast_plots/western sahara_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![World](forecast_plots/world_aggregate.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Yemen](forecast_plots/yemen_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Zambia](forecast_plots/zambia_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|

|![Zimbabwe](forecast_plots/zimbabwe_SIRClosedForm.png)|
|:----------------------------------------:|
| *Latest data point: 18-04-2020*|
[sir_model_wiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model
[csse-data-repo]: https://github.com/CSSEGISandData/COVID-19
[john-hopkins-dashboard]: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
[Bohner et al (2018)]: https://arxiv.org/abs/1812.09759
[Bailey (1975)]: https://www.amazon.com/Mathematical-Theory-Infectious-Diseases-2nd/dp/0852642318 

