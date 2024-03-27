import this
import funkcje
#6
dane =(2024,'Python',3.8)
rok,jezyk,wersja=dane
print( rok,jezyk,wersja)
#7
oceny=[4,3,5,2,5,4]
pierwsza,*srodek,ostatnia=oceny
print(pierwsza, srodek, ostatnia)

#8 
info=('Jan','Kowalski',30,'Polska','programista')
imie,nazwisko,_,_,zawod=info
print(imie,nazwisko,zawod)
#9
dane =(2024,['Python',3.8,('Stabilna','Wersja')])
rok=dane[0]
jezyk=dane[1][0]
wersja=dane[1][1]
opis=dane[1][2]
print(rok,jezyk,wersja,opis)
#10
a=b=[1,2,3]
b[0]='zmieniono'
print(a,b)

#11
c=a[:]
c[0]='nowa wartosc'
print(a,b,c)

#12
x=y=10
y=y+1
print(x,y)
#13
K=[1,2]
L=K
K=K+[3,4]
M=[1,2]
N=M
M+=[3,4]
print(K,L,M,N)

#14
imiona=['Anna','Jan','Ewa']
oceny=[5,4,3]
zip(imiona,oceny)

for i in range(3):
    print(imiona[i])

#generatory, yield poczytac
#nonlocal a,b,c poczytac
#
    #15
def kwadrat(x):
    return x ** 2
liczby = [1, 2, 3, 4, 5]
kwadraty = list(map(kwadrat, liczby))

print(kwadraty)

#16

przyklad=2

print(liczby)
print(przyklad)
funkcje.zmien_wartosc(liczby)
przyklad=funkcje.zmien_wartosc(przyklad)
print(liczby)
print(przyklad)

#17


zamowienia = [['chleb',1.50,5],['sok',2.50,10],['majonez',5,2]]

for _ in range(3):
    [podsumowanie,wz]= funkcje.zamowienie_produktu(zamowienia[_][0],zamowienia[_][1],zamowienia[_][2])
    print(podsumowanie)
#18
# #def stworz_raport(*args, **kwargs):
#     for id_produktu in args:
#         print(f"Informacje o produkcie o ID {id_produktu}:")
#         for key, value in kwargs.items():
#             if key.startswith(f"{id_produktu}_"):
#                 print(f"{key.split('_')[1].capitalize()}: {value}")
#         print()


#stworz_raport(101, 102, 101_nazwa="Kubek termiczny", 101_cena="45.99 zł", 102_nazwa="Długopis", 102_cena="4.99 zł")

#19

potega_2 = funkcje.stworz_funkcje_potegujaca(2) 
print(potega_2(6))

#20


# licznik_a = funkcje.licznik()
# print(licznik_a())  
# print(licznik_a())  
# print(licznik_a()) 



globalny_licznik = 0



print(funkcje.licznik())  
print(funkcje.licznik())  
print(funkcje.licznik())





licznik_c = funkcje.Licznik()
print(licznik_c())  
print(licznik_c())  
print(licznik_c())





print(funkcje.licznik())  
print(funkcje.licznik())  
print(funkcje.licznik())


#21
# def licznik():
#     licznik_stan = 0

#     def zwieksz_licznik():
#         nonlocal licznik_stan
#         licznik_stan += 1
#         return licznik_stan

#     return zwieksz_licznik

# licznik_a = licznik()
# print(licznik_a())  
# print(licznik_a())  
# print(licznik_a()) 

#22
lista_ksiazek = [
    {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Władca Pierścieni: Drużyna Pierścienia', 'autor': 'J.R.R. Tolkien', 'rok_wydania': 1954},
    {'tytul': 'Game of Thrones', 'autor': 'George R.R. Martin', 'rok_wydania': 1996},
    {'tytul': 'Czarodziejka z Księżyca', 'autor': 'Naoko Takeuchi', 'rok_wydania': 1991},
    {'tytul': 'Programowanie w Pythonie', 'autor': 'Eric Matthes', 'rok_wydania': 2016},
    {'tytul': 'Czysty kod', 'autor': 'Robert C. Martin', 'rok_wydania': 2008}
]

posortowane_ksiazki = sorted(lista_ksiazek, key=lambda x: x['rok_wydania'])
print("Posortowane książki według roku wydania:")
for ksiazka in posortowane_ksiazki:
    print(ksiazka)

ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, lista_ksiazek))
print("\nKsiążki wydane po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(ksiazka)

tytuly_ksiazek = list(map(lambda x: x['tytul'], lista_ksiazek))
print("\nTytuły książek:")
print(tytuly_ksiazek)

#23


print("Pełny tydzień:")
for dzien in funkcje.generator_dni_tygodnia():
    print(dzien)

print("Pierwsze trzy dni tygodnia:")
iterator_dni = funkcje.generator_dni_tygodnia()
pierwszy_dzien = next(iterator_dni)
drugi_dzien = next(iterator_dni)
trzeci_dzien = next(iterator_dni)
print(pierwszy_dzien, drugi_dzien, trzeci_dzien)

