# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
matplotlib.rc('font', family='Arial')
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Arial"
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})


class PlotThresholdCurrentTemp:
    def __init__(self, threshold_current, temp):
        self.threshold_current = threshold_current
        self.temp = temp

    def __repr__(self):
        return 'temperature [K]: %s\nthreshold current [mA]: %s ' %(self.temp, self.threshold_current)

    @property
    def plot_linear_temp_i_th(self):
        fig, ax1 = plt.subplots()
        ax1.plot(self.temp, self.threshold_current, 'ro', markersize=10)
        ax1.set_xlabel("Temperatura [K], $T$")
        ax1.set_ylabel("Prąd progowy [mA], $I_{th}$")
        ax1.set_ylim([min(self.threshold_current)-0.1*min(self.threshold_current),
                      max(self.threshold_current)+0.1 * max(self.threshold_current)])
        plt.grid(True)
        plt.show()

    @property
    def plot_temp_log_i_th(self):
        fig, ax1 = plt.subplots()
        ax1.plot(self.temp, np.log(self.threshold_current), 'bo', markersize=10)
        ax1.set_xlabel("Temperatura [K], $T$")
        ax1.set_ylabel("Prąd progowy [mA], $I_{th}$")
        plt.grid(True)
        plt.show()


def temp_celsjusz_to_kelvin(temp_c):
    return temp_c + 273

temp_C = np.arange(10, 95, 10)
temp_K = list(map(temp_celsjusz_to_kelvin, temp_C))
I_0_vscel850 = [1.7, 1.6, 1.6, 1.6, 1.7, 1.9, 2.1, 2.3, 2.7]
I_0_980 = [1.0, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.4]

pl_vscel850 = PlotThresholdCurrentTemp(I_0_vscel850, temp_K)
pl_vscel850.plot_linear_temp_i_th

pl_980 = PlotThresholdCurrentTemp(I_0_980, temp_K)
pl_980.plot_linear_temp_i_th
pl_980.plot_temp_log_i_th
