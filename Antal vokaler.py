# 1. Läs in text från användaren
# 2. Sätt en räknare till 0
# 3. Loopa genom varje tecken i texten
# 4. Om tecknet är en vokal, öka räknaren med 1
# 5. Skriv ut räknarens värde

# Läser in text från användaren
text = input("Skriv in en text så räknar jag vokalerna åt dig: ")

# Lista med vokaler
vokaler = "aeiouyåäöAEIOUYÅÄÖ"

# Sätter en räknare till 0
antal = 0

# Loopar genom varje tecken i texten från användaren
for tecken in text:
    # Kollar om tecknet är en vokal, ökar isånafall räknaren med 1
    if tecken in vokaler:
        antal += 1

# Skriver ut räknarens värde (antal vokaler)
print(f"Din text innehåller {antal} vokaler")
