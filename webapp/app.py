from flask import Flask, render_template, jsonify, request
from zaber_motion.ascii import Connection
from zaber_motion import Units
from zaber_motion.ascii import Lockstep
import time


app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/background')
def background():
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        print("Found {} devices".format(len(device_list)))
    
        device1 = device_list[0]
        device2 = device_list[1]
    
        axis1 = device1.get_axis(1)
        axis2 = device2.get_axis(1)
    
        axis1.move_absolute(10, Units.LENGTH_MILLIMETRES)
        axis2.move_absolute(10, Units.LENGTH_MILLIMETRES)
        
        axis1.home()
        axis2.home()
    
    return ("nothing")

@app.route('/design')
def design():
    return 'This is a seperate page'

#@app.route('/hello/<name>')
#def hello(name):
#    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
#http://127.0.0.1:5000/ is the web browser URL
    
