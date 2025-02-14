import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) # 100 points between 0 and 10
y1 = np.sin(x) # sine wave
y2 = np.cos(x) # cosine wave

# create figure with 2 subplots
plt.figure(figsize=(10, 5)) # width, height

# First subplot: sin wave
plt.subplot(1, 2, 1) # rows, columns, index
plt.plot(x, y1, label='sin(x)', color='blue')
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# Second subplot: cos wave
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('Cosine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# show plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()