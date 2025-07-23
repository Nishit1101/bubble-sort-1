size = int(input("Enter how many numbers: "))
numbers = [0] * size 

for i in range(size):
    numbers[i] = int(input(f"Enter number {i + 1}: "))

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
