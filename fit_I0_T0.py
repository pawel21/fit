# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
matplotlib.rc('font', family='Arial')
matplotlib.use('GTK')
matplotlib.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 25})


def f(x, a, b):
    return a*x + b


def temp_C_to_kelvin(temp_C):
    return temp_C + 273.15


temp_C = [10, 15, 20, 25, 30, 35, 40, 45,
          50, 55, 60, 65, 70, 75, 80, 85, 90]

I_0 = np.array([1448, 1475, 1497, 1488, 1528,
                1525, 1538, 1591, 1635, 1739,
                1798, 1897, 2023, 2118, 2205,
                2354, 2467])*1e-6

temp_kelvin = list(map(temp_C_to_kelvin, temp_C))

plt.plot(temp_kelvin, np.log(I_0), 'bo')

popt, pcov = curve_fit(f, temp_kelvin[:], np.log(I_0[:]))
R= np.corrcoef(temp_kelvin[:], np.log(I_0[:]))
print(R[1][0])
a= popt[0]
b = popt[1]
x = np.linspace(280, 370, 100)
y = a*x + b
I_0 = math.e**b
T_0 = 1/a



plt.plot(x, y, 'r--')


plt.xlabel("Temperatura [K], x")
plt.ylabel("logarytm z wartości prądu, y")
plt.grid(True)
plt.text(340, -6.35, "$R^2$ = %.3f" %R[1][0])
plt.text(340, -6.4, "$y = a \cdot x + b$")
plt.text(340, -6.45, r"$a$ =  %.4f $\frac{1}{\mathtt{T}}$" % a)
plt.text(340, -6.5, "$b$ =  %.4f" % b)
plt.text(340, -6.55, "$I_0$ =  %.6f $\mathtt{A}$" % I_0)
plt.text(340, -6.60, "$T_0$ =  %.4f $\mathtt{K}$" % T_0)
plt.show()