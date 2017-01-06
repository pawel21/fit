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


class Fit:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.current, self.voltage, self.power = np.loadtxt(self.path_to_data, unpack=True, skiprows=1)
        self.a = 0
        self.b = 0
        self.da = 0
        self.db = 0
        self.I_0 = 0
        self.dI_0 = 0

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
        self.I_0 = self._find_I0()
        self.dI_0 = self._find_dI0()
        print(u"a = %s \u00B1 %s" % (self.a, self.da))
        print(u"b = %s \u00B1 %s" % (self.b, self.db))
        print(u"I_0 = (%.10f \u00B1 %.10f) mA" % (self.I_0, self.dI_0))
        #self._fit_plot(start_to_fit, end_to_fit)
        return self.a, self.b, self.I_0, self.dI_0

    @property
    def get_data(self):
        return self.current*1000, self.voltage*1000, self.power*1000

    def get_fit_parameters(self):
        return self.a, self.da, self.b, self.db, self.I_0, self.dI_0

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
        I_0 = solve(self.a * I + self.b, I)
        return float(I_0[0])

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
                 "$I_{th}$ = (%.1f $\pm$ %.1f)mA" % (float(self.I_0), self.dI_0 + 0.1))
        ax1.set_xlabel(u"prąd [mA]")
        ax1.set_ylabel(u"moc wyjściowa [mW]")
        plt.grid(True)
        plt.show()

pl20 = Fit("data_635nm_20.txt")
a_20, b_20, I_0_20, dI_0_20 = pl20.do_fit(22.4, 29)
x_20 = np.linspace(22.4, 29, 100)
y_20 = a_20*x_20 + b_20
current_20, voltage_20, power_20 = pl20.get_data

pl30 = Fit("data_635nm_30.txt")
a_30, b_30, I_0_30, dI_0_30 = pl30.do_fit(28, 35)
x_30 = np.linspace(28, 35, 100)
y_30 = a_30*x_30 + b_30
current_30, voltage_30, power_30 = pl30.get_data

pl35 = Fit("data_635nm_35.txt")
a_35, b_35, I_0_35, dI_0_35 = pl35.do_fit(31.2, 35)
x_35 = np.linspace(31.2, 35, 100)
y_35 = a_35*x_35 + b_35
current_35, voltage_35, power_35 = pl35.get_data

fig, ax1 = plt.subplots()

ax1.plot(current_20, power_20, 'ko', markersize=5,label="293 K")
ax1.plot(x_20, y_20, 'r-', linewidth=2)
plt.text(20, -0.8, "$I_{th}$ = (%.1f $\pm$ %.1f)mA" % (float(I_0_20), dI_0_20 + 0.1), size=22, color="black")

ax1.plot(current_30, power_30, 'bo', markersize=5, label="303 K")
ax1.plot(x_30, y_30, 'r-', linewidth=2)
plt.text(25, -0.8, "$I_{th}$ = (%.1f $\pm$ %.1f)mA" % (float(I_0_30), dI_0_30 + 0.1), size=22, color="blue")

ax1.plot(current_35, power_35, 'go', markersize=5, label="308 K")
ax1.plot(x_35, y_35, 'r-', linewidth=2)
plt.text(30, -0.8, "$I_{th}$ = (%.1f $\pm$ %.1f)mA" % (float(I_0_35), dI_0_35 + 0.1), size=22, color="green")

ax1.set_xlabel(u"prąd [mA]")
ax1.set_ylabel(u"moc wyjściowa [mW]")

plt.legend(loc=2)
plt.grid(True)
plt.show()