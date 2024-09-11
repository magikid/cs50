def average(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)

print(average([1, 1, 1]))
print(average([]))
