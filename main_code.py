import serial

# Open the serial connection
ser = serial.Serial('COM9', 9600,bytesize=8, stopbits=1,rtscts=True,xonxoff=True)  # Replace 'COM1' with the appropriate port and '9600' with the baud rate

# Send command to request weight
command = "I0"  # Replace with the command/query to request weight from the scale
command_bytes = command.encode()
ser.write(command_bytes)

# Read response from the scale
response = ser.readline().decode().strip()
print("Scale response:", response)

# Close the serial connection
ser.close()
