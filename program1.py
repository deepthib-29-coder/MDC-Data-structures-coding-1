result = []

for number in range(2000, 3201):
    if number % 7 == 0:
        if number % 3 != 0:
            result.append(str(number))

print(",".join(result))
