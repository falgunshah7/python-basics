import matplotlib.pyplot as plt

# data for bar chart
labels = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# create bar chart
plt.figure(figsize=(6, 4)) # width, height
plt.bar(labels, values, color='skyblue', alpha=0.7)

# add labels and title
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# show plot
plt.show()