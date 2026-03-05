import numpy as np
n = 1000

x = np.random.rand(n)
y = np.random.rand(n)

inside_circle = (x**2 + y**2) <=1
p_estimate = 4 * np.sum(inside_circle) /n
print(p_estimate)