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

ple90 = PlotLaserEfficiency("temp_90.txt")
ple90.plot_slope_efficiency_via_power(5.0)

a_90, b_90, c_90, d_90 = ple90.fit_via_power_poly_3(5.0)
input_power_90, _ = ple90.get_data_to_fit_via_power(5.0)
dP_90 = 3*a_90*input_power_90**2 + 2*b_90*input_power_90 + c_90

# fig, ax1 = plt.subplots()
#
#
# ax1.plot(input_power_90, dP_90, label="363 K")
# ax1.set_xlim([0, max(input_power_90)])
# ax1.set_xlabel("Moc wejściowa [mW]")
# ax1.set_ylabel("Sprawność rożniczkowa")
# plt.legend()
# plt.grid(True)
# plt.show()

ple90.fit_step_by_step(5.0)