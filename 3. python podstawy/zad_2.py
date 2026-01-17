def multiply_numbers_I(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result
print(multiply_numbers_I([1, 2, 3, 4, 5]))

def multiply_numbers_II(numbers):
    return [number * 2 for number in numbers]
print(multiply_numbers_II([1, 2, 3, 4, 5]))