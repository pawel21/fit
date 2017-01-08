# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

I, V, L = np.loadtxt("temp_10.txt", unpack=True, skiprows=1)

x = []
y = []

for i in range(0, len(I)-1):
    if I[i] != I[i+1]:
        x.append(I[i])
        y.append(L[i])

fig, ax1 = plt.subplots()
ax1.plot(x, y, 'ko', markersize=5)
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

ax1.text(0.0035, 0.0008, '$P = a \cdot I + b$', verticalalignment='bottom', horizontalalignment='right',
         color='red', fontsize=28)
ax1.text(0.0028, -0.00045, r"$I_{th} = - \frac{b}{a}$", verticalalignment='bottom', horizontalalignment='right',
         color='red', fontsize=28)
plt.grid(True)
plt.show()