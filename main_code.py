import serial
import time
import csv





# Open the serial connection
ser = serial.Serial('COM9', 9600)  # Replace 'COM1' with the appropriate port and '9600' with the baud rate
command = "\W"  # Replace with the command/query to request weight from the scale


readings_list = []


replacements = [("ST",""),(",",""),("GS",""),("UG","")]

counter = 0

while counter != 10:
    
# Send command to request weight
    
    command_bytes = command.encode()
    ser.write(command_bytes)
    time.sleep(0.6)

# Read response from the scale
    response = str(ser.readline().decode().strip())
    response = response.replace('ST,GS',"").replace(" ","").replace("US,GS","")
    print("Scale response:", response)
    readings_list.append(response)
    
    counter += 1

# Close the serial connection
ser.close()

csv_file_path = "readings.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Reading"])  # Write header row
    for reading in readings_list:
        writer.writerow([reading])
        
print(readings_list)

