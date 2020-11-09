start = 0
input_lista =[]
freq_list = [0]


def bin_search(input_list,value):
    input_list.sort()
    start = round((len(input_list)-1)/2)
    countup = start
    trys = 0
    while True:
        if input_list[start] == value:
            return True
        elif input_list[start] > value:
            start = round(start - countup)

        elif input_list[start] < value:
            start = round(start +countup)
        countup = round(countup/2)
        trys += 1
        if trys > 40:
            return False



# take input out of file
with open("day1.txt","r") as f:
    for i in f:
        input_lista.append(int(i))
i = 0
while True:
    if bin_search(freq_list, start):
        print("target is in list")
    else:
        freq_list.append(start)
        start += input_lista[i]
    i += 1
    if i > len(input_lista):
        i = 1


print("First double: {} in {} cycles".format(start,cycle))
freq_list.sort()
print(freq_list)