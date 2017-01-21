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

current_5, voltage_5, power_5 = np.loadtxt("temp_5.txt", unpack=True, skiprows=1)
current_15, voltage_15, power_15 = np.loadtxt("temp_15.txt", unpack=True, skiprows=1)
current_25, voltage_25, power_25 = np.loadtxt("temp_25.txt", unpack=True, skiprows=1)
current_35, voltage_35, power_35 = np.loadtxt("temp_35.txt", unpack=True, skiprows=1)

fig, ax1 = plt.subplots()
ax1 = plt.subplot(221)
ax2 = ax1.twinx()
ax1.plot(current_5 * 1000, power_5 * 1000, marker='o', color='red', ls='none')
ax2.plot(current_5 * 1000, voltage_5, marker='o', color='green', ls='none')

ax1.set_xlabel('Prąd [mA]')
ax1.set_ylabel('Moc wyjściowa [mW]', color="red")
ax2.set_ylabel("Napięcie [V]", color="green")
ax1.set_title("278 K")
ax2.yaxis.labelpad = 15
for ax1_y_tick in ax1.get_yticklabels():
    ax1_y_tick.set_color("red")
for ax2_y_tick in ax2.get_yticklabels():
    ax2_y_tick.set_color("green")
#ax1.set_ylim([1.8, 2.25])
plt.grid(True)

ax3 = plt.subplot(222)
ax4 = ax3.twinx()
ax3.plot(current_15 * 1000, power_15 * 1000, marker='o', color='red', ls='none')
ax4.plot(current_15 * 1000, voltage_15, marker='o', color='green', ls='none')

ax3.set_xlabel('Prąd [mA]')
ax3.set_ylabel('Moc wyjściowa [mW]', color="red")
ax4.set_ylabel("Napięcie [V]", color="green")
ax4.yaxis.labelpad = 15
ax4.set_title("288 K")
for ax3_y_tick in ax3.get_yticklabels():
    ax3_y_tick.set_color("red")
for ax4_y_tick in ax4.get_yticklabels():
    ax4_y_tick.set_color("green")
plt.grid(True)

ax5 = plt.subplot(223)
ax6 = ax5.twinx()
ax5.plot(current_25 * 1000, power_25 * 1000, marker='o', color='red', ls='none')
ax6.plot(current_25 * 1000, voltage_25, marker='o', color='green', ls='none')

ax5.set_xlabel('Prąd [mA]')
ax5.set_ylabel('Moc wyjściowa [mW]', color="red")
ax6.set_ylabel("Napięcie [V]", color="green")
ax6.set_title("298 K")
ax6.yaxis.labelpad = 15
for ax5_y_tick in ax5.get_yticklabels():
    ax5_y_tick.set_color("red")
for ax6_y_tick in ax6.get_yticklabels():
    ax6_y_tick.set_color("green")
plt.grid(True)

ax7 = plt.subplot(224)
ax8 = ax7.twinx()
ax7.plot(current_35 * 1000, power_35 * 1000, marker='o', color='red', ls='none')
ax8.plot(current_35 * 1000, voltage_35, marker='o', color='green', ls='none')

ax7.set_xlabel('Prąd [mA]')
ax7.set_ylabel('Moc wyjściowa [mW]', color="red")
ax8.set_ylabel("Napięcie [V]", color="green")
ax8.set_title("308 K")
ax8.yaxis.labelpad = 15
for ax7_y_tick in ax7.get_yticklabels():
    ax7_y_tick.set_color("red")
for ax8_y_tick in ax8.get_yticklabels():
    ax8_y_tick.set_color("green")
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()