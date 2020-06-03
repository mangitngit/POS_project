import time
import numpy as np
import matplotlib.pyplot as plt

from tools import alghoritm
from sensors import RS485, RH_010_GN, LB_856
from devices import HC35_3S, humidifier, HUNTER, windows
from tools.read_save_data import read_settings, read_desired_values, save_mean_values


class GreenHouse:
    """ Main class of program which contains every need parts """
    def __init__(self):
        """ Initialization variables and loading data """
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
        self.amount_of_time = 0.1

        self.data = []
        self.settings = []
        self.desired_values = []

        self.read_data()
        self.read_desired_values()

        self.read_settings()
        self.set_settings_values()

        plt.ion()

    def loop(self):
        """ Main loop """
        counter = 0  # variable to emulate time passes
        while self.running:
            time.sleep(self.amount_of_time)  # Waiting time for check measurements

            self.read_settings()
            self.set_settings_values()

            self.read_data()

            if self.set_automatic and counter >= self.waiting_time:
                counter = 0
                self.auto()
            elif not self.set_automatic:
                self.set_settings_devices()
                counter = 0

            self.launch_devices()
            save_mean_values(self.save_mean_path, self.samples_size, self.data)  # Save actual data for plotting

            self.plot()
            counter += 1

    def auto(self):
        """ Automatically change devices settings """
        self.set_thermostat = 1 if self.desired_values[0] > self.data[0] else 0
        self.set_humidifier = 1 if self.desired_values[1] > self.data[1] else 0
        self.set_sprinklers = 1 if self.desired_values[2] > self.data[2] else 0
        self.set_windows = 1 if (self.desired_values[3] > self.data[3] or self.desired_values[4] < self.data[4]) else 0

    def launch_devices(self):
        """ Function for emulate a launching devices, get value of change and set that  """
        self.data[0], temp = alghoritm.temperature(self.data[0], self.set_thermostat, 0)  # get value
        HC35_3S.launch(self.data_path, self.samples_size, temp)  # set it via device

        self.data[1], humidi = alghoritm.humidity(self.data[1], self.set_humidifier, 0)
        humidifier.launch(self.data_path, self.samples_size, humidi)

        self.data[2], moistu = alghoritm.moisture(self.data[2], self.set_sprinklers, 0)
        HUNTER.launch(self.data_path, self.samples_size, moistu)

        self.data[3], o2 = alghoritm.o2(self.data[3], self.set_windows, 0)
        windows.launch_o2(self.data_path, self.samples_size, o2)

        self.data[4], co2 = alghoritm.co2(self.data[4], self.set_windows, 0)
        windows.launch_co2(self.data_path, self.samples_size, co2)

    def read_data(self):
        """ Load data from CSV files """
        temperature_data = RS485.read_temperature(self.data_path)
        humidity_data = RS485.read_humidity(self.data_path)
        moisture_data = RH_010_GN.read_moisture(self.data_path)
        o2_data = LB_856.read_o2(self.data_path)
        co2_data = LB_856.read_co2(self.data_path)

        self.data = [temperature_data, humidity_data, moisture_data, o2_data, co2_data]

    def read_desired_values(self):
        """ Read actual desired values from CSV file """
        self.desired_values = read_desired_values(self.desired_path, self.room)

    def read_settings(self):
        """ Read actual settings from CSV file """
        self.settings = read_settings(self.settings_path)

    def set_settings_values(self):
        """ Set operation values """
        self.running, self.room, self.set_automatic = self.settings[:3]
        self.data_path = "room" + str(self.room)  # Path to actual room
        self.read_desired_values()  # Load actual desired values

    def set_settings_devices(self):
        """ Set devices values - on/off """
        self.set_thermostat, self.set_humidifier, self.set_sprinklers, self.set_windows = self.settings[3:]

    def plot(self):
        """ Help function to check the correct operation of the program """
        x = np.arange(5)
        # labels = ['temp', 'humi', 'mais', 'o2', 'co2']
        plt.bar(x - 0.35/2, self.data, 0.35, label='actual')
        plt.bar(x + 0.35/2, self.desired_values, 0.35, label='desire')
        plt.ylim(-5, 80)
        plt.legend()

        plt.draw()
        plt.pause(0.000001)
        plt.clf()


if __name__ == "__main__":
    emulator = GreenHouse()
    emulator.loop()
