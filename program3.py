limit = int(input("Enter the limit: "))

square_dict = {}

for number in range(1, limit + 1):
    square_dict[number] = number ** 2

print(square_dict)
