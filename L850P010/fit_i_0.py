import numpy as np
from plot_threshold_current_temp import PlotThresholdCurrentTemp

temp = np.linspace(10, 80, 15) + 273
i_0 = [10.48, 10.86, 11.05, 11.33, 11.65, 11.98, 12.34, 12.71, 13.11, 13.57, 14.08, 14.58, 15.18, 15.74, 16.55]
error_i_0 = [0.090,  0.10, 0.100, 0.050, 0.060, 0.070, 0.070, 0.080, 0.090, 0.070, 0.100, 0.100, 0.110, 0.130, 0.160]

pl = PlotThresholdCurrentTemp(i_0, temp, y_err=error_i_0)
pl.plot_linear_temp_i_th_with_err
pl.fit_temp_log_i_th(x_text=340, y_text=2.6, dy_text=0.05)
pl.plot_fit_exp_with_error()