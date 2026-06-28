class Bankkonto:
    def __init__(self,ägare,saldo=0):
        self.ägare = ägare
        self.saldo = saldo

    def sätt_in(self,belopp):
    
            self.saldo += belopp
            print(f"{belopp} kr har satts in på kontot. Nytt saldo: {self.saldo} kr.")
    def ta_ut(self,belopp):
                if belopp > self.saldo:
                    print("Otillräckligt saldo.")
                else:
                    self.saldo -= belopp
                    print(f"{belopp} kr har tagits ut från kontot. Nytt saldo: {self.saldo} kr.")

konto1 = Bankkonto("Alice", 1000)
konto1.sätt_in(500)
konto1.ta_ut(200)

        
