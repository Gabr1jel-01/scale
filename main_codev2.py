import serial
import datetime
import time
import csv
import customtkinter as ctk
import tkinter as tk
import keyboard
import re
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

def stop_reading():
    default_bool = False
    #while default_bool == False:
        #if keyboard.is_pressed("s"):
    pass
            
            
def current_date():
    date_this_moment = datetime.datetime.now()
    date_this_moment_modified = date_this_moment.strftime("%H:%M:%S")
    return date_this_moment_modified

def current_time():
    time_this_moment = datetime.datetime.now()
    time_this_moment_modified = time_this_moment.strftime("%d.%m.%Y")
    return time_this_moment_modified


def scale_reading():
    try:
        # Open the serial connection
        ser = serial.Serial('COM9', 9600,bytesize=8,stopbits=1)  # appropriate port and '9600' baud rate
        command = "\W"  # command/query to request weight from the scale
        counter = 1
        csv_file_path = "readings.csv"
        while counter != 50000:
        # Send command to request weight
            command_bytes = command.encode()
            ser.write(command_bytes)
            
            
        # Read response from the scale
            response = ser.readline().decode().strip()
            #response = response.replace('ST,GS',"").replace(" ","").replace("US,GS","").replace("kg","")
            print("{} / {}".format(response[5:15], counter))
            response_certain = response[5:15]
            counter += 1
            
            if counter - (10 * int(counter / 10)) == 0:
              
                with open(csv_file_path,mode="a",newline="") as file:
                    writer = csv.writer(file)
                    counter_new = counter 
                    writer.writerow([response_certain] + [current_time()] + [current_date()] + [counter_new])
             

                
        # Close the serial connection
        ser.close()
    except Exception as e:
        print(e.message, e.args)
        
scale_reading()   
print("Reading DONE!!!")
    


