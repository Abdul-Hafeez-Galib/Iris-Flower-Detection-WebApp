# Importing the libraries
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import pickle

# Importing data
df = pd.read_csv('Iris.csv')

X = np.array(df.iloc[:, 1:5])
y = np.array(df.iloc[:, 5])

# Label Encoding the Species Column
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Training the model
sv = SVC(kernel='linear').fit(X_train, y_train)

# Exporting to pickle file
pickle.dump(sv, open('iris.pkl', 'wb'))