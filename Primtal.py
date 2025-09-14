# Skapa en funktion som heter is_prime(n) som avgör om n är ett primtal
# Be användaren mata in ett heltal
# Om inmatningen inte är ett heltal, skriv ut ett felmeddelande
# Kontrollera om talet är ett primtal
# Om talet bara är delbart med 1 och sig själv, skriv ut talet

# Skapa en funktion som heter is_prime(n) och som avgör om ett tal är ett primtal
def is_prime(n):
    if n < 2:
        return False
    # Kontrollera om n är delbart med något tal mellan 2 och roten ur n (sig självt)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def huvudprogram():
    try:
        # Be användaren mata in ett heltal
        user_input = input("Mata in ett heltal: ")
        max_number = int(user_input)
        print(f"Primtal upp till {max_number}:")

    # Loopa igenom alla tal från 2 upp till max_number
        for number in range(2, max_number + 1):
            if is_prime(number):
                print(number)

    except ValueError:
        # Hantera felinmatning, t.ex. om användaren matar in en sträng

        print("Fel: Du måste mata in ett giltigt heltal.")


# Kör programmet
huvudprogram()
