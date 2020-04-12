import os
import os.path as op
from models import SIRParams, SIR
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

PLOT_FOLDER = 'plots/sir_sim'
os.makedirs(PLOT_FOLDER, exist_ok=True)

BETA = 0.6
GAMMA = 0.35
N = 1.0
I0 = 0.01
R0 = 0.001
S0 = N - I0 - R0

sir_params = SIRParams(
    beta=BETA,
    gamma=GAMMA,
    S0=S0,
    I0=I0,
    R0=R0
)

t_eval = range(100)
model = SIR(params=sir_params)
St, It, Rt = model.simulate(t_eval=t_eval, N=N)

plt.plot(t_eval, St, label='$S_t$')
plt.plot(t_eval, It, label='$I_t$')
plt.plot(t_eval, Rt, label='$R_t$')
plt.legend()
plt.xlabel('Time')
plt.title(f'Simulated SIR paths – $\\beta$={BETA}, $\\gamma$={GAMMA}')
plt.savefig(op.join(PLOT_FOLDER, 'sir_sim.png'))

# Estimating beta with "back out" method
df = pd.DataFrame({'S': St, 'I': It, 'R': Rt, 'beta': BETA})
df['beta_backed_out'] = (df['I'].diff() / df['I'].shift(-1) + GAMMA) / df['S']
df.plot(y=['beta_backed_out', 'beta'], title='Estimate of beta from simulated SIR paths')
plt.savefig(op.join(PLOT_FOLDER, 'beta_backed_out.png'))
