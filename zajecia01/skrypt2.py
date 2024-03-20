import random
import math
wartosc=100
dodawanie=wartosc+123.15
potega=dodawanie**123
tekst=str(potega)
wartosc_pi=math.pi
tekst = f"Wartosc: {tekst}"
lista = [1, 2, 3, 4, 5]
losowa = random.choice(lista)
print(len(tekst))
print(tekst[1:4])
print(dir(lista))
tekst=tekst.upper()
print(tekst)
#tekst[2]="p"
lista=list(tekst)
lista=lista[0:8]
bufor=[1,2,3,4,5]
lista.append(bufor)
lista.remove(':')
print(lista)


print(f"wartosc {wartosc}, dodawanie {dodawanie}, potega {potega}, tekst {tekst}, wartoscpi {wartosc_pi}, losowa  {losowa}")

lista2 = [1,2,3,"banan",100]
lista3=[]
lista4=[]
for i in range(len(lista2)):
    if lista2[i] != "banan":
        lista3.append(lista2[i] ** 2)


for i in range(2,16,2):
    lista4.append(i)
print(f"lista2:{lista2},lista3:{lista3},lista4:{lista4}")


ja = {
    'imie': 'Piotr','nazwisko': 'Krajewski','wiek': 21,
    'rodzice': [
        {'imie': 'Malgorzata', 'wiek': 44},
        {'imie': 'Marek', 'wiek': 47}
    ]
}

print(ja['rodzice'])
print(ja['rodzice'][0]['imie'])
print(ja.keys())
booll='rodzenstwo' in ja
print(booll)

krotka=(1,2,"3",4,2,5)
print(len(krotka),krotka[0])

print(krotka.count(2))
#krotka[0]=2
