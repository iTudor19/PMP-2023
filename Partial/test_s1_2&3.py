import random
import matplotlib.pyplot as plt
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination

# Reteaua Bayesiana
model = BayesianModel([('Jucator_curent', 'Steme_p0'), 
                       ('Jucator_curent', 'Steme_p1'),
                       ('Steme_p0', 'Castiguri_p0'),
                       ('Steme_p1', 'Castiguri_p1')])
# Adaugam Fata_monedei in reteaua noastra pt 3.
model.add_edge('Jucator_curent', 'Fata_monedei')
model.add_edge('Steme_p0', 'Fata_monedei')
model.add_edge('Steme_p1', 'Fata_monedei')

# Definire cpd-uri
cpd_jucator_curent = ParameterEstimator(model).estimate_cpd('Jucator_curent')
model.add_cpds(cpd_jucator_curent)

cpd_steme_p0 = ParameterEstimator(model).estimate_cpd('Steme_p0')
model.add_cpds(cpd_steme_p0)

cpd_steme_p1 = ParameterEstimator(model).estimate_cpd('Steme_p1')
model.add_cpds(cpd_steme_p1)

cpd_castiguri_p0 = ParameterEstimator(model).estimate_cpd('Castiguri_p0')
model.add_cpds(cpd_castiguri_p0)

cpd_castiguri_p1 = ParameterEstimator(model).estimate_cpd('Castiguri_p1')
model.add_cpds(cpd_castiguri_p1)

# Cpd pt a vedea ce fata monezii pt 3.
cpd_fata_monedei = ParameterEstimator(model).estimate_cpd('Fata_monedei')
model.add_cpds(cpd_fata_monedei)

# Codul pe care il avem si la 1.
def arunca_moneda(probabilitate):
    return random.choices([0, 1], weights=[1 - probabilitate, probabilitate])[0]

numar_simulari=20000

def simuleaza_joc(numar_simulari):
    castiguri_p0 = 0
    castiguri_p1 = 0

    for _ in range(numar_simulari):
        steme_p0= 0
        steme_p1= 0
        jucator_curent = random.choice([0, 1])

        if jucator_curent == 0:
            steme_p0 = arunca_moneda(1/3)
            if steme_p0 == 1:
                ct=steme_p0 + 1
                while ct>0:
                    steme_p1 += arunca_moneda(1/2)
                    ct=ct-1
            if(steme_p0>=steme_p1):
                castiguri_p0+=1
            else:
                castiguri_p1+=1

        else:

            steme_p1 = arunca_moneda(1/2)
            if steme_p1 == 1:
                ct=steme_p1 + 1
                while ct>0:
                    steme_p0 += arunca_moneda(1/3)
                    ct=ct-1
            if(steme_p1>=steme_p0):
                castiguri_p1+=1
            else:
                castiguri_p0+=1

    if castiguri_p0>castiguri_p1:
        print("p0")
    else:
        print("p1")    

# Efectuam inferente pentru Jucator_curent=0 și steme_p1=0            
inference = VariableElimination(model)
result_jucator0_steme1 = inference.query(variables=['Fata_monedei'], evidence={'Jucator_curent': 0, 'Steme_p1': 0})

# Efectuam inferente pentru jucator_curent=1 și steme_p0=0
result_jucator1_steme0 = inference.query(variables=['Fata_monedei'], evidence={'Jucator_curent': 1, 'Steme_p0': 0})

# Suma probabilitătilor
probabilitati_agregate = result_jucator0_steme1.values + result_jucator1_steme0.values

if probabilitati_agregate > 0.5:
    print("stema")
else:
    print("nu stema")