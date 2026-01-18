from modules import Student, Library, Employee, Book, Order

student_bartek = Student("Bartek Bartkowski", [81, 90, 69])
student_beata = Student("Beata Beatowska", [60, 90, 40])



library_warszawa = Library(
    "Warszawa", "Uliczna 1",
    "00-001", "8-20",
    "123-456-789"
)
library_krakow = Library(
    "Kraków", "Uliczna 2",
    "00-002", "8-20",
    "987-654-321"
)
employee_adam = Employee(
    "Adam", "Kowalski", "01.01.2020",
    "01.01.2000", "Warszawa", "Uliczna 1",
    "00-001", "123-123-123"
)
employee_anna = Employee(
    "Anna", "Nowak", "02.02.2020",
    "02.02.2000", "Kraków", "Uliczna 2",
    "00-002", "456-456-456"
)
employee_antoni = Employee(
    "Antoni", "Azbest", "03.03.2020",
    "03.03.2000", "Warszawa", "Uliczna 3",
    "00-001", "789-789-789"
)
student_blazej = Student("Błażej Błażejski", [])
book1 = Book(
    library_warszawa, "04.04.2000", "Autor",
    "Autorski", "123"
)
book2 = Book(
    library_warszawa, "05.05.2000", "Autorka",
    "Autorska", "321"
)
book3 = Book(
    library_warszawa, "06.06.2000", "Autor",
    "Autorowicz", "456"
)
book4 = Book(
    library_warszawa, "07.07.2000", "Autorka",
    "Autorowiczówna", "654"
)
book5 = Book(
    library_warszawa, "08.08.2000", "Autor",
    "Autorewicz", "789"
)
order1 = Order(
    employee_antoni, student_bartek,
    [book1, book3], "01.01.2026"
)
order2 = Order(
    employee_anna, student_beata,
    [book2, book4], "02.01.2026"
)

print(order1)
print(order2)
