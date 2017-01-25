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


temp_850 = np.linspace(10, 90, 17) + 273
I_th_850 = [1.70, 1.67, 1.60, 1.55, 1.59, 1.63, 1.65, 1.68, 1.73, 1.83, 1.89, 2.00, 2.14, 2.24, 2.38, 2.57, 2.74]
error_I_0_850 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.07]

ax1 = plt.subplot(121)
ax1.errorbar(temp_850, I_th_850, yerr=error_I_0_850, fmt='o')
ax1.set_xlabel("temperatura, $T$ [K]")
ax1.set_ylabel("prąd progowy, $I_{\mathrm{th}}$ [mA]")
plt.grid(True)

ax2 = plt.subplot(122)
ax2.plot(temp_850, np.log(I_th_850), 'ro')
ax2.set_xlabel("temperatura, $T$ [K]")
ax2.set_ylabel("$\ln(I_{\mathrm{th}})$")
plt.grid(True)

plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.1, hspace=0.20, wspace=0.20)
plt.show()