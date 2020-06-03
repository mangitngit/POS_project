import csv
from statistics import mean


def read_moisture(path):
    data = []
    with open("database/rooms/"+path+"/moisture_data.csv", mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[-1]])
    file.close()

    return mean(data[0])
