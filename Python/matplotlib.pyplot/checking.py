import matplotlib.pyplot as plt
import numpy as np

nVals = []
linear = []
quadric = []
cubic = []
exponential = []

for n in range(0, 30):
    nVals.append(n)
    #....................................
    linear.append(n)
    quadric.append(n**2)
    cubic.append(n**3)
    exponential.append(1.5**n)

y =plt.plot(nVals,exponential,color ='red')
plt.xlabel('this is x')
plt.grid(True)

plt.show()