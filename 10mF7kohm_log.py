import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y = np.array(np.log([3.05, 2.03, 1.34, 0.906, 0.606, 0.407, 0.277, 0.187, 0.129, 0.088, 0.061, 0.043, 0.030]))
plt.plot(x,y,'kx-')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
plt.xlim([0, 370])
plt.ylim([-3.6, 1.2])
plt.show()