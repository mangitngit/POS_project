import csv
from statistics import mean


def read_o2(path):
    data = []
    with open("database/rooms/"+path+"/o2_data.csv", mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[-1]])
    file.close()

    return mean(data[0])


def read_co2(path):
    data = []
    with open("database/rooms/"+path+"/co2_data.csv", mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[-1]])
    file.close()

    return mean(data[0])
