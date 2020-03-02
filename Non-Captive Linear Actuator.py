# Uses the pySerial library to send and receive data from a Tic.
#
# NOTE: The Tic's control mode must be "Serial / I2C / USB".
# NOTE: You will need to change the "port_name =" line below to specify the
#   right serial port.
 
import serial
 
class TicSerial(object):
  def __init__(self, port, device_number=None):
    self.port = port
    self.device_number = device_number
 
  def send_command(self, cmd, *data_bytes):
    if self.device_number == None:
      header = [cmd]  # Compact protocol
    else:
      header = [0xAA, device_number, cmd & 0x7F]  # Pololu protocol
    self.port.write(bytes(header + list(data_bytes)))
 
  # Sends the "Exit safe start" command.
  def exit_safe_start(self):
    self.send_command(0x83)
 
  # Sets the target position.
  #
  # For more information about what this command does, see the
  # "Set target position" command in the "Command reference" section of the
  # Tic user's guide.
  def set_target_position(self, target):
    self.send_command(0xE0,
     ((target >>  7) & 1) | ((target >> 14) & 2) |
     ((target >> 21) & 4) | ((target >> 28) & 8),
     target >> 0 & 0x7F,
     target >> 8 & 0x7F,
     target >> 16 & 0x7F,
     target >> 24 & 0x7F)
 
  # Gets one or more variables from the Tic.
  def get_variables(self, offset, length):
    self.send_command(0xA1, offset, length)
    result = self.port.read(length)
    if len(result) != length:
      raise RuntimeError("Expected to read {} bytes, got {}."
        .format(length, len(result)))
    return bytearray(result)
 
  # Gets the "Current position" variable from the Tic.
  def get_current_position(self):
    b = self.get_variables(0x22, 4)
    position = b[0] + (b[1] << 8) + (b[2] << 16) + (b[3] << 24)
    if position >= (1 << 31):
      position -= (1 << 32)
    return position
 
# Choose the serial port name.
port_name = "/dev/serial1"
 
# Choose the baud rate (bits per second).  This must match the baud rate in
# the Tic's serial settings.
baud_rate = 9600
 
# Change this to a number between 0 and 127 that matches the device number of
# your Tic if there are multiple serial devices on the line and you want to
# use the Pololu Protocol.
device_number = None
 
port = serial.Serial(port_name, baud_rate, timeout=0.1, write_timeout=0.1)
 
tic = TicSerial(port, device_number)
 
position = tic.get_current_position()
print("Current position is {}.".format(position))
 
new_target = -200 if position > 0 else 200
print("Setting target position to {}.".format(new_target));
tic.exit_safe_start()
tic.set_target_position(new_target)