import LDC4005_USB2
import PM100USB
import time
import numpy as np
import matplotlib.pyplot as plt


PM=PM100USB.Thorlabs_PM100usb("/dev/usbtmc0")
LDC=LDC4005_USB2.LDC4005("/dev/usbtmc1")

PM.Set_Wavelength(850)

I=np.linspace(0,0.080,400) #zakres pradu
time.sleep(3)

LDC.LD_Current_Setpoint(0)
time.sleep(1)

LDC.ON()
time.sleep(3)


Current=[]

Voltage=[]
Power=[]

for i in range(0,len(I)):
    
    LDC.LD_Current_Setpoint(str(I[i]))
    time.sleep(0.05)
    Current.append(LDC.LD_Current_Reading())
    time.sleep(0.02)	
    Voltage.append(LDC.LD_Voltage_Reading())
    Power.append(PM.MeasurePower())
    #time.sleep(1)

#LDC.OFF()

J=np.array(Current,dtype=float)
V=np.array(Voltage,dtype=float)
L=np.array(Power,dtype=float)


np.savetxt('L850P010_temp_80.txt',zip(J,V,L),fmt='%1.12e',header=' J [A] \t V \t L [w] ')


I_p = np.linspace(0.080,0,400)
Current_p=[]

Voltage_p=[]
Power_p=[]

for i in range(0,len(I)):
    
    LDC.LD_Current_Setpoint(str(I_p[i]))
    time.sleep(0.05)
    Current_p.append(LDC.LD_Current_Reading())
    time.sleep(0.02)
    Voltage_p.append(LDC.LD_Voltage_Reading())
    Power_p.append(PM.MeasurePower())
    
LDC.OFF()
print PM.currentWavelength()

J_p=np.array(Current_p,dtype=float)
V_p=np.array(Voltage_p,dtype=float)
L_p=np.array(Power_p,dtype=float)


np.savetxt('L850P010_temp_80_rev.txt',zip(J_p,V_p,L_p),fmt='%1.12e',header=' J [A] \t V \t L [w] ')
