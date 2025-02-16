import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    #return x**3 - x + 1
   return np.cos(x)+2*x-3
def yrav(a, b, f, tol=0.0001):
    c = (a + b) / 2
    while (b - a) / 2 >= tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c
x = np.linspace(-20, 10, 100)
y = f1(x)
plt.plot(x, y)
plt.axhline(0, color='red', lw=0.5)
plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
x1 = yrav(-1.5, 2, f1)
print(x1)

