import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def posterior_grid(grid_points=50, heads=6, tails=9, prior=None):
   
    grid = np.linspace(0, 1, grid_points)
    
    if prior is None:
        prior = np.repeat(1/grid_points, grid_points)
    
    likelihood = stats.binom.pmf(heads, heads + tails, grid)
    posterior = likelihood * prior
    posterior /= posterior.sum()
    
    return grid, posterior

data = np.repeat([0, 1], (10, 3))
points = 10
h = data.sum()
t = len(data) - h

grid_uniform, posterior_uniform = posterior_grid(points, h, t)
plt.plot(grid_uniform, posterior_uniform, 'o-', label='Prior Uniform')

prior_binary = (grid_uniform <= 0.5).astype(int)
grid_binary, posterior_binary = posterior_grid(points, h, t, prior=prior_binary)
plt.plot(grid_binary, posterior_binary, 'o-', label='Prior Binary (<= 0.5)')

prior_abs = abs(grid_uniform - 0.5)
grid_abs, posterior_abs = posterior_grid(points, h, t, prior=prior_abs)
plt.plot(grid_abs, posterior_abs, 'o-', label='Prior Abs(grid - 0.5)')

plt.title(f'heads = {h}, tails = {t}')
plt.yticks([])
plt.xlabel('θ')
plt.legend()
plt.show()
