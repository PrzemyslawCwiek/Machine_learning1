# a)
def przyklad_a(lista_imion):
    for imie in lista_imion:
        print(imie)

lista_imion = ["Hubercik", "Przemek", "Julia", "Magda", "Jakub"]
przyklad_a(lista_imion)

# b)
def przyklad_b(liczby):
    liczby2 = []
    for liczba in liczby:
        liczba = liczba * 2
        liczby2.append(liczba)

    return liczby2

lista_liczb = (3, 4, 5, 6, 1)
print(przyklad_b(lista_liczb))

def przyklad_b2(liczby):
    liczby2 = [liczba*2 for liczba in liczby]
    return liczby2

lista_liczb = (3, 4, 5, 6, 1)
print(przyklad_b2(lista_liczb))

# c)

def przyklad_c(liczby):
    liczby2 = []
    for liczba in liczby:
        if (liczba % 2 == 0):
            liczby2.append(liczba)
    return liczby2

lista_liczbc = [*range(1,10)]
print(lista_liczbc)
print(przyklad_c(lista_liczbc))

def przyklad_d(liczby):
    liczby2 = []
    i = 0
    for liczba in liczby:
        i = i + 1
        if (i % 2 == 0):
            liczby2.append(liczba)
    return liczby2

print(lista_liczbc)
print(przyklad_d(lista_liczbc))