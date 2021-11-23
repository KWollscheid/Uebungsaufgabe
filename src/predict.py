# predict model

import pickle
import numpy as np

mpg = pickle.load(open("data/models/model.pickle", "rb"))

# zylinder,ps,gewicht,beschleunigung,baujahr
x_query = np.array([8, 240, 3000, 10, 70])

print("Ein Auto mit {} Zylindern, {} PS, {} kg, Beschleunigung von {}(?), Baujahr 19{} wird vermutlich {} l/100km verbrauchen".format(
    x_query[0], x_query[1], x_query[2]*0.453592, x_query[3], x_query[4], (235.215/(mpg.predict(x_query.reshape(1, -1)))[0]).round(2)))
