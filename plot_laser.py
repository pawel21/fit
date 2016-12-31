# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.family"] = "Arial"
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})


class PlotLaser:
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    def __init__(self, path_to_data, temp):
        self.path_to_data = path_to_data
        self.temp = temp + 273
        self.current, self.voltage, self.power = np.loadtxt(self.path_to_data, unpack=True, skiprows=1)

    def plot_ivl(self):
        self.ax1.plot(self.current, self.power, marker='o', color='red', ls='none')
        self.ax2.plot(self.current, self.voltage, marker='o', color='green', ls='none')

        self._set_label()
        self._set_ax1_ticks()
        self._set_ticks_color()
        self._set_limit()

        plt.grid(True)
        plt.show()

    def _set_label(self):
        self.ax1.set_xlabel('Prąd [mA]')
        self.ax1.set_ylabel('Moc wyjściowa [mW]', color='r')
        self.ax2.set_ylabel('Napięcie [V]', color='g')

    def _set_ax1_ticks(self):
        self.ax1.set_xticks(list(np.linspace(0., 0.02, 5)))
        self.ax1.set_xticklabels(np.linspace(0., 20, 5, dtype=int))
        self.ax1.set_yticks(list(np.linspace(0, 0.007, 8)))
        self.ax1.set_yticklabels(list(np.linspace(0, 7, 8)))

    def _set_ticks_color(self):
        for ax1_y_tick in self.ax1.get_yticklabels():
            ax1_y_tick.set_color("red")
        for ax2_y_tick in self.ax2.get_yticklabels():
            ax2_y_tick.set_color("green")

    def _set_limit(self):
        self.ax1.set_ylim([0, max(self.power) + 0.1 * max(self.power)])
        self.ax2.set_ylim([0, max(self.voltage) + 0.1 * max(self.voltage)])

    def _add_info(self):
        plt.text(0.003, 2, "%s K" %self.temp)

    def plot_power(self):
        fig, ax3 = plt.subplots()
        power_in = self.current * self.voltage
        ax3.plot(power_in, self.power, 'bo')
        ax3.set_xlabel("Moc wejściowa [mW]")
        ax3.set_ylabel("Moc wyjściowa [mW]")

        ax3.set_xlim([0, max(power_in) + 0.1 * max(power_in)])
        ax3.set_ylim([0, max(self.power) + 0.1 * max(self.power)])
        ax3.set_xticks(list(np.linspace(0., 0.045, 10)))
        ax3.set_xticklabels(np.linspace(0., 45, 10))
        ax3.set_yticks(list(np.linspace(0, 0.007, 8)))
        ax3.set_yticklabels(list(np.linspace(0, 7, 8)))
        plt.grid(True)
        plt.show()

pl = PlotLaser("dataVcsel850/temp_10.txt", 10)
pl.plot_ivl()
#pl.plot_power()