# Assignment: Data Loading, Analysis, and Visualization

# 📦 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========== Task 1: Load and Explore Dataset ==========
# Load dataset (using seaborn’s built-in iris dataset for simplicity)
iris = sns.load_dataset("iris")

# Display first few rows
print("First 5 rows of dataset:")
print(iris.head())

# Check structure, datatypes, and missing values
print("\nDataset Info:")
print(iris.info())

print("\nMissing values per column:")
print(iris.isnull().sum())

# No missing values in this dataset, but if there were:
# iris = iris.dropna()  # OR fill with mean: iris.fillna(iris.mean())

# ========== Task 2: Basic Data Analysis ==========
# Summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Grouping: Average petal length per species
grouped = iris.groupby("species")["petal_length"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Interesting finding example:
# Versicolor has petal lengths roughly midway between Setosa (short) and Virginica (long).

# ========== Task 3: Data Visualization ==========

# 1. Line chart: simulate time-series by plotting first 50 petal lengths
plt.figure(figsize=(8, 5))
plt.plot(iris.index[:50], iris["petal_length"][:50], marker="o", linestyle="-")
plt.title("Petal Length Trend (First 50 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar chart: average petal length per species
plt.figure(figsize=(7, 5))
grouped.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: distribution of sepal length
plt.figure(figsize=(7, 5))
plt.hist(iris["sepal_length"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: Sepal length vs. Petal length
plt.figure(figsize=(7, 5))
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species", palette="Set2")
plt.title("Sepal Length vs. Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
