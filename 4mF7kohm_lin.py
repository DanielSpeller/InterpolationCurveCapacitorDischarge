import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


x=np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y=np.array([3.09, 1.31, 0.567, 0.253, 0.120, 0.060, 0.028, 0.0147, 0.0072, 0.0040, 0.0022, 0.0012, 0.0007])
plt.plot(x,y,'kx')
xnew = np.linspace(x.min(), x.max(), 13)
spl = make_interp_spline(x, y, k=9,)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth,'k')
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
x1, y1 = [24, 24], [0, 1.545]
x2, y2 = [0, 24], [1.545, 1.545]
x3, y3 = [48, 48], [0, 0.7725]
x4, y4 = [0, 48], [0.7725, 0.7725]
x5, y5 = [75, 75], [0, 0.38625]
x6, y6 = [0, 75], [0.38625, 0.38625]
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, color='#000000' , linestyle='--')
plt.xlim([0, 370])
plt.ylim([0, 3.2])
plt.show()
