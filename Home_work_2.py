import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(5)
y = np.random.rand(5)


plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='blue', edgecolors='black')
plt.title('Scatter Plot of Random Data')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()
