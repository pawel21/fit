# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt

from plot_laser_efficiency import PlotLaserEfficiency


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

ple10 = PlotLaserEfficiency("temp_10.txt")
current_10, _, _ = ple10.get_data()
ratio_power_10 = ple10.get_ratio_power()

ple60 = PlotLaserEfficiency("temp_60.txt")
current_60, _, _ = ple60.get_data()
ratio_power_60 = ple60.get_ratio_power()

ple90 = PlotLaserEfficiency("temp_90.txt")
current_90, _, _ = ple90.get_data()
ratio_power_90 = ple90.get_ratio_power()

fig, ax1 = plt.subplots()

ax1.plot(current_10, ratio_power_10, 'bo', label="283 K")
ax1.plot(current_60, ratio_power_60, 'yo', label="333 K")
ax1.plot(current_90, ratio_power_90, 'ro', label="363 K")
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel("sprawność całkowita")
ax1.set_ylim([0, max(ratio_power_10) + 0.1 * max(ratio_power_10)])
plt.legend(loc=2)
plt.grid(True)
plt.show()