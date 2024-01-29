import numpy as np
from scipy.stats import linregress
import pandas as pd

file_path = r'C:\Users\Tudor\Desktop\pmp-lab1\Sesiune\BostonHousing.csv'
df = pd.read_csv(file_path, usecols=['medv', 'rm', 'crim', 'indus'])

X = df[['rm', 'crim', 'indus']].values
y = df['medv'].values

#standardizam datele pentru a avea o convergenta mai buna
X_standardized = (X - X.mean(axis=0)) / X.std(axis=0)
y_standardized = (y - y.mean()) / y.std()

#adaugare coloana pentru intercept
X_with_intercept = np.column_stack((np.ones(X_standardized.shape[0]), X_standardized))

#calculam regresia lineara
result = linregress(X_with_intercept, y_standardized)

#afisam rezultatele
print(f"Intercept (alpha): {result.intercept}")
print(f"Coeficienți (beta): {result.slope[1:]}")

#calcul interval de incredere
alpha_ci = [result.intercept - 1.96 * result.stderr_intercept, result.intercept + 1.96 * result.stderr_intercept]
beta_ci = [(result.slope[i] - 1.96 * result.stderr[i + 1], result.slope[i] + 1.96 * result.stderr[i + 1]) for i in range(len(result.slope))]

#afisare interval de incredere
print(f"Interval de încredere 95% pentru intercept (alpha): {alpha_ci}")
for i, ci in enumerate(beta_ci):
    print(f"Interval de încredere 95% pentru coeficientul beta_{i + 1}: {ci}")


#coeficientul cu magnitudinea cea mai mare va influenta cel mai mult rezultatul
