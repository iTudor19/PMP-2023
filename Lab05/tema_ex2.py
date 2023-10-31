import numpy as np
import pymc as pm
import pandas as pd

data = pd.read_csv('trafic.csv')

with pm.Model() as traffic_model:
    alpha = 1
    beta = 1

    lambda_ = pm.Gamma("lambda_", alpha, beta)

    traffic = pm.Poisson("traffic", lambda_, observed=data['nr_masini'].values)

    growth_effect = pm.switch(pm.or_(pm.eq(data['minut'] % 1440, 420), pm.eq(data['minut'] % 1440, 960)), 0.2 * traffic, 0)

    decay_effect = pm.switch(pm.or_(pm.eq(data['minut'] % 1440, 480), pm.eq(data['minut'] % 1440, 1140)), -0.2 * traffic, 0)

    observed_traffic = traffic + growth_effect + decay_effect

    map_estimate = pm.find_MAP(model=traffic_model)

lambda_values = map_estimate['lambda_']
sorted_indices = np.argsort(lambda_values)

print("Cele mai probabile cinci intervale de timp și valorile asociate ale lui λ sunt:")
for i in range(5):
    index = sorted_indices[-(i+1)]
    print(f"Intervalul de timp: {data['minut'][index]} - {data['minut'][index] + 1}, Valoarea lui λ: {lambda_values[index]}")
