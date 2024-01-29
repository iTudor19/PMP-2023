import pymc as pm
import numpy as np
import pandas as pd

# Incarca datele din fisierul CSV intr-un DataFrame
file_path = r"C:\Users\Tudor\Desktop\pmp-lab1\Sesiune\BostonHousing.csv"
housing_data = pd.read_csv(file_path)

# Extrage datele relevante
X = housing_data[["rm", "crim", "indus"]].values
y = housing_data["medv"].values

X_with_intercept = np.column_stack((np.ones(len(X)), X))

linear_model = pm.Model()

with linear_model:
    beta = pm.Normal("beta", mu=0, tau=1, size=X_with_intercept.shape[1])

    mu = pm.dot(X_with_intercept, beta)

    precision = pm.Gamma("precision", alpha=0.1, beta=0.1)

    likelihood = pm.Normal("likelihood", mu=mu, tau=precision, observed=y)