import numpy as np

temp = np.linspace(10, 90, 17) + 273
I_th = [0.92, 0.94, 0.98, 1.05, 1.10, 1.18, 1.23, 1.25, 1.36, 1.47, 1.59, 1.63, 1.76, 1.86, 2.07, 2.25, 2.43]
error_I_th = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.03, 0.04, 0.03, 0.04, 0.04, 0.04, 0.06, 0.05, 0.06, 0.06]

np.savetxt("/home/pawel1/Pulpit/Studia/PracaInz/plot_all_laser/current_threshold_980.txt",
            np.c_[temp, I_th, error_I_th], fmt='%1.4f', header="temp [K]\t threshold current [mA]\t error current [ma]\t")