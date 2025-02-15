import matplotlib.pyplot as plt
import numpy as np

def f(x):
   # return np.cos(x)
   return -np.tanh(x - np.pi/2)
x = np.linspace(0, np.pi, 100)
y = f(x)
plt.plot(x, y)
dlina = 0
j =0
while j <= np.pi:
    dlina += np.sqrt(0.0001**2+(f(x)-f(x-0.0001))**2)
    j +=0.01
plt.axhline(0, color='red', lw=0.5)
print(f"Длина кривой: {sum(dlina)}")
plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
