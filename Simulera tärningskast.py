# Skapa ett program som kastar två tärningar och som visar den sammanglada summan
# Tärningarna ska visa slumptal mellan 1 & 6

# Använd import random
import random

# Generera ett slumpmässigt tal mellan 1 & 6 och spara det som "kast1"
# Generera ett till slumpmässigt tal mellan 1 & 6 och spara det som "kast2"


def kasta_tarning():
    kast1 = random.randint(1, 6)
    kast2 = random.randint(1, 6)

    # Beräkna summan av "kast1" & "kast2"
    summa = kast1 + kast2

    # Skriv ut värdet av "kast1" & "kast2"
    print(f"Första kastet: {kast1} ")
    print(f"Andra kastet: {kast2}")

    # Returnera summan
    return summa


# Spara resultatet från funktionen "kasta_tarning" i variabeln "resultat"
resultat = kasta_tarning()
# Skriv ut summan av de två tärningskasten
print(f"Summan av två tärningskast är: {resultat}")
