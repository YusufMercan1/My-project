import json
def ladda_kontaktbok(filnamn):
    try:
        with open(filnamn, 'r') as fil:
            kontaktbok = json.load(fil)
            return kontaktbok
    except FileNotFoundError:
        return []


kontaktbok = ladda_kontaktbok("kontaktbok.json")
while True:
    print("1. Lägg till kontakt")
    print("2. Visa kontakter")
    print("3. Sök kontakt")
    print("4. Ta bort kontakt")
    print("5. Spara kontaktbok")
    print("6. Avsluta")
    val = input("Välj ett alternativ: ")

    if val == "1":
        namn = input("Ange namn: ")
        telefonnummer = input("Ange telefonnummer: ")
        kontakt = {"namn": namn, "telefonnummer": telefonnummer}
        kontaktbok.append(kontakt)
        print("Kontakt tillagd!\n")
    elif val == "2":
        if not kontaktbok:
            print("Ingen kontakt finns i boken.\n")
        else:
            for kontakt in kontaktbok:
                print(f"Namn: {kontakt['namn']}, Telefonnummer: {kontakt['telefonnummer']}")
            print()
    elif val == "3":
        sok_namn = input("Ange namn att söka efter:\n")
        hittade_kontakter = [kontakt for kontakt in kontaktbok if sok_namn.lower() in kontakt['namn'].lower()]
        if hittade_kontakter:
            for kontakt in hittade_kontakter:
                print(f"Namn: {kontakt['namn']}, Telefonnummer: {kontakt['telefonnummer']}")
        else:
            print("Ingen kontakt hittades med det namnet.\n")
    elif val == "4":
        ta_bort_namn = input("Ange namn på kontakten att ta bort: ")
        kontakt_borttagen = False
        for kontakt in kontaktbok:
            if kontakt['namn'].lower() == ta_bort_namn.lower():
                kontaktbok.remove(kontakt)
                kontakt_borttagen = True
                print("Kontakt borttagen!\n")
                break
        if not kontakt_borttagen:
            print("Ingen kontakt hittades med det namnet.\n")
    elif val == "5":
        filnamn = input("Ange filnamn att spara kontaktboken (t.ex. kontaktbok.json): ")
        with open(filnamn, 'w') as fil:
            json.dump(kontaktbok, fil)
        print("Kontaktbok sparad!\n")       
    elif val == "6":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val, försök igen.\n")
