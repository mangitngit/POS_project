import time
import numpy as np
from tools import alghoritm
from tools.read_save_data import read_settings, read_desired_values, save_mean_values
from sensors import RS485, RH_010_GN, LB_856
from devices import HC35_3S, humidifier, HUNTER, windows

import matplotlib.pyplot as plt


class GreenHouse:
    def __init__(self):
        self.running = 1
        self.room = 1
        self.set_automatic = 1
        self.set_thermostat = 0
        self.set_humidifier = 0
        self.set_sprinklers = 0
        self.set_windows = 0

        self.settings_path = "settings.csv"
        self.desired_path = "rooms_desired_values.csv"
        self.save_mean_path = "mean_data.csv"
        self.data_path = "room" + str(self.room)
        self.samples_size = 72
        self.waiting_time = 10

        self.data = []
        self.settings = []
        self.desired_values = []

        self.read_data()
        self.read_desired_values()

        self.read_settings_values()
        self.set_settings_values()

    def loop(self):
        counter = 0
        while self.running:
            time.sleep(0.1)
            self.read_settings_values()
            self.set_automatic = self.settings[2]
            self.read_data()

            if self.set_automatic and counter >= self.waiting_time:
                counter = 0
                self.auto()
            elif not self.set_automatic:
                self.set_settings_values()
                counter = 0

            self.launch_devices()
            save_mean_values(self.save_mean_path, self.samples_size, self.data)

            self.plot()
            counter += 1

    def plot(self):
        plt.clf()
        plt.plot(self.data)
        plt.draw()

    def auto(self):
        self.set_thermostat = 1 if self.desired_values[0] > self.data[0] else 0
        self.set_humidifier = 1 if self.desired_values[1] > self.data[1] else 0
        self.set_sprinklers = 1 if self.desired_values[2] > self.data[2] else 0
        self.set_windows = 1 if (self.desired_values[3] > self.data[3] or self.desired_values[4] < self.data[4]) else 0

    def launch_devices(self):
        self.data[0], temp = alghoritm.temperature(self.data[0], self.set_thermostat, 0)
        HC35_3S.launch(self.data_path, self.samples_size, temp)

        self.data[1], humidi = alghoritm.humidity(self.data[1], self.set_humidifier, 0)
        humidifier.launch(self.data_path, self.samples_size, humidi)

        self.data[2], moistu = alghoritm.moisture(self.data[2], self.set_sprinklers, 0)
        HUNTER.launch(self.data_path, self.samples_size, moistu)

        self.data[3], o2 = alghoritm.o2(self.data[3], self.set_windows, 0)
        windows.launch_o2(self.data_path, self.samples_size, o2)

        self.data[4], co2 = alghoritm.co2(self.data[4], self.set_windows, 0)
        windows.launch_co2(self.data_path, self.samples_size, co2)

    def read_data(self):
        temperature_data = RS485.read_temperature(self.data_path)
        humidity_data = RS485.read_humidity(self.data_path)
        moisture_data = RH_010_GN.read_moisture(self.data_path)
        o2_data = LB_856.read_o2(self.data_path)
        co2_data = LB_856.read_co2(self.data_path)

        self.data = [temperature_data, humidity_data, moisture_data, o2_data, co2_data]

    def read_desired_values(self):
        self.desired_values = read_desired_values(self.desired_path, self.room)

    def read_settings_values(self):
        self.settings = read_settings(self.settings_path)

    def set_settings_values(self):
        self.running, self.room, self.set_automatic, self.set_thermostat, self.set_humidifier,\
        self.set_sprinklers, self.set_windows = self.settings


# Humidity - gas
# Moisture - liquid

if __name__ == "__main__":
    emulator = GreenHouse()
    emulator.loop()
