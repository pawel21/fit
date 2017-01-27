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
plt.rcParams.update({'font.size': 26})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

temp_980, current_980, error_current_980 = np.loadtxt("current_threshold_980.txt", unpack=1, skiprows=1)
temp_850_vcsel, current_850_vcsel, error_current_850_vcsel = np.loadtxt("current_threshold_vcsel850.txt", unpack=1, skiprows=1)

temp_635, current_635, error_current_635 = np.loadtxt("current_threshold_635.txt", unpack=1, skiprows=1)
temp_850_p10, current_850_p10, error_current_850_p10 = np.loadtxt("current_threshold_850_p010.txt", unpack=1, skiprows=1)


ax1 = plt.subplot(121)
ax1.errorbar(temp_635, current_635, yerr=error_current_635, fmt='o', color="blue", label="krawędziówka 635\,nm")
ax1.errorbar(temp_850_p10, current_850_p10, yerr=error_current_850_p10, fmt='o', color="red", label="krawędziówka 850\,nm")
ax1.set_xlabel('Temperatura [K]')
ax1.set_ylabel('Prąd progowy [mA]')
plt.legend(loc='upper right', prop={'size':20})
plt.grid(True)

ax2 = plt.subplot(122)
ax2.errorbar(temp_980, current_980, yerr=error_current_980, fmt='o', color="green", label="VCSEL 980\,nm")
ax2.errorbar(temp_850_vcsel, current_850_vcsel, yerr=error_current_850_vcsel, fmt='o', color="red", label="VCSEL 850\,nm")
ax2.set_xlabel('Temperatura [K]')
ax2.set_ylabel('Prąd progowy [mA]')
plt.legend(loc=2, prop={'size':20})
plt.grid(True)

plt.show()