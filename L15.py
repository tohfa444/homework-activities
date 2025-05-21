def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

my_numbers = [1, 2, 3, 4, 5, 6]

result = sum_even_numbers(my_numbers)
print("Sum of even numbers:", result)