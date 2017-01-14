import numpy as np

temp_850 = np.linspace(10, 90, 17) + 273
I_th_850 = [1.70, 1.67, 1.60, 1.55, 1.59, 1.63, 1.65, 1.68, 1.73, 1.83, 1.89, 2.00, 2.14, 2.24, 2.38, 2.57, 2.74]
error_I_th_850 = [0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.07]

np.savetxt("/home/pawel1/Pulpit/Studia/PracaInz/plot_all_laser/current_threshold_vcsel850.txt",
           np.c_[temp_850, I_th_850, error_I_th_850], fmt='%1.4f',
           header="temp [K]\t threshold current [mA]\t error current [ma]\t")