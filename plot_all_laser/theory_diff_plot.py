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
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


x_2 = np.linspace(0, 1.1, 20)
y_2 = x_2**12

x_3 = [1.1, 2.3]
y_3 = [1.1**12, 50]

fig, ax1 = plt.subplots()

ax1.plot(x_2, y_2, 'b-', linewidth=2)
ax1.plot(x_3, y_3, 'b-', linewidth=2)

ax1.set_xticks(list(np.linspace(0., 2.3, 21)))
ax1.set_xticklabels([])
ax1.set_yticks(list(np.linspace(0., 50, 21)))
ax1.set_yticklabels([0])
ax1.set_xlabel("Prąd")
ax1.set_ylabel("Moc wyjściowa")
plt.annotate("Prąd progowy", (1.0, 2.8), xycoords='data',
xytext=(0.65, 20),
arrowprops=dict(arrowstyle='->'))
plt.grid(True)
plt.show()