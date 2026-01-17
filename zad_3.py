def even(number: int) -> bool:
    return number % 2 == 0
result = even(5)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")