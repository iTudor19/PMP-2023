import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):
    x, y = np.random.uniform(-1, 1, size=(2, N))
    inside = (x**2 + y**2) <= 1
    pi = inside.sum()*4/N
    error = abs((pi - np.pi) / pi) * 100
    return error

N_values = [10, 100, 1000, 10000, 100000]

num_simulations = 10

errors = []

for N in N_values:
    errors_for_N = []
    for _ in range(num_simulations):
        error = estimate_pi(N)
        errors_for_N.append(error)
    errors.append(errors_for_N)

mean_errors = np.mean(errors, axis=1)
std_dev_errors = np.std(errors, axis=1)

plt.errorbar(N_values, mean_errors, yerr=std_dev_errors, fmt='o-', capsize=5)
plt.xscale('log')
plt.xlabel('Numarul de puncte (N)')
plt.ylabel('Eroare (%)')
plt.title('Estimarea lui pi în functie de nr de puncte')
plt.grid(True)
plt.show()

#In urma rularii se observa cum eroarea scade si tine inspre 0 cu cat crestem valoarea lui N