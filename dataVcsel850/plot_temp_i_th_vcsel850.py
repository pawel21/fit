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


temp_850 = np.linspace(10, 90, 17) + 273
I_th_850 = [1.70, 1.67, 1.60, 1.55, 1.59, 1.63, 1.65, 1.68, 1.73, 1.83, 1.89, 2.00, 2.14, 2.24, 2.38, 2.57, 2.74]
error_I_0_850 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.07]

fig, ax1 = plt.subplots()
ax1.errorbar(temp_850, I_th_850, yerr=error_I_0_850, fmt='o', color="red")
ax1.set_xlabel("Temperatura [K]")
ax1.set_ylabel("Prąd progowy [mA]")
plt.grid(True)
#plt.show()

from matplotlib2tikz import save as tikz_save
tikz_save('plot_i_th.tex', figureheight='9cm', figurewidth='16cm')


#pl_850 = PlotThresholdCurrentTemp(I_0_850, temp_850, y_err=error_I_0_850)
#pl_850.plot_linear_temp_i_th_with_err