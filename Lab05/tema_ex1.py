import numpy as np
import pymc as pm
import pandas as pd

data = pd.read_csv('trafic.csv')

with pm.Model() as traffic_model:
    lambda_ = 1.5

    traffic = pm.Poisson("traffic", lambda_, observed=data['nr_masini'].values)

    growth_effect = pm.switch(pm.or_(pm.eq(data['minut'] % 1440, 420), pm.eq(data['minut'] % 1440, 960)), 0.2 * traffic, 0)

    decay_effect = pm.switch(pm.or_(pm.eq(data['minut'] % 1440, 480), pm.eq(data['minut'] % 1440, 1140)), -0.2 * traffic, 0)

    observed_traffic = traffic + growth_effect + decay_effect

    map_estimate = pm.find_MAP(model=traffic_model)
    print(map_estimate)
