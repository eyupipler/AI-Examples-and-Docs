
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.preprocessing import Binarizer
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

url = "pima_indians_diabetes.csv"
names = ['preg', 'plas','pres','skin','test','mass','pedi', 'age','class']
dataframe = pd.read_csv(url, names=names)
dataframe.shape
dataframe.head


# In[2]:


array = dataframe.values
X = array[:, 0:8]
y = array[:,8]
seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(base_estimator=cart, n_estimators= num_trees, random_state=seed)
results = model_selection.cross_val_score(model, X, y,cv = kfold)
print(results.mean())


# In[3]:


model2 = DecisionTreeClassifier()
result2 = model_selection.cross_val_score(model2, X, y,cv = kfold)
print(result2.mean())


# In[4]:


from sklearn.ensemble import RandomForestClassifier
max_feature = 3
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model3 = RandomForestClassifier(n_estimators = num_trees, max_features= max_feature)
result3 = model_selection.cross_val_score(model3, X, y,cv = kfold)
print(result3.mean())

