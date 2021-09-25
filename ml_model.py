import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

data = load_iris()
X = pd.DataFrame(data['data'] , columns = data['feature_names'])

y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )

rfc = RandomForestClassifier()

rfc.fit(X_train, y_train)

y_pred = rfc.predict(X_test)

print("Model Performance : {:.2f}".format(accuracy_score(y_test, y_pred)))
print("Confusion Matrix : {}".format(confusion_matrix(y_test, y_pred)))

