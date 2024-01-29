import pymc as pm
import numpy as np
from scipy.stats import hdi
import pandas as pd

file_path = r'C:\Users\Tudor\Desktop\pmp-lab1\Sesiune\BostonHousing.csv'
df = pd.read_csv(file_path, usecols=['medv', 'rm', 'crim', 'indus'])

#definire date
X = df[['rm', 'crim', 'indus']].values
y = df['medv'].values

#standardizare date
X_standardized = (X - X.mean(axis=0)) / X.std(axis=0)
y_standardized = (y - y.mean()) / y.std()

#adaugarea unei coloane de constate
X_with_intercept = np.column_stack((np.ones(X_standardized.shape[0]), X_standardized))

#definire model
linear_model = pm.Model()
with linear_model:
    #parametri coeficienti de regresie
    beta = pm.Normal('beta', mu=0, tau=1, size=X_with_intercept.shape[1])

    #model liniar
    mu = pm.Dot('mu', X_with_intercept, beta)

    #precizie erori
    sigma = pm.HalfNormal('sigma', tau=1)

    #distributia normala
    y_obs = pm.Normal('y_obs', mu=mu, tau=1/sigma**2, value=y_standardized, observed=True)
    y_pred = pm.Normal('y_pred', mu=mu, tau=1/sigma**2)

#antrenare folosind mcmc
mcmc = pm.MCMC(linear_model)
mcmc.sample(10000, burn=1000)

y_pred_samples = mcmc.trace('y_pred')[:]

#calcul interval de predictie 50% HDI
prediction_hdi = hdi(y_pred_samples, 0.5)

#afisare rezultate
print(f"Interval de predicție de 50% HDI: {prediction_hdi}")
