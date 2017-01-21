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
SPACE_BETWEEN_VALUE_AND_LABEL = 8

current_10, voltage_10, power_10 = np.loadtxt("temp_10.txt", unpack=True, skiprows=1)
current_25, voltage_25, power_25 = np.loadtxt("temp_25.txt", unpack=True, skiprows=1)
current_55, voltage_55, power_55 = np.loadtxt("temp_55.txt", unpack=True, skiprows=1)
current_90, voltage_90, power_90 = np.loadtxt("temp_90.txt", unpack=True, skiprows=1)

fig, ax1 = plt.subplots()
ax1 = plt.subplot(221)
ax2 = ax1.twinx()
ax1.plot(current_10 * 1000, power_10 * 1000, marker='o', color='red', ls='none')
ax2.plot(current_10 * 1000, voltage_10, marker='o', color='green', ls='none')

ax1.set_xlabel('Prąd [mA]')
ax1.set_ylabel('Moc wyjściowa [mW]', color="red")
ax2.set_ylabel("Napięcie [V]", color="green")
ax1.set_title("283 K")
ax1.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
ax2.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
for ax1_y_tick in ax1.get_yticklabels():
    ax1_y_tick.set_color("red")
for ax2_y_tick in ax2.get_yticklabels():
    ax2_y_tick.set_color("green")
plt.grid(True)

ax3 = plt.subplot(222)
ax4 = ax3.twinx()
ax3.plot(current_55 * 1000, power_55 * 1000, marker='o', color='red', ls='none')
ax4.plot(current_55 * 1000, voltage_55, marker='o', color='green', ls='none')

ax3.set_xlabel('Prąd [mA]')
ax3.set_ylabel('Moc wyjściowa [mW]', color="red")
ax4.set_ylabel("Napięcie [V]", color="green")
ax3.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
ax4.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
ax4.set_title("328 K")
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
ax5.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
ax6.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
for ax5_y_tick in ax5.get_yticklabels():
    ax5_y_tick.set_color("red")
for ax6_y_tick in ax6.get_yticklabels():
    ax6_y_tick.set_color("green")
plt.grid(True)

ax7 = plt.subplot(224)
ax8 = ax7.twinx()
ax7.plot(current_90 * 1000, power_90 * 1000, marker='o', color='red', ls='none')
ax8.plot(current_90 * 1000, voltage_90, marker='o', color='green', ls='none')

ax7.set_xlabel('Prąd [mA]')
ax7.set_ylabel('Moc wyjściowa [mW]', color="red")
ax8.set_ylabel("Napięcie [V]", color="green")
ax8.set_title("363 K")
ax7.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
ax8.yaxis.labelpad = SPACE_BETWEEN_VALUE_AND_LABEL
for ax7_y_tick in ax7.get_yticklabels():
    ax7_y_tick.set_color("red")
for ax8_y_tick in ax8.get_yticklabels():
    ax8_y_tick.set_color("green")
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()