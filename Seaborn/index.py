import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load example dataset
tips = sns.load_dataset('tips')

# 1. Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time', style='smoker', palette='viridis')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# 2. Line plot
plt.figure(figsize=(8, 6))
sns.lineplot(x='total_bill', y='tip', data=tips, hue='time', style='smoker', markers=True, dashes=False)
plt.title('Line Plot of Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# 3. Bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='day', y='total_bill', data=tips, hue='sex', palette='coolwarm', errorbar='sd')
plt.title('Bar Plot of Total Bill by Day and Sex')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# 4. Histogram
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, kde=True, color='purple')
plt.title('Histogram of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# 5. Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex', palette='Set2')
plt.title('Box Plot of Total Bill by Day and Sex')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# 6. Heatmap
# Create a correlation matrix
numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
corr = numeric_tips.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Heatmap of Correlation Matrix')
plt.show()

# 7. Pair plot
sns.pairplot(tips, hue='sex', palette='husl', diag_kind='kde')
plt.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.show()

# 8. Violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True, palette='pastel')
plt.title('Violin Plot of Total Bill by Day and Sex')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()