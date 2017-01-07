import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.family"] = "Arial"
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})

current_10, voltage_10, power_10 = np.loadtxt("temp_10.txt", unpack=True, skiprows=1)
current_20, voltage_20, power_20 = np.loadtxt("temp_20.txt", unpack=True, skiprows=1)
current_30, voltage_30, power_30 = np.loadtxt("temp_30.txt", unpack=True, skiprows=1)
current_40, voltage_40, power_40 = np.loadtxt("temp_40.txt", unpack=True, skiprows=1)
current_50, voltage_50, power_50 = np.loadtxt("temp_50.txt", unpack=True, skiprows=1)
current_60, voltage_60, power_60 = np.loadtxt("temp_60.txt", unpack=True, skiprows=1)
current_70, voltage_70, power_70 = np.loadtxt("temp_70.txt", unpack=True, skiprows=1)
current_80, voltage_80, power_80 = np.loadtxt("temp_80.txt", unpack=True, skiprows=1)
current_90, voltage_90, power_90 = np.loadtxt("temp_90.txt", unpack=True, skiprows=1)

fig, ax1 = plt.subplots()
ax1.plot(current_10, power_10, 'b*', label="283 K")
ax1.plot(current_20, power_20, 'y^', label="293 K")
ax1.plot(current_30, power_30, 'r>', label="303 K")
ax1.plot(current_40, power_40, 'k<', label="313 K")
ax1.plot(current_50, power_50, 'bo', label="323 K")
ax1.plot(current_60, power_60, 'g^', label="333 K")
ax1.plot(current_70, power_70, 'rd', label="343 K")
ax1.plot(current_80, power_80, 'yh', label="353 K")
ax1.plot(current_90, power_90, 'bp', label="363 K")

ax1.set_xticks(list(np.linspace(0., 0.02, 5)))
ax1.set_xticklabels(np.linspace(0., 20, 5, dtype=int))
ax1.set_yticks(list(np.linspace(0, 0.006, 7)))
ax1.set_yticklabels(list(np.linspace(0, 6, 7, dtype=int)))
ax1.set_xlabel('Prąd [mA]')
ax1.set_ylabel('Moc wyjściowa [mW]')
plt.grid(True)
plt.legend(loc=2)
plt.show()
