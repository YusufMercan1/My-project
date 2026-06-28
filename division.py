import random, string

string.ascii_letters, string.digits, string.punctuation

random.choice(string.ascii_letters + string.digits + string.punctuation)

tecken = ""

användbokstäver = input("Vill du använda bokstäver? (ja/nej): ")

if användbokstäver.lower() == "ja":
    tecken = tecken + string.ascii_letters

användsiffror = input("Vill du använda siffror? (ja/nej): ")

if användsiffror.lower() == "ja":
    tecken = tecken + string.digits

användspecialtecken = input("Vill du använda specialtecken? (ja/nej): ")

if användspecialtecken.lower() == "ja":
    tecken = tecken + string.punctuation

längd = int(input("Hur lång ska lösenordet vara? "))

lösenord = ''.join(random.choice(tecken) for i in range(längd))

print("Ditt genererade lösenord är:", lösenord)