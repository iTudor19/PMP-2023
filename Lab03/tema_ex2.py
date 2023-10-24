import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

lambda_numar_clienti = 20
media_timp_comanda = 2
std_timp_comanda = 0.5

def binary_search():
    left = 0
    right = 15
    target_probability = 0.95

    while right - left > 1e-5:
        alpha_timp_pregatire = (left + right) / 2
        timp_pregatire = stats.expon.rvs(scale=alpha_timp_pregatire, size=10000)

        total_time = media_timp_comanda + timp_pregatire
        exceeded_time_prob = np.mean(total_time > 15)

        if exceeded_time_prob > 1 - target_probability:
            right = alpha_timp_pregatire
        else:
            left = alpha_timp_pregatire

    return (left + right) / 2

alpha_maxim_cautare_binar = binary_search()

timp_pregatire_gasit = stats.expon.rvs(scale=alpha_maxim_cautare_binar, size=10000)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(timp_pregatire_gasit, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
ax.set_title('Distribuția timpului de pregătire cu valoarea găsită pentru alpha')
plt.show()
