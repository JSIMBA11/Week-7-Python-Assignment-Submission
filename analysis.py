# ============================
# Analyzing Iris and Bank Marketing Data
# ============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

# ---- Load Iris Dataset ----
print("=== IRIS DATASET ===")
try:
    iris = load_iris(as_frame=True)
    df_iris = iris.frame
    df_iris['species'] = df_iris['target'].map(dict(enumerate(iris.target_names)))
    print("First 5 rows of Iris dataset:")
    print(df_iris.head())
    print("\nIris Dataset Info:")
    df_iris.info()
    print("\nIris missing values:")
    print(df_iris.isnull().sum())
except Exception as e:
    print("Error loading Iris dataset:", e)

# ---- Load Bank Marketing Dataset ----
print("\n=== BANK MARKETING DATASET ===")
bank_path = r"c:\Users\jeral\Downloads\bank+marketing\bank\bank.csv"
if os.path.exists(bank_path):
    try:
        df_bank = pd.read_csv(bank_path, sep=';')
        print("First 5 rows of Bank dataset:")
        print(df_bank.head())
        print("\nBank Dataset Info:")
        df_bank.info()
        print("\nBank missing values:")
        print(df_bank.isnull().sum())
    except Exception as e:
        print("Error loading Bank dataset:", e)
else:
    print(f"Bank dataset not found at {bank_path}")

# ---- Example: Basic Analysis on Bank Dataset ----
if 'df_bank' in locals():
    print("\nBank Dataset Descriptive Statistics:")
    print(df_bank.describe(include='all'))
    print("\nValue counts for target column (y):")
    print(df_bank['y'].value_counts())