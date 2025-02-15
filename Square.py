import matplotlib.pyplot as plt
import numpy as np
def f1(x):
    return  np.sin(2*x)+1
def f2(x):
    return -0.2*x**2+0.5
x1 = np.linspace(0,np.pi,100)
x2 = np.linspace(0,np.pi,100)
y1 = f1(x1)
y2 = f2(x2)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.grid()
plt.show()