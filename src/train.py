# Train Model

import numpy as np
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsRegressor

data = pd.read_csv("data/mpg.csv", sep=";", header=0)

data.head(5)

y = data["mpg"].values
X = data.drop(columns="mpg")

mpg = KNeighborsRegressor(n_neighbors=20)

mpg.fit(X, y)

filename = "data/models/model.pickle"
pickle.dump(mpg, open(filename, "wb"))
