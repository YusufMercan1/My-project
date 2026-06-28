mening=input("Skriv en mening: ")

print ("Antal tecken i meningen: ", len (mening))
print ("Mening i versaler: ", mening.upper())
print ("Mening i gemener: ", mening.lower())
if "Python" in mening:
    print ("Mening innehåller ordet 'Python'")
else:
    print ("Mening innehåller inte ordet 'Python'")