import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y = np.array(np.log([3.11, 2.06, 1.390, 0.939, 0.631, 0.429, 0.290, 0.196, 0.133, 0.0926, 0.0637, 0.0431, 0.0310]))
plt.plot(x,y,'kx-')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
plt.xlim([0, 370])
plt.ylim([-3.6, 1.2])
plt.show()