# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

from plot_threshold_current_temp import PlotThresholdCurrentTemp

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

temp = np.linspace(10, 90, 17) + 273
I_0 = [0.92, 0.94, 0.98, 1.05, 1.10, 1.18, 1.23, 1.25, 1.36, 1.47, 1.59, 1.63, 1.76, 1.86, 2.07, 2.25, 2.43]
error_I_0 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.03, 0.04, 0.03, 0.04, 0.04, 0.04, 0.06, 0.05, 0.06, 0.06]
pl = PlotThresholdCurrentTemp(I_0, temp, y_err=error_I_0)
#pl.plot_linear_temp_i_th_with_err
pl.fit_temp_log_i_th(x_text=340, y_text=0.2, dy_text=0.10)
#pl.get_latex_table()



def f(t, I_0, T_0):
    return I_0*np.exp(t/T_0)

fig, ax1 = plt.subplots()
x = np.linspace(5, 95, 100) + 273
y = f(x, 0.02799, 82.4241)
ax1.plot(x, y, 'b-')
ax1.errorbar(temp, I_0, yerr=error_I_0, fmt="o", color="red")
ax1.set_xlabel("Temperatura [K], $T$")
ax1.set_ylabel("Wartości prądu progowego , I_{th}$")
plt.grid(True)
plt.show()
