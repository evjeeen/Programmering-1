# 1. Be användaren mata in ett pris
# 2. Spara priset i en variabel
# 3. Multiplicera priset med (1 + moms)
# 4. Skriv ut det nya priset med 2 decimaler

# Definiera momssatsen som konstant
MOMS = 0.25

# Användaren skriver in ett pris exkl. moms
pris = float(input('Ange pris exkl. moms: '))

# Beräkna priset inkl. moms
momsbelopp = pris * MOMS

# Beräkna den totala kostnaden inkl. moms
total_kostnad = pris + momsbelopp

# Skriv ut momsbelopp & totalt pris inkl moms med två decimaler
print(f'Momsbelopp: {momsbelopp:.2f} kr')
print(f'Totalt pris inkl. moms: {total_kostnad:.2f} kr')
