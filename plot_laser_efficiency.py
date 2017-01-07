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


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class PlotLaserEfficiency:
    def __init__(self, path_to_data):
        current, voltage, power = np.loadtxt(path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.output_power = power * 1000

    def get_data(self):
        return self.current, self.voltage, self.output_power

    def get_input_power(self):
        # return value mW
        return self.current*self.voltage

    def get_ratio_power(self):
        input_power = self.get_input_power()
        return self.output_power / input_power

    def plot_wall_plug_efficiency(self):
        fig, ax1 = plt.subplots()
        input_power = self.get_input_power()
        ax1.plot(input_power, self.output_power, 'bo')
        ax1.set_xlabel("Moc wejściowa [mW]")
        ax1.set_ylabel("Moc wyjściowa [mW]")
        ax1.set_xlim([0, max(input_power)])
        plt.grid(True)
        plt.show()

    def plot_ratio_power_to_current(self):
        fig, ax1 = plt.subplots()
        input_power = self.current * self.voltage
        ratio_power = self.get_ratio_power()
        ax1.plot(self.current, ratio_power, 'bo')
        ax1.set_xlabel("Prąd [mA]")
        ax1.set_ylabel("Moc wyjściowa / Moc wejściowa")
        ax1.set_xlim([0, max(input_power)])
        plt.grid(True)
        plt.show()


ple20 = PlotLaserEfficiency("dataVcsel850/temp_20.txt")
current_20, _, _ = ple20.get_data()
ratio_power_20 = ple20.get_ratio_power()

ple90 = PlotLaserEfficiency("dataVcsel850/temp_90.txt")
current_90, _, _ = ple90.get_data()
ratio_power_90 = ple90.get_ratio_power()

fig, ax1 = plt.subplots()

ax1.plot(current_20, ratio_power_20, 'bo', label="293 K")
ax1.plot(current_90, ratio_power_90, 'ro', label="363 K")
ax1.set_xlabel("Prąd [mA]")
ax1.set_ylabel("Moc wyjściowa / Moc wejściowa")
ax1.set_ylim([0, max(ratio_power_20) + 0.1*max(ratio_power_20)])
plt.legend(loc=2)
plt.grid(True)
plt.show()

#ple20.plot_wall_plug_efficiency()
#ple20.plot_ratio_power_to_current()