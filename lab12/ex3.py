import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def metropolis_beta_binomial(alpha, beta, draws=10000):
    func = stats.beta(alpha, beta)
    
    trace = np.zeros(draws)
    old_x = func.mean()
    old_prob = func.pdf(old_x)
    delta = np.random.normal(0, 0.5, draws)
    
    for i in range(draws):
        new_x = old_x + delta[i]
        new_prob = func.pdf(new_x)
        
        acceptance = new_prob / old_prob
        if acceptance >= np.random.random():
            trace[i] = new_x
            old_x = new_x
            old_prob = new_prob
        else:
            trace[i] = old_x
    
    return trace

alpha = 2
beta = 5

trace_metropolis = metropolis_beta_binomial(alpha, beta)

grid_points = 50
heads = 6
tails = 9
grid = np.linspace(0, 1, grid_points)
prior = stats.beta(alpha, beta).pdf(grid)
likelihood = stats.binom.pmf(heads, heads + tails, grid)
posterior_grid = likelihood * prior
posterior_grid /= posterior_grid.sum()

x = np.linspace(0.01, 0.99, 100)
y_true = stats.beta(alpha, beta).pdf(x)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y_true, 'C1-', lw=3, label='True distribution')
plt.hist(trace_metropolis[trace_metropolis > 0], bins=25, density=True, label='Metropolis Estimated distribution')
plt.xlabel('x')
plt.ylabel('pdf(x)')
plt.yticks([])
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(grid, posterior_grid, 'C1-', lw=3, label='True distribution (grid)')
plt.xlabel('x')
plt.ylabel('pdf(x)')
plt.yticks([])
plt.legend()

plt.tight_layout()
plt.show()
