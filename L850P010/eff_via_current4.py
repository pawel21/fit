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
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

ple90 = PlotLaserEfficiency("/home/pawel1/Pulpit/Studia/PracaInz/fit/L850P010/L850P010_temp_80.txt")
x_90, y_90 = ple90.plot_slope_efficiency_via_current(17.5)
current_90, _, output_power_90 = ple90.get_data()
a_90, b_90, c_90 = ple90.fit_via_current_poly_2(17.5)
current_90_fit, _ = ple90.get_data_to_fit_via_current(17.5)
dP_90 = 2*a_90 * current_90_fit + b_90
#x_slope_90, slope_90 = ple90.fit_step_by_step_via_current(17.5, 10)


ple20 = PlotLaserEfficiency("/home/pawel1/Pulpit/Studia/PracaInz/fit/L850P010/L850P010_temp_20.txt")
x_20, y_20 = ple20.plot_slope_efficiency_via_current(12)
current_20, _, output_power_20 = ple20.get_data()
a_20, b_20, c_20 = ple20.fit_via_current_poly_2(12)
current_20_fit, _ = ple20.get_data_to_fit_via_current(12)
dP_20 = 2*a_20 * current_20_fit + b_20
#x_slope_20, slope_20 = ple20.fit_step_by_step_via_current(12, 10)




ax1 = plt.subplot(221)
ax1.plot(current_90, output_power_90, 'bo', markersize=4)
ax1.plot(x_90, y_90, 'r-', linewidth=2)
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel("moc wyjściowa [mW]")
ax1.set_title("353 K")
plt.grid(True)

ax2 = plt.subplot(223)
ax2.plot(current_90_fit, dP_90, 'g-', linewidth=2)
#ax2.plot(x_slope_90, slope_90, 'ko')
ax2.set_xlabel("prąd [mA]")
ax2.set_ylabel("sprawność [W/A]")
plt.grid(True)

ax3 = plt.subplot(222)
ax3.plot(current_20, output_power_20, 'bo', markersize=4)
ax3.plot(x_20, y_20, 'r-', linewidth=2)
ax3.set_xlabel("prąd [mA]")
ax3.set_ylabel("moc wyjściowa [mW]")
ax3.set_title("293 K")
plt.grid(True)

ax4 = plt.subplot(224)
ax4.plot(current_20_fit, dP_20, 'g-', linewidth=2)
#ax4.plot(x_slope_20, slope_20, 'ko')
ax4.set_xlabel("prąd [mA]")
ax4.set_ylabel("sprawność [W/A]")
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()