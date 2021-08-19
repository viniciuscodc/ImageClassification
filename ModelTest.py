import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd
                                
trained_model = pd.read_pickle('./Data/trainedModel.pickle')
x_test = pd.read_pickle('./Data/x_test.pickle')
y_test = pd.read_pickle('./Data/y_test.pickle')

y_pred=trained_model.predict(x_test)

accuracy_percent = accuracy_score(y_pred,y_test)*100

print("The predicted Data is :")

print(y_pred)

print("The actual data is:")

print(np.array(y_test))

print(f"The model is {accuracy_percent:.2f}% accurate")
