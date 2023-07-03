import serial
import datetime
import time
import csv
import customtkinter as ctk
import tkinter as tk
import keyboard

"""
class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600+325+50")
        self.title("DOK-ING SCALE")
        

if __name__ == "__main__":
    window = Window()
    window.mainloop()
"""
"""
def stop_reading_s_key():
    default_bool = False
    
    while True:
        if keyboard.ispressed("s"):
            default_bool = True
"""            
            
def current_time():
    time_this_moment = datetime.datetime.now()
    time_this_moment_modified = time_this_moment.strftime("%m/%d/%Y, %H:%M:%S")
    return time_this_moment_modified

def scale_reading():
    # Open the serial connection
    ser = serial.Serial('COM9', 9600)  # appropriate port and '9600' baud rate
    command = "\W"  # command/query to request weight from the scale
    weight_list = []
    counter = 0
    while counter != 15:
    # Send command to request weight
        command_bytes = command.encode()
        ser.write(command_bytes)
        time.sleep(0.6)
    # Read response from the scale
        response = str(ser.readline().decode().strip())
        response = response.replace('ST,GS',"").replace(" ","").replace("US,GS","").replace("kg","")
        print("Scale response:", response)
        weight_list.append([response,current_time()])
        counter += 1
    # Close the serial connection
    ser.close()
    csv_file_path = "readings.csv"

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["WEIGHT"])  # Write header row
        for weight_reading in weight_list:
            writer.writerow([weight_reading])
    
scale_reading()
