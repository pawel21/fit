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

MARKER_SIZE = 7


current_5, voltage_5, power_5 = np.loadtxt("temp_5.txt", unpack=True, skiprows=1)
current_20, voltage_20, power_20 = np.loadtxt("temp_20.txt", unpack=True, skiprows=1)
current_35, voltage_35, power_35 = np.loadtxt("temp_35.txt", unpack=True, skiprows=1)


ax1 = plt.subplot(211)
ax1.plot(current_5 * 1000, voltage_5, 'rh', label="278 K", markersize=MARKER_SIZE)
ax1.plot(current_20*1000, voltage_20, 'y^', label="293 K", markersize=MARKER_SIZE)
ax1.plot(current_35 * 1000, voltage_35, 'g<', label="308 K", markersize=MARKER_SIZE)

ax1.set_ylim([1.85, 2.25])
ax1.set_xlabel('prąd [mA]')
ax1.set_ylabel('napięcie [V]')
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)


ax2 = plt.subplot(212)
ax2.plot(current_5 * 1000, power_5 * 1000, 'rh', label="278 K", markersize=MARKER_SIZE)
ax2.plot(current_20*1000, power_20*1000, 'y^', label="293 K", markersize=MARKER_SIZE)
ax2.plot(current_35 * 1000, power_35 * 1000, 'g<', label="308 K", markersize=MARKER_SIZE)

#ax2.set_ylim([0, 5.2])
ax2.set_xlabel('prąd [mA]')
ax2.set_ylabel('moc wyjściowa [mW]')
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.9, box.height])
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)


plt.show()