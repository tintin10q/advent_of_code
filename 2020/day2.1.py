import re

pat = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
result = 0

with open("input2.txt") as f:
    for line in f:
        password = pat.split(line)
        low = int(password[1])
        high = int(password[2])
        occurrences = password[4].count(password[3])
        if low <= occurrences <= high:
            result += 1

print(f"Result is: {result}")
