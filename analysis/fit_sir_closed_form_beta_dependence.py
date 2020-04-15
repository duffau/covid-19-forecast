import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from models import SIR, SIRParams

S0 = 0.999
I0 = 0.001
R0 = 0.00
GAMMA = 1.0


def i_t_Bohner_et_al(t, b, c, S0=S0, I0=I0, t0=0):
    kappa = I0 / S0
    i_t = I0 * (1 + kappa) ** (b / (b - c))
    i_t *= (1 + kappa * np.exp((b - c) * (t - t0))) ** (-b / (b - c))
    i_t *= np.exp((b - c) * (t - t0))
    return i_t


def sum_sq_Bohner_et_al(t, infected_obs, b, c, S0=S0, I0=I0, t0=0):
    I_hat_t = i_t_Bohner_et_al(t, b, c, S0, I0, t0)
    val = 0
    val += ((I_hat_t - infected_obs) ** 2).mean()
    # print('sumsq:', val)
    return val


def minimize_wrapper(params, t, infected_obs):
    params = inv_repam(params)
    return sum_sq_Bohner_et_al(t, infected_obs, *params)


def inv_repam(params):
    return np.exp(params)


def repam(params):
    return np.log(params)


i_t = i_t_Bohner_et_al


betas = np.linspace(0.01, 2.0, num=50)
gamma = GAMMA
gammas = [0.25, 0.5, 1.0, 1.25]

for gamma in gammas:
    estimated_bs = []
    for beta in betas:
        print(f'beta: {beta}')
        true_params = [beta, gamma, S0, I0, R0]
        sir_params = SIRParams(*true_params)
        sir_model = SIR(params=sir_params)

        t_eval = np.array(range(50))
        t = t_eval
        s_sim, i_sim, r_sim = sir_model.simulate(t_eval)

        rand_scale = np.array([0.01, 0.01]) * 0
        uniform_rand = (np.random.random(size=2) * 2 - 1) * rand_scale
        start_params = np.array([beta, gamma]) + uniform_rand
        fit_params = repam(start_params)

        res = minimize(
            fun=minimize_wrapper,
            x0=np.array(fit_params),
            args=(t, i_sim),
            method='Nelder-Mead',
            options={'gtol': 1e-14}
        )
        print(res)
        params_hat = inv_repam(res.x)
        print(params_hat)
        estimated_bs.append(params_hat[0])

    p = plt.plot(betas, estimated_bs, label=f'gamma = {gamma}')
    plt.axvline(gamma, ls='--', color=p[0].get_color())


    def translator_candidate(beta, gamma):
        return np.fmax(beta + 0.5*(beta)/(beta - gamma), 0)

    # plt.plot(betas, translator_candidate(betas, gamma), color='k', label='candidate')


plt.xlabel('beta')
plt.ylabel('b')
plt.legend()
plt.title('Relation between beta and b from Bohner et. al.')
plt.savefig(f'plots/closed_form/beta_b_relation.png')
plt.close()


