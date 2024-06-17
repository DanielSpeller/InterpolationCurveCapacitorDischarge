import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]) 
y = np.array([3.05, 2.03, 1.34, 0.906, 0.606, 0.407, 0.277, 0.187, 0.129, 0.088, 0.061, 0.043, 0.030])
plt.plot(x,y,'kx')
xnew = np.linspace(x.min(), x.max(), 15)
spl = make_interp_spline(x, y, k=3,)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth,'k')
plt.ylabel('Volatge /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
x1, y1 = [51, 51], [0, 1.525]
x2, y2 = [0, 51], [1.525, 1.525]
x3, y3 = [102, 102], [0, 0.7625]
x4, y4 = [0, 102], [0.7625, 0.7625]
x5, y5 = [153, 153], [0, 0.38125]
x6, y6 = [0, 153], [0.38125, 0.38125]
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, color='#000000' , linestyle='--')
plt.xlim([0, 370])
plt.ylim([0, 3.2])
plt.show()