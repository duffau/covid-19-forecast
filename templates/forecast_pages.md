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
