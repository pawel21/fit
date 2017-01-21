import numpy as np

from plot_threshold_current_temp import PlotThresholdCurrentTemp

temp_850 = np.linspace(10, 90, 17) + 273
I_0_850 = [1.70, 1.67, 1.60, 1.55, 1.59, 1.63, 1.65, 1.68, 1.73, 1.83, 1.89, 2.00, 2.14, 2.24, 2.38, 2.57, 2.74]
error_I_0_850 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.07]
pl_850 = PlotThresholdCurrentTemp(I_0_850, temp_850, y_err=error_I_0_850)
pl_850.plot_linear_temp_i_th_with_err