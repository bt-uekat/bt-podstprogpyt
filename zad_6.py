def process_lists(x: list, y: list) -> list:
    unique_numbers = set(x + y)
    cubed_numbers = []
    for number in unique_numbers:
        cubed_numbers.append(number ** 3)
    return cubed_numbers


print(process_lists([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
