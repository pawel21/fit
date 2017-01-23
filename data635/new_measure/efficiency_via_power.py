# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, "/home/pawel1/Pulpit/Studia/PracaInz/fit")

from plot_laser_efficiency import PlotLaserEfficiency

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


ple5 = PlotLaserEfficiency("temp_5.txt")
#ple5.plot_slope_efficiency_via_power(41)

ple10 = PlotLaserEfficiency("temp_10.txt")
#ple10.plot_slope_efficiency_via_power(44.5)

ple15 = PlotLaserEfficiency("temp_15.txt")
#ple15.plot_slope_efficiency_via_power(46.5)

ple20 = PlotLaserEfficiency("temp_20.txt")
#ple20.plot_slope_efficiency_via_power(53)

ple25 = PlotLaserEfficiency("temp_25.txt")
#ple25.plot_slope_efficiency_via_power(60.5)

ple30 = PlotLaserEfficiency("temp_30.txt")
#ple30.plot_slope_efficiency_via_power(68.5)

ple35 = PlotLaserEfficiency("temp_35.txt")
#ple35.plot_slope_efficiency_via_power(78.5)

a_5, b_5, c_5 = ple5.fit_via_power_poly_2(41)
input_power_5, _ = ple5.get_data_to_fit_via_power(41)
dP_5 = 2*a_5*input_power_5 + b_5

a_10, b_10, c_10 = ple10.fit_via_power_poly_2(44.5)
input_power_10, _ = ple10.get_data_to_fit_via_power(44.5)
dP_10 = 2*a_10*input_power_10 + b_10

a_15, b_15, c_15 = ple15.fit_via_power_poly_2(46.5)
input_power_15, _ = ple15.get_data_to_fit_via_power(46.5)
dP_15 = 2*a_15*input_power_15 + b_15

a_20, b_20, c_20 = ple20.fit_via_power_poly_2(53)
input_power_20, _ = ple20.get_data_to_fit_via_power(53)
dP_20 = 2*a_20*input_power_20 + b_20

a_25, b_25, c_25 = ple25.fit_via_power_poly_2(60.5)
input_power_25, _ = ple25.get_data_to_fit_via_power(60.5)
dP_25 = 2*a_25*input_power_25 + b_25

a_30, b_30, c_30 = ple30.fit_via_power_poly_2(68.5)
input_power_30, _ = ple30.get_data_to_fit_via_power(68.5)
dP_30 = 2*a_30*input_power_30 + b_30

a_35, b_35, c_35 = ple35.fit_via_power_poly_2(78.5)
input_power_35, _ = ple35.get_data_to_fit_via_power(78.5)
dP_35 = 2*a_35*input_power_35 + b_35
x_slope_20, slope_20 = ple20.fit_step_by_step(53, 15)

fig, ax1 = plt.subplots()

ax1.plot(input_power_5, dP_5, label="278\,K", linewidth=2)
ax1.plot(input_power_10, dP_10, label="283\,K", linewidth=2)
ax1.plot(input_power_15, dP_15, label="288\,K", linewidth=2)
ax1.plot(input_power_20, dP_20, label="293\,K", linewidth=2)
ax1.plot(input_power_25, dP_25, label="298\,K", linewidth=2)
ax1.plot(input_power_30, dP_30, label="303\,K", linewidth=2)
#ax1.plot(input_power_35, dP_35, label="308\,K", linewidth=2)
ax1.plot(x_slope_20, slope_20, 'ko')

ax1.set_xlim([0, max(input_power_20)])
ax1.set_xlabel("Moc wejściowa [mW]")
ax1.set_ylabel("Sprawność rożniczkowa")
plt.legend()
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])


ax1.set_xlim([40, 90])
# Put a legend to the right of the current axis
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.show()

#from matplotlib2tikz import save as tikz_save
#tikz_save('plot_eff_via_power.tex')