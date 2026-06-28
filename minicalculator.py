tal1= float(input("Skriv in det första talet: "))

operator= input("Skriv in operatorn (+, -, *, /): ")

tal2= float(input("Skriv in det andra talet: "))

if operator == "+":
    resultat= tal1 + tal2
elif operator == "-":
    resultat= tal1 - tal2
elif operator == "*":
    resultat= tal1 * tal2
elif operator == "/":
    if tal2 != 0:
        resultat= tal1 / tal2
    else:
        print("Fel: Division med noll är inte tillåten.")
        exit()
else:
    print("Fel: Ogiltig operator.")
    exit()

print(f"Resultat: {tal1} {operator} {tal2} = {resultat}")