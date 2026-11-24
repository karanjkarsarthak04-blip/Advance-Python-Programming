import numpy as np

# Step 1: Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)
print("Array:", arr)

# Step 2: Slicing operations
print("\nFirst five elements:", arr[:5])
print("Last three elements:", arr[-3:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])
print("Reversed array:", arr[::-1])

# Step 3: Statistical measures
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Step 4: Broadcasting
print("\nAdd 5 to each element:", arr + 5)
print("Multiply each element by 2:", arr * 2)
print("Square each element:", arr ** 2)

# Broadcasting a scalar into a slice to modify the array in place
arr[:3] = arr[:3] * 10
print("First three elements multiplied by 10:", arr)