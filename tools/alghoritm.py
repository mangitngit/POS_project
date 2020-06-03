import random
from numpy import random as np_rd


def temperature(data, thermo, change_value):
    if thermo:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.1, 0.5)
    else:
        if change_value:
            data -= change_value
        else:
            data -= random.uniform(0.1, 0.5)

    return data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]


def humidity(data, humidi, change_value):
    if humidi:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.3, 1.2)
    else:
        data -= random.uniform(0.3, 0.8)

    return data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]


def moisture(data, moistu, change_value):
    if moistu:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.7, 1.2)
    else:
        data -= random.uniform(0.2, 0.5)

    return data, np_rd.normal(loc=data, scale=0.04, size=(1, 5))[0]


def o2(data, air, change_value):
    if air:
        if change_value:
            data += change_value
        else:
            data += random.uniform(0.01, 0.03)
    else:
        data -= random.uniform(0.01, 0.03)

    return data, np_rd.normal(loc=data, scale=0.0005, size=(1, 2))[0]


def co2(data, air, change_value):
    if air:
        if change_value:
            data -= change_value
        else:
            data -= random.uniform(0.01, 0.03)
    else:
        data += random.uniform(0.01, 0.03)

    return data, np_rd.normal(loc=data, scale=0.0005, size=(1, 2))[0]
