import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit
from sympy.solvers import solve
from sympy import Symbol

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Find_I_th:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        current, voltage, power = np.loadtxt(path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.power = power*1000
        self.a = 0
        self.b = 0
        self.da = 0
        self.db = 0
        self.I_th = 0
        self.dI_th = 0

    def get_input_power(self):
        return self.current*self.voltage

    def do_fit(self, start_to_fit, end_to_fit):
        x, y = self._get_data_to_fit(start_to_fit, end_to_fit)
        popt, pcov = curve_fit(self.f, x, y)
        self.a = popt[0]
        self.b = popt[1]
        error = np.abs(np.diag(pcov) ** 0.5)
        self.da = error[0]
        self.db = error[1]
        self.I_th = self._find_I0()
        self.dI_th = self._find_dI0()
        print(u"a = %s \u00B1 %s" % (self.a, self.da))
        print(u"b = %s \u00B1 %s" % (self.b, self.db))
        print(u"I_th = (%.10f \u00B1 %.10f) mA" % (self.I_th, self.dI_th))
        return self.a, self.b, self.I_th, self.dI_th

    @property
    def get_data(self):
        return self.current, self.voltage, self.power

    def get_fit_parameters(self):
        return self.a, self.da, self.b, self.db, self.I_th, self.dI_th

    def _get_data_to_fit(self, start_to_fit, end_to_fit):
        x_to_fit = []
        y_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i] > start_to_fit and self.current[i] < end_to_fit:
                x_to_fit.append(self.current[i])
                y_to_fit.append(self.power[i])
        return x_to_fit, y_to_fit

    def _find_I0(self):
        I = Symbol('I')
        I_th = solve(self.a * I + self.b, I)
        return float(I_th[0])

    def _find_dI0(self):
        return abs((-self.b / (self.a ** 2))) * self.da + abs((-1 / self.a)) * self.db

    def _fit_plot(self, start_to_fit, end_to_fit):
        self.do_fit(start_to_fit, end_to_fit)
        fig, ax1 = plt.subplots()
        ax1.plot(self.current, self.power, 'ro', markersize=4)
        ax1.set_xlim([0, max(self.current)])
        ax1.set_ylim([0, max(self.power)])
        x = np.linspace(start_to_fit, end_to_fit, 100)
        y = self.a * x + self.b
        ax1.axhline(0., ls='-', color='k')
        ax1.plot(x, y, 'b-', linewidth=2)
        plt.text(start_to_fit + 0.1 * start_to_fit, -0.8,
                 "$I_{th}$ = (%.5f $\pm$ %.5f)mA" % (float(self.I_th), self.dI_th + 0.01))
        ax1.set_xlabel(u"prąd [mA]")
        ax1.set_ylabel(u"moc wyjściowa [mW]")
        plt.grid(True)
        plt.show()

    @staticmethod
    def f(x, a, b):
        return a*x + b




l850_temp_10 = Find_I_th("L850P010_temp_10.txt")
#l850_temp_10._fit_plot(11, 20)

l850_temp_25 = Find_I_th("L850P010_temp_25.txt")
#l850_temp_25._fit_plot(11.5, 20)

l850_temp_60 = Find_I_th("L850P010_temp_60.txt")
#l850_temp_60._fit_plot(15, 23)

l850_temp_80 = Find_I_th("L850P010_temp_80.txt")
l850_temp_80._fit_plot(16.5, 22)

ax1 = plt.subplot(221)
ax1.plot(l850_temp_10.current, l850_temp_10.power, 'r^')
a_10, b_10, _, _ = l850_temp_10.do_fit(11, 20)
x_10 = np.linspace(10, 20)
y_10 = a_10*x_10 + b_10
ax1.plot(x_10, y_10, 'b-')
ax1.set_xlim([5, 18])
ax1.set_ylim([-1, 5.5])
ax1.text(10, -0.8, "$I_{th}$ = (%.2f $\pm$ %.2f)\,mA" % (10.48, 0.09), size=20)
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel("moc wyjściowa [mW]")
ax1.set_title("283\,K")
plt.axhline(color='black')
plt.grid(True)

ax2 = plt.subplot(222)
ax2.plot(l850_temp_25.current, l850_temp_25.power, 'r^')
a_25, b_25, _, _ = l850_temp_25.do_fit(11.5, 20)
x_25 = np.linspace(10.9, 20)
y_25 = a_25*x_25 + b_25
ax2.plot(x_25, y_25, 'b-')
ax2.set_xlim([5, 18])
ax2.set_ylim([-1, 5])
ax2.text(10.9, -0.8, "$I_{th}$ = (%.2f $\pm$ %.2f)\,mA" % (11.33, 0.05), size=20)
ax2.set_xlabel("prąd [mA]")
ax2.set_ylabel("moc wyjściowa [mW]")
ax2.set_title("298\,K")
plt.axhline(color='black')
plt.grid(True)

ax3 = plt.subplot(223)
ax3.plot(l850_temp_60.current, l850_temp_60.power, 'r^')
a_60, b_60, _, _ = l850_temp_60.do_fit(15, 23)
x_60 = np.linspace(13.5, 23)
y_60 = a_60*x_60 + b_60
ax3.plot(x_60, y_60, 'b-')
ax3.set_xlim([5, 22])
ax3.set_ylim([-1, 5])
ax3.text(14.5, -0.8, "$I_{th}$ = (%.1f $\pm$ %.1f)\,mA" % (14.1, 0.2), size=20)
ax3.set_xlabel("prąd [mA]")
ax3.set_ylabel("moc wyjściowa [mW]")
ax3.set_title("333\,K")
plt.axhline(color='black')
plt.grid(True)

ax4 = plt.subplot(224)
ax4.plot(l850_temp_80.current, l850_temp_80.power, 'r^')
a_90, b_90, _, _ = l850_temp_80.do_fit(16.5, 22)
x_90 = np.linspace(15.8, 22)
y_90 = a_90*x_90 + b_90
ax4.plot(x_90, y_90, 'b-')
ax4.set_xlim([8, 22.5])
ax4.set_ylim([-1, 4])
ax4.text(16, -0.8, "$I_{th}$ = (%.1f $\pm$ %.1f)\,mA" % (16.5, 0.2), size=20)
ax4.set_xlabel("prąd [mA]")
ax4.set_ylabel("moc wyjściowa [mW]")
ax4.set_title("353\,K")
plt.axhline(color='black')
plt.grid(True)


plt.subplots_adjust(left=0.06, right=0.95, top=0.93, bottom=0.1, hspace=0.34, wspace=0.26)
plt.show()