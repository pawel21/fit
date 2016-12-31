# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

matplotlib.use('qt5Agg')
matplotlib.rc('font', family='Arial')
matplotlib.rcParams['text.latex.unicode'] = True
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
        ax1.set_ylabel("logarytm z wartości prąd progowego , $\ln (I_{th})$")
        plt.grid(True)
        plt.show()

    def fit_temp_log_i_th(self, **kwargs):
        fig, ax1 = plt.subplots()
        ax1.plot(self.temp, np.log(self.threshold_current), 'bo', markersize=10)
        ax1.set_xlabel("Temperatura [K], $T$")
        ax1.set_ylabel("logarytm z wartości prądu progowego , $\ln (I_{th})$")

        popt, pcov = curve_fit(self.f, self.temp, np.log(self.threshold_current))
        a = popt[0]
        b = popt[1]
        error = np.diag(pcov)
        da = error[0]
        db = error[1]
        t0, dt0 = self.get_t0(a, da)
        i_0, di_0 = self.get_i_0(b, db)

        x = np.linspace(min(self.temp)-10, max(self.temp)+10, 101)
        y = a*x + b
        ax1.plot(x, y, 'r-')
        if kwargs.__contains__('x_text') and kwargs.__contains__("y_text") and kwargs.__contains__("dy_text"):
            plt.text(kwargs['x_text'], kwargs['y_text'], r"$\ln I_{th}=\frac{T}{T_{0}} + \ln I_{0}$", fontsize=30)
            plt.text(kwargs['x_text'], kwargs['y_text'] - kwargs["dy_text"],
                     r"$T_0 = (%.1f \pm %.1f)$ K" % (t0, dt0),
                     fontsize=30)
            plt.text(kwargs['x_text'], kwargs['y_text']-2*kwargs["dy_text"], r"$I_0 = (%.2f \pm %.2f)$ mA" %(i_0, di_0),
                     fontsize=30)
        print(u"a = %s \u00B1 %s" %(a, da))
        print(u"b = %s \u00B1 %s" % (b, db))
        print(u"T_0 = %s \u00B1 %s" % (t0, dt0))
        print(u"I_0 = %s \u00B1 %s" % (i_0, di_0))
        plt.grid(True)
        plt.show()

    @staticmethod
    def f(x, a, b):
        return a*x + b

    @staticmethod
    def get_t0(a, da):
        t0 = 1 / a
        dt0 = abs(-1 / a ** 2) * da
        return t0, dt0

    @staticmethod
    def get_i_0(b, db):
        i_th = np.e ** b
        di_th = abs(b * np.e ** b) * db
        return i_th, di_th


def temp_celsjusz_to_kelvin(temp_c):
    return temp_c + 273

temp_C = np.arange(10, 95, 10)
temp_K = list(map(temp_celsjusz_to_kelvin, temp_C))
I_0_vscel850 = [1.7, 1.6, 1.6, 1.6, 1.7, 1.9, 2.1, 2.3, 2.7]
I_0_980 = [1.0, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.4]

pl_vscel850 = PlotThresholdCurrentTemp(I_0_vscel850, temp_K)
#pl_vscel850.fit_temp_log_i_th(x_text=340, y_text=0.2, dy_text=0.15)
#pl_vscel850.plot_linear_temp_i_th

pl_980 = PlotThresholdCurrentTemp(I_0_980, temp_K)
pl_980.plot_linear_temp_i_th
#pl_980.plot_temp_log_i_th
pl_980.fit_temp_log_i_th(x_text=340, y_text=0.2, dy_text=0.10)