import matplotlib.pyplot as plt
import numpy as np

g = 77.2 * 10**3
P = 15 * 10**3
s_tallow = 150 
s_callow = -80
x = P/2

a = np.linspace(0, 2, 20)
l_one = np.sqrt(1**2 + (2-a)**2)
l_two = np.sqrt(1 + a**2)

W = g * (x * ((l_one**2 / s_tallow) - (l_two**2 / s_callow)))

# Index of the minimum value of W
min_index = np.argmin(W)

# Minimum W value and corresponding "a" value
min_a = a[min_index]
min_W = W[min_index]
print(f"Minimum W: {min_W} at $y_B$ = {min_a}")

# Index where a = 0
a_0_index = np.where(a == 0)[0][0]
W_0 = W[a_0_index]
print(f"At a = 0, W = {W_0}")
plt.scatter(0, W_0, color='blue', zorder=5, label=f'({0}, {W_0})')

# graph of W vs "a" or (y_B)
plt.plot(a, W, 'r', label="W vs $y_B$")

# Minimum W on graph 
plt.scatter(min_a, min_W, color='blue', zorder=5, label=f'Min W ({min_a:.2f}, {min_W:.2f})')
plt.text((min_a*0.60), (min_W+0.125*10**7), f'({min_a:.2f}, {min_W:.2f})')

# Title and Labels
plt.xlabel('Position of Joint B ($y_B$)')
plt.ylabel('Weight of Truss (W)')
plt.title('Weight of Truss vs. Position of Joint B')

plt.legend() # Legend

plt.show()