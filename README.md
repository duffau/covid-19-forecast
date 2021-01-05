<h1 align="center">Forecasting COVID-19 cases</h1>


Attempt to forecast the number of cases of COVID-19 around the world using the simple [SIR model][sir_model_wiki].

The development of the estimation method is documented in the [CHANGELOG of the analysis section](analysis/CHANGELOG.md).

The site is hosted here: https://duffau.github.io/covid-19-forecast/.
## Forecasts
*Updated: 05-01-2021*

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

## Plots

- [World](#world)
- [Afghanistan](#afghanistan)
- [Albania](#albania)
- [Algeria](#algeria)
- [Andorra](#andorra)
- [Angola](#angola)
- [Antigua-and-barbuda](#antigua-and-barbuda)
- [Argentina](#argentina)
- [Armenia](#armenia)
- [Australia](#australia)
- [Austria](#austria)
- [Azerbaijan](#azerbaijan)
- [Bahamas](#bahamas)
- [Bahrain](#bahrain)
- [Bangladesh](#bangladesh)
- [Barbados](#barbados)
- [Belarus](#belarus)
- [Belgium](#belgium)
- [Belize](#belize)
- [Benin](#benin)
- [Bhutan](#bhutan)
- [Bolivia](#bolivia)
- [Bosnia-and-herzegovina](#bosnia-and-herzegovina)
- [Botswana](#botswana)
- [Brazil](#brazil)
- [Brunei](#brunei)
- [Bulgaria](#bulgaria)
- [Burkina-faso](#burkina-faso)
- [Burma](#burma)
- [Burundi](#burundi)
- [Cabo-verde](#cabo-verde)
- [Cambodia](#cambodia)
- [Cameroon](#cameroon)
- [Canada](#canada)
- [Central-african-republic](#central-african-republic)
- [Chad](#chad)
- [Chile](#chile)
- [China](#china)
- [Colombia](#colombia)
- [Comoros](#comoros)
- [Congo-brazzaville](#congo-brazzaville)
- [Congo-kinshasa](#congo-kinshasa)
- [Costa-rica](#costa-rica)
- [Cote-divoire](#cote-divoire)
- [Croatia](#croatia)
- [Cuba](#cuba)
- [Cyprus](#cyprus)
- [Czechia](#czechia)
- [Denmark](#denmark)
- [Diamond-princess](#diamond-princess)
- [Djibouti](#djibouti)
- [Dominica](#dominica)
- [Dominican-republic](#dominican-republic)
- [Ecuador](#ecuador)
- [Egypt](#egypt)
- [El-salvador](#el-salvador)
- [Equatorial-guinea](#equatorial-guinea)
- [Eritrea](#eritrea)
- [Estonia](#estonia)
- [Eswatini](#eswatini)
- [Ethiopia](#ethiopia)
- [Fiji](#fiji)
- [Finland](#finland)
- [France](#france)
- [Gabon](#gabon)
- [Gambia](#gambia)
- [Georgia](#georgia)
- [Germany](#germany)
- [Ghana](#ghana)
- [Greece](#greece)
- [Grenada](#grenada)
- [Guatemala](#guatemala)
- [Guinea-bissau](#guinea-bissau)
- [Guinea](#guinea)
- [Guyana](#guyana)
- [Haiti](#haiti)
- [Holy-see](#holy-see)
- [Honduras](#honduras)
- [Hungary](#hungary)
- [Iceland](#iceland)
- [India](#india)
- [Indonesia](#indonesia)
- [Iran](#iran)
- [Iraq](#iraq)
- [Ireland](#ireland)
- [Israel](#israel)
- [Italy](#italy)
- [Jamaica](#jamaica)
- [Japan](#japan)
- [Jordan](#jordan)
- [Kazakhstan](#kazakhstan)
- [Kenya](#kenya)
- [Korea--south](#korea--south)
- [Kosovo](#kosovo)
- [Kuwait](#kuwait)
- [Kyrgyzstan](#kyrgyzstan)
- [Laos](#laos)
- [Latvia](#latvia)
- [Lebanon](#lebanon)
- [Lesotho](#lesotho)
- [Liberia](#liberia)
- [Libya](#libya)
- [Liechtenstein](#liechtenstein)
- [Lithuania](#lithuania)
- [Luxembourg](#luxembourg)
- [Madagascar](#madagascar)
- [Malawi](#malawi)
- [Malaysia](#malaysia)
- [Maldives](#maldives)
- [Mali](#mali)
- [Malta](#malta)
- [Marshall-islands](#marshall-islands)
- [Mauritania](#mauritania)
- [Mauritius](#mauritius)
- [Mexico](#mexico)
- [Moldova](#moldova)
- [Monaco](#monaco)
- [Mongolia](#mongolia)
- [Montenegro](#montenegro)
- [Morocco](#morocco)
- [Mozambique](#mozambique)
- [Ms-zaandam](#ms-zaandam)
- [Namibia](#namibia)
- [Nepal](#nepal)
- [Netherlands](#netherlands)
- [New-zealand](#new-zealand)
- [Nicaragua](#nicaragua)
- [Niger](#niger)
- [Nigeria](#nigeria)
- [North-macedonia](#north-macedonia)
- [Norway](#norway)
- [Oman](#oman)
- [Pakistan](#pakistan)
- [Panama](#panama)
- [Papua-new-guinea](#papua-new-guinea)
- [Paraguay](#paraguay)
- [Peru](#peru)
- [Philippines](#philippines)
- [Poland](#poland)
- [Portugal](#portugal)
- [Qatar](#qatar)
- [Romania](#romania)
- [Russia](#russia)
- [Rwanda](#rwanda)
- [Saint-kitts-and-nevis](#saint-kitts-and-nevis)
- [Saint-lucia](#saint-lucia)
- [Saint-vincent-and-the-grenadines](#saint-vincent-and-the-grenadines)
- [Samoa](#samoa)
- [San-marino](#san-marino)
- [Sao-tome-and-principe](#sao-tome-and-principe)
- [Saudi-arabia](#saudi-arabia)
- [Senegal](#senegal)
- [Serbia](#serbia)
- [Seychelles](#seychelles)
- [Sierra-leone](#sierra-leone)
- [Singapore](#singapore)
- [Slovakia](#slovakia)
- [Slovenia](#slovenia)
- [Solomon-islands](#solomon-islands)
- [Somalia](#somalia)
- [South-africa](#south-africa)
- [South-sudan](#south-sudan)
- [Spain](#spain)
- [Sri-lanka](#sri-lanka)
- [Sudan](#sudan)
- [Suriname](#suriname)
- [Sweden](#sweden)
- [Switzerland](#switzerland)
- [Syria](#syria)
- [Taiwan](#taiwan)
- [Tajikistan](#tajikistan)
- [Tanzania](#tanzania)
- [Thailand](#thailand)
- [Timor-leste](#timor-leste)
- [Togo](#togo)
- [Trinidad-and-tobago](#trinidad-and-tobago)
- [Tunisia](#tunisia)
- [Turkey](#turkey)
- [Uganda](#uganda)
- [Ukraine](#ukraine)
- [United-arab-emirates](#united-arab-emirates)
- [United-kingdom](#united-kingdom)
- [United-states](#united-states)
- [Uruguay](#uruguay)
- [Uzbekistan](#uzbekistan)
- [Vanuatu](#vanuatu)
- [Venezuela](#venezuela)
- [Vietnam](#vietnam)
- [West-bank-and-gaza](#west-bank-and-gaza)
- [Yemen](#yemen)
- [Zambia](#zambia)
- [Zimbabwe](#zimbabwe)

### World

|![World](forecast_plots/world_aggregate.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Afghanistan

|![Afghanistan](forecast_plots/afghanistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Albania

|![Albania](forecast_plots/albania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Algeria

|![Algeria](forecast_plots/algeria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Andorra

|![Andorra](forecast_plots/andorra_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Angola

|![Angola](forecast_plots/angola_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Antigua-and-barbuda

|![Antigua-and-barbuda](forecast_plots/antigua-and-barbuda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Argentina

|![Argentina](forecast_plots/argentina_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Armenia

|![Armenia](forecast_plots/armenia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Australia

|![Australia](forecast_plots/australia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Austria

|![Austria](forecast_plots/austria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Azerbaijan

|![Azerbaijan](forecast_plots/azerbaijan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bahamas

|![Bahamas](forecast_plots/bahamas_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bahrain

|![Bahrain](forecast_plots/bahrain_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bangladesh

|![Bangladesh](forecast_plots/bangladesh_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Barbados

|![Barbados](forecast_plots/barbados_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Belarus

|![Belarus](forecast_plots/belarus_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Belgium

|![Belgium](forecast_plots/belgium_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Belize

|![Belize](forecast_plots/belize_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Benin

|![Benin](forecast_plots/benin_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bhutan

|![Bhutan](forecast_plots/bhutan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bolivia

|![Bolivia](forecast_plots/bolivia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bosnia-and-herzegovina

|![Bosnia-and-herzegovina](forecast_plots/bosnia-and-herzegovina_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Botswana

|![Botswana](forecast_plots/botswana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Brazil

|![Brazil](forecast_plots/brazil_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Brunei

|![Brunei](forecast_plots/brunei_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Bulgaria

|![Bulgaria](forecast_plots/bulgaria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Burkina-faso

|![Burkina-faso](forecast_plots/burkina-faso_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Burma

|![Burma](forecast_plots/burma_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Burundi

|![Burundi](forecast_plots/burundi_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cabo-verde

|![Cabo-verde](forecast_plots/cabo-verde_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cambodia

|![Cambodia](forecast_plots/cambodia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cameroon

|![Cameroon](forecast_plots/cameroon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Canada

|![Canada](forecast_plots/canada_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Central-african-republic

|![Central-african-republic](forecast_plots/central-african-republic_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Chad

|![Chad](forecast_plots/chad_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Chile

|![Chile](forecast_plots/chile_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### China

|![China](forecast_plots/china_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Colombia

|![Colombia](forecast_plots/colombia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Comoros

|![Comoros](forecast_plots/comoros_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Congo-brazzaville

|![Congo-brazzaville](forecast_plots/congo-brazzaville_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Congo-kinshasa

|![Congo-kinshasa](forecast_plots/congo-kinshasa_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Costa-rica

|![Costa-rica](forecast_plots/costa-rica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cote-divoire

|![Cote-divoire](forecast_plots/cote-divoire_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Croatia

|![Croatia](forecast_plots/croatia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cuba

|![Cuba](forecast_plots/cuba_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Cyprus

|![Cyprus](forecast_plots/cyprus_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Czechia

|![Czechia](forecast_plots/czechia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Denmark

|![Denmark](forecast_plots/denmark_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Diamond-princess

|![Diamond-princess](forecast_plots/diamond-princess_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Djibouti

|![Djibouti](forecast_plots/djibouti_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Dominica

|![Dominica](forecast_plots/dominica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Dominican-republic

|![Dominican-republic](forecast_plots/dominican-republic_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ecuador

|![Ecuador](forecast_plots/ecuador_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Egypt

|![Egypt](forecast_plots/egypt_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### El-salvador

|![El-salvador](forecast_plots/el-salvador_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Equatorial-guinea

|![Equatorial-guinea](forecast_plots/equatorial-guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Eritrea

|![Eritrea](forecast_plots/eritrea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Estonia

|![Estonia](forecast_plots/estonia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Eswatini

|![Eswatini](forecast_plots/eswatini_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ethiopia

|![Ethiopia](forecast_plots/ethiopia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Fiji

|![Fiji](forecast_plots/fiji_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Finland

|![Finland](forecast_plots/finland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### France

|![France](forecast_plots/france_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Gabon

|![Gabon](forecast_plots/gabon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Gambia

|![Gambia](forecast_plots/gambia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Georgia

|![Georgia](forecast_plots/georgia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Germany

|![Germany](forecast_plots/germany_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ghana

|![Ghana](forecast_plots/ghana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Greece

|![Greece](forecast_plots/greece_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Grenada

|![Grenada](forecast_plots/grenada_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Guatemala

|![Guatemala](forecast_plots/guatemala_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Guinea-bissau

|![Guinea-bissau](forecast_plots/guinea-bissau_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Guinea

|![Guinea](forecast_plots/guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Guyana

|![Guyana](forecast_plots/guyana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Haiti

|![Haiti](forecast_plots/haiti_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Holy-see

|![Holy-see](forecast_plots/holy-see_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Honduras

|![Honduras](forecast_plots/honduras_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Hungary

|![Hungary](forecast_plots/hungary_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Iceland

|![Iceland](forecast_plots/iceland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### India

|![India](forecast_plots/india_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Indonesia

|![Indonesia](forecast_plots/indonesia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Iran

|![Iran](forecast_plots/iran_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Iraq

|![Iraq](forecast_plots/iraq_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ireland

|![Ireland](forecast_plots/ireland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Israel

|![Israel](forecast_plots/israel_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Italy

|![Italy](forecast_plots/italy_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Jamaica

|![Jamaica](forecast_plots/jamaica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Japan

|![Japan](forecast_plots/japan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Jordan

|![Jordan](forecast_plots/jordan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Kazakhstan

|![Kazakhstan](forecast_plots/kazakhstan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Kenya

|![Kenya](forecast_plots/kenya_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Korea--south

|![Korea--south](forecast_plots/korea--south_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Kosovo

|![Kosovo](forecast_plots/kosovo_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Kuwait

|![Kuwait](forecast_plots/kuwait_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Kyrgyzstan

|![Kyrgyzstan](forecast_plots/kyrgyzstan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Laos

|![Laos](forecast_plots/laos_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Latvia

|![Latvia](forecast_plots/latvia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Lebanon

|![Lebanon](forecast_plots/lebanon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Lesotho

|![Lesotho](forecast_plots/lesotho_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Liberia

|![Liberia](forecast_plots/liberia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Libya

|![Libya](forecast_plots/libya_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Liechtenstein

|![Liechtenstein](forecast_plots/liechtenstein_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Lithuania

|![Lithuania](forecast_plots/lithuania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Luxembourg

|![Luxembourg](forecast_plots/luxembourg_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Madagascar

|![Madagascar](forecast_plots/madagascar_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Malawi

|![Malawi](forecast_plots/malawi_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Malaysia

|![Malaysia](forecast_plots/malaysia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Maldives

|![Maldives](forecast_plots/maldives_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mali

|![Mali](forecast_plots/mali_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Malta

|![Malta](forecast_plots/malta_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Marshall-islands

|![Marshall-islands](forecast_plots/marshall-islands_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mauritania

|![Mauritania](forecast_plots/mauritania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mauritius

|![Mauritius](forecast_plots/mauritius_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mexico

|![Mexico](forecast_plots/mexico_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Moldova

|![Moldova](forecast_plots/moldova_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Monaco

|![Monaco](forecast_plots/monaco_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mongolia

|![Mongolia](forecast_plots/mongolia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Montenegro

|![Montenegro](forecast_plots/montenegro_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Morocco

|![Morocco](forecast_plots/morocco_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Mozambique

|![Mozambique](forecast_plots/mozambique_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ms-zaandam

|![Ms-zaandam](forecast_plots/ms-zaandam_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Namibia

|![Namibia](forecast_plots/namibia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Nepal

|![Nepal](forecast_plots/nepal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Netherlands

|![Netherlands](forecast_plots/netherlands_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### New-zealand

|![New-zealand](forecast_plots/new-zealand_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Nicaragua

|![Nicaragua](forecast_plots/nicaragua_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Niger

|![Niger](forecast_plots/niger_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Nigeria

|![Nigeria](forecast_plots/nigeria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### North-macedonia

|![North-macedonia](forecast_plots/north-macedonia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Norway

|![Norway](forecast_plots/norway_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Oman

|![Oman](forecast_plots/oman_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Pakistan

|![Pakistan](forecast_plots/pakistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Panama

|![Panama](forecast_plots/panama_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Papua-new-guinea

|![Papua-new-guinea](forecast_plots/papua-new-guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Paraguay

|![Paraguay](forecast_plots/paraguay_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Peru

|![Peru](forecast_plots/peru_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Philippines

|![Philippines](forecast_plots/philippines_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Poland

|![Poland](forecast_plots/poland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Portugal

|![Portugal](forecast_plots/portugal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Qatar

|![Qatar](forecast_plots/qatar_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Romania

|![Romania](forecast_plots/romania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Russia

|![Russia](forecast_plots/russia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Rwanda

|![Rwanda](forecast_plots/rwanda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Saint-kitts-and-nevis

|![Saint-kitts-and-nevis](forecast_plots/saint-kitts-and-nevis_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Saint-lucia

|![Saint-lucia](forecast_plots/saint-lucia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Saint-vincent-and-the-grenadines

|![Saint-vincent-and-the-grenadines](forecast_plots/saint-vincent-and-the-grenadines_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Samoa

|![Samoa](forecast_plots/samoa_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### San-marino

|![San-marino](forecast_plots/san-marino_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Sao-tome-and-principe

|![Sao-tome-and-principe](forecast_plots/sao-tome-and-principe_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Saudi-arabia

|![Saudi-arabia](forecast_plots/saudi-arabia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Senegal

|![Senegal](forecast_plots/senegal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Serbia

|![Serbia](forecast_plots/serbia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Seychelles

|![Seychelles](forecast_plots/seychelles_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Sierra-leone

|![Sierra-leone](forecast_plots/sierra-leone_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Singapore

|![Singapore](forecast_plots/singapore_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Slovakia

|![Slovakia](forecast_plots/slovakia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Slovenia

|![Slovenia](forecast_plots/slovenia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Solomon-islands

|![Solomon-islands](forecast_plots/solomon-islands_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Somalia

|![Somalia](forecast_plots/somalia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### South-africa

|![South-africa](forecast_plots/south-africa_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### South-sudan

|![South-sudan](forecast_plots/south-sudan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Spain

|![Spain](forecast_plots/spain_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Sri-lanka

|![Sri-lanka](forecast_plots/sri-lanka_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Sudan

|![Sudan](forecast_plots/sudan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Suriname

|![Suriname](forecast_plots/suriname_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Sweden

|![Sweden](forecast_plots/sweden_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Switzerland

|![Switzerland](forecast_plots/switzerland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Syria

|![Syria](forecast_plots/syria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Taiwan

|![Taiwan](forecast_plots/taiwan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Tajikistan

|![Tajikistan](forecast_plots/tajikistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Tanzania

|![Tanzania](forecast_plots/tanzania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Thailand

|![Thailand](forecast_plots/thailand_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Timor-leste

|![Timor-leste](forecast_plots/timor-leste_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Togo

|![Togo](forecast_plots/togo_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Trinidad-and-tobago

|![Trinidad-and-tobago](forecast_plots/trinidad-and-tobago_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Tunisia

|![Tunisia](forecast_plots/tunisia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Turkey

|![Turkey](forecast_plots/turkey_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Uganda

|![Uganda](forecast_plots/uganda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Ukraine

|![Ukraine](forecast_plots/ukraine_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### United-arab-emirates

|![United-arab-emirates](forecast_plots/united-arab-emirates_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### United-kingdom

|![United-kingdom](forecast_plots/united-kingdom_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### United-states

|![United-states](forecast_plots/united-states_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Uruguay

|![Uruguay](forecast_plots/uruguay_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Uzbekistan

|![Uzbekistan](forecast_plots/uzbekistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Vanuatu

|![Vanuatu](forecast_plots/vanuatu_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Venezuela

|![Venezuela](forecast_plots/venezuela_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Vietnam

|![Vietnam](forecast_plots/vietnam_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### West-bank-and-gaza

|![West-bank-and-gaza](forecast_plots/west-bank-and-gaza_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Yemen

|![Yemen](forecast_plots/yemen_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Zambia

|![Zambia](forecast_plots/zambia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


### Zimbabwe

|![Zimbabwe](forecast_plots/zimbabwe_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 04-01-2021*|


[sir_model_wiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model
[csse-data-repo]: https://github.com/CSSEGISandData/COVID-19
[john-hopkins-dashboard]: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
[Bohner et al (2018)]: https://arxiv.org/abs/1812.09759
[Bailey (1975)]: https://www.amazon.com/Mathematical-Theory-Infectious-Diseases-2nd/dp/0852642318 

