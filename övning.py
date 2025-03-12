class husdjur:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder
        self.energi = 10  # Instansvariabel energi som startar på 10

    def presentera(self):
        print(f"Mitt husdjur heter {self.namn}, är {self.ålder} år gammal och har {self.energi} energi.")

    def äta(self):
        self.energi += 5  # Ökar energi med 5
        print(f"{self.namn} har ätit och har nu {self.energi} energi.")

    def hoppa(self):
        if self.energi > 0:  # Minskar energi med 3 om energi är större än 0
            self.energi -= 3
            print(f"{self.namn} har hoppat och har nu {self.energi} energi.")
        else:
            print(f"{self.namn} är för trött för att hoppa!")

# Skapar ett husdjur
mitt_husdjur = husdjur("Fido", 1)

# Presenterar husdjuret
mitt_husdjur.presentera()

# While-loop för interaktion med husdjuret
while True:
    # Meny för användaren
    print("\nVad vill du göra med ditt husdjur?")
    print("1. Mata husdjuret")
    print("2. Låt husdjuret hoppa")
    print("3. Avsluta programmet")
    
    val = input("Välj ett alternativ (1, 2 eller 3): ")  # Tar emot användarens val

    if val == "1":
        mitt_husdjur.äta()  # Mata husdjuret
    elif val == "2":
        mitt_husdjur.hoppa()  # Låt husdjuret hoppa
    elif val == "3":
        print("Programmet avslutas. Hej då!")
        break  # Avslutar loopen och programmet
    else:
        print("Ogiltigt val. Försök igen.")  # Hanterar ogiltiga val

    # Visar husdjurets status efter varje interaktion
    mitt_husdjur.presentera()