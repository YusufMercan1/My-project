def binarsok(lista, mål):
    vänster, höger = 0, len(lista) - 1
    
    while vänster <= höger:
        mitten = (vänster + höger) // 2

        if lista[mitten] == mål:
            return mitten  # Målet hittades, returnera index
        elif lista[mitten] < mål:
            vänster = mitten + 1  # Sök i den högra halvan
        else:
            höger = mitten - 1  # Sök i den vänstra halvan 

    return -1  # Målet hittades inte

lista = list(range(1, 1000001))  # 1 till 1 000 000
print(binarsok(lista, 742531))


import time

# Binärsökning
start = time.time()
print(binarsok(lista, 742531))
print(f"Binärsökning: {time.time() - start:.6f} sekunder")

# Linjärsökning
start = time.time()
print(lista.index(742531))
print(f"Linjärsökning: {time.time() - start:.6f} sekunder")