import numpy as np
arr = np.array([[21, 12, 33],
                [12,  7, 13],
                [31, 20, 21]])
print("La Matriz original es:\n", arr)

print("La Matriz ordenada ascendente es:\n")
print(np.sort(arr, axis=0))