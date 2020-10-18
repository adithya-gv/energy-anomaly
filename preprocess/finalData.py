import pandas as pd

data = pd.read_csv("training-set.csv", sep=";")

a_file = open("final10112.dat", "w")

for i in range (0, data.shape[0]):
    print(i)
    if str(data['meter_id'][i]) == "38_10112":
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
        timeCount = (int(a[11:13]) * 60) + int(a[14:16]) + (int(a[20:22]) * 60)
        if str(data['Values'][i]) != "nan":
            a_file.write(str(dayCount) + " ")
            a_file.write(str(timeCount) + " ")
            a_file.write(str(data['Values'][i]) + "\n")

a_file.close()
