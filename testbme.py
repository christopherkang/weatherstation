import smbus2
import bme280
import numpy as np

## demo usage
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)

print("Initializing sensor")
print("Testing out sample readings")

print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)
print(data)



