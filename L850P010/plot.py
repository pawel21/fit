import numpy as np
import matplotlib.pyplot as plt
import argparse

plt.rcParams.update({'font.size':25})


parser = argparse.ArgumentParser()
parser.add_argument("name", help="The name of file to read ", type=str)
parser.add_argument("temp", help="temp ", type=str)



args = parser.parse_args() 
args = parser.parse_args() 

print args.temp

J,V,L=np.loadtxt(args.name,skiprows=1,unpack=True)



fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(J, L, marker='o',color='red',ls='none')
ax2.plot(J, V, marker='o',color='green',ls='none')

ax1.set_xlabel('J [A]')
ax1.set_ylabel('L [W]', color='r')
ax2.set_ylabel('U [V]', color='g')

plt.grid(True)
plt.title("Temp = "+args.temp)
plt.show()
