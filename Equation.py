import matplotlib.pyplot as plt
import numpy as np
x1 = int(input())
x2 = int(input())
y1= int(input())
y2 = int(input())
n1 = float(input())
n2 = float(input())
plt.scatter(x1,y1,1)
plt.scatter(x2,y2,2)
plt.axhline(0, color='red', lw=0.5)
x=x1+0.001
def length(x0):
    L1=(x1-x)**2+y1**2
    L2=(x2-x)**2 + y2**2
    return L1*n1+L2*n2
x0_min = np.linspace(x1, x2, 1000)
lengths = [length(x0) for x0 in x0_min]
x0_min = x0_min[np.argmin(lengths)]
print(x0_min)
plt.scatter(x0_min,0)
a = [x1,x0_min,x2]
b = [y1,0,y2]
plt.plot(a,b)
plt.show()
