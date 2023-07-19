    # Open the serial connection
        ser = serial.Serial('COM9', 9600)  # appropriate port and '9600' baud rate
        command = "\W"  # command/query to request weight from the scale
        counter = 1
        csv_file_path = "readings.csv"
        while counter != 5000:
        # Send command to request weight
            command_bytes = command.encode()
            ser.write(command_bytes)
            
        # Read response from the scale
            response = ser.readline().decode().strip()
            response = response.replace('ST,GS',"").replace(" ","").replace("US,GS","").replace("kg","")
            print("{} / {}".format(response, counter))
            #a = current_time()
            counter += 1
            time.sleep(0.5)
            """   
            with open(csv_file_path,mode="a",newline="") as file:
                writer = csv.writer(file)
                counter_new = counter - 1
                writer.writerow([response] + [current_time()] + [current_date()] + [counter_new])
            """ 

                
        # Close the serial connection
        ser.close()
        while True:
            print("RADI")
            time.sleep(0.2)