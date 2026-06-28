import tkinter as tk

saldo = 1000
senaste_val = "insättning"


def insättning():
    global saldo

    try:
        belopp = int(inmatning.get())
        saldo += belopp

        text.config(
            text=f"Du satte in {belopp} kr.\nSaldo: {saldo} kr"
        )

        inmatning.delete(0, tk.END)

    except ValueError:
        text.config(text="Skriv ett giltigt nummer!")


def uttag():
    global saldo

    try:
        belopp = int(inmatning.get())

        if belopp > saldo:
            text.config(
                text="Inte tillräckligt med pengar."
            )
        else:
            saldo -= belopp

            text.config(
                text=f"Du tog ut {belopp} kr.\nSaldo: {saldo} kr"
            )

        inmatning.delete(0, tk.END)

    except ValueError:
        text.config(text="Skriv ett giltigt nummer!")


def välj_insättning():
    global senaste_val
    senaste_val = "insättning"
    text.config(text="Insättning vald\nSkriv belopp och tryck Enter")


def välj_uttag():
    global senaste_val
    senaste_val = "uttag"
    text.config(text="Uttag valt\nSkriv belopp och tryck Enter")


def enter_tryck(event):
    if senaste_val == "insättning":
        insättning()
    else:
        uttag()


def visa_saldo():
    text.config(
        text=f"Ditt saldo är {saldo} kr"
    )


def avsluta():
    text.config(
        text="Tack för att du använde vår ATM.\nHa en bra dag!"
    )
    fönster.after(2000, fönster.destroy)


fönster = tk.Tk()

fönster.title("Min ATM")
fönster.geometry("300x350")


text = tk.Label(
    fönster,
    text="Välkommen till ATM",
    font=("Arial", 12)
)

text.pack(pady=20)


etikett = tk.Label(
    fönster,
    text="Skriv belopp:"
)

etikett.pack()


inmatning = tk.Entry(fönster)
inmatning.pack(pady=10)

inmatning.focus_set()

# ENTER-knappen
inmatning.bind("<Return>", enter_tryck)


tk.Button(
    fönster,
    text="Insättning",
    command=välj_insättning
).pack(pady=5)


tk.Button(
    fönster,
    text="Uttag",
    command=välj_uttag
).pack(pady=5)


tk.Button(
    fönster,
    text="Visa saldo",
    command=visa_saldo
).pack(pady=5)


tk.Button(
    fönster,
    text="Avsluta",
    command=avsluta
).pack(pady=5)


fönster.mainloop()