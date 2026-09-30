def count_above_50(numbers):
    count=0
    for number in numbers:
        if number > 50:
            count += 1
    return count
numbers = [10, 55, 60, 45, 70, 30]
result = count_above_50(numbers)
print("Count of numbers above 50:", result)