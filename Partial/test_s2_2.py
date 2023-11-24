import pymc
import numpy as np

# Genereaza date sintetice pentru exemplificare
np.random.seed(1)
timp_mediu_asteptare_sintetic = np.random.normal(10, 3, 200)

# Definirea modelului în Pymc
with pymc.Model() as model:
    
    # Folosim o distribuție normală pentru a priori a 
    # măritimii medii (miu). Aceasta are o medie de 0 și 
    # o varianță inversă mică (tau=0.001). Alegerea unei 
    # varianțe inverse mici ajută la exprimarea faptului 
    # că nu avem cunostinte anterioare semnificative 
    # despre măritimea medie.
    miu = pymc.Normal('miu', mu=0, tau=0.001)

    # Alegem o distribuție uniformă pentru a priori 
    # a deviației standard (sigma). Aceasta 
    # este o alegere comună pentru distribuții 
    # neinformative.
    sigma = pymc.Uniform('sigma', lower=0, upper=10)

    # Distributie a posteriori pentru timpul mediu de asteptare
    timp_mediu_asteptare = pymc.Normal('timp_mediu_asteptare', mu=miu, sd=sigma, observed=timp_mediu_asteptare_sintetic)
