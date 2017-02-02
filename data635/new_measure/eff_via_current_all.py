# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Eff:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        current, voltage, power = np.loadtxt(path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.output_power = power * 1000

    def get_input_power(self):
        return self.current*self.voltage

    def fit_slope_eff(self, threshold_current):
        #ax = plt.subplot()
        #ax.plot(self.current, self.output_power, 'bo')
        current_to_fit, power_to_fit = self.get_data_to_fit_via_current(threshold_current)
        popt, pcov = curve_fit(self.poly_2, current_to_fit, power_to_fit)
        a = popt[0]
        b = popt[1]
        c = popt[2]
        #ax.plot(current_to_fit, a*current_to_fit**2 + b*current_to_fit + c, 'r-')
        #plt.show()
        x = current_to_fit
        y = 2*a*current_to_fit + b
        return x, y

    @staticmethod
    def poly1(x, a, b):
        return a*x + b

    @staticmethod
    def poly_2(x, a, b, c):
        return a*x**2 + b*x + c

    def get_data_to_fit_via_current(self, start_to_fit):
        current_to_fit = []
        output_power_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i] > start_to_fit:
                current_to_fit.append(self.current[i])
                output_power_to_fit.append(self.output_power[i])

        return np.array(current_to_fit), np.array(output_power_to_fit )


data = ["temp_5.txt", "temp_10.txt", "temp_15.txt", "temp_20.txt",
        "temp_25.txt", "temp_30.txt"]
i_th = np.array([19.1, 20.7, 22.6, 25.0, 27.9, 31.4]) + 1
temperature = np.linspace(5, 30, 6) + 273

for name_file, fit_start, temp in zip(data, i_th, temperature):
    print(name_file, fit_start, temp)
    eff = Eff(name_file)
    x, y = eff.fit_slope_eff(fit_start)
    plt.plot(x, y, label=str(temp)+"\,K", lw=2)

plt.xlabel("prąd [mA]")
plt.ylabel(r"sprawność rożniczkowa [W/A]")
plt.grid(True)
plt.legend(loc=3)
plt.show()
