import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 1000 random numbers from a normal distribution

# create histogram
plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')

# Add labels and title
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()