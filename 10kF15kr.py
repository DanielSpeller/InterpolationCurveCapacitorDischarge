import matplotlib.pyplot as plt

plt.plot([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360],[3.12, 2.56, 2.10, 1.73, 1.43, 1.18, 0.986, 0.812, 0.674, 0.560, 0.462, 0.384, 0.319],'kX-')
plt.ylabel('Volatge /V',fontsize=8.5)
plt.xlabel('Time /s',fontsize=8.5)
plt.title('Graph of voltage against time during the discharge of a 10,00 $\mu F$ capacitor through a 15 $k\Omega$ resistor',fontsize=8.5)
plt.show()
