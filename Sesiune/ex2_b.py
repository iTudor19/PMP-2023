import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def posterior_grid(grid_points=50, heads=6, tails=9):
    """
    A grid implementation for the coin-flipping problem
    """
    grid = np.linspace(0, 1, grid_points)
    prior = np.repeat(1/grid_points, grid_points)
    #modelam aparitia stemei la a 5a aruncare
    likelihood = stats.geom.pmf(5, grid)
    for _ in range(heads - 1):
        likelihood = np.convolve(likelihood, stats.geom.pmf(1, grid), mode='full')[:grid_points]
    for _ in range(tails):
        likelihood = np.convolve(likelihood, stats.geom.pmf(0, grid), mode='full')[:grid_points]
    posterior = likelihood * prior
    posterior /= posterior.sum()
    return grid, posterior

def find_mode(grid, posterior):
    """
    Find the mode (value with the highest frequency) of the posterior distribution
    """
    return grid[np.argmax(posterior)]

data = np.repeat([0, 1], (10, 3))
points = 10
h = data.sum()
t = len(data) - h

#calculare distributie a priori
grid, posterior = posterior_grid(points, h, t)

mode_theta = find_mode(grid, posterior)

#vizualizare date
plt.plot(grid, posterior, 'o-')
plt.title(f'Prima stema la a 5-a aruncare - heads = {h}, tails = {t}')
plt.axvline(x=mode_theta, color='r', linestyle='--', label=f'Mode: θ = {mode_theta:.3f}')
plt.yticks([])
plt.xlabel('θ')
plt.legend()
plt.show()
