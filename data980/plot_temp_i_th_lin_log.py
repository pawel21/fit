# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


temp_980 = np.linspace(10, 90, 17) + 273
I_th_980 = [0.92, 0.94, 0.98, 1.05, 1.10, 1.18, 1.23, 1.25, 1.36, 1.47, 1.59, 1.63, 1.76, 1.86, 2.07, 2.25, 2.43]
error_I_th_980 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.03, 0.04, 0.03, 0.04, 0.04, 0.04, 0.06, 0.05, 0.06, 0.06]

ax1 = plt.subplot(121)
ax1.errorbar(temp_980, I_th_980, yerr=error_I_th_980, fmt='o')
ax1.set_xlabel("temperatura, $T$ [K]")
ax1.set_ylabel("prąd progowy, $I_{\mathrm{th}}$ [mA]")
plt.grid(True)

ax2 = plt.subplot(122)
ax2.plot(temp_980, np.log(I_th_980), 'ro')
ax2.set_xlabel("temperatura, $T$ [K]")
ax2.set_ylabel("$\ln(I_{\mathrm{th}})$")
plt.grid(True)

plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.1, hspace=0.20, wspace=0.20)
plt.show()
