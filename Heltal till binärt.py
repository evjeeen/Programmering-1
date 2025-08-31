# - Läs in tre heltal från användaren
# - Omvandla varje heltal till binär form med funktionen bin()
# - Lagra de binära talen i en lista
# - Skriv ut hela listan med de binära representationerna

# Skapa en tom lista för lagring av binära tal
binära_tal = []

# Läs in tre heltal från användaren
for i in range(3):
    heltal = int(input(f"Ange heltal nummer {i+1}: "))
    # Omvandla till binärt
    binärt = bin(heltal)
# Lägg till i lista
    binära_tal.append(binärt)

# Skriv ut hela listan med binära representationer
print("Binära representationer:", binära_tal)
