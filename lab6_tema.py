import pymc as pm
import arviz as az

Y_values = [0, 5, 10]
theta_values = [0.2, 0.5]
n_samples = 10000

def calculate_posterior(Y, theta):
    with pm.Model() as model:
        prior_n = pm.Poisson('prior_n', mu=10)

        Y_binomial = pm.Binomial('Y_binomial', n=prior_n, p=theta, observed=Y)

        trace = pm.sample(n_samples)

        posterior_n = trace['prior_n']

    return posterior_n

all_posteriors = []
for Y in Y_values:
    for theta in theta_values:
        posterior_n = calculate_posterior(Y, theta)
        all_posteriors.append(posterior_n)

idata = az.convert_to_inference_data(all_posteriors)
az.plot_posterior(idata)
