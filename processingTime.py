import pandas as pd

data = pd.read_csv("training-set.csv", sep=";")
timeSet = []

a_file = open("times.dat", "w")

for i in range (0, data.shape[0]):
    a = str(data['Timestamp'][i])
    time = int(a[11:13]) * 60 + int(a[14:16]) + int(a[20:22]) * 60
    timeSet.append(time)
    a_file.write(str(time) + "\n")

a_file.close()