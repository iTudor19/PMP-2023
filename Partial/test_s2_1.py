import numpy as np
import matplotlib.pyplot as plt

# Alegem parametrii distributiei normale
miu = 10
sigma = 3 

# Generam 200 de timpuri medii de asteptare folosind distributia normala
timp_mediu_asteptare = np.random.normal(miu, sigma, 200)

# Afisam histograma timpilor medii de asteptare
plt.hist(timp_mediu_asteptare, bins=20, density=True, alpha=0.7, color='blue')
plt.title('Histograma Timpilor Medii de Așteptare')
plt.xlabel('Timp Mediu de Așteptare')
plt.ylabel('Frecvență relativă')
plt.show()