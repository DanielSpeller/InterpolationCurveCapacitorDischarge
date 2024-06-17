import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


x=np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y=np.array([3.11, 2.06, 1.390, 0.939, 0.631, 0.429, 0.290, 0.196, 0.133, 0.0926, 0.0637, 0.0431, 0.0310])
plt.plot(x,y,'kx')
xnew = np.linspace(x.min(), x.max(), 15)
spl = make_interp_spline(x, y, k=7,)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth,'k')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
x1, y1 = [51, 51], [0, 1.555]
x2, y2 = [0, 51], [1.555, 1.555]
x3, y3 = [104, 104], [0, 0.7775]
x4, y4 = [0, 104], [0.7775, 0.7775]
x5, y5 = [155, 155], [0, 0.38875]
x6, y6 = [0, 155], [0.38875, 0.388]
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, color='#000000' , linestyle='--')
plt.xlim([0, 370])
plt.ylim([0, 3.2])
plt.show()
