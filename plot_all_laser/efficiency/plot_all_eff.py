# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

from plot_laser_efficiency import PlotLaserEfficiency

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Data:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        current, voltage, power = np.loadtxt(path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.power = power*1000

    def get_input_power(self):
        return self.current*self.voltage

# data635 = Data("L635_temp_25.txt")
#
# plt.plot(data635.current, data635.power, 'bo')
# plt.show()

eff_635_current = PlotLaserEfficiency("L635_temp_25.txt")
eff_635_current.plot_slope_efficiency_via_current(28)

eff_850_vcsel_current = PlotLaserEfficiency("L850_VCSEL_temp_25.txt")


a_635_current, b_635_current, _ = eff_635_current.fit_via_current_poly_2(28)
l635_current_25, _ = eff_635_current.get_data_to_fit_via_current(28)
dP_635_current = 2 * a_635_current * l635_current_25 + b_635_current

ax1= plt.subplot(131)

ax1.plot(l635_current_25, dP_635_current)
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel(r"sprawność różniczkowa [W/A]")
plt.grid(True)
plt.show()