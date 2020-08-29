---
mathjax: true
---

{%- include mathjax.html -%}


<h1 align="center">Forecasting COVID-19 cases</h1>


Attempt to forecast the number of cases of COVID-19 around the world using the simple [SIR model][sir_model_wiki].

The development of the estimation method is documented in the [CHANGELOG of the analysis section](analysis/CHANGELOG.md).
## Forecasts
*Updated: 29-08-2020*

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
\begin{equation}
I(t) = I_0 (1 + \kappa)^{b/(b-c)} \left(1 + \kappa e^{(b-c)(t-t_0)}\right)^{-b/(b-c)}e^{(b-c)(t-t_0)}.
\end{equation}
$$

where $b$ and $c$ are free parameters governing the rate of transmission and recovery, respectively, 
$I_0$ is the number of infected at time $t_0$ and $\kappa = I_0/S_0$.

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
- [Venezuela](#venezuela)
- [Vietnam](#vietnam)
- [West-bank-and-gaza](#west-bank-and-gaza)
- [Western-sahara](#western-sahara)
- [Yemen](#yemen)
- [Zambia](#zambia)
- [Zimbabwe](#zimbabwe)

### World

|![World](forecast_plots/world_aggregate.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Afghanistan

|![Afghanistan](forecast_plots/afghanistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Albania

|![Albania](forecast_plots/albania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Algeria

|![Algeria](forecast_plots/algeria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Andorra

|![Andorra](forecast_plots/andorra_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Angola

|![Angola](forecast_plots/angola_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Antigua-and-barbuda

|![Antigua-and-barbuda](forecast_plots/antigua-and-barbuda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Argentina

|![Argentina](forecast_plots/argentina_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Armenia

|![Armenia](forecast_plots/armenia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Australia

|![Australia](forecast_plots/australia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Austria

|![Austria](forecast_plots/austria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Azerbaijan

|![Azerbaijan](forecast_plots/azerbaijan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bahamas

|![Bahamas](forecast_plots/bahamas_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bahrain

|![Bahrain](forecast_plots/bahrain_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bangladesh

|![Bangladesh](forecast_plots/bangladesh_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Barbados

|![Barbados](forecast_plots/barbados_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Belarus

|![Belarus](forecast_plots/belarus_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Belgium

|![Belgium](forecast_plots/belgium_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Belize

|![Belize](forecast_plots/belize_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Benin

|![Benin](forecast_plots/benin_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bhutan

|![Bhutan](forecast_plots/bhutan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bolivia

|![Bolivia](forecast_plots/bolivia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bosnia-and-herzegovina

|![Bosnia-and-herzegovina](forecast_plots/bosnia-and-herzegovina_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Botswana

|![Botswana](forecast_plots/botswana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Brazil

|![Brazil](forecast_plots/brazil_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Brunei

|![Brunei](forecast_plots/brunei_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Bulgaria

|![Bulgaria](forecast_plots/bulgaria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Burkina-faso

|![Burkina-faso](forecast_plots/burkina-faso_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Burma

|![Burma](forecast_plots/burma_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Burundi

|![Burundi](forecast_plots/burundi_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cabo-verde

|![Cabo-verde](forecast_plots/cabo-verde_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cambodia

|![Cambodia](forecast_plots/cambodia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cameroon

|![Cameroon](forecast_plots/cameroon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Canada

|![Canada](forecast_plots/canada_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Central-african-republic

|![Central-african-republic](forecast_plots/central-african-republic_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Chad

|![Chad](forecast_plots/chad_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Chile

|![Chile](forecast_plots/chile_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### China

|![China](forecast_plots/china_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Colombia

|![Colombia](forecast_plots/colombia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Comoros

|![Comoros](forecast_plots/comoros_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Congo-brazzaville

|![Congo-brazzaville](forecast_plots/congo-brazzaville_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Congo-kinshasa

|![Congo-kinshasa](forecast_plots/congo-kinshasa_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Costa-rica

|![Costa-rica](forecast_plots/costa-rica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cote-divoire

|![Cote-divoire](forecast_plots/cote-divoire_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Croatia

|![Croatia](forecast_plots/croatia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cuba

|![Cuba](forecast_plots/cuba_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Cyprus

|![Cyprus](forecast_plots/cyprus_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Czechia

|![Czechia](forecast_plots/czechia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Denmark

|![Denmark](forecast_plots/denmark_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Diamond-princess

|![Diamond-princess](forecast_plots/diamond-princess_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Djibouti

|![Djibouti](forecast_plots/djibouti_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Dominica

|![Dominica](forecast_plots/dominica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Dominican-republic

|![Dominican-republic](forecast_plots/dominican-republic_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ecuador

|![Ecuador](forecast_plots/ecuador_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Egypt

|![Egypt](forecast_plots/egypt_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### El-salvador

|![El-salvador](forecast_plots/el-salvador_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Equatorial-guinea

|![Equatorial-guinea](forecast_plots/equatorial-guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Eritrea

|![Eritrea](forecast_plots/eritrea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Estonia

|![Estonia](forecast_plots/estonia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Eswatini

|![Eswatini](forecast_plots/eswatini_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ethiopia

|![Ethiopia](forecast_plots/ethiopia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Fiji

|![Fiji](forecast_plots/fiji_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Finland

|![Finland](forecast_plots/finland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### France

|![France](forecast_plots/france_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Gabon

|![Gabon](forecast_plots/gabon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Gambia

|![Gambia](forecast_plots/gambia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Georgia

|![Georgia](forecast_plots/georgia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Germany

|![Germany](forecast_plots/germany_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ghana

|![Ghana](forecast_plots/ghana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Greece

|![Greece](forecast_plots/greece_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Grenada

|![Grenada](forecast_plots/grenada_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Guatemala

|![Guatemala](forecast_plots/guatemala_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Guinea-bissau

|![Guinea-bissau](forecast_plots/guinea-bissau_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Guinea

|![Guinea](forecast_plots/guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Guyana

|![Guyana](forecast_plots/guyana_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Haiti

|![Haiti](forecast_plots/haiti_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Holy-see

|![Holy-see](forecast_plots/holy-see_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Honduras

|![Honduras](forecast_plots/honduras_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Hungary

|![Hungary](forecast_plots/hungary_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Iceland

|![Iceland](forecast_plots/iceland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### India

|![India](forecast_plots/india_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Indonesia

|![Indonesia](forecast_plots/indonesia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Iran

|![Iran](forecast_plots/iran_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Iraq

|![Iraq](forecast_plots/iraq_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ireland

|![Ireland](forecast_plots/ireland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Israel

|![Israel](forecast_plots/israel_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Italy

|![Italy](forecast_plots/italy_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Jamaica

|![Jamaica](forecast_plots/jamaica_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Japan

|![Japan](forecast_plots/japan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Jordan

|![Jordan](forecast_plots/jordan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Kazakhstan

|![Kazakhstan](forecast_plots/kazakhstan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Kenya

|![Kenya](forecast_plots/kenya_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Korea--south

|![Korea--south](forecast_plots/korea--south_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Kosovo

|![Kosovo](forecast_plots/kosovo_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Kuwait

|![Kuwait](forecast_plots/kuwait_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Kyrgyzstan

|![Kyrgyzstan](forecast_plots/kyrgyzstan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Laos

|![Laos](forecast_plots/laos_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Latvia

|![Latvia](forecast_plots/latvia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Lebanon

|![Lebanon](forecast_plots/lebanon_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Lesotho

|![Lesotho](forecast_plots/lesotho_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Liberia

|![Liberia](forecast_plots/liberia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Libya

|![Libya](forecast_plots/libya_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Liechtenstein

|![Liechtenstein](forecast_plots/liechtenstein_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Lithuania

|![Lithuania](forecast_plots/lithuania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Luxembourg

|![Luxembourg](forecast_plots/luxembourg_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Madagascar

|![Madagascar](forecast_plots/madagascar_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Malawi

|![Malawi](forecast_plots/malawi_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Malaysia

|![Malaysia](forecast_plots/malaysia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Maldives

|![Maldives](forecast_plots/maldives_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mali

|![Mali](forecast_plots/mali_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Malta

|![Malta](forecast_plots/malta_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mauritania

|![Mauritania](forecast_plots/mauritania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mauritius

|![Mauritius](forecast_plots/mauritius_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mexico

|![Mexico](forecast_plots/mexico_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Moldova

|![Moldova](forecast_plots/moldova_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Monaco

|![Monaco](forecast_plots/monaco_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mongolia

|![Mongolia](forecast_plots/mongolia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Montenegro

|![Montenegro](forecast_plots/montenegro_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Morocco

|![Morocco](forecast_plots/morocco_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Mozambique

|![Mozambique](forecast_plots/mozambique_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ms-zaandam

|![Ms-zaandam](forecast_plots/ms-zaandam_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Namibia

|![Namibia](forecast_plots/namibia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Nepal

|![Nepal](forecast_plots/nepal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Netherlands

|![Netherlands](forecast_plots/netherlands_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### New-zealand

|![New-zealand](forecast_plots/new-zealand_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Nicaragua

|![Nicaragua](forecast_plots/nicaragua_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Niger

|![Niger](forecast_plots/niger_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Nigeria

|![Nigeria](forecast_plots/nigeria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### North-macedonia

|![North-macedonia](forecast_plots/north-macedonia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Norway

|![Norway](forecast_plots/norway_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Oman

|![Oman](forecast_plots/oman_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Pakistan

|![Pakistan](forecast_plots/pakistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Panama

|![Panama](forecast_plots/panama_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Papua-new-guinea

|![Papua-new-guinea](forecast_plots/papua-new-guinea_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Paraguay

|![Paraguay](forecast_plots/paraguay_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Peru

|![Peru](forecast_plots/peru_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Philippines

|![Philippines](forecast_plots/philippines_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Poland

|![Poland](forecast_plots/poland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Portugal

|![Portugal](forecast_plots/portugal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Qatar

|![Qatar](forecast_plots/qatar_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Romania

|![Romania](forecast_plots/romania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Russia

|![Russia](forecast_plots/russia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Rwanda

|![Rwanda](forecast_plots/rwanda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Saint-kitts-and-nevis

|![Saint-kitts-and-nevis](forecast_plots/saint-kitts-and-nevis_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Saint-lucia

|![Saint-lucia](forecast_plots/saint-lucia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Saint-vincent-and-the-grenadines

|![Saint-vincent-and-the-grenadines](forecast_plots/saint-vincent-and-the-grenadines_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### San-marino

|![San-marino](forecast_plots/san-marino_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Sao-tome-and-principe

|![Sao-tome-and-principe](forecast_plots/sao-tome-and-principe_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Saudi-arabia

|![Saudi-arabia](forecast_plots/saudi-arabia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Senegal

|![Senegal](forecast_plots/senegal_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Serbia

|![Serbia](forecast_plots/serbia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Seychelles

|![Seychelles](forecast_plots/seychelles_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Sierra-leone

|![Sierra-leone](forecast_plots/sierra-leone_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Singapore

|![Singapore](forecast_plots/singapore_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Slovakia

|![Slovakia](forecast_plots/slovakia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Slovenia

|![Slovenia](forecast_plots/slovenia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Somalia

|![Somalia](forecast_plots/somalia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### South-africa

|![South-africa](forecast_plots/south-africa_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### South-sudan

|![South-sudan](forecast_plots/south-sudan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Spain

|![Spain](forecast_plots/spain_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Sri-lanka

|![Sri-lanka](forecast_plots/sri-lanka_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Sudan

|![Sudan](forecast_plots/sudan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Suriname

|![Suriname](forecast_plots/suriname_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Sweden

|![Sweden](forecast_plots/sweden_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Switzerland

|![Switzerland](forecast_plots/switzerland_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Syria

|![Syria](forecast_plots/syria_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Taiwan

|![Taiwan](forecast_plots/taiwan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Tajikistan

|![Tajikistan](forecast_plots/tajikistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Tanzania

|![Tanzania](forecast_plots/tanzania_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Thailand

|![Thailand](forecast_plots/thailand_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Timor-leste

|![Timor-leste](forecast_plots/timor-leste_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Togo

|![Togo](forecast_plots/togo_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Trinidad-and-tobago

|![Trinidad-and-tobago](forecast_plots/trinidad-and-tobago_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Tunisia

|![Tunisia](forecast_plots/tunisia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Turkey

|![Turkey](forecast_plots/turkey_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Uganda

|![Uganda](forecast_plots/uganda_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Ukraine

|![Ukraine](forecast_plots/ukraine_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### United-arab-emirates

|![United-arab-emirates](forecast_plots/united-arab-emirates_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### United-kingdom

|![United-kingdom](forecast_plots/united-kingdom_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### United-states

|![United-states](forecast_plots/united-states_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Uruguay

|![Uruguay](forecast_plots/uruguay_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Uzbekistan

|![Uzbekistan](forecast_plots/uzbekistan_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Venezuela

|![Venezuela](forecast_plots/venezuela_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Vietnam

|![Vietnam](forecast_plots/vietnam_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### West-bank-and-gaza

|![West-bank-and-gaza](forecast_plots/west-bank-and-gaza_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Western-sahara

|![Western-sahara](forecast_plots/western-sahara_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Yemen

|![Yemen](forecast_plots/yemen_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Zambia

|![Zambia](forecast_plots/zambia_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


### Zimbabwe

|![Zimbabwe](forecast_plots/zimbabwe_SIRClosedForm.png.png)|
|:----------------------------------------:|
| *Latest data point: 28-08-2020*|


[sir_model_wiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model
[csse-data-repo]: https://github.com/CSSEGISandData/COVID-19
[john-hopkins-dashboard]: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
[Bohner et al (2018)]: https://arxiv.org/abs/1812.09759
[Bailey (1975)]: https://www.amazon.com/Mathematical-Theory-Infectious-Diseases-2nd/dp/0852642318 

