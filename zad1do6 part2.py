def funkcja_1(name: str, surname: str):
    return print("Cześć", name, surname)

imie = "Kamil"
nazwisko = "ZPlocka"
funkcja_1(imie, nazwisko)

def funkcja_2(liczba1: int, liczba2: int):
    return print(liczba1*liczba2)

liczba1 = 4
liczba2 = 3
funkcja_2(liczba1, liczba2)

def funkcja_3(liczba: int):
    if liczba % 2 == 0:
        return True
    else:
        return False


if funkcja_3(3):
    print("Parzysta")
else:
    print("Nieparzysta")

def funkcja_4(argument1: int, argument2: int, argument3: int):
    if argument1 + argument2 >= argument3:
        return True

print(funkcja_4(1,3,4))

def funkcja_5(lista: list, liczba: int):
    for licz in lista:
        if licz == liczba:
            return True

funkcja_5([1,2,3], 2)

def funkcja_6(lista1: list, lista2: list):
    final_list = lista1 + lista2
    final_list = list(dict.fromkeys(final_list))
    return [x**3 for x in final_list]

print(funkcja_6([1,2,3,4],[2,3,6,10]))