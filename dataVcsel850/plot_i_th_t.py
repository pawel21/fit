# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
matplotlib.rc('font', family='Arial')
matplotlib.rcParams['text.latex.unicode'] = True

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams["font.family"] = "Arial"
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})



def f(x, a, b):
    return x*a + b


def temp_celsjusz_to_kelvin(temp_c):
    return temp_c + 273.15


def get_t0(a, da):
    t0 = 1/a
    dt0 = abs(-1/a**2)*da
    return t0, dt0


def get_ith(b, db):
    ith = math.e**b
    dith = abs(b*math.e**b)*db
    return ith, dith


def plot_i_th(I_0, T_0):
    fig, ax1 = plt.subplots()
    temp = np.linspace(270, 370, 51)
    i_th = I_0*np.exp(temp/T_0)
    ax1.plot(temp, i_th)
    ax1.set_xlabel("Temperatura [K], $T$")
    ax1.set_ylabel("Prąd progowy [mA],$I_{th}$ ")
    plt.text(300, 1.5, r"$I_{th}$ = $0.04 \cdot \exp \left( \frac{T}{89.9} \right)$")
    plt.grid(True)
    plt.show()

temp_C = np.arange(10, 95, 10)
temp_K = list(map(temp_celsjusz_to_kelvin, temp_C))

#I_0 = np.array([0.8, 0.8, 0.9, 1.0, 1.1, 1.1, 1.1, 1.1, 1.2, 1.4, 1.5, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4])*10**-3

I_0 = [1.0, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.4]
dict_key_temp_values_I = dict(zip(temp_K, I_0))

# popt, pcov = curve_fit(f, temp_K, np.log(I_0))
#
# a = popt[0]
# b = popt[1]
# error = np.diag(pcov)
# da = error[0]
# db = error[1]
# x = np.linspace(270, 370, 101)
# y = a*x + b



plt.xlabel("Temperatura [K], T")
plt.ylabel("logarytm z wartości prądu progowego, $\ln(I_{th})$")
# plt.text(340, 0, r"$\ln I_{th}=\frac{T}{T_{0}} + \ln I_{0} $", fontsize=30)
# plt.text(340, -0.1, r"$T_0=(89.9 \pm 0.1)$K", fontsize=30)
# plt.text(340, -0.2, r"$I_{0}=(0.04 \pm 0.01)$mA", fontsize=30)
plt.grid(True)
plt.plot(temp_K, np.log(I_0), 'bo')
plt.show()

# plot_i_th(0.04, 89.9)