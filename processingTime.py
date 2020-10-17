import pandas as pd

data = pd.read_csv("training-set.csv", sep=";")
timeSet = []

a_file = open("times.dat", "w")

for i in range (0, data.shape[0]):
    a = str(data['Timestamp'][i])
    dayCount = 0
    time1 = a[5:7]
    if(time1 in ["01", "03", "05", "07", "08", "10", "12"]):
        dayCount = dayCount + 31 * int(time1)
    elif(time1 in ["02"]):
        dayCount = dayCount + 28 * int(time1)
    else:
        dayCount = dayCount + 30 * int(time1)
    dayCount = dayCount + int(a[8:10])
    timeSet.append(dayCount)
    a_file.write(str(dayCount) + "\n")

a_file.close()