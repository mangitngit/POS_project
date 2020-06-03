import csv
from statistics import mean


def read_temperature(path):
    data = []
    with open("database/rooms/"+path+"/temp_data.csv", mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[-1]])
    file.close()

    return mean(data[0])


def read_humidity(path):
    data = []
    with open("database/rooms/"+path+"/humidity_data.csv", mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[-1]])
    file.close()

    return mean(data[0])