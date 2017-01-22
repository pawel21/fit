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
a_10, b_10, I_0_10, dI_0_10 = pl10.do_fit(1.65, 6)
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


pl55 = Fit("temp_55.txt")
a_55, b_55, I_0_55, dI_0_55 = pl55.do_fit(1.85, 6)
x_55 = np.linspace(1.7, 5, 100)
y_55 = a_55 * x_55 + b_55
current_55, voltage_55, power_55 = pl55.get_data
ax3 = plt.subplot(222)
ax3.plot(current_55, power_55, 'r^', markersize=7)
ax3.plot(x_55, y_55, 'b-', linewidth=2)
ax3.axhline(color='black')
ax3.set_xlabel(u"prąd [mA]")
ax3.set_ylabel(u"moc wyjściowa [mW]")
ax3.set_xlim([0, 5])
ax3.set_ylim([-0.3, 1.2])
ax3.text(1.7, -0.15, "$I_{\mathrm{th}}$ = (%.2f $\pm$ %.2f)mA" % (1.83, 0.04), size=20)
ax3.set_title("328 K")
plt.grid(True)


pl25 = Fit("temp_25.txt")
a_25, b_25, I_0_25, dI_0_25 = pl25.do_fit(1.55, 6)
x_25 = np.linspace(1.5, 5, 100)
y_25 = a_25 * x_25 + b_25
current_25, voltage_25, power_25 = pl25.get_data
ax2 = plt.subplot(223)
ax2.plot(current_25, power_25, 'r^', markersize=7)
ax2.plot(x_25, y_25, 'b-', linewidth=2)
ax2.axhline(color='black')
ax2.set_xlabel(u"prąd [mA]")
ax2.set_ylabel(u"moc wyjściowa [mW]")
ax2.set_xlim([0, 5])
ax2.set_ylim([-0.3, 1.2])
ax2.text(1.5, -0.15, "$I_{\mathrm{th}}$ = (%.2f $\pm$ %.2f)mA" % (1.55, 0.03), size=20)
ax2.set_title("298 K")
plt.grid(True)


pl90 = Fit("temp_90.txt")
a_90, b_90, I_0_90, dI_0_90 = pl90.do_fit(2.9, 5.5)
x_90 = np.linspace(2.7, 5, 100)
y_90 = a_90 * x_90 + b_90
current_90, voltage_90, power_90 = pl90.get_data
ax4 = plt.subplot(224)
ax4.plot(current_90, power_90, 'r^', markersize=7)
ax4.plot(x_90, y_90, 'b-', linewidth=2)
ax4.axhline(color='black')
ax4.set_xlabel(u"prąd [mA]")
ax4.set_ylabel(u"moc wyjściowa [mW]")
ax4.set_xlim([0, 5])
ax4.set_ylim([-0.2, 0.7])
ax4.text(2.5, -0.1, "$I_{\mathrm{th}}$ = (%.1f $\pm$ %.1f)mA" % (2.8, 0.1), size=20)
ax4.set_title("363 K")
plt.grid(True)


plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()