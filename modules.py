class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        if len(self.marks) == 0:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student {self.name}, marks: {self.marks}"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w {self.city}, ul. {self.street}'


class Employee:
    def __init__(
            self, first_name, last_name, hire_date,
            birth_date, city, street, zip_code, phone
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"


class Book:
    def __init__(
            self, library, publication_date, author_name,
            author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka autorstwa {self.author_name} "
            f"{self.author_surname} Zbiory w {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = (
            ", ".join([f"{b.author_name} "
                       f"{b.author_surname}" for b in self.books]
                      ))
        return (f"Zamówienie z dnia {self.order_date}:\n"
                f"-> Obsługa: {self.employee}\n"
                f"-> Klient: {self.student.name}\n"
                f"-> Książki: {book_list}"
                )


class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość na ul. {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"dom: ul. {self.address}, "
            f"powierzchnia: {self.area}m^2,"
            f" pokoje: {self.rooms}, "
            f"cena: {self.price},"
            f" działka: {self.plot}m^2"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"mieszkanie: ul. {self.address},"
                f" powierzchnia: {self.area}m^2,"
                f" pokoje: {self.rooms}, "
                f"cena: {self.price},"
                f" piętro: {self.floor}"
                )
