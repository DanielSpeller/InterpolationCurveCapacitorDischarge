import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])
y = np.array(np.log([3.09, 1.31, 0.567, 0.253, 0.120, 0.060, 0.028, 0.0147, 0.0072, 0.0040, 0.0022, 0.0012, 0.0007]))
plt.plot(x,y,'kx')
xnew = np.linspace(x.min(), x.max(), 15)
spl = make_interp_spline(x, y, 3,)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth,'k',snap=True)
plt.ylabel('Voltage /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.grid(visible='true', which='major', color='#DDDDDD', linestyle='-')
plt.grid(visible='true', which='minor', color='#EEEEEE', linestyle='-')
plt.minorticks_on()
plt.xlim([0, 370])
plt.ylim([-8, 1.2])
plt.show()