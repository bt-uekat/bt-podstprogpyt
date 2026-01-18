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
        return f"dom: ul. {self.address}, powierzchnia: {self.area}m^2, pokoje: {self.rooms}, cena: {self.price}, działka: {self.plot}m^2"
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f"mieszkanie: ul. {self.address}, powierzchnia: {self.area}m^2, pokoje: {self.rooms}, cena: {self.price}, piętro: {self.floor}"
dom_1 = House(100, 5, 1000000,  "Uliczna 1", 200)
mieszkanie_1 = Flat(60, 3, 500000, "Uliczna 2", 2)

print(dom_1)
print(mieszkanie_1)