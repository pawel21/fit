# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

from plot_laser_efficiency import PlotLaserEfficiency

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

ple5 = PlotLaserEfficiency("temp_20.txt")
ple5.plot_slope_efficiency_via_power(54.0)

ple5.fit_step_by_step(54.0, 40)