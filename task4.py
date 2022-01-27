# WAP to accept a list of numbers from user and display only odd numbers from the list.

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)

for i in range(5):
    if numbers[i] % 2 == 0:
        print(numbers[i])
