"""Question 12: Exploratory data analysis using NumPy, Pandas, and Matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_customer_data(file_name):
    """Load a CSV file, or use a small demo dataset when it is unavailable."""
    file_path = Path(file_name)
    if file_path.exists():
        return pd.read_csv(file_path)

    print(f"'{file_name}' was not found; using demonstration customer data.")
    return pd.DataFrame({
        "Customer": ["Asha", "Bharat", "Chitra", "Dev", "Esha", "Farhan"],
        "Age": [24, 31, np.nan, 45, 29, 38],
        "Income": [35000, 52000, 47000, np.nan, 61000, 58000],
        "City": ["Pune", "Mumbai", "Pune", "Nashik", None, "Mumbai"],
        "Purchases": [4, 8, 6, 3, 10, 7],
    })


def clean_data(data):
    """Fill numerical nulls with medians and categorical nulls with modes."""
    cleaned = data.copy()
    numeric_columns = cleaned.select_dtypes(include=np.number).columns
    for column in numeric_columns:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    categorical_columns = cleaned.select_dtypes(exclude=np.number).columns
    for column in categorical_columns:
        mode = cleaned[column].mode(dropna=True)
        cleaned[column] = cleaned[column].fillna(mode.iloc[0] if not mode.empty else "Unknown")
    return cleaned


def create_visualizations(data):
    """Create a histogram and a city-wise purchase chart."""
    numeric_columns = data.select_dtypes(include=np.number).columns
    if len(numeric_columns) > 0:
        data[numeric_columns].hist(figsize=(10, 6), bins=8)
        plt.suptitle("Distribution of Numerical Customer Data")
        plt.tight_layout()
        plt.show()

    if "City" in data.columns and "Purchases" in data.columns:
        data.groupby("City")["Purchases"].mean().plot(kind="bar", color="teal")
        plt.title("Average Purchases by City")
        plt.ylabel("Average Purchases")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    csv_name = input("Enter customer CSV file name (or press Enter for customer_data.csv): ").strip()
    data = load_customer_data(csv_name or "customer_data.csv")

    print("\nOriginal data:\n", data)
    print("\nMissing values before cleaning:\n", data.isnull().sum())

    cleaned_data = clean_data(data)
    print("\nCleaned data:\n", cleaned_data)
    print("\nSummary statistics:\n", cleaned_data.describe(include="all"))
    print("\nCorrelation matrix for numerical columns:\n", cleaned_data.select_dtypes(include=np.number).corr())

    create_visualizations(cleaned_data)
