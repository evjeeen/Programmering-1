# 1. Sätt startkapital till 100,000 kr
# 2. Läs in räntesats från användaren
# 3. Loopa över 5 år
#    a) Beräkna kapital med ränta
#    b) Skriv ut kapitalet för året
# 4. Avsluta programmet

# Startkapital
startkapital = 100000

# Frågar användaren efter en räntesats
räntesats = float(input("Ange årlig räntesats: "))

# Omvandlar räntesatsen från procent till decimalform
ränta = räntesats / 100

# Skriver ut tabellen
print("\nKapitalutveckling över 5 år")
print("---------------------------- ")
print("År\tBelopp (kr)")

# Initiera kapitalet med startvärdet
kapital = startkapital

# Loop för att beräkna och skriva ut beloppet för varje år
for år in range(1, 6):

    # Beräkna nytt kapital med ränta
    kapital *= (1 + ränta)

    # Skriv ut årets nummer och kapitalet med två decimaler
    print(f"{år}\t{kapital:.2f}")
