nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pair_list = []

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]

for line in lines:
    first_found = False
    last_found = False
    first = 0
    last = 0
    for i in range(len(line)):
        if not first_found and line[i] in nums:
            first = int(line[i])
            first_found = True
        if not last_found and line[len(line) - i - 1] in nums:
            last = int(line[len(line) - i - 1])
            last_found = True
    num = (first * 10) + last
    pair_list.append(num)

print(sum(pair_list))
