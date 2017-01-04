# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sympy.solvers import solve
from sympy import Symbol

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

current_10, voltage_10, power_10 = np.loadtxt("dataVcsel850/temp_10.txt", unpack=True, skiprows=1)
current_90, voltage_90, power_90 = np.loadtxt("dataVcsel850/temp_90.txt", unpack=True, skiprows=1)
fig, ax1 = plt.subplots()
ax1.plot(current_10, power_10, 'ko', markersize=5)
ax1.plot(current_90, power_90, 'bo', markersize=5)
a =  0.32682
b = -0.000553
x = np.linspace(0, 0.007, 100)
y = a *x + b
ax1.axhline(0., ls='-', color='k')
ax1.plot(x, y, 'r-', linewidth=2)
ax1.set_xticks(list(np.linspace(0., 0.02, 21)))
ax1.set_xticklabels([])
ax1.set_yticks(list(np.linspace(0, 0.007, 8)))
ax1.set_yticklabels([])
ax1.set_xlabel(u"prąd [mA], $I$")
ax1.set_ylabel("moc wyjściowa [mW], $P$")

ax1.text(0.003, 0.0008, '$P = a \cdot I + b$', verticalalignment='bottom', horizontalalignment='right',
        color='red', fontsize=25)
ax1.text(0.0027, -0.00055, r"$I_0 = - \frac{b}{a}$", verticalalignment='bottom', horizontalalignment='right',
        color='red', fontsize=25)
ax1.text(0.0078, 0.0026, r"$T_1", verticalalignment='bottom', horizontalalignment='right',
         color='black', fontsize=25)
ax1.text(0.010, 0.0017, r"$T_2", verticalalignment='bottom', horizontalalignment='right',
         color='blue', fontsize=25)
ax1.text(0.016, 0.003, r"$T_2 > T_1", verticalalignment='bottom', horizontalalignment='right',
         color='black', fontsize=25)
plt.grid(True)

plt.show()
