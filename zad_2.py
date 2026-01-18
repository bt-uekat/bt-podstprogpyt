from zad_1 import Student

student_bartek = Student("Bartek Bartkowski", [81, 90, 69])
student_beata = Student("Beata Beatowska", [60, 90, 40])
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
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
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
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
       return f"Książka autorstwa {self.author_name} {self.author_surname} Zbiory w {self.library}"
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        book_list = ", ".join([f"{b.author_name} {b.author_surname}" for b in self.books])
        return f"Zamówienie z dnia {self.order_date}:\n" f"-> Obsługa: {self.employee}\n" f"-> Klient: {self.student.name}\n" f"-> Książki: {book_list}"


library_warszawa = Library("Warszawa", "Uliczna 1", "00-001", "8-20", "123-456-789")
library_krakow = Library("Kraków", "Uliczna 2", "00-002", "8-20", "987-654-321")
employee_adam = Employee("Adam", "Kowalski", "01.01.2020", "01.01.2000", "Warszawa", "Uliczna 1", "00-001", "123-123-123")
employee_anna = Employee("Anna", "Nowak", "02.02.2020", "02.02.2000","Kraków", "Uliczna 2", "00-002", "456-456-456")
employee_antoni = Employee("Antoni", "Azbest", "03.03.2020", "03.03.2000", "Warszawa", "Uliczna 3", "00-001", "789-789-789")
student_blazej = Student("Błażej Błażejski", [])
book1 = Book(library_warszawa, "04.04.2000", "Autor", "Autorski", "123")
book2 = Book(library_warszawa, "05.05.2000", "Autorka", "Autorska", "321")
book3 = Book(library_warszawa, "06.06.2000", "Autor", "Autorowicz", "456")
book4 = Book(library_warszawa, "07.07.2000", "Autorka", "Autorowiczówna", "654")
book5 = Book(library_warszawa, "08.08.2000", "Autor", "Autorewicz", "789")
order1 = Order(employee_antoni, student_bartek, [book1, book3], "01.01.2026")
order2 = Order(employee_anna, student_beata, [book2, book4], "02.01.2026")

print(order1)
print(order2)
