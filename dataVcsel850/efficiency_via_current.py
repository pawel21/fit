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
#ple10.plot_slope_efficiency_via_current(1.7)

ple20 = PlotLaserEfficiency("temp_20.txt")
#ple20.plot_slope_efficiency_via_current(1.7)

ple30 = PlotLaserEfficiency("temp_30.txt")
#ple30.plot_slope_efficiency_via_current(1.6)

ple40 = PlotLaserEfficiency("temp_40.txt")
#ple40.plot_slope_efficiency_via_current(1.8)

ple50 = PlotLaserEfficiency("temp_50.txt")
#ple50.plot_slope_efficiency_via_current(2.0)

ple60 = PlotLaserEfficiency("temp_60.txt")
#ple60.plot_slope_efficiency_via_current(2.2)

ple70 = PlotLaserEfficiency("temp_70.txt")
#ple70.plot_slope_efficiency_via_current(2.3)

ple80 = PlotLaserEfficiency("temp_80.txt")
#ple80.plot_slope_efficiency_via_current(2.7)

ple90 = PlotLaserEfficiency("temp_90.txt")
#ple90.plot_slope_efficiency_via_current(3.0)

a_10, b_10, c_10 = ple10.fit_via_current_poly_2(1.7)
current_10, _ = ple10.get_data_to_fit_via_current(1.7)
dP_10 = 2*a_10*current_10 + b_10

a_20, b_20, c_20 = ple20.fit_via_current_poly_2(1.7)
current_20, _ = ple20.get_data_to_fit_via_current(1.7)
dP_20 = 2*a_20*current_20 + b_20

a_30, b_30, c_30 = ple30.fit_via_current_poly_2(1.6)
current_30, _ = ple30.get_data_to_fit_via_current(1.6)
dP_30 = 2*a_30*current_30 + b_30

a_40, b_40, c_40 = ple40.fit_via_current_poly_2(1.8)
current_40, _ = ple40.get_data_to_fit_via_current(1.8)
dP_40 = 2*a_40*current_40 + b_40

a_50, b_50, c_50 = ple50.fit_via_current_poly_2(2.0)
current_50, _ = ple50.get_data_to_fit_via_current(2.0)
dP_50 = 2*a_50*current_50 + b_50

a_60, b_60, c_60 = ple60.fit_via_current_poly_2(2.2)
current_60, _ = ple60.get_data_to_fit_via_current(2.2)
dP_60 = 2*a_60*current_60 + b_60

a_70, b_70, c_70 = ple70.fit_via_current_poly_2(2.3)
current_70, _ = ple70.get_data_to_fit_via_current(2.3)
dP_70 = 2*a_70*current_70 + b_70

a_80, b_80, c_80 = ple80.fit_via_current_poly_2(2.7)
current_80, _ = ple80.get_data_to_fit_via_current(2.7)
dP_80 = 2*a_80*current_80 + b_80

a_90, b_90, c_90 = ple90.fit_via_current_poly_2(3.0)
current_90, _ = ple90.get_data_to_fit_via_current(3.0)
dP_90 = 2*a_90*current_90 + b_90


fig, ax1 = plt.subplots()

ax1.plot(current_10, dP_10, label="283 K", lw=2)
ax1.plot(current_20, dP_20, label="293 K", lw=2)
ax1.plot(current_30, dP_30, label="303 K", lw=2)
ax1.plot(current_40, dP_40, label="313 K", lw=2)
ax1.plot(current_50, dP_50, label="323 K", lw=2)
ax1.plot(current_60, dP_60, label="333 K", lw=2)
ax1.plot(current_70, dP_70, label="343 K", lw=2)
ax1.plot(current_80, dP_80, label="353 K", lw=2)
ax1.plot(current_90, dP_90, label="363 K", lw=2)
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel(r"sprawność rożniczkowa [W/A]")


plt.legend()
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])
# Put a legend to the right of the current axis
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid(True)
plt.show()