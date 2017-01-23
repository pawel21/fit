# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

#from plot_threshold_current_temp import PlotThresholdCurrentTemp

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


temp_635 = np.linspace(5, 35, 7) + 273
I_th_635 = [19.1, 20.7, 22.6, 25.0, 27.9, 31.4, 36]
error_I_0_635 = [0.2, 0.2,  0.2, 0.2, 0.3, 0.5, 2]

fig, ax1 = plt.subplots()
ax1.errorbar(temp_635, I_th_635, yerr=error_I_0_635, fmt='o', color="red", markersize=3)
ax1.set_xlabel("Temperatura [K]")
ax1.set_ylabel("Prąd progowy [mA]")
plt.grid(True)
#plt.show()

from matplotlib2tikz import save as tikz_save
tikz_save('plot_i_th.tex', figureheight='8cm', figurewidth='15cm')


# pl_635 = PlotThresholdCurrentTemp(I_th_635, temp_635, y_err=error_I_0_635)
# pl_635.plot_linear_temp_i_th_with_err
# pl_635.fit_temp_log_i_th(x_text=300, y_text=3, dy_text=0.1)
# pl_635.plot_fit_exp_with_error()