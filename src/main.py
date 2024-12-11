###This code reads IMU sensors data and logs them in CSV file.###
import os
import time
from imu import MPU6050
from machine import Pin, I2C
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
imu = MPU6050(i2c)
led=Pin(25,Pin.OUT)
imu.accel_range = 3    # set accelerometer sensitivity to +/- 16g
imu.gyro_range = 0	   # set gyroscope sensitivity to +/- 250 degrees/sec
def logData(data):
    with open("Data_Log.csv", "a") as file:
        first_char = file.read(1)
        print(not first_char)
        if not first_char:
            file.write("Epoch_time_s,milliseconds_elapsed,Ax,Ay,Az,Gx,Gy,Gz"+"\n") 
        data_in_text=",".join(str(data_item) for data_item in data)+"\n"
        file.write(data_in_text)
        file.flush() # flush data to the file        
if __name__=='__main__':
    for i in range(4):  #Blinks led before it starts reading sensors data
        led.value(i % 2)
        time.sleep(0.5)
    led.value(0)
    prev_tick=0
    time_in_ms=0#count time in milliseconds
    prev_epoch=0
    while True:
        ax=round(imu.accel.x,8)
        ay=round(imu.accel.y,8)
        az=round(imu.accel.z,8)
        gx=round(imu.gyro.x,8)
        gy=round(imu.gyro.y,8)
        gz=round(imu.gyro.z,8)
        current_time_in_epoch_s=time.time()#current
        current_tick=time.ticks_ms()#milliseconds elapsed
        tick_diff=abs(time.ticks_diff(prev_tick,current_tick))
        if prev_tick!=0:
            time_in_ms+=tick_diff
            if prev_epoch!=current_time_in_epoch_s:
                time_in_ms=0
            else:
                time_in_ms%=1000# value might exceed 1000 ms
        data=[current_time_in_epoch_s,time_in_ms,ax,ay,az,gx,gy,gz]
        #time starts from jan 1, 2021 12:00:00 AM
        print(data)
        logData(data)
        prev_tick=current_tick
        prev_epoch=current_time_in_epoch_s
        time.sleep(0.2)