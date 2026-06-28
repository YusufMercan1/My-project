mening="the quick brown fox jumps over the lazy dog the fox"
frekvens = {}
for ord in mening.split():
    if ord in frekvens:
        frekvens[ord] += 1
    else:
        frekvens[ord] = 1        
sorted_frekvens = sorted(frekvens.items(), key=lambda x: x[1], reverse=True)
print("Ord och deras frekvens i meningen:")
for ord, antal in sorted_frekvens:
    print(f"{ord}: {antal}")