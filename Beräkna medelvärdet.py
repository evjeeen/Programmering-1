# 1. Läs in tre tal från användaren
# 2. Beräkna medelvärdet
# 3. Skriv ut medelvärdet
# 4. Om medelvärdet > 90, skriv ut "Bra jobbat!"

# Fråga användaren efter tre provresultat
prov1 = float(input("Ange poäng för prov 1: "))
prov2 = float(input("Ange poäng för prov 2: "))
prov3 = float(input("Ange poäng för prov 3: "))

# Beräkna medelvärdet
medelvärde = (prov1 + prov2 + prov3) / 3

# Skriv ut medelvärdet
print(f"Medelvärdet av dina tre provresultat är: {medelvärde:.2f}")

# Kontrollera resultat med if-sats
if medelvärde > 90:
    print("Bra jobbat!")
