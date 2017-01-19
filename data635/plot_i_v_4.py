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

current_5, voltage_5, _ = np.loadtxt("temp_5.txt", unpack=True, skiprows=1)
current_15, voltage_15, _ = np.loadtxt("temp_15.txt", unpack=True, skiprows=1)
current_25, voltage_25, _ = np.loadtxt("temp_25.txt", unpack=True, skiprows=1)
current_35, voltage_35, _ = np.loadtxt("temp_35.txt", unpack=True, skiprows=1)

ax1 = plt.subplot(221)
ax1.plot(current_5*1000, voltage_5, 'go')
ax1.set_xlabel('Moc wejściowa [mW]')
ax1.set_ylabel('Napięcie [V]')
ax1.set_title("278 K")
plt.grid(True)

ax2 = plt.subplot(222)
ax2.plot(current_15*1000, voltage_15, 'go')
ax2.set_xlabel('Moc wejściowa [mW]')
ax2.set_ylabel('Napięcie [V]')
ax2.set_title("288 K")
plt.grid(True)

ax3 = plt.subplot(223)
ax3.plot(current_25*1000, voltage_25, 'go')
ax3.set_xlabel('Moc wejściowa [mW]')
ax3.set_ylabel('Napięcie [V]')
ax3.set_title("298 K")
plt.grid(True)

ax4 = plt.subplot(224)
ax4.plot(current_35*1000, voltage_35, 'go')
ax4.set_xlabel('Moc wejściowa [mW]')
ax4.set_ylabel('Napięcie [V]')
ax4.set_title("308 K")
plt.grid(True)



plt.show()