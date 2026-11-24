import pandas as pd
import numpy as np

# Step 1: Create a Series containing ten random numbers
np.random.seed(42)
data = np.random.randint(1, 100, 10)
s = pd.Series(data, index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
print("Series:")
print(s)

# Step 2: Indexing
print("\nElement at label 'c':", s["c"])
print("Element at position 0:", s.iloc[0])
print("First three elements:")
print(s[:3])
print("Elements 'b' to 'e':")
print(s["b":"e"])

# Step 3: Filtering
print("\nValues greater than 50:")
print(s[s > 50])
print("\nValues between 20 and 70:")
print(s[(s >= 20) & (s <= 70)])
print("\nEven values:")
print(s[s % 2 == 0])

# Step 4: Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())