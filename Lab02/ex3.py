import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

num_aruncari = 10
num_simulari = 100
prob_stema = 0.3
rezultate_posibile = ['s', 'b']
numar_rezultate = {'ss': [], 'sb': [], 'bs': [], 'bb': []}

for _ in range(num_simulari):
    rezultat_experiment = ''
    for _ in range(num_aruncari):
        moneda1 = np.random.choice(rezultate_posibile)
        moneda2 = np.random.choice(rezultate_posibile, p=[1 - prob_stema, prob_stema])
        rezultat_experiment += moneda1 + moneda2
    for rezultat_posibil in numar_rezultate:
        numar_rezultate[rezultat_posibil].append(rezultat_experiment.count(rezultat_posibil))

distributie_ss = np.array(numar_rezultate['ss'])
distributie_sb = np.array(numar_rezultate['sb'])
distributie_bs = np.array(numar_rezultate['bs'])
distributie_bb = np.array(numar_rezultate['bb'])

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(distributie_ss, bins=np.arange(0, num_aruncari + 2) - 0.5, density=True, alpha=0.7)
plt.title('Distributia ss')
plt.xlabel('Numar ss')
plt.ylabel('Probabilitate')

plt.subplot(2, 2, 2)
plt.hist(distributie_sb, bins=np.arange(0, num_aruncari + 2) - 0.5, density=True, alpha=0.7)
plt.title('Distributia sb')
plt.xlabel('Numar sb')
plt.ylabel('Probabilitate')

plt.subplot(2, 2, 3)
plt.hist(distributie_bs, bins=np.arange(0, num_aruncari + 2) - 0.5, density=True, alpha=0.7)
plt.title('Distributia bs')
plt.xlabel('Numar bs')
plt.ylabel('Probabilitate')

plt.subplot(2, 2, 4)
plt.hist(distributie_bb, bins=np.arange(0, num_aruncari + 2) - 0.5, density=True, alpha=0.7)
plt.title('Distributia bb')
plt.xlabel('Numar bb')
plt.ylabel('Probabilitate')

plt.tight_layout()
plt.show()
