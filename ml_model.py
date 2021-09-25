# Library Imports
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pickle

# Loading Data - Note : I've used a public dataset available with sklearn for convenience and reproducibility 
# To read more about the Iris dataset : https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
data = load_iris()

# Converting the "data" dictionary to a DataFrame for simplicity 
X = pd.DataFrame(data['data'] , columns = data['feature_names'])
# Target Column
y = data['target']

# Splitting data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )

# Creating/ Initialising the Random Forest Classifier Classifier
rfc = RandomForestClassifier()

# Fitting the data to the Algorithm / Model
rfc.fit(X_train, y_train)

# Predicting on Test Data
y_pred = rfc.predict(X_test)

# Checking the Accuracy and Confusion Matrix to evaluate performance
print("Model Performance : {:.2f}".format(accuracy_score(y_test, y_pred)))
print("Confusion Matrix : {}".format(confusion_matrix(y_test, y_pred)))

# Saving the model for future usage
pickle.dump(rfc, open("rfc_model.sav", 'wb'))
