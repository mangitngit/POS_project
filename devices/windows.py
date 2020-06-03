import csv


def launch_o2(path, samples, data):
    reader = []
    with open("database/rooms/" + path + "/o2_data.csv", mode='r', newline='') as file:
        reader = list(csv.reader(file))
    file.close()

    if len(reader) >= samples:
        with open("database/rooms/" + path + "/o2_data.csv", mode='w', newline='') as file:
            reader[:-1] = reader[1:]
            reader[-1] = data
            writer = csv.writer(file)
            writer.writerows(reader)
        file.close()
    else:
        with open("database/rooms/" + path + "/o2_data.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        file.close()


def launch_co2(path, samples, data):
    reader = []
    with open("database/rooms/" + path + "/co2_data.csv", mode='r', newline='') as file:
        reader = list(csv.reader(file))
    file.close()

    if len(reader) >= samples:
        with open("database/rooms/" + path + "/co2_data.csv", mode='w', newline='') as file:
            reader[:-1] = reader[1:]
            reader[-1] = data
            writer = csv.writer(file)
            writer.writerows(reader)
        file.close()
    else:
        with open("database/rooms/" + path + "/co2_data.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        file.close()