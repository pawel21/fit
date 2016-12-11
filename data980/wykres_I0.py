# -*- coding: utf-8 -*-
import matplotlib
matplotlib.rc('font', family='Arial')
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.interpolate import spline

plt.rcParams.update({'font.size':25})

def remove_duplicate(J, L):
    x = []
    y = []
    for i in range(0, len(J)):
        if J[i] not in x:
            x.append(J[i])
            y.append(L[i])
    return x,y


J_10, V_10, L_10 = np.loadtxt("temp_10.txt", unpack=True)
J_80, V_80, L_80 = np.loadtxt("temp_80.txt", unpack=True)

# plt.plot(J_10, L_10, "bo")
# plt.plot(J_80, L_80, "ro")
# plt.grid(True)
x_10, y_10 = remove_duplicate(J_10, L_10)
plt.plot(x_10, y_10, 'bo')
x_80, y_80 = remove_duplicate(J_80, L_80)
plt.plot(x_80, y_80, 'ro')
plt.xlabel(r'Prąd [$\mathtt{A}$]')
plt.show()
