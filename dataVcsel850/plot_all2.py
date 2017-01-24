import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

MARKER_SIZE = 9


current_10, voltage_10, power_10 = np.loadtxt("temp_10.txt", unpack=True, skiprows=1)
current_20, voltage_20, power_20 = np.loadtxt("temp_20.txt", unpack=True, skiprows=1)
current_40, voltage_40, power_40 = np.loadtxt("temp_40.txt", unpack=True, skiprows=1)
current_60, voltage_60, power_60 = np.loadtxt("temp_60.txt", unpack=True, skiprows=1)
current_90, voltage_90, power_90 = np.loadtxt("temp_90.txt", unpack=True, skiprows=1)

ax1 = plt.subplot(211)
ax1.plot(current_10*1000, voltage_10, 'rh', label="283 K", markersize=MARKER_SIZE)
# ax1.plot(current_20*1000, voltage_20, 'y^', label="293 K", markersize=MARKER_SIZE)
# ax1.plot(current_40*1000, voltage_40, 'k<', label="313 K", markersize=MARKER_SIZE)
ax1.plot(current_60*1000, voltage_60, 'g^', label="333 K", markersize=MARKER_SIZE)
ax1.plot(current_90*1000, voltage_90, 'bp', label="363 K", markersize=MARKER_SIZE)
ax1.set_ylim([1.4, 2.4])
ax1.set_xlabel('prąd [mA]')
ax1.set_ylabel('napięcie [V]')
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)


ax2 = plt.subplot(212)
ax2.plot(current_10*1000, power_10*1000, 'rh', label="283 K", markersize=MARKER_SIZE)
# ax2.plot(current_20*1000, power_20*1000, 'y^', label="293 K", markersize=MARKER_SIZE)
# ax2.plot(current_40*1000, power_40*1000, 'k<', label="313 K", markersize=MARKER_SIZE)
ax2.plot(current_60*1000, power_60*1000, 'g^', label="333 K", markersize=MARKER_SIZE)
ax2.plot(current_90*1000, power_90*1000, 'bp', label="363 K", markersize=MARKER_SIZE)
ax2.set_ylim([0, 5.2])
ax2.set_xlabel('prąd [mA]')
ax2.set_ylabel('moc wyjściowa [mW]')
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.9, box.height])
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)

plt.show()