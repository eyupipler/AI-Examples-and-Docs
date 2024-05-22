
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer

url = "pima_indians_diabetes.csv"
names = ['preg', 'plas','pres','skin','test','mass','pedi', 'age','class']
dataframe = pd.read_csv(url, names=names)
dataframe.shape
dataframe.head


# In[2]:


array = dataframe.values
X = array[:, 0:8]
y = array[:,8]


# In[5]:


scalar = Normalizer()
rescaled = scalar.fit_transform(X)
np.set_printoptions(precision=3)
print(rescaled[:,0:5])

