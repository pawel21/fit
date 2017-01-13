# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
import numpy as np
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

temp_635, current_635, error_current_635 = np.loadtxt("current_threshold_635.txt", unpack=1, skiprows=1)

temp_850_p10, current_850_p10, error_current_850_p10 = np.loadtxt("current_threshold_850_p010.txt", unpack=1, skiprows=1)

fig, ax1 = plt.subplots()
ax1.errorbar(temp_635, current_635, yerr=error_current_635, fmt='o', color="blue", label="635")
ax1.errorbar(temp_850_p10, current_850_p10, yerr=error_current_850_p10, fmt='o', color="red", label="850")
ax1.set_xlabel('Temperatura [K]')
ax1.set_ylabel('Prąd progowy [mA]')
plt.grid(True)
plt.legend()
plt.show()