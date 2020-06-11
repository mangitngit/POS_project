#POS GreenHouse project
ETI IDIO mgr I sem

This application emulates a greenhouse behaviour. It contains sensors and devices to
measurement and control microclimate.

Sensor | Purpose
------------ | -------------
RS485 | temperature, humidity
RH_010_GN | moisture
LB_856 | CO2, O2

Device | Purpose
------------ | -------------
HC35_3S | temperature
humidifier | humidity
HUNTER | moisture
ventilation | CO2, O2

There is a possibility to check auto setting or manual settings.

##How to run
Run the main.py file. Program control is performed by the assigned website.

##CSV files
###settings.csv:
Representing by array:

**[is_running, room_number, auto/manual, thermostat, humidifier, sprinklers, windows]**

* 1 - is on / 0 - is off
* except room_numbers - from 1 to 3

###mean_data.csv and room_desired_values.csv
**[temperature [C], air_humidity [%], soil_moisture [%], CO2 [%], O2 [%]]**
* data type - floats

###data csv files:
CO2 and O2 have two values in arrays **[float, float]**

others have five values **[float, float, float, float, float]**
