FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

# Driver Program


# print(fibonacci(9))

numbers = []
odd_numbers = []

for n in range(1, 601):
    numbers.append(fibonacci(n))

# print(numbers)

for n in range(0, (len(numbers))):
    if (numbers[n] % 2) != 0:
        odd_numbers.append(numbers[n])

# print(odd_numbers)
print(len(odd_numbers))
