# ============================
# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# ============================

# ---- Imports ----
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ============================
# Task 1: Load and Explore the Dataset
# ============================

try:
    # Load dataset
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # Add species names

    # Preview data
    print("First 5 rows of dataset:")
    print(df.head())

    print("\nDataset Info:")
    df.info()

    print("\nChecking for missing values:")
    print(df.isnull().sum())

    # Clean data if missing values are found
    if df.isnull().sum().any():
        df = df.dropna()
        print("\nMissing values found and removed.")
    else:
        print("\nNo missing values found.")

except Exception as e:
    print("Unexpected error while loading dataset:", str(e))


# ============================
# Task 2: Basic Data Analysis
# ============================

print("\nDescriptive Statistics:")
print(df.describe())

species_means = df.groupby("species").mean(numeric_only=True)
print("\nMean values grouped by species:")
print(species_means)

print("\nObservation: Iris-virginica has the largest petal dimensions on average.")


# ============================
# Task 3: Data Visualization
# ============================

sns.set(style="whitegrid")

# ---- 1. Line Chart ----
plt.figure(figsize=(8,5))
df_sorted = df.sort_index()
plt.plot(df_sorted.index, df_sorted['sepal length (cm)'].cumsum(),
         label='Cumulative Sepal Length', color='blue', linewidth=2)
plt.title("Line Chart: Cumulative Sepal Length over Samples", fontsize=14)
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Sepal Length (cm)")
plt.legend()
plt.show()

# ---- 2. Bar Chart ----
plt.figure(figsize=(7,5))
species_means['petal length (cm)'].plot(kind='bar', color=['#1f77b4','#ff7f0e','#2ca02c'])
plt.title("Bar Chart: Average Petal Length by Species", fontsize=14)
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# ---- 3. Histogram ----
plt.figure(figsize=(7,5))
plt.hist(df['sepal width (cm)'], bins=15, edgecolor='black', color='skyblue')
plt.title("Histogram: Distribution of Sepal Width", fontsize=14)
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# ---- 4. Scatter Plot ----
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)',
                hue='species', palette='Set1', s=80, edgecolor="black")
plt.title("Scatter Plot: Sepal Length vs Petal Length", fontsize=14)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()


# ============================
# Findings
# ============================

print("FINDINGS:")
print("1. Iris-virginica has the largest petals compared to other species.")
print("2. Sepal width is mostly clustered around 3 cm.")
print("3. The scatter plot clearly shows separation between species, especially by petal length.")