import numpy as np


miejsca=np.empty((2,20,20),dtype='U30')
for i in range(20):
    for j in range(20):
        miejsca[0][i][j]="wolne"

#TA FUNKCJA ZROBIONA NA WYJATKACH
def sprawdzmiejsca(miejsca):
    flag=0
    for i in range(20):
        for j in range(20):
            if miejsca[0][i][j]=="wolne":
                flag=1
    try:
        if flag ==0:
            raise ValueError("BRAK DOSTEPNYCH MIEJSC")
    except ValueError as e:
        komunikat="UWAGA: "+ str(e)
    else:
        komunikat=("DOSTEPNE MIEJSCA")
    return komunikat


#TA FUNKCJA ZROBIONA NA IF/ELSE ABY ZOBRAZOWAC PODOBIENSTWA DO WYJATKOW
def rezerwujmiejsce(miejsca):
    print("Do wyboru jest 20 miejsc w 20 rzedach")
    rzad=int(input("Podaj rzad"))
    numer=int(input("Podaj numer fotela od lewej"))
    if miejsca[0][rzad-1][numer-1]=="wolne":
        nazwisko=input("Podaj imie i nazwisko")
        flag=0
        for i in range(20):
            for j in range(20):
                if miejsca[1][i][j]==nazwisko:
                    flag=1
        if flag==0:
            print("Zarezerwowano miejsce nr ", numer, " w rzedzie ",rzad, " na nazwisko ",nazwisko)
            miejsca[0][rzad-1][numer-1]="ZAJETE"
            miejsca[1][rzad-1][numer-1]=nazwisko
        else:
            print("Wpisane nazwisko ma juz zarezerwowane miejsce")
    else:
        print("Wybrane miejsce jest zajete/nie ma takiego miejsca")
    return rzad, numer


#TA FUNKCJA ZROBIONA ZNOW NA WYJATKACH
def anuluj(miejsca):
    try:
        rzad = int(input("Podaj rzad: "))
        numer = int(input("Podaj numer fotela od lewej: "))
        if miejsca[0][rzad - 1][numer - 1] != "ZAJETE":
            raise ValueError("Wybrane miejsce nie jest zajete")
        nazwisko = input("Podaj imie i nazwisko: ")
        if miejsca[1][rzad - 1][numer - 1] != nazwisko:
            raise ValueError("Wybrana rezerwacja nie istnieje na dane nazwisko")
        print("Anulowano rezerwacje: miejsce nr", numer, "w rzedzie", rzad, "na nazwisko", nazwisko)
        miejsca[0][rzad - 1][numer - 1] = "wolne"
        miejsca[1][rzad - 1][numer - 1] = ""
    except ValueError as e:
        print("Wystapil blad:", e)
    return rzad, numer


def rezerwacje(miejsca):
    opcja=0
    while opcja!=4:
        opcja=int(input("Co chcesz zrobic? \n 1.Sprawdz dostepnosc miejsc \n 2.Zarezerwuj konkretne miejsce \n 3.Anuluj swoja rezerwacje\n 4.Zamknij program\n"))
        if opcja==1:
            print("Sprawdz dostepnosc miejsc")
            print(sprawdzmiejsca(miejsca))
        elif opcja==2:
            print("Zarezerwuj konkretne miejsce")
            rezerwujmiejsce(miejsca)
        elif opcja==3:
            print("Anuluj swoja rezerwacje")
            anuluj(miejsca)
        elif opcja==4:
            print("ZAMYKAM PROGRAM")
            exit
        else:
            print("Nie wybrano opcji 1,2,3 lub 4.")

rezerwacje(miejsca)
