import sys
from mpmath import mp
import os

class Tablica:
    def __init__(self, n):
        self.n = n
        self.pobierz()

    def pobierz(self):
        mp.dps = self.n**2+1
        liczba = str(mp.pi).replace(".", "")
        self.tab = [int(cyfra) for cyfra in liczba]


    def wyswietl(self):
        result = ""
        k = 0

        for i in range(self.n):
            for j in range(self.n):
                result += f"{self.tab[k]}   "
                k += 1
            result += "\n"

        result += "\nSumy \"przekątnych\":\n"
        for d in range(-(self.n - 1), self.n):
            if d >= 0:
                suma = sum(int(self.tab[i + (j + d) * self.n]) for i, j in zip(range(self.n - d), range(self.n)))
            else:
                suma = sum(int(self.tab[i - d + j * self.n]) for i, j in zip(range(self.n), range(self.n + d)))
            result += f"{suma}  "

        return result

if __name__ == "__main__":

    katalog = "wejscie"
    katalog_wyniki = "wyniki"
    obiekty_klas = []

    if not os.path.exists(katalog):
        sys.exit(f"Podany katalog '{katalog}' nie istnieje.")

    lista_plikow = os.listdir(katalog)
    lista_plikow2 = os.listdir(katalog)

    if not os.path.exists(katalog_wyniki):
        os.makedirs(katalog_wyniki)

    for idx, plik in enumerate(lista_plikow2):
        if plik.endswith(".txt"):
            sciezka_pliku = os.path.join(katalog, plik)
            try:
                with open(sciezka_pliku, 'r') as file:
                    zawartosc = file.read().strip()

                    if not zawartosc:
                        komunikat = f"Błąd w pliku '{sciezka_pliku}': Plik jest pusty."
                        print(komunikat)
                        nazwa_pobranego_pliku = os.path.splitext(plik)[0]
                        with open(os.path.join(katalog_wyniki, f"{nazwa_pobranego_pliku}_wynik.txt"), 'w') as blad_file:
                            blad_file.write(komunikat)
                        lista_plikow.remove(plik)
                        continue

                    if not zawartosc.isdigit() or int(zawartosc) <= 0:
                        komunikat = f"Błąd w pliku '{sciezka_pliku}': Plik nie zawiera poprawnej liczby dodatniej."
                        print(komunikat)
                        nazwa_pobranego_pliku = os.path.splitext(plik)[0]
                        with open(os.path.join(katalog_wyniki, f"{nazwa_pobranego_pliku}_wynik.txt"), 'w') as blad_file:
                            blad_file.write(komunikat)
                        lista_plikow.remove(plik)
                        continue

                    liczba = int(zawartosc)
                    nazwa_obiektu = f"obiekt{idx + 1}"
                    obiekt_klasy = Tablica(liczba)
                    obiekty_klas.append(obiekt_klasy)

            except (ValueError, IOError) as e:
                komunikat = f"Błąd podczas odczytu pliku '{sciezka_pliku}': {e}"
                print(komunikat)
                nazwa_pobranego_pliku = os.path.splitext(plik)[0]
                with open(os.path.join(katalog_wyniki, f"{nazwa_pobranego_pliku}_wynik.txt"), 'w') as blad_file:
                    blad_file.write(komunikat)
                lista_plikow.remove(plik)

    if obiekty_klas:
        print()
        for nazwa_pobranego_pliku, obiekt_klasy in zip(lista_plikow, obiekty_klas):
            nazwa = os.path.splitext(nazwa_pobranego_pliku)[0]
            sciezka_wyniku = os.path.join(katalog_wyniki, f"{nazwa}_wynik.txt")

            print(f"Wynik dla pliku: {katalog}\\{nazwa_pobranego_pliku}")
            print(obiekt_klasy.wyswietl())
            print()

            try:
                with open(sciezka_wyniku, 'w') as wynik_file:
                    wynik_file.write(obiekt_klasy.wyswietl())

            except IOError as e:
                komunikat = f"Błąd podczas zapisu do pliku '{sciezka_wyniku}': {e}"
                print(komunikat)
                with open(os.path.join(katalog_wyniki, f"{nazwa_pobranego_pliku}_wynik.txt"), 'w') as blad_file:
                    blad_file.write(komunikat)
                lista_plikow.remove(nazwa_pobranego_pliku)


