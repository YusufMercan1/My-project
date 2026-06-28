varor = []

while True:
    vara = input("Lägg till en vara (eller 'klar'): ")
    if vara == "klar":
        break
    else:
        varor.append(vara)

print("Inköpslistan:")
for vara in varor:
    print(vara)