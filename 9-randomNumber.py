import numpy as np
import matplotlib.pyplot as plt
import zlib

seed = 3
n = 1000
x = seed

A = np.empty(n, dtype=np.uint16)

def LGC(x):
    a = 16843009 
    c = 3014898611
    m = 2**32
    return (a*x+c) % m

def shannon_entropy(arr, symbols=100):
    counts = np.bincount(arr, minlength=symbols)
    p = counts / counts.sum()
    p_nonzero = p[p > 0]
    return -np.sum(p_nonzero * np.log2(p_nonzero))

for i in range(n):
    x = LGC(x)
    A[i] = (x >> 16) & 0xFFFF # Prend les 16 bits du milieu de x
    #A[i] = x % 100

Shannon = shannon_entropy(A, symbols=101)

data_bytes_A = A.tobytes()
ratioA = len(zlib.compress(data_bytes_A)) / len(data_bytes_A)

print("Shannon A:", Shannon)
print("Ratio A:", ratioA)

X = A[:int(n/2)]
Y = A[int(n/2):]

plt.scatter(X, Y)
plt.show()