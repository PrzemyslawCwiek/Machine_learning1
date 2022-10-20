class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_1 = (sum(self.marks) / len(self.marks))
        if (marks_1 > 2.5):
            return True
        else:
            return False


st1 = Student("John", (3, 1, 3, 2, 1, 2, 3))
st2 = Student("Peter", (5, 5, 5, 4, 5, 4, 5))

print(st1.is_passed())
print(st2.is_passed())

# zad 2

class Library:

    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return 'Książka z ' + self.publication_date + ' autora ' + self.author_name + ' ' + self.author_surname + ' Mająca ' + self.number_of_pages + ' stron'

class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return 'Zamówienie obsługiwane przez ' + self.employee + ' Zamówione przez ' + self.student + ' Zawierające ' + str(str([ksiazka]) for ksiazka in self.books) + ' o dacie ' + self.order_date

l1 = Library('Katowcie', 'Ulicowa', '42-144', '2-12', 654465867)
l2 = Library('Płock', 'Kamila Mamońskiego', '60-997', '8-20', 876548384)

e1 = Employee('Mateusz', 'Grzegoszewski', '12.03.2000', '12.03.2020', 'Bytom', 'Bytomska', '24-333', 123456789)
e2 = Employee('Andrzej', 'Andrzejowski', '12.03.2000', '12.03.2020', 'Bytom', 'Bytomska', '23-231', 123456789)
e3 = Employee('Johannes', 'Paul', '12.03.2000', '12.03.2020', 'der Bytom', 'Czeska', '25-120',
                      123456780)

b1 = Book(l1, '07.07.2000', 'Henryk', 'Pisarski', '777')
b2 = Book(l1, '07.07.2000', 'Henryk', 'Pisarski', '665')
b3 = Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '656')
b4 = Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '566')
b5 = Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '997')

o1 = Order(e1 , 'Andrzej Hubert', [b1, b2], '07.07.2107')
o2 = Order(e2 , 'Julia Juliowska', [b2, b3], '07.07.2106')

# print(o1, o2)

# zad 3


class Property:
    def __init__(self, area, rooms:int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self,area, rooms:int, price, address, plot, rozmair_dzialki:int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        self.rozmiar_dzialki = rozmair_dzialki

    def __str__(self):
        return f'House with area of {self.area} and {self.rooms} rooms, costs {self.price}, in {self.address}, plot {self.plot}, area {self.rozmiar_dzialki}'


class Flat(Property):
    def __init__(self,area, rooms: int, price, address,floor):
        super().__init__(area,rooms,price,address)
        self.floor = floor

    def __str__(self):
        return f'Flat with area of {self.area} and {self.rooms} rooms, costs {self.price}, in {self.address}, on {self.floor} floor'

house = House(4321, 4, 50000, 'Katowice', 'Uliczna', 10)
flat = Flat(44, 3, 10000, 'Hubertów', 6)

print(house)
print(flat)