from zaber_motion.ascii import Connection
from zaber_motion import Units
from zaber_motion.ascii import Lockstep
import time

with Connection.open_serial_port("/dev/ttyUSB0") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    
    device1 = device_list[0]
    device2 = device_list[1]
    
    axis1 = device1.get_axis(1)
    axis2 = device2.get_axis(1)
    
    axis1.move_velocity(-2.0, unit = Units.VELOCITY_MILLIMETRES_PER_SECOND)
    axis2.move_velocity(-2.0, unit = Units.VELOCITY_MILLIMETRES_PER_SECOND)
    
    axis1.home()
    axis2.home()
    
    axis1.move_absolute(30, Units.LENGTH_MILLIMETRES, wait_until_idle=False)
    axis2.move_absolute(30, Units.LENGTH_MILLIMETRES, wait_until_idle=False)
    
    axis1.wait_until_idle()
    axis2.wait_until_idle()
