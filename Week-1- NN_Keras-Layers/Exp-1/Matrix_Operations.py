import numpy as np
import matplotlib.pyplot as plt
print("MATRIX Operations")
print("="*70)
# Create matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
C = np.array([[1, 0], [0, 1]]) # Identity 2x2
print(f"\nMatrix A (3x3):\n{A}")
print(f"Matrix B (3x3):\n{B}")
print(f"Matrix C (2x2):\n{C}")
#BASIC MATRIX OPERATIONS
print("\nBasic Operations")
print("-"*50)
print(f"Addition: \n{A + B}")
print(f"Subtraction: \n{A - B}")
print(f"Element-wise: \n{A * B}")
print(f"Scalar mult: \n{2 * A}")
#Matrix Multiplication
print("\nMatrix Multiplication")
print("-"*50)
print(f"A @ B (3x3):\n{np.matmul(A, B)}")
print(f"A @ A^T: \n{np.matmul(A, A.T)}")
print(f"A @ A: \n{np.matmul(A, A)}")



#Transpose of a Matrix
print("\nTranspose")
print("-"*50)
print(f"A shape: {A.shape}")
print(f"A transpose: {A.T.shape}")
print(f"A^T:\n{A.T}")
#Determinant & Inverse of a Matrix
print("\nDeterminant & Inverse")
print("-"*50)
det_C = np.linalg.det(C)
inv_C = np.linalg.inv(C)
print(f"Det(C): {det_C:.3f}")
print(f"Inv(C):\n{inv_C}")
#MATRIX Properties
print("\nMATRIX Properties")
print("-"*50)
print(f"Rank(A): {np.linalg.matrix_rank(A)}")
print(f"Trace(A): {np.trace(A)}")
print(f"Norm(A): {np.linalg.norm(A):.2f}")
#EIGENVALUES & EIGENVECTORS
print("\nEigen Values and Eigen Vectors")
print("-"*50)
eigvals, eigvecs = np.linalg.eig(A)
print(f"Eigenvalues: {eigvals}")
print(f"Eigenvectors:\n{eigvecs[:, 0]}")
#SOLVE LINEAR SYSTEM: Ax = b
print("\nSOLVE Ax = b")
print("-"*50)
A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print(f"Solution x: {x}")
print("="*70)
