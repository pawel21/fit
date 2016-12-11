import sys
sys.path.insert(0, "/home/pawel1/Pulpit/Studia/PracaInz")
from fit import Fit

fit = Fit("temp_10.txt")
start_to_fit = 0.0019
end_to_fit = 0.01
fit.do_fit(start_to_fit, end_to_fit)

fit.plot_I_V_L()