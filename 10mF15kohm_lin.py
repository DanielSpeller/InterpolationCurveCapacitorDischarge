import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


x=np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y=np.array([3.12, 2.56, 2.10, 1.73, 1.43, 1.18, 0.986, 0.812, 0.674, 0.560, 0.462, 0.384, 0.319])
plt.plot(x,y,'kx')
xnew = np.linspace(x.min(), x.max(), 13)
spl = make_interp_spline(x, y, k=7,)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth,'k')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
x1, y1 = [107, 107], [0, 1.56]
x2, y2 = [0, 107], [1.56, 1.56]
x3, y3 = [215, 215], [0, 0.78]
x4, y4 = [0, 215], [0.78, 0.78]
x5, y5 = [324, 324], [0, 0.39]
x6, y6 = [0, 324], [0.39, 0.39]
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, color='#000000' , linestyle='--')
plt.xlim([0, 370])
plt.ylim([0, 3.2])
plt.show()



