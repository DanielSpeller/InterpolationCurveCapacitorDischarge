import matplotlib.pyplot as plt
import numpy as np

x= np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y= np.array(np.log([3.12, 2.56, 2.10, 1.73, 1.43, 1.18, 0.986, 0.812, 0.674, 0.560, 0.462, 0.384, 0.319]))
plt.plot(x,y,'kx-')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
plt.xlim([0, 370])
plt.ylim([-1.2, 1.2])
plt.show()