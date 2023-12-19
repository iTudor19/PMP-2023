import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import seaborn as sns

means = [5, 0, -5]
std_devs = [2, 2, 2]
n_cluster = [200, 150, 150]
n_total = sum(n_cluster)
mix = np.concatenate([np.random.normal(means[i], std_devs[i], n_cluster[i]) for i in range(len(means))])

num_components = [2, 3, 4]

for n_components in num_components:
    model = GaussianMixture(n_components=n_components, random_state=42)
    model.fit(mix.reshape(-1, 1))

    responsibilities = model.predict_proba(mix.reshape(-1, 1))

    plt.figure(figsize=(8, 5))
    plt.title(f'Modelul de mixtură cu {n_components} componente')

    sns.histplot(mix, bins=30, kde=True, color='blue', label='Date reale')

    for i in range(n_components):
        plt.plot(mix, responsibilities[:, i] * n_total, label=f'Componenta {i + 1}')

    plt.legend()
    plt.show()
