import numpy as np
import matplotlib.pyplot as plt

#vom presupune ca vom da cu banul de 15 ori

def posterior_grid(points, heads, tails, first_flag):
    grid = np.linspace(0, 1, points)
    prior = np.ones(points)
    likelihood = np.exp(np.log(grid) * heads + np.log(1 - grid) * tails)
    
    if first_flag:
        #penalizam probabilitatile sub 1/5.
        likelihood[grid < 0.2] = 0
    
    unnormalized_posterior = prior * likelihood
    posterior = unnormalized_posterior / unnormalized_posterior.sum()
    return grid, posterior

#date conectate pt prima aparitie a stemei la a 5a aruncare
data = np.concatenate([np.zeros(4), np.ones(1), np.zeros(8), np.ones(2)])
points = 100
h = data.sum()
t = len(data) - h

#calcul distributie a posteroiri
grid, posterior = posterior_grid(points, h, t, first_flag=True)

#vizualizam datele
plt.plot(grid, posterior, 'o-')
plt.title(f'heads = {h}, tails = {t}')
plt.yticks([])
plt.xlabel('θ')
plt.show()