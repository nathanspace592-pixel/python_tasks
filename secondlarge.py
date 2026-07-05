def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return "No second largest value."
    else:
        return second


# Collect input from the user
n = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Display the list
print("List:", numbers)

# Call the function
result = second_largest(numbers)

# Display the result
print("Second largest value:", result)