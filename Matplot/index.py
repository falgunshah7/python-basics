import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) # 100 points between 0 and 10
y = np.sin(x) # sine wave

# create plot
plt.figure(figsize=(8, 4)) # width, height
plt.plot(x, y, label='sin(x)', color='red', linestyle='-', linewidth=2) # solid line

# add labels and title
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# add grid
plt.grid(True, linestyle='--', alpha=0.6)

# add legend
plt.legend()

# show plot
plt.show()