# Fall Detection and Alerting System
Once a wise man said:
> Fall seven times, stand up eight.

But fall can be fatal , so this system of ours detects fall and alerts accordingly.

This project is a combinaiton of hardware and machine learning.
The sensor used for the movement and position measurement is **MPU6050**
The system is divided into two sub-systems:
+ Wearable detector
+ System Groundstation

## Activity diagram
The project system works as follows:
![This is the Activity Diagram](/OOSE_UML/activity_diagram.png)

## Wearable detector
This is the data fetching and processing part of the system, the data is fed into the system through the 6-axis accelerometer and gyro sensor: MPU6050.
The components used in building of the sub-system are:
+ Raspberry Pi Pico
+ MPU6050
+ RF Transmitter
+ DC power supply

The ML model is trained and deployed into the microcontroller using TinyML. Here, we used **somethinf cool** ml model.
5v supply powers the system. Here the data is transmitted to the groundstation using RF Transmitter of 433MHz frequency.

### PCB of waerable sub-system
![This is PCB of the host](/Resources/Images/Hostside_sys_pcb_front_view.png)

## System Groundstation
This is the groundstation of the system , which also acts as the alerting system. The components used in this sub-system are:
+ Atmega328p
+ RF REceiver
+ 5V Power supply
+ Buzzer
+ LEDs

### PCB of the groundstation
+ to be added

## Rectifier 
This is the bridge rectifier and regulator used to power the groundstation.
Componenets used:
+ Diodes
+ LM6805
+ Capacitors
+ Resistor

### PCB of rectifier
![This is the PCB of rectifier](/Resources/Images/Bridge_Rectifier_Regulator1.jpg)
