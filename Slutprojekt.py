# While loop och felhantering av felaktig inmatning från användaren
while True:
    kön = input("Man eller kvinna?: ").strip().lower()
    if kön == "man" or kön == "kvinna":
        break  # Avslutar loopen om allt är korrekt
    else:  # Skrivs ut om kön inte är man eller kvinna
        print("Felaktig inmatning. Skriv 'man' eller 'kvinna'. Försök igen.")

# Funktion med while loop och felhanteirng ifall användaren skriver in felaktig inmatning


def inputAndValidate(prompt, value_type):
    while True:
        try:
            value = value_type(input(prompt))
            if value <= 0:  # Kontrollerar om värdet är ett negativt tal
                print(f"Värdet måste vara ett positivt tal. Försök igen.")
                continue
            return value
        except ValueError:
            print(
                f"Felaktig inmatning. Försök {prompt.lower().strip(': ')} igen.")


# Anropas
ålder = inputAndValidate("Ange ålder:", int)
vikt = inputAndValidate("Ange vikt i kg:", int)
längd = inputAndValidate("Ange längd i cm:", int)

# Ordbok med kommentarer till de olika valen för aktivitetsnivå
beskrivningar = {
    1: "Lite/ingen träning - dags att komma igång kanske?",
    2: "Du tränar 1-3 dagar i veckan - bra jobbat!",
    3: "Du tränar 4-5 dagar i veckan - starkt jobbat!",
    4: "Du tränar 6-7 dagar i veckan - imponerande!",
    5: "Du tränar två gånger om dagen - IRONMAN!"
}

# Ordbok med PAL värden
pal_värden = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

# Skriver ut val för aktivitetsnivå
print("Välj aktivitetsnivå")
print("Välj 1 för Lite/ingen träning")
print("Välj 2 för 1-3 dagar/vecka")
print("Välj 3 för 4-5 dagar/vecka")
print("Välj 4 för 6-7 dagar/vecka")
print("Välj 5 för 2 ggr per dag")

# While loop med try, if, else & except för inmatning av aktivitetsnivå
while True:
    try:
        pal = int(input("Enter value (1-5): "))
        if pal in [1, 2, 3, 4, 5]:
            print(beskrivningar[pal])
            break
        else:
            print("Du måste skriva in ett heltal mellan 1 och 5. \n")
    except ValueError:
        print("Du måste skriva in ett heltal mellan 1 och 5. \n")

# Funktion för beräkning av BMR


def beräkna_bmr_tdee(kön, vikt, längd, ålder):

    # Kontrollerar kön
    if kön.lower() == "man":
        bmr = 10 * vikt + 6.25 * längd - 5 * ålder + 5
    else:
        bmr = 10 * vikt + 6.25 * längd - 5 * ålder - 161
    return bmr


# Beräknar TDEE
tdee = beräkna_bmr_tdee(kön, vikt, längd, ålder) * pal_värden[pal]

# Printar ut kcal per dag för användaren
print(f"Din kropp förbrukar {tdee:.2f} kcal per dag, vill du gå ned i vikt så ät färre än {tdee:.2f} kcal, vill du gå upp i vikt så ät fler än {tdee:.2f} kcal")
