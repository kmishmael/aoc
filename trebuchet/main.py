INPUT_FILE = 'input.txt'

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nums_words =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pair_list = []

file = open(INPUT_FILE, 'r')

lines = [line.strip() for line in file.readlines()]

def search_and_replace(line):
    front = 0
    back = len(line) - 1
    first_found = False
    last_found = False
    for i in range(len(line)):
        front_section = line[front:i+1]
        back_section = line[back - i:len(line)]
        for word in nums_words:
            if not first_found and word in front_section:
                index = nums_words.index(word)
                line = line.replace(word, nums[index + 1])
                first_found = True
            if not last_found and word in back_section:
                index = nums_words.index(word)
                line = line.replace(word, nums[index + 1])
                last_found = True
            if first_found and last_found:
                break
    return line


    # for index, word in enumerate(nums_words):
    #     if word in line:
    #         line = line.replace(word, nums[index + 1])
    # return line

for line in lines:
    first_found = False
    last_found = False
    first = 0
    last = 0
    line = search_and_replace(line)
    print(line)
    for i in range(len(line)):
        if not first_found and line[i] in nums:
            first = int(line[i])
            first_found = True
        if not last_found and line[len(line) - i - 1] in nums:
            last = int(line[len(line) - i - 1])
            last_found = True
    num = (first * 10) + last
    pair_list.append(num)

print(pair_list)
print(sum(pair_list))
