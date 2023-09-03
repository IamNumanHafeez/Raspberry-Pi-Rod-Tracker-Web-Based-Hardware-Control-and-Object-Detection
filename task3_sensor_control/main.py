import time
from sensor_controller import SensorController


sensor_controller = SensorController()
sensor_controller.track_rod()
print("Distance: ", sensor_controller.get_distance())
print("Color from distance: ", sensor_controller.get_color_from_distance())
