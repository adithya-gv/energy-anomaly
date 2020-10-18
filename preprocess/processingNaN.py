import pandas as pd
import numpy as np

data = np.loadtxt('data.dat', dtype=str)
a_file = open("data2.dat", "w")

for i in range(0, data.shape[0]):
    print(i)
    if (not (data[i][2] == "nan")):
        a_file.write(str(data[i][0]) + " ")
        a_file.write(str(data[i][1]) + " ")
        a_file.write(str(data[i][2]) + "\n")
a_file.close()