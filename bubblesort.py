import time
import random

lista = [random.randint(1, 10000) for _ in range(1000)]

def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Bubble sort
lista_kopia = lista.copy()
start = time.time()
bubblesort(lista_kopia)

print(f"Bubble sort: {time.time() - start:.4f} sekunder")

# Pythons sorted()
start = time.time()
sorted(lista)
print(f"Python sorted(): {time.time() - start:.4f} sekunder")