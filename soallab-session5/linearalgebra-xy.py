import numpy as np

A = np.array([[2, 1],[1, 3]])
B = np.array([5, 6])

# Sistem persamaan
solusi = np.linalg.solve(A, B)

print(f"Nilai x = {solusi[0]}")
print(f"Nilai y = {solusi[1]}")