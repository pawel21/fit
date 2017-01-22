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
        print(u"I_th = (%.10f \u00B1 %.10f) mA" % (self.I_th, self.dI_th))
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



pl5 = Fit("temp_5.txt")
a_5, b_5, I_th_5, dI_th_5 = pl5.do_fit(19.8, 25)
x_5 = np.linspace(19, 25, 100)
y_5 = a_5 * x_5 + b_5
current_5, voltage_5, power_5 = pl5.get_data
ax1 = plt.subplot(221)
ax1.plot(current_5, power_5, 'r^', markersize=7)
ax1.plot(x_5, y_5, 'b-', linewidth=2)
ax1.axhline(color='black')
ax1.set_xlabel(u"prąd [mA]")
ax1.set_ylabel(u"moc wyjściowa [mW]")
ax1.set_xlim([15, 25])
ax1.set_ylim([-0.6, 4])
ax1.text(18, -0.5, "$I_{\mathrm{th}}$ = (%.1f $\pm$ %.1f)\,mA" % (19.1, 0.2), size=22)
ax1.set_title("278\,K")
plt.grid(True)


pl25 = Fit("temp_25.txt")
a_25, b_25, I_th_25, dI_th_25 = pl25.do_fit(28, 32)
x_25 = np.linspace(27.8, 32, 100)
y_25 = a_25 * x_25 + b_25
current_25, voltage_25, power_25 = pl25.get_data
ax3 = plt.subplot(222)
ax3.plot(current_25, power_25, 'r^', markersize=7)
ax3.plot(x_25, y_25, 'b-', linewidth=2)
ax3.axhline(color='black')
ax3.set_xlabel(u"prąd [mA]")
ax3.set_ylabel(u"moc wyjściowa [mW]")
ax3.set_xlim([25, 30])
ax3.set_ylim([-0.3, 1.2])
ax3.text(27.5, -0.19, "$I_{\mathrm{th}}$ = (%.1f $\pm$ %.1f)\,mA" % (27.9, 0.3), size=22)
ax3.set_title("298\,K")
plt.grid(True)
#
#
pl15 = Fit("temp_15.txt")
a_15, b_15, I_th_15, di_th_15 = pl15.do_fit(23, 28)
x_15 = np.linspace(22.5, 28, 100)
y_15 = a_15 * x_15 + b_15
current_15, voltage_15, power_15 = pl15.get_data
ax2 = plt.subplot(223)
ax2.plot(current_15, power_15, 'r^', markersize=7)
ax2.plot(x_15, y_15, 'b-', linewidth=2)
ax2.axhline(color='black')
ax2.set_xlabel(u"prąd [mA]")
ax2.set_ylabel(u"moc wyjściowa [mW]")
ax2.set_xlim([20, 28])
ax2.set_ylim([-0.8, 3.5])
ax2.text(21.5, -0.5, "$I_{\mathrm{th}}$ = (%.1f $\pm$ %.1f)\,mA" % (22.6, 0.2), size=22)
ax2.set_title("288\,K")
plt.grid(True)


pl35 = Fit("temp_35.txt")
a_35, b_35, I_th_35, dI_th_35 = pl35.do_fit(36, 39)
x_35 = np.linspace(35.9, 39, 100)
y_35 = a_35 * x_35 + b_35
current_35, voltage_35, power_35 = pl35.get_data
ax4 = plt.subplot(224)
ax4.plot(current_35, power_35, 'r^', markersize=7)
ax4.plot(x_35, y_35, 'b-', linewidth=2)
ax4.axhline(color='black')
ax4.set_xlabel(u"prąd [mA]")
ax4.set_ylabel(u"moc wyjściowa [mW]")
ax4.set_xlim([32, 39])
ax4.set_ylim([-0.2, 1.2])
ax4.text(35.5, -0.15, "$I_{\mathrm{th}}$ = (%d $\pm$ %d)\,mA" % (36.0, 2.0), size=22)
ax4.set_title("308\,K")
plt.grid(True)


plt.subplots_adjust(left=0.06, right=0.94, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)

plt.show()

#from matplotlib2tikz import save as tikz_save
#tikz_save('plot_i_th4.tex')