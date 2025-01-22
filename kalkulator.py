def kalkulator():
    print("Prosty kalkulator:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz operację (1/2/3/4): ")

    if wybor in ['1', '2', '3', '4']:
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {liczba1 + liczba2}")
        elif wybor == '2':
            print(f"Wynik: {liczba1 - liczba2}")
        elif wybor == '3':
            print(f"Wynik: {liczba1 * liczba2}")
        elif wybor == '4':
            if liczba2 != 0:
                print(f"Wynik: {liczba1 / liczba2}")
            else:
                print("Błąd: dzielenie przez zero!")
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    kalkulator()

