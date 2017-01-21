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
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Fit:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.current, self.voltage, self.power = np.loadtxt(self.path_to_data, unpack=True, skiprows=1)
        self.a = 0
        self.b = 0
        self.da = 0
        self.db = 0
        self.I_th = 0
        self.dI_th = 0

    @staticmethod
    def f(x, a, b):
        return a*x + b

    def do_fit(self, start_to_fit, end_to_fit):
        x, y = self._get_data_to_fit(start_to_fit, end_to_fit)
        popt, pcov = curve_fit(self.f, x, y)
        self.a = popt[0]
        self.b = popt[1]
        error = np.abs(np.diag(pcov)**0.5)
        self.da = error[0]
        self.db = error[1]
        self.I_th = self._find_I0()
        self.dI_th = self._find_dI0()
        print(u"a = %s \u00B1 %s" % (self.a, self.da))
        print(u"b = %s \u00B1 %s" % (self.b, self.db))
        print(u"I_0 = (%.10f \u00B1 %.10f) mA" % (self.I_th, self.dI_th))
        #self._fit_plot(start_to_fit, end_to_fit)
        return self.a, self.b, self.I_th, self.dI_th

    @property
    def get_data(self):
        return self.current*1000, self.voltage*1000, self.power*1000

    def get_fit_parameters(self):
        return self.a, self.da, self.b, self.db, self.I_th, self.dI_th

    def _get_data_to_fit(self, start_to_fit, end_to_fit):
        x_to_fit = []
        y_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i]*1000 > start_to_fit and self.current[i]*1000 < end_to_fit:
                x_to_fit.append(self.current[i]*1000)
                y_to_fit.append(self.power[i]*1000)
        np.savetxt('data_to_fit.txt', np.c_[x_to_fit, y_to_fit], fmt='%1.12e', header=' J [A] \t V \t L [w] ')
        return x_to_fit, y_to_fit

    def _find_I0(self):
        I = Symbol('I')
        I_th = solve(self.a * I + self.b, I)
        return float(I_th[0])

    def _find_dI0(self):
        return abs((-self.b/(self.a**2))) * self.da + abs((-1/self.a)) * self.db

    def _fit_plot(self, start_to_fit, end_to_fit):
        fig, ax1 = plt.subplots()
        ax1.plot(self.current * 1000, self.power * 1000, 'ro', markersize=4)
        ax1.set_xlim([0, max(self.current * 1000)])
        ax1.set_ylim([0, max(self.power * 1000)])
        x = np.linspace(start_to_fit, end_to_fit, 100)
        y = self.a * x + self.b
        ax1.axhline(0., ls='-', color='k')
        ax1.plot(x, y, 'b-', linewidth=2)
        plt.text(start_to_fit + 0.1 * start_to_fit, 0.1,
                 "$I_{th}$ = (%.1f $\pm$ %.1f)mA" % (float(self.I_th), self.dI_th + 0.1))
        ax1.set_xlabel(u"prąd [mA]")
        ax1.set_ylabel(u"moc wyjściowa [mW]")
        plt.grid(True)
        plt.show()

pl10 = Fit("temp_10.txt")
a_10, b_10, I_0_20, dI_0_10 = pl10.do_fit(1.65, 6)
x_10 = np.linspace(1.6, 5, 100)
y_10 = a_10 * x_10 + b_10
current_10, voltage_10, power_10 = pl10.get_data

ax1 = plt.subplot(221)
ax1.plot(current_10, power_10, 'r^', markersize=7)
ax1.plot(x_10, y_10, 'b-', linewidth=2)
ax1.axhline(color='black')
ax1.set_xlabel(u"prąd [mA]")
ax1.set_ylabel(u"moc wyjściowa [mW]")
ax1.set_xlim([0, 5])
ax1.set_ylim([-0.3, 1.2])
ax1.text(1.5, -0.15, "$I_{\mathrm{th}}$ = (%.2f $\pm$ %.2f)mA" % (1.70, 0.03), size=20)
ax1.set_title("283 K")
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()