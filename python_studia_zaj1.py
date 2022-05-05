import random
import math

# Funkcja ktora przyjmuje sekwencje/słowo(seq) oraz słownik(cn),
# nastepnie do slownika zostają dodane dane o ilosci wystapien danej litery w slowie.
def counter(cn, seq):
    if cn is None:
        cn = {}
    for i in seq:
        cn[i] = cn.get(i, 0) + 1
    return cn


# Funkcja dzieli wyraz na podane wycinki, nastepnie tworzy liste z numeracja kazdego wycinka.
def zbalansowanie(txt, n):
    lista = []
    for i in range(0, len(txt), n):
        lista.append(txt[i : n + i])
    print(lista)

    result = []
    for i in range(len(lista)):
        slownik = counter(None, lista[i])
        slownik = set(slownik.values())
        if len(slownik) == 1:
            result.append(i)
    return result


# print(zbalansowanie("motory", 2))


def counter(cn, add, sub=None):
    if cn is None:
        cn = {}
    for i in add:
        cn[i] = cn.get(i, 0) + 1

    if sub is not None:
        for i in sub:
            cn[i] = cn.get(i, 0) - 1
    return cn


lista = ["aaa", "aa", "aaa", "b", "b"]
lista2 = "Jakis tekst ha ha ha"
slownik2 = {"h": 2, "b": 2, "c": 4}
# print(counter(slownik2,"hhhhhbb","bbbc"))


def zbalansowanie(txt, n, step=1):
    lista = []
    for i in range(0, len(txt), step):
        lista.append(txt[i : n + i])
    print(lista)

    result = []
    for i in range(len(lista)):
        slownik = counter(None, lista[i])
        slownik = set(slownik.values())
        if len(slownik) == 1:
            if i == 0:
                result.append(i)
            else:
                result.append(i * n - step)
    return result


# print(zbalansowanie("aaaaabbc", 3,4))


def wycinek(t, n, step=1):
    i = 0
    while n <= len(t):
        print(t[i:n])
        n = n + 1
        i = i + 1


# wycinek("abecaclo",3,1)
def testowanie():
    x = y = list("abcde")
    y[0] = "d"
    print(x)
    # czy caly wycinek to lista?
    print(x[:] is x)
    # zamiana na niepowtarzalne znaki oryginalne tab
    x[:] = set(x)
    print(x)


# testowanie()


def predykt():
    # to co chce kolekcjonować, dziedzina, predykat opcjonalnie
    print([a**-3 for a in range(8, 29) if a % 4 == 3])


# predykt()

# wczytujemy tekst, litere i dzielimy na slowa, a potem listy comprahension i filtruje po literach
def zadanie1():
    tekst = input("podaj slowa:")
    tekst = tekst.split()
    litera = input("podaj litere")
    print([i for i in tekst if litera == i[0]])


# zadanie1()

# generujemy liste i dzielimy na wycinki
def zadanie2():
    lista = input("podaj liste:")
    lista = lista.split()
    n = 0
    print([lista[i : i + 2] for i in range(0, len(lista), 2)])  # if len(i)%2 == 0


# zadanie2()


def zad3():
    a = range(1, 11)
    print([[i * w for i in a] for w in a])


# zad3()

# filtrujemy elem z tekstu zeby sie nie powtarzalo
# dzielimy na slowa, potem przegladamy, jezeli slowo ma
# mniej niz 3 litery pomijamy, a jak maja wiecej niz 3 litery to wyciagamy ostatnie 3 litery
def zad4():
    tekst = input("podaj slowa")
    tekst = tekst.split()
    print(set([i[-3:] for i in tekst if len(i) > 3]))


# zad4()


def zad5():
    # lista = input("podaj liste:")
    lista = "Podaj tekst sialala siaial aaaa bbbb"
    lista = lista.split()
    pary = [lista[i : i + 2] for i in range(0, len(lista), 2)]
    print(pary)
    slownik = {i[1].upper(): i[0] for i in pary}
    print(slownik)


def zad6():
    tekst = "Ruda kot mati plot"
    tekst = tekst.split(" ")
    pary = [tekst[i : i + 2] for i in range(0, len(tekst), 2)]
    slownik = {i[1].upper(): i[0] for i in pary}
    slownik2 = {y: x for x, y in slownik.items()}
    print(slownik2)


# zad6()


# 7 elementowa liste liczb pseudolosowych z zakresu {-5,5} liczby zmiennoprzecinkowe
def zad7():
    random.seed(7)
    x0 = [random.random() * 10 - 5 for i in range(0, 7)]
    print(x0)


# zad7()

# przegladamy liczby od 2 do pierwaistka i sprawdzic czy dzieli w modulo
def zad8(liczba):
    liczba = int(liczba)
    for i in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % i != 0:
            return False
    return True


# liczba = input("podaj liczbe: ")
# zad8(liczba)

# zwraca liste wszystkich ktore sa mniejsze od n
# do zrobienia: podzielnosci przez liczby pierwsze ktore byly znalezione. for i in lista_pierwszych
def zad9(liczba):
    lista_pierwszych = []
    if liczba > 1:
        for i in range(2, liczba + 1):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                lista_pierwszych.append(i)
    return lista_pierwszych


# print(zad9(11))

# Optymalizacja do sprawdzania przez liste liczb pierwszych.
def zad10(liczba):
    lista_pierwszych = [2]
    if liczba > 2:
        for i in range(2, liczba + 1):
            for j in lista_pierwszych:
                if i % j == 0:
                    break
            else:
                lista_pierwszych.append(i)
    return lista_pierwszych


# print(zad10(25))


def test(a, b=1, c=2, d=3, e=4):
    print(a, b, c, d, e)

# test(4, d=13)
# test(a=10, d=13)
# test(d=3, a=5)


# Jezeli pojawi sie jedno podstawienie w funkcji np F(a=2,4,5), to to nei zadziała,
# poniewaz python traci informacje o pozycjonowaniu.


# Dodac na koniec i na poczatek element
# Historia dzialan na seq jest widoczna, przy kazdym  uzyciu wartosci sa dodawane. Nie chcemy tego!
def H(el, seq=None):
    if seq is None:
        seq = []
    else:
        seq.append(el)
        seq.insert(0, el)
        print(seq)


# H(3)
# H(-1, [])
# H("abc")
# H("kop")
# print(type(H))

# funkcje ktora wrzuci informacje o czasie wykonania czynnosci.
# uruchamiamy 10  razy funkcje.
# wypisujemy roznice miedzy wynikami. mnozymy razy 1 000 000
import time

#Funkcja liczaca czas operacji.
def czas(seq=None):
    if seq is None:
        seq = []
    else:
        for i in range(1, 11):
            start_time = time.time()
            print("--- %s seconds ---" % (time.time() - start_time))


# czas([])

#PARAMETRY ANONIMOWE
def M(a, *b):
    print(a, b)

#M(1)
#M(3, 4)
#M(3, 4, 5, 6, 7, 8, 10)

#Przechodzi przez anonimowe atrybuty, skleja 1 i 2 parametr z anonimowymi i wyswietla w linijce
def zad2(a, b, *c):
    a = str(a)
    b = str(b)
    for i in c:
        print(a + str(i) + b)


zad2(1, 3, 2, 5, 6)

#Rozpakowanie
K = (1,2)
def zad3(a,*b):
    print(str(a) + str(b))
#Liczba parametrow musi sie zgadzac
zad3(*K)


#Napisac funkcje ktora odpowiada bool, czy pkt x y lezy w celu o srodku 0,0 i promieniu r
import random

#x = random.randint(-5, 5)
#y = random.randint(-5, 5)
#r = random.randint(0, 3)
def aim(x,y,r):
        return x**2 + y**2 < r**2


X = [random.randrange(-5,5) for i in range(0,8)]
Y = [random.randrange(-5,5) for j in range(0,8)]
R = [random.randrange(0,3) for k in range(0,8)]


for krotka in zip(X,Y,R):
    #print(aim(krotka[0], krotka[1], krotka[2]))
    print(aim(*krotka))








