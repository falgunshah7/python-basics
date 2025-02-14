import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# create scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')

# add labels and title
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a colorbar
plt.colorbar(label='Color Intensity')

# Show the plot
plt.show()