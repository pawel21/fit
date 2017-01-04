# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

def plot_i_th(I_0, T_0):
    fig, ax1 = plt.subplots()
    temp = np.linspace(270, 370, 51)
    i_th = I_0*np.exp(temp/T_0)
    ax1.plot(temp, i_th)
    ax1.set_xlabel("Temperatura [K], $T$")
    ax1.set_ylabel("Prąd progowy [mA],$I_{th}$ ")
    plt.text(300, 60, r"$I_{th}$ = $0.03 \cdot \exp \left( \frac{T}{43.2} \right)$")
    plt.grid(True)
    plt.show()

plot_i_th(0.03, 43.2)