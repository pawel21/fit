import matplotlib
matplotlib.use('qt5Agg')
matplotlib.rc('font', family='Arial')
matplotlib.rcParams['text.latex.unicode'] = True

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 25})

I, V, L = np.loadtxt("temp_10.txt", unpack=True)
