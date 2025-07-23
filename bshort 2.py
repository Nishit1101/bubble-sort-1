numbers = []
size = int(input("Enter how many numbers: "))

for i in range(size):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
