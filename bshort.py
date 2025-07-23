n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    v= int(input(f"Enter number {i+1}: "))
    arr.append(v)

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Bubble Sort:", arr)
