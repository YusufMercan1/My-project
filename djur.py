class Djur:
    def __init__(self, namn, ljud):
        self.namn = namn
        self.ljud = ljud
    def prata(self):
            return self.ljud

class Hund(Djur):
    def __init__(self, namn):
        super().__init__(namn, ljud="Voff")  


class Katt(Djur):
    def __init__(self, namn):
        super().__init__(namn, ljud="Mjau")
    
Hund1 = Hund("Fido")
Katt1 = Katt("Misse")
djur_lista = [Hund1, Katt1]
for djur in djur_lista:
    print(f"{djur.namn} säger {djur.prata()}")