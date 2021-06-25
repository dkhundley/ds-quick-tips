# Importing the required Python libraries
import numpy as np
import pandas as pd
import pickle
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Loading the iris dataset from Scikit-Learn
iris = datasets.load_iris()

# Converting the iris dataset into a Pandas DataFrame
df_iris = pd.DataFrame(data = np.c_[iris['data'], iris['target']],
											 columns = iris['feature_names'] + ['target'])

# Separating the training dataset (X) from the predictor value (y)
X = df_iris.drop(columns = ['target'])
y = df_iris[['target']]

# Instantiating a Logistic Regression (LR) model
lr_model = LogisticRegression()

# Fitting the dataset to the LR model
lr_model.fit(X, y)

# Saving the model to a serialized .pkl file
pkl_filename = "../models/iris_model.pkl"
with open(pkl_filename, 'wb') as file:
	pickle.dump(lr_model, file)