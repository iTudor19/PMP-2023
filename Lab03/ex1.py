from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx

model = BayesianNetwork()
model.add_nodes_from(['Cutremur', 'Incendiu', 'Alarma'])

cpd_cutremur = TabularCPD(variable='Cutremur', variable_card=2, values=[[0.9995], [0.0005]])
cpd_incendiu = TabularCPD(variable='Incendiu', variable_card=2, values=[[0.99, 0.03], [0.01, 0.97]],
                         evidence=['Cutremur'], evidence_card=[2], state_names={'Incendiu': ['Fals', 'Adevarat'],
                                                                              'Cutremur': ['Fals', 'Adevarat']})
cpd_alarma = TabularCPD(variable='Alarma', variable_card=2,
                       values=[[0.9999, 0.95, 0.97, 0.98],
                               [0.0001, 0.05, 0.03, 0.02]],
                       evidence=['Cutremur', 'Incendiu'], evidence_card=[2, 2],
                       state_names={'Alarma': ['Fals', 'Adevarat'],
                                    'Cutremur': ['Fals', 'Adevarat'],
                                    'Incendiu': ['Fals', 'Adevarat']})

model.add_cpds(cpd_cutremur, cpd_incendiu, cpd_alarma)
