from datetime import datetime
idag = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
input_text = input("Skriv in din dagbokspost: ")
with open("dagbok.txt", "a") as f:
    f.write(f"{idag} - {input_text}\n")
with open("dagbok.txt", "r") as f:
    print(f.read())
