import serial
import time



# Open the serial connection
ser = serial.Serial('COM9', 9600)  # Replace 'COM1' with the appropriate port and '9600' with the baud rate
command = "\W"  # Replace with the command/query to request weight from the scale

while True:
    
# Send command to request weight
    
    command_bytes = command.encode()
    ser.write(command_bytes)
    time.sleep(0.5)

# Read response from the scale
    response = str(ser.readline().decode().strip())
    print("Scale response:", response)

# Close the serial connection

