import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

lambda1 = 4
lambda2 = 6
prob_1 = 0.4
samples = 10000
servire_1 = np.random.choice([True, False], size=samples, p=[prob_1, 1 - prob_1])
timp_servire = np.zeros(samples)

for i in range(samples):
    if servire_1[i]:
        timp_servire[i] = stats.expon.rvs(scale=1/lambda1)
    else:
        timp_servire[i] = stats.expon.rvs(scale=1/lambda2)

media_X = np.mean(timp_servire)
deviatia_standard_X = np.std(timp_servire)

print(f"Media: {media_X}")
print(f"Deviația standard: {deviatia_standard_X}")

az.plot_posterior({'X': timp_servire})
plt.show()
