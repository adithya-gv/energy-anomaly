import numpy as np
import pandas as pd
import time

data = pd.read_csv("training-set.csv", sep=";")
stations = np.loadtxt('stations.dat', dtype=str)
times = np.loadtxt('times.dat')

a_file = open("data.dat", "w")

for i in stations:
    print(i)
    for j in range (0, data.shape[0]):
        if i == str(data['meter_id'][j]):
            a = str(data['meter_id'][j])
            b = -1
            if ("_" in i):
                b = a.index("_")
            a_file.write(a[b+1:] + " ")
            a_file.write(str(times[j]) + " ")
            a_file.write(str(data['Values'][j]) + "\n")

a_file.close()

