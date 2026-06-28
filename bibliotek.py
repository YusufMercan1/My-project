class Bibliotek:
    def __init__(self):
        self.böcker = []

    def lägg_till_bok(self, bok):
        self.böcker.append(bok)

    def visa_böcker(self):
        for bok in self.böcker:
            print(bok)
    def låna_bok(self, isbn):
        for bok in self.böcker:
            if bok.isbn == isbn and not bok.utlånad:
                bok.utlånad = True
                print(f"Du har lånat {bok.titel}.")
                return
        print("Boken är inte tillgänglig för utlåning.")
    def söka_bok(self, titel):
        for bok in self.böcker:
            if bok.titel.lower() == titel.lower():
                print(bok)
                return
        print("Boken hittades inte.")

    def återlämna_bok(self, isbn):
        for bok in self.böcker:
            if bok.isbn == isbn and bok.utlånad:
                bok.utlånad = False
                print(f"Du har återlämnat {bok.titel}.")
                return
        print("Boken är inte utlånad eller finns inte i biblioteket.")
    def visa_utlånade_böcker(self):
        for bok in self.böcker:
            if bok.utlånad:
                print(bok)
    def visa_tillgängliga_böcker(self):
        for bok in self.böcker:
            if not bok.utlånad:
                print(bok)
                
    

    



class Bok:
    def __init__(self, titel, författare, isbn):
        self.titel = titel
        self.författare = författare
        self.isbn = isbn
        self.utlånad = False


    def __str__(self):
        return f"{self.titel} av {self.författare} (ISBN: {self.isbn})"    
    

    

bibliotek = Bibliotek()
bok1 = Bok("Harry Potter", "J.K. Rowling", "123")
bok2 = Bok("The Hobbit", "Tolkien", "456")
bibliotek.lägg_till_bok(bok1)
bibliotek.lägg_till_bok(bok2)
bibliotek.visa_tillgängliga_böcker()
bibliotek.låna_bok("123")
bibliotek.visa_tillgängliga_böcker()