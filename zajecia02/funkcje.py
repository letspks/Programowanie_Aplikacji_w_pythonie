def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg


def zamowienie_produktu(nazwa_produktu, cena, ilosc=1):
    wartosc_zamowienia = cena * ilosc
    podsumowanie = f"Produkt: {nazwa_produktu}, Cena: {cena}, Ilość: {ilosc}, Łączna cena: {wartosc_zamowienia}"
    return podsumowanie, wartosc_zamowienia

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj


def licznik():
    licznik_stan = 0

    def zwieksz_licznik():
        nonlocal licznik_stan
        licznik_stan += 1
        return licznik_stan

    return zwieksz_licznik


def licznik():
    global globalny_licznik
    globalny_licznik += 1
    return globalny_licznik


class Licznik:
    def __init__(self):
        self.licznik_stan = 0

    def __call__(self):
        self.licznik_stan += 1
        return self.licznik_stan
    


def licznik():
    if not hasattr(licznik, 'licznik_stan'):
        licznik.licznik_stan = 0
    licznik.licznik_stan += 1
    return licznik.licznik_stan

def generator_dni_tygodnia():
    dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    for dzien in dni_tygodnia:
        yield dzien

