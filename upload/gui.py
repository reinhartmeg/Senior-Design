from flask import Flask, render_template, jsonify, request
from zaber_motion import Units
from zaber_motion.ascii import Connection
import time

#from zaber_motion.ascii import Lockstep, Stream, StreamMode, Connection, StreamAxisType, StreamAxisDefinition

app = Flask(__name__)

#all useful Zaber functions for reference: https://www.zaber.com/software/docs/motion-library/ascii/references/python/
#how-to guides with example zaber code: https://www.zaber.com/software/docs/motion-library/ascii/howtos/streams/ 
#http://127.0.0.1:5000/ is the web browser URL for the development server


#axis.move_velocity(velocity, unit = Units.NATIVE)
#axis.stop(wait_until_idle = True) #Stops ongoing axis movement. Decelerates until zero speed.
#axis.wait_until_idle(throw_error_on_fault = True) #Waits until axis stops moving.

    
#http://127.0.0.1:5000/ is the web browser URL

#rendiner the HTML page which has the interface
@app.route('/')
def button():
    return render_template('buttonexample_splitpage_update1.html')

#background process happening without any refreshing
@app.route('/back')
#stop motion
def stop():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis1.stop()
        axis2.stop()
    return ("nothing")

@app.route('/back1')
#home motion
def home():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis1.home()
        axis2.home()
    return ("nothing")

@app.route('/back3')
def home1():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis1.home()
    return ("nothing")

@app.route('/back4')
def home2():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis2.home()
    return ("nothing")


# full X, axis 2
@app.route('/back2')
def upcont():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        velocity = 10 # update if with - & + shortly
        axis2.move_velocity(velocity, Units.VELOCITY_MILLIMETRES_PER_SECOND)
        axis2.move_absolute(50, Units.LENGTH_MILLIMETRES)

        #all_axes.stop(wait_until_idle = True)
    return ("nothing")

@app.route('/back5')
def upstep():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis2.move_relative(5, Units.LENGTH_MILLIMETRES)
        #all_axes.stop(wait_until_idle = True)
    return ("nothing")

@app.route('/back6')
def downstep():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis2.move_relative(-5, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")

@app.route('/back7')
def downcont():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        velocity = 10 # update if with - & + shortly
        axis2.move_velocity(velocity, Units.VELOCITY_MILLIMETRES_PER_SECOND)
        axis2.move_absolute(0, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")

#full Y, axis 1
@app.route('/back8')
def leftcont():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        velocity = 10 # update if with - & + shortly
        axis1.move_velocity(velocity, Units.VELOCITY_MILLIMETRES_PER_SECOND)
        axis1.move_absolute(50, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")

@app.route('/back9')
def leftstep():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis1.move_relative(5, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")

@app.route('/back10')
def rightstep():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        axis1.move_relative(-5, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")

@app.route('/back11')
def rightcont():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        device1 = device_list[0]
        device2 = device_list[1]
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
        velocity = 10 # update if with - & + shortly
        axis1.move_velocity(velocity, Units.VELOCITY_MILLIMETRES_PER_SECOND)
        axis1.move_absolute(0, Units.LENGTH_MILLIMETRES)
        
    return ("nothing")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
