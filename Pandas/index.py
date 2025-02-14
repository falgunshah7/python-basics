import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 36, 29, 42],
    'Location': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing rows and columns
print("Name:\n", df['Name'])
print("Age:\n", df.Age)

# Adding a new column
df['Salary'] = [3000, 4000, 5000, 6000]
print("DataFrame with Salary column:\n", df)

# Filtering rows
filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame:\n", filtered_df)

# Basic statistics
print("Mean Age:", df['Age'].mean())
print("Max Salary:", df['Salary'].max())

# Sorting the DataFrame
sorted_df = df.sort_values(by='Salary', ascending=False)
print("Sorted DataFrame by Salary:\n", sorted_df)

# Grouping data
grouped_df = df.groupby('Location').mean(numeric_only=True)
print("Grouped DataFrame by Location:\n", grouped_df)

# Save the DataFrame to a CSV file
# df.to_csv('example.csv', index=False)

# Load a DataFrame from a CSV file
loaded_df = pd.read_csv('example.csv')
print("Loaded DataFrame from example.csv:\n", loaded_df)