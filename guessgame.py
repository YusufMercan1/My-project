import random
hemligt=random.randint(1, 100)
print("Välkommen till gissningsspelet!")
while True:
    gissning=int(input("Gissa ett tal mellan 1 och 100: "))
    if gissning < hemligt:
        print("För lågt! Försök igen.")
    elif gissning > hemligt:
        print("För högt! Försök igen.")
    else:
        print("Grattis! Du gissade rätt!")
        break