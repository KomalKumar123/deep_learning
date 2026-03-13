import numpy as np
import matplotlib.pyplot as plt
print("Working with Arrays")
print("="*70)
# Creating Arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"\nArray 1 (2x2):\n{arr1}")
print(f"Array 2 (2x2):\n{arr2}")
## Array Reshape
arr3 = np.arange(12).reshape(3, 4)
print(f"Array 3 (3x4):\n{arr3}")
# Arithmetic Operations
print("\nArithmetic Operations")
print("-"*50)
print(f"Addition:\n{arr1 + arr2}")
print(f"Subtract: \n{arr1 - arr2}")
print(f"Multiply: \n{arr1 * arr2}")
print(f"Divide: \n{arr1 / arr2}")
print(f"Power: \n{arr1 ** 2}")
# Array Properties
print("\nArray Properties")
print("-"*50)
1
print(f"Shape arr1: {arr1.shape}")
print(f"Shape arr3: {arr3.shape}")
print(f"Dtype arr1: {arr1.dtype}")
print(f"Size arr1: {arr1.size}")
print(f"ndim arr1: {arr1.ndim}")
#Aggregrate Functions
print("\nAggregrate Functions")
print("-"*50)
print(f"Sum: {np.sum(arr3)}")
print(f"Mean: {np.mean(arr3):.2f}")
print(f"Min/Max: {np.min(arr3)}, {np.max(arr3)}")
print(f"Std: {np.std(arr3):.2f}")
print(f"Row sums: {np.sum(arr3, axis=1)}")
print(f"Col sums: {np.sum(arr3, axis=0)}")
#Array Manipulation
print("\nArray Manipulation")
print("-"*50)
print(f"Reshape: {np.arange(12).reshape(2, 6)}")
print(f"Flatten: {arr3.ravel()}")
print(f"Transpose:{arr3.T.shape}")
#Universal Functions
print("\nUniversal Functions")
print("-"*50)
print(f"Sqrt: {np.sqrt(arr1)}")
print(f"Exp: {np.exp(arr1[:1])}")
print(f"Sin: {np.sin(arr3[:3])}")
#MATRIX Operations
print("\nMATRIX Operations")
print("-"*50)
print(f"Dot product:\n{np.dot(arr1, arr2)}")
print(f"Matrix mult:\n{np.matmul(arr1, arr2)}")
#Statisticl Operations
print("\nStatisticl Operations")
print("-"*50)
print(f"Median: {np.median(arr3):.2f}")
print(f"Percentile 25: {np.percentile(arr3, 25):.2f}")
print("="*70)