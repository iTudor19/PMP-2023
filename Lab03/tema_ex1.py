import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

lambda_numar_clienti = 20
media_timp_comanda = 2
std_timp_comanda = 0.5
alpha_timp_pregatire = 1.5

numar_clienti = stats.poisson.rvs(mu=lambda_numar_clienti, size=10000)
timp_comanda = stats.norm.rvs(loc=media_timp_comanda, scale=std_timp_comanda, size=10000)
timp_pregatire = stats.expon.rvs(scale=alpha_timp_pregatire, size=10000)

media_numar_clienti = np.mean(numar_clienti)
media_timp_comanda = np.mean(timp_comanda)
media_timp_pregatire = np.mean(timp_pregatire)

deviatia_std_numar_clienti = np.std(numar_clienti)
deviatia_std_timp_comanda = np.std(timp_comanda)
deviatia_std_timp_pregatire = np.std(timp_pregatire)

print(f"Media numărului de clienți: {media_numar_clienti}")
print(f"Media timpului de comandă: {media_timp_comanda}")
print(f"Media timpului de pregătire: {media_timp_pregatire}")

print(f"Deviația standard a numărului de clienți: {deviatia_std_numar_clienti}")
print(f"Deviația standard a timpului de comandă: {deviatia_std_timp_comanda}")
print(f"Deviația standard a timpului de pregătire: {deviatia_std_timp_pregatire}")

fig, ax = plt.subplots(3, 1, figsize=(8, 10))
ax[0].hist(numar_clienti, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
ax[0].set_title('Distribuția numărului de clienți')
ax[1].hist(timp_comanda, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
ax[1].set_title('Distribuția timpului de comandă')
ax[2].hist(timp_pregatire, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
ax[2].set_title('Distribuția timpului de pregătire')
plt.tight_layout()
plt.show()
