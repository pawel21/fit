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


class PlotTheoryExp:
    def __init__(self, temp, threshold_current, error_threshold_current, I_0, T_0):
        self.temp = temp
        self.threshold_current = threshold_current
        self.error_threshold_current = error_threshold_current
        self.I_0 = I_0
        self.T_0 = T_0

    def plot(self):
        fig, ax1 = plt.subplots()
        temp = np.linspace(min(self.temp)-10, max(self.temp), 51)
        i_th = self.I_0 * np.exp(temp / self.T_0)
        ax1.plot(temp, i_th)
        ax1.errorbar(self.temp, self.threshold_current, yerr=self.error_threshold_current)
        ax1.set_xlabel("Temperatura [K], $T$")
        ax1.set_ylabel("Prąd progowy [mA],$I_{th}$ ")
        plt.text(300, 60, r"$I_{th}$ = $0.03 \cdot \exp \left( \frac{T}{43.2} \right)$")
        plt.grid(True)
        plt.show()


temp_635 = np.linspace(20, 40, 5) + 273
I_th_635 = [22.4, 25.0, 28.1, 31.3, 35.7]
y_err = [0.3, 0.2, 0.3, 0.6, 0.9]
I_0_635, T_0_635 = 0.025, 43.2

plot635 = PlotTheoryExp(temp_635, I_th_635, y_err, I_0_635, T_0_635)
plot635.plot()