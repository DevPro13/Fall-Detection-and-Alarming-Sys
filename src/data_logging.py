#import pandas as pd
import time
import serial
import csv

#df = pd.DataFrame(columns=["Time", "Gx", "Gy","Gz","AAx","AAy","AAz"])

ser = serial.Serial("/dev/tty.usbmodem1101", 115200)

with open("/Users/akankshagiri/fall10.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(['Time','Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz'])
    while True:
    #read the data from serial port
        data = ser.readline().decode("utf-8").strip()
        #print(data)
        values = data.split(' ')
        print(values)
        Ax = float(values[0])
        Ay = float(values[2])
        Az = float(values[4])
        Gx = float(values[6])
        Gy = float(values[8])
        Gz = float(values[10])

        current_time = time.strftime("%H:%M:%S")

        writer.writerow([current_time,Ax,Ay,Az,Gx,Gy,Gz])
        file.flush() # flush data to the file
        time.sleep(0.1)

        #timestamp = time.time.now().strftime('%H:%M:%S.%f')



