import csv


def read_settings(path):
    """ Load setting data form CSV file """
    # "running, room, auto, thermostat, sprinklers, humidifier, windows"
    data = []
    with open("database/"+path, mode='r', newline='') as file:
        data.append([int(x) for x in list(csv.reader(file))[0]])
    file.close()

    return data[0]


def read_desired_values(path, room):
    """ Load desired values form CSV file """
    # "temperature, soil, air, CO2, O2"
    data = []
    with open("database/"+path, mode='r', newline='') as file:
        data.append([float(x) for x in list(csv.reader(file))[room-1]])
    file.close()

    return data[0]


def save_mean_values(path, samples, data):
    """ Write actual data to CSV file """
    # "temperature, soil, air, CO2, O2"
    reader = []
    with open("database/" + path, mode='r', newline='') as file:
        reader = list(csv.reader(file))
    file.close()

    if len(reader) >= samples:
        with open("database/" + path, mode='w', newline='') as file:
            reader[:-1] = reader[1:]
            reader[-1] = data
            writer = csv.writer(file)
            writer.writerows(reader)
        file.close()
    else:
        with open("database/" + path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        file.close()