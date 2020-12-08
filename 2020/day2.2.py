import re

pat = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
result = 0
line_count = 0
with open("input2.txt") as f:
    for line in f:
        line_count += 1
        line = pat.split(line)
        index1 = int(line[1]) - 1
        index2 = int(line[2]) - 1
        target = line[3]
        password = line[4]
        c1 = password[index1]
        c2 = password[index2]
        if c1 == target or c2 == target:
            if c1 == c2:
                result += 1
        else:
            result += 1

print(f"Result is: {line_count - result}")
