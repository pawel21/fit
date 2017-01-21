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
#ple20.plot_slope_efficiency_via_power(2.7)

ple30 = PlotLaserEfficiency("temp_30.txt")
#ple30.plot_slope_efficiency_via_power(2.8)

ple40 = PlotLaserEfficiency("temp_40.txt")
#ple40.plot_slope_efficiency_via_power(2.9)

ple50 = PlotLaserEfficiency("temp_50.txt")
#ple50.plot_slope_efficiency_via_power(3.0)

ple60 = PlotLaserEfficiency("temp_60.txt")
#ple60.plot_slope_efficiency_via_power(3.5)

ple70 = PlotLaserEfficiency("temp_70.txt")
#ple70.plot_slope_efficiency_via_power(3.85)

ple80 = PlotLaserEfficiency("temp_80.txt")
#ple80.plot_slope_efficiency_via_power(4.5)

ple90 = PlotLaserEfficiency("temp_90.txt")
#ple90.plot_slope_efficiency_via_power(5.0)

a_20, b_20, c_20 = ple20.fit_via_power_poly_2(2.7)
input_power_20, _ = ple20.get_data_to_fit_via_power(2.7)
dP_20 = 2*a_20*input_power_20 + b_20

a_30, b_30, c_30 = ple30.fit_via_power_poly_2(2.8)
input_power_30, _ = ple30.get_data_to_fit_via_power(2.8)
dP_30 = 2*a_30*input_power_30 + b_30

a_40, b_40, c_40 = ple40.fit_via_power_poly_2(2.9)
input_power_40, _ = ple40.get_data_to_fit_via_power(2.9)
dP_40 = 2*a_40*input_power_40 + b_40

a_50, b_50, c_50 = ple50.fit_via_power_poly_2(3.0)
input_power_50, _ = ple50.get_data_to_fit_via_power(3.0)
dP_50 = 2*a_50*input_power_50 + b_50

a_60, b_60, c_60 = ple60.fit_via_power_poly_2(3.5)
input_power_60, _ = ple60.get_data_to_fit_via_power(3.5)
dP_60 = 2*a_60*input_power_60 + b_60

a_70, b_70, c_70 = ple70.fit_via_power_poly_2(3.5)
input_power_70, _ = ple70.get_data_to_fit_via_power(3.5)
dP_70 = 2*a_70*input_power_70 + b_70

a_80, b_80, c_80 = ple80.fit_via_power_poly_2(4.5)
input_power_80, _ = ple80.get_data_to_fit_via_power(4.5)
dP_80 = 2*a_80*input_power_80 + b_80

a_90, b_90, c_90 = ple90.fit_via_power_poly_2(5.0)
input_power_90, _ = ple90.get_data_to_fit_via_power(5.0)
dP_90 = 2*a_90*input_power_90 + b_90

fig, ax1 = plt.subplots()

ax1.plot(input_power_20, dP_20, label="293 K", linewidth=2)
ax1.plot(input_power_30, dP_30, label="303 K", linewidth=2)
ax1.plot(input_power_40, dP_40, label="313 K", linewidth=2)
ax1.plot(input_power_50, dP_50, label="323 K", linewidth=2)
ax1.plot(input_power_60, dP_60, label="333 K", linewidth=2)
ax1.plot(input_power_70, dP_70, label="343 K", linewidth=2)
ax1.plot(input_power_80, dP_80, label="353 K", linewidth=2)
ax1.plot(input_power_90, dP_90, label="363 K", linewidth=2)
ax1.set_xlim([0, max(input_power_20)])
ax1.set_xlabel("Moc wejściowa [mW]")
ax1.set_ylabel("Sprawność rożniczkowa")
plt.legend()
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])

# Put a legend to the right of the current axis
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.show()