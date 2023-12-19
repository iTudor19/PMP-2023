import numpy as np
import arviz as az
import matplotlib.pyplot as plt

means = [5, 0, -5]
std_devs = [2, 2, 2]
n_cluster = [200, 150, 150]
n_total = sum(n_cluster)

mix = np.concatenate([np.random.normal(means[i], std_devs[i], n_cluster[i]) for i in range(len(means))])

az.plot_kde(mix)
plt.title('Distributie mixtă de 3 Gaussiene')
plt.show()
