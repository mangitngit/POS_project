import random
from numpy import random as np_rd


def temperature(data, thermo, change_value):
    """ Temperature change calculation """
    if thermo:  # if is working
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.1, 0.5)
    else:
        if change_value:
            data -= change_value
        else:
            data -= random.uniform(0.1, 0.5)

    # [data, np_dt] <- data is for mean, np_dt is for csv file with 5 sensors
    # prevents to low temperature drop
    return [data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]] if data > 10 else [10, np_rd.normal(loc=10, scale=0.04, size=(1, 5))[0]]


def humidity(data, humidi, change_value):
    """ Humidity change calculation """
    if humidi:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.3, 0.8)
    else:
        data -= random.uniform(0.3, 0.8)

    return [data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]] if data > 15 else [15, np_rd.normal(loc=15, scale=0.04, size=(1, 5))[0]]


def moisture(data, moistu, change_value):
    """ Moisture change calculation """
    if moistu:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.2, 0.7)
    else:
        data -= random.uniform(0.2, 0.5)

    return [data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]] if data > 0 else [0, [0, 0, 0, 0, 0]]


def o2(data, air, change_value):
    """ O2 change calculation """
    if air:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.01, 0.03)
    else:
        data -= random.uniform(0.01, 0.03)

    return [data, np_rd.normal(loc=data, scale=0.0005, size=(1, 2))[0]] if data > 0 else [0, [0, 0, 0, 0, 0]]


def co2(data, air, change_value):
    """ CO2 change calculation """
    if air:
        if change_value:
            data -= change_value
        else:
            data -= random.uniform(0.01, 0.03)
    else:
        data += random.uniform(0.01, 0.03)

    return [data, np_rd.normal(loc=data, scale=0.0005, size=(1, 2))[0]] if data > 0 else [0, [0, 0, 0, 0, 0]]
