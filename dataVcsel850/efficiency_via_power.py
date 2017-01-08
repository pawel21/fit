# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt

from plot_laser_efficiency import PlotLaserEfficiency

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


ple20 = PlotLaserEfficiency("temp_20.txt")
ple20.plot_slope_efficiency_via_power(2.7)

ple60 = PlotLaserEfficiency("temp_60.txt")
ple60.plot_slope_efficiency_via_power(3.5)

ple90 = PlotLaserEfficiency("temp_90.txt")
ple90.plot_slope_efficiency_via_power(5.0)

a_20, b_20, c_20 = ple20.fit_via_power_poly_2(2.7)
input_power_20 = ple20.get_input_power()
dP_20 = 2*a_20*input_power_20 + b_20

a_60, b_60, c_60 = ple60.fit_via_power_poly_2(3.5)
input_power_60 = ple60.get_input_power()
dP_60 = 2*a_60*input_power_60 + b_60

a_90, b_90, c_90 = ple90.fit_via_power_poly_2(5.0)
input_power_90 = ple90.get_input_power()
dP_90 = 2*a_90*input_power_90 + b_90

fig, ax1 = plt.subplots()

ax1.plot(input_power_20, dP_20, label="293 K")
ax1.plot(input_power_60, dP_60, label="333 K")
ax1.plot(input_power_90, dP_90, label="363 K")
ax1.set_xlim([0, max(input_power_20)])
ax1.set_xlabel("Moc wejściowa [mW]")
ax1.set_ylabel("Sprawność rożniczkowa")
plt.legend()
plt.grid(True)
plt.show()