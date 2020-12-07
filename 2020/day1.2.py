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
    needed_n = abs(2020 - number)
    for number2 in numbers:
        needed_n2 = abs(needed_n - number2)
        if needed_n2 in numbers and number + number2 + needed_n2 == 2020:
            print(f"{number}+{number2}+{needed_n2}={number + number2 + needed_n2}")
            print(f"{number}*{number2}*{needed_n2}={number * number2 * needed_n2}")
