from functools import lru_cache
@lru_cache(maxsize=None)
def fakultet(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakultet(n - 1)
    
print(fakultet(5))   # ska ge 120
print(fakultet(10))  # ska ge 3628800
import time

start = time.time()
print(fakultet(100))
print(f"Tid: {time.time() - start:.6f} sekunder")

# Rensa cachen och testa utan
fakultet.cache_clear()
start = time.time()
print(fakultet(100))
print(f"Tid utan cache: {time.time() - start:.6f} sekunder")

fakultet.cache_clear()

start = time.time()
for i in range(1000):
    fakultet(50)
print(f"Med cache: {time.time() - start:.6f} sekunder")

start = time.time()
for i in range(1000):
    fakultet.cache_clear()
    fakultet(50)
print(f"Utan cache: {time.time() - start:.6f} sekunder")