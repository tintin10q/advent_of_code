numbers = []
with open("input1.txt") as f:
    for number in f:
        numbers.append(int(number))

# numbers = [1721,
# 979,
# 366,
# 299,
# 675,
# 1456]
numbers.sort()
for number in numbers:
    needed_n = 2020 - number
    if needed_n in numbers:
        print(needed_n * number)
