# Guia 4) Tutotial de como ajustar distribuciones en python.(traduccion r a python)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli,norm


n= 100

s = norm(0,1).rvs(size=n) #distribucion normal entre 0 y 1, que arroja un avlor aleatorio de tamaño uno
h= norm(0,0.5*np.abs(5)).rvs(size = n)

sns.scatterplot(data=s)
sns.scatterplot(data=h)

D = np.random.binomial(n=1, p=0.5, size = n)
histar = h.copy()
histar[D==1] = np.nan