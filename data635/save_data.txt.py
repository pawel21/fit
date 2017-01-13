import numpy as np

temp_635 = np.linspace(20, 40, 5) + 273
I_th_635 = [22.4, 25.0, 28.1, 31.3, 35.7]
y_err = [0.3, 0.2, 0.3, 0.6, 0.9]

np.savetxt("/home/pawel1/Pulpit/Studia/PracaInz/plot_all_laser/current_threshold_635.txt",
           np.c_[temp_635, I_th_635, y_err], fmt='%1.4f', header="temp [K]\t threshold current [mA]\t error current [ma]\t")