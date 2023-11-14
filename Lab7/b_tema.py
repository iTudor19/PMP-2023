import numpy as np
import pymc as pm
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/Tudor/Desktop/pmp-lab1/PMP-2023-main/Lab7/auto-mpg.csv'
df = pd.read_csv(file_path)

CP = df['CP'].values
mpg = df['mpg'].values

with pm.Model():
    a = pm.Normal('a', mu=0, tau=0.0001)
    b = pm.Normal('b', mu=0, tau=0.0001)

    @pm.Deterministic
    def model(CP=CP, a=a, b=b):
        return (a + b * CP)

    observed = pm.Normal('observed', mu=model, tau=1.0, value=mpg, observed=True)

    mcmc = pm.MCMC()
    mcmc.sample(iter=10000, burn=1000)

    a_samples = mcmc.trace('a')[:]
    b_samples = mcmc.trace('b')[:]