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
ple10.plot_slope_efficiency_via_current(20)

ple35 = PlotLaserEfficiency("temp_30.txt")
ple35.plot_slope_efficiency_via_current(31)



a_10, b_10, c_10 = ple10.fit_via_current_poly_2(20)
current_10, _ = ple10.get_data_to_fit_via_current(20)
dP_10 = 2*a_10*current_10 + b_10