
**Nazwa projektu:** Integracja danych dotyczących konfliktów zbrojnych i cen surowców

**Skład grupy projektowej:**
- Mateusz Pielak: Konfiguracja bazy danych, implementacja mechanizmu uwierzytelnienia i autoryzacji.
- Piotr Plewka: Implementacja kodu do integracji danych, przygotowanie interfejsu użytkownika.

**Wykorzystane technologie:**
- Python (pandas, matplotlib, Flask)
- MySQL
- JWT (do uwierzytelniania i autoryzacji)
- Aiven (serwer relacyjnej bazy danych)

**Opis projektu:** 
Projekt integruje dane dotyczące konfliktów zbrojnych (z Global Terrorism Database) z cenami surowców (z pliku JSON). Aplikacja umożliwia analizę zależności między konfliktami zbrojnymi a cenami surowców na przestrzeni lat. Przykładowe pytania, na które można znaleźć odpowiedzi przy użyciu aplikacji:
1. Jak zmieniała się cena ropy Brent w okresie zwiększonej aktywności terrorystycznej?
2. Czy można zauważyć korelację między ceną ropy naftowej a liczbą ataków terrorystycznych w danym regionie?
3. Czy cena cukru europejskiego jest zależna od ceny cukru amerykańśkiego??

Projekt zawiera skrypty napisane w języku Python do analizy danych oraz wizualizacji przy użyciu różnych zestawów danych.

**Informacje o konfiguracji środowiska IDE:**
Do uruchomienia kodu źródłowego, wymagane są następujące zależności:
- Python 3.x
- Biblioteki: pandas, matplotlib, Flask, PyJWT
- Baza danych MySQL

**Źródła wykorzystanych danych:**
1. Global Terrorism Database (https://www.kaggle.com/datasets/START-UMD/gtd/data)
2. Commodity Prices Filtered (https://www.kaggle.com/code/josephdepalo/commodity-prices-time-series/input)
