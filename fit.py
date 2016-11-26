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

matplotlib.rc('font', family='Arial')
matplotlib.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})


class Fit:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.current, self.voltage, self.power = np.loadtxt(self.path_to_data,
                                                            unpack=True, skiprows=1)

    @staticmethod
    def f(x, a, b):
        return a*x + b

    def do_fit(self, start_to_fit, end_to_fit):
        x, y = self._get_data_to_fit(start_to_fit, end_to_fit)

        popt, pcov = curve_fit(self.f, x, y)
        self.a = popt[0]
        self.b = popt[1]
        self.I_0 = self._find_I0()
        self._fit_plot(start_to_fit, end_to_fit)

    def _get_data_to_fit(self, start_to_fit, end_to_fit):
        x_to_fit = []
        y_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i] > start_to_fit and self.current[i] < end_to_fit:
                x_to_fit.append(self.current[i])
                y_to_fit.append(self.power[i])
        return x_to_fit, y_to_fit

    def _find_I0(self):
        I = Symbol('I')
        I_0 = solve(self.a * I + self.b, I)
        return I_0

    def _fit_plot(self, start_to_fit, end_to_fit):
        plt.plot(self.current, self.power, 'bo', markersize=4)
        x = np.linspace(0, end_to_fit, 100)
        y = self.a *x + self.b
        plt.axhline(0., ls='-', color='k')
        plt.plot(x, y, 'r-', linewidth=2)
        plt.text(0.015, 0.0015, "$L = a \cdot I + b$")
        plt.text(0.015, 0.0011, r"$a$ = %.3f $\frac{W}{A}$" % self.a)
        plt.text(0.015, 0.0007, "$b$ = %.5f $\mathtt{W}$" % self.b)
        plt.text(0.015, 0.0003, "$I_0$ = %.6f $\mathtt{A}$" % float(self.I_0[0]))
        plt.xlabel("prąd $[\mathtt{A}] $, $I$")
        plt.ylabel("moc $[\mathtt{W}]$, $L$")
        plt.grid(True)
        plt.show()

    @property
    def plot_I_V_L(self):
        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.plot(self.current, self.power, marker='o', color='red', ls='none')
        ax2.plot(self.current, self.voltage, marker='o', color='green', ls='none')

        ax1.set_xlabel('Prąd $[\mathtt{A}]$')
        ax1.set_ylabel('Moc $[\mathtt{W}]$', color='r')
        ax2.set_ylabel('Napięcie $[\mathtt{V}]$', color='g')

        ax1.set_ylim([0, max(self.power) + 0.1 * max(self.power)])
        ax2.set_ylim([0, max(self.voltage)+0.1 * max(self.voltage)])
        plt.grid(True)
        plt.show()

fit = Fit("data980/temp_10.txt")
fit.do_fit(0.002, 0.01)
