from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

data = np.loadtxt('training.dat')

max = np.amax(data[:, 2])
min = np.amin(data[:, 2])
data[:, 2] = data[:, 2] / (max - min)

dataSort = data[:, 2]

dataSort = np.sort(dataSort)
med = dataSort[int(dataSort.shape[0] / 2)]
UQ = dataSort[int(3 * dataSort.shape[0] / 4)]
LQ = dataSort[int(dataSort.shape[0] / 4)]
IQR = UQ - LQ
bound = med + (1.5 * IQR)


x1 = data.shape[0]

anomaly = np.zeros(x1)

for i in range (0, x1):
    if(data[i, 2] > bound):
        anomaly[i] = 1

X = np.transpose([data[:, 1], data[:, 2]])

X_train, X_test, y_train, y_test = train_test_split(X, anomaly, test_size=0.5, random_state=0)
tr = tree.DecisionTreeClassifier()
y_pred = tr.fit(X_train, y_train).predict(X_test)

correct = 0
for i in range(0, y_pred.shape[0]):
    if(y_test[i] == y_pred[i]):
        correct = correct + 1

print("Accuracy: " + str(correct / y_pred.shape[0]))
time.sleep(3)

newData = np.loadtxt('final10112.dat')
max = np.amax(newData[:, 2])
min = np.amin(newData[:, 2])
newData[:, 2] = newData[:, 2] / (max - min)

newX = np.transpose([newData[:, 1], newData[:, 2]])
y_pred = tr.predict(newX)
a_file = open("predictSet1.dat", "w")

for i in range(0, y_pred.shape[0]):
    print(i)
    a_file.write(str(newX[i][0]) + " ")
    a_file.write(str(newX[i][1]) + " ")
    a_file.write(str(y_pred[i]) + "\n")
a_file.close()
