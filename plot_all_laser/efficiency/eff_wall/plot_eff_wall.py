import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class WallEfficiency:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        current, voltage, power = np.loadtxt(path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.output_power = power * 1000

    def get_input_power(self):
        return self.current*self.voltage

    def get_ratio_power(self):
        return self.output_power/self.get_input_power()

L635_temp5 = WallEfficiency("L635_temp_5.txt")
L635_temp35 = WallEfficiency("L635_temp_35.txt")
ax1 = plt.subplot(221)
ax1.plot(L635_temp5.current, L635_temp5.get_ratio_power(), 'bo', label="278\,K")
ax1.plot(L635_temp35.current, L635_temp35.get_ratio_power(), 'ro', label="308\,K")
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel("sprawność całkowita")
ax1.set_title("laser krawędziowy 635\,nm")
plt.legend(loc="upper left", prop={'size':20})
plt.grid(True)


L850_vcsel_10 = WallEfficiency("L850_vcsel_temp_10.txt")
L850_vcsel_90 = WallEfficiency("L850_vcsel_temp_90.txt")
ax2 = plt.subplot(222)
ax2.plot(L850_vcsel_10.current, L850_vcsel_10.get_ratio_power(), 'bo', label="283\,K")
ax2.plot(L850_vcsel_90.current, L850_vcsel_90.get_ratio_power(), 'ro', label="363\,K")
ax2.set_ylim([0, 0.15])
ax2.set_xlabel("prąd [mA]")
ax2.set_ylabel("sprawność całkowita")
ax2.set_title("laser VCSEL 850\,nm")
plt.legend(loc="lower right", prop={'size':20})
plt.grid(True)

L_850_edge_5 = WallEfficiency("L850P010_temp_5.txt")
L_850_edge_80 = WallEfficiency("L850P010_temp_80.txt")
ax3 = plt.subplot(223)
ax3.plot(L_850_edge_5.current, L_850_edge_5.get_ratio_power(), 'bo', label="278\,K")
ax3.plot(L_850_edge_80.current, L_850_edge_80.get_ratio_power(), 'ro', label="353\,K")
ax3.set_xlabel("prąd [mA]")
ax3.set_ylabel("sprawność całkowita")
ax3.set_title("laser krawędziowy 850\,nm")
plt.legend(loc="upper left", prop={'size':20})
plt.grid(True)

L_980_10 = WallEfficiency("L980_temp_10.txt")
L_980_90 = WallEfficiency("L980_temp_90.txt")
ax4 = plt.subplot(224)
ax4.plot(L_980_10.current, L_980_10.get_ratio_power(), 'bo', label="283\,K")
ax4.plot(L_980_90.current, L_980_90.get_ratio_power(), 'ro', label="363\,K")
ax4.set_xlabel("prąd [mA]")
ax4.set_ylabel("sprawność całkowita")
ax4.set_title("laser VCSEL 980\,nm")
plt.legend(loc="lower right", prop={'size':20})
plt.grid(True)

plt.show()
