from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib as plt

def within(id, s):
    for i in id:
        if i == s:
            return True
    return False

data = pd.read_csv("training-set.csv", sep=";")
ids = ["0"]
for i in range(0, data.shape[0]):
    if not (within(ids, data['meter_id'][i])):
        ids.append(data['meter_id'][i])
ids.pop(0)
print(ids)
a_file = open("stations.dat", "w")
for i in ids:
    a_file.write(i + "\n")

a_file.close()