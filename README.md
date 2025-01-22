#### **Wykonane kroki**

1. **Utworzenie repozytorium na GitHub:**
  ****
  - Utworzyłem publiczne repozytorium o nazwie `kalkulator-python` na koncie GitHub: [https://github.com/mkonefal2/kalkulator-python](https://github.com/mkonefal2/kalkulator-python).
  - Zainicjalizowałem repozytorium z plikiem README.
2. **Klonowanie repozytorium:**
  
  - Skopiowałem repozytorium na lokalny komputer przy użyciu polecenia:
    
    ```bash
    git clone https://github.com/mkonefal2/kalkulator-python.git
    ```
    
  - Sprawdziłem, że repozytorium zostało sklonowane poprawnie.
3. **Stworzenie pliku `kalkulator.py`:**
  
  - Utworzyłem plik `kalkulator.py` za pomocą `touch` i napisałem prosty kalkulator w Pythonie obsługujący dodawanie, odejmowanie, mnożenie i dzielenie.
  - Kod został zapisany i przetestowany lokalnie:
    
    ```bash
    python3 kalkulator.py
    ```
    
  - Wynik działania kalkulatora był prawidłowy.
4. **Dodanie pliku do repozytorium lokalnego:**
  
  - Plik `kalkulator.py` został dodany do obszaru staging:
    
    ```bash
    git add kalkulator.py
    ```
    
5. **Konfiguracja Git:**
  
  - Po pierwszym commicie Git zgłosił brak danych tożsamości autora.
  - Rozwiązałem to, konfigurując globalną nazwę i adres e-mail:
    
    ```bash
    git config --global user.name "Mkonefal"
    git config --global user.email "michalkonefal@hotmail.com"
    ```
    
6. **Commit pliku:**
  
  - Wykonałem commit z opisem:
    
    ```bash
    git commit -m "Dodano kalkulator w Pythonie"
    ```
    
7. **Wypchnięcie zmian na GitHub:**
  
  - Przesłałem zmiany do zdalnego repozytorium za pomocą:
    
    ```bash
    git push origin main
    ```
    
  - Plik `kalkulator.py` został poprawnie przesłany do repozytorium.

---

#### **Napotkane wyzwania**

1. **Brak narzędzia Git w systemie:**
  
  - Przy pierwszej próbie klonowania repozytorium system zgłosił brak polecenia `git`.
  - Rozwiązanie: Zainstalowałem Git za pomocą:
    
    ```bash
    sudo apt install git -y
    ```
    
2. **Brak konfiguracji użytkownika Git:**
  
  - Podczas pierwszego commitu Git zgłosił brak ustawionej tożsamości autora.
  - Rozwiązanie: Skonfigurowałem globalne dane użytkownika (nazwa i e-mail).
3. **Autoryzacja z GitHub:**

 - Przy pushowaniu zmian wymagana była autoryzacja za pomocą tokenu GitHub, zamiast hasła.
- Rozwiązanie: Użyłem wcześniej skonfigurowanego tokenu GitHub do autoryzacji.

``
