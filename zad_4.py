def print_every_second(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])


numbers = range(10)
print_every_second(numbers)
