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

ple20 = PlotLaserEfficiency("temp_20.txt")

current_20, _, _ = ple20.get_data()
ratio_power_20 = ple20.get_ratio_power()

ple90 = PlotLaserEfficiency("temp_90.txt")
current_90, _, _ = ple90.get_data()
ratio_power_90 = ple90.get_ratio_power()

fig, ax1 = plt.subplots()

ax1.plot(current_20, ratio_power_20, 'bo', label="293 K")
ax1.plot(current_90, ratio_power_90, 'ro', label="363 K")
ax1.set_xlabel("Prąd [mA]")
ax1.set_ylabel("Moc wyjściowa / Moc wejściowa")
ax1.set_ylim([0, max(ratio_power_20) + 0.1*max(ratio_power_20)])
plt.legend(loc=2)
plt.grid(True)
plt.show()