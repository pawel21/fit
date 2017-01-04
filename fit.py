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


#matplotlib.rc('font', family='Arial')
#matplotlib.rcParams['text.latex.unicode'] = True
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#plt.rcParams["font.family"] = "Arial"
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Fit:
    def __init__(self, path_to_data, temp):
        self.path_to_data = path_to_data
        self.temp = temp + 273
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
        self._fit_plot(start_to_fit, end_to_fit)
        print(u"a = %s \u00B1 %s" %(self.a, self.da))
        print(u"b = %s \u00B1 %s" % (self.b, self.db))
        print(u"I_0 = (%.10f \u00B1 %.10f) mA" %(self.I_0*1000, self.dI_0*1000))
        return self.a, self.da, self.b, self.db, self.I_0, self.dI_0

    def get_fit_parameters(self):
        return self.a, self.da, self.b, self.db, self.I_0, self.dI_0

    def _get_data_to_fit(self, start_to_fit, end_to_fit):
        x_to_fit = []
        y_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i] > start_to_fit and self.current[i] < end_to_fit:
                x_to_fit.append(self.current[i])
                y_to_fit.append(self.power[i])
        np.savetxt('data_to_fit.txt', np.c_[x_to_fit, y_to_fit], fmt='%1.12e', header=' J [A] \t V \t L [w] ')
        return x_to_fit, y_to_fit

    def _find_I0(self):
        I = Symbol('I')
        I_0 = solve(self.a * I + self.b, I)
        return float(I_0[0])

    def _find_dI0(self):
        return abs((-self.b/(self.a**2))) * self.da + abs((-1/self.a)) * self.db

    def save_info(self, path):
        with open(path, "a") as f:
            f.write("plik = %s \t a = %s \t da = %s \t b = %s \t db = %s \t I_0 = %s \t dI_0 = %s \n"
                    % (self.path_to_data, self.a, self.da, self.b, self.db, self.I_0, self.dI_0))

    def _fit_plot(self, start_to_fit, end_to_fit):
        fig, ax1 = plt.subplots()
        ax1.plot(self.current, self.power, 'ro', markersize=4)
        x = np.linspace(0, end_to_fit, 100)
        y = self.a *x + self.b
        ax1.axhline(0., ls='-', color='k')
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.set_xticks(list(np.linspace(0., 0.02, 21)))
        ax1.set_xticklabels(np.linspace(0., 20., 21))
        ax1.set_yticks(list(np.linspace(0, 0.007, 8)))
        ax1.set_yticklabels(list(np.linspace(0, 7, 8)))
        plt.text(0.0018, -0.0004, "$I_{th}$ = (%.2f $\pm$ %.2f)mA" % (float(self.I_0*1000), self.dI_0*1000 + 0.01))
        ax1.set_xlabel(u"prąd [mA]")
        ax1.set_ylabel(u"moc wyjściowa [mW]")
        plt.grid(True)
        plt.show()


fit = Fit("dataVcsel850/temp_10.txt", 10)
fit.do_fit(0.0016, 0.007)
