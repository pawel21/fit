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
ple10.plot_slope_efficiency_via_current(25)

ple35 = PlotLaserEfficiency("temp_30.txt")
ple35.plot_slope_efficiency_via_current(31)



a_10_current, b_10_current, c_10 = ple10.fit_via_current_poly_2(25)
current_10, _ = ple10.get_data_to_fit_via_current(25)
dP_10_current = 2 * a_10_current * current_10 + b_10_current

ax1 = plt.subplot()
ax1.plot(current_10, dP_10_current)

plt.grid(True)
plt.show()