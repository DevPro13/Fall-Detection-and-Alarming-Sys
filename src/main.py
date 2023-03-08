
from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
imu = MPU6050(i2c)

imu.accel_range = 3    # set accelerometer sensitivity to +/- 16g
imu.gyro_range = 0	   # set gyroscope sensitivity to +/- 250 degrees/sec

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x,2)
    gy=round(imu.gyro.y,2)
    gz=round(imu.gyro.z,2)

    print(ax,"",ay,"",az,"",gx,"",gy,"",gz)
    sleep(0.2)