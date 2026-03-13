import numpy as np
import matplotlib.pyplot as plt
print("="*60)
print("VECTOR OPERATIONS")
print("="*60)
# Creation of vectors
v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([5, 4, 3, 2, 1])
print(f"\nVector 1: {v1}")
print(f"Vector 2: {v2}")
1
# Element-Wise Operations
print("\nElement-Wise Operations")
print("-"*40)
print(f"Addition: {v1} + {v2} = {v1 + v2}")
print(f"Subtraction: {v1} - {v2} = {v1 - v2}")
print(f"Multiplication:{v1} * {v2} = {v1 * v2}")
print(f"Division: {v1} / {v2} = {v1 / v2}")
print(f"Power: {v1} ** 2 = {v1 ** 2}")
# Magnitude of the Vector (Length/Norm)
print("\nVector Magnitude")
print("-"*40)
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)
print(f"Magnitude v1: {mag_v1:.2f}")
print(f"Magnitude v2: {mag_v2:.2f}")
# Dot product of vectors
print("\nDot Product")
print("-"*40)
dot_product = np.dot(v1, v2)
print(f"v1 • v2 = {dot_product}")
# CROSS PRODUCT (3D vectors only)
print("\nCross Product")
print("-"*40)
v3 = np.array([1, 2, 3])
v4 = np.array([4, 5, 6])
cross_product = np.cross(v3, v4)
print(f"v3 = {v3}, v4 = {v4}")
print(f"v3 × v4 = {cross_product}")
# Angle Between Vectors
print("\nAngle Between Vectors")
print("-"*40)
cos_theta = np.dot(v1, v2) / (mag_v1 * mag_v2)
angle_deg = np.arccos(np.clip(cos_theta, -1, 1)) * 180 / np.pi
print(f"Cos  = {cos_theta:.3f}")
print(f"Angle = {angle_deg:.1f}°")
# Normalized Vectors
print("\nNormalized Vectors")
print("-"*40)
v1_norm = v1 / mag_v1
v2_norm = v2 / mag_v2
print(f"Normalized v1: {v1_norm}")
print(f"Normalized v2: {v2_norm}")
print("="*60)