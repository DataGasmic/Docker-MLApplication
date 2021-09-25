# Import Packages
import pickle
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# Loading Saved Model
rfc_model = pickle.load(open("rfc_model.sav","rb"))

# Loading Data to get Target Name Mapping
data = load_iris()
target_names = data['target_names']
output_mapper = (dict(zip(set(data['target']),target_names)))

# Predicting based on a set of inputs
def predict_flower_class(sl, sw, pl, pw ):
    return output_mapper[rfc_model.predict(np.array([[sl,sw,pl,pw]]))[0]]

# Test the function for formatting
# print(predict_flower_class(5.8,2.8,5.1,2.4))
