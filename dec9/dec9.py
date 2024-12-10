with open('dec9.txt', 'r') as f:
    line = f.read().strip()

file = []
length_dots = []
length_nums = []

counter = 0
for i in range(int(len(line)/2)):
    file += int(line[2*i])*[counter]
    length_nums.append(int(line[2*i + 1]))

    file += int(line[2*i + 1])*'.'
    length_dots.append(int(line[2*i + 1]))

    counter += 1
if len(line)%2 == 1:
    file += (int(line[len(line)-1])*[counter])
    length_nums.append(int(line[len(line)-1]))

def rule1():
    temp = file.copy()
    i = 0
    while temp.index('.') + i != len(temp):
        if temp[::-1][i] != '.':
            x = temp.index('.')
            y = len(temp) - i - 1
            temp[x], temp[y] = temp[y], temp[x] 
        i += 1

    num = 0
    for i in range(len(temp)):
        if temp[i] != '.':
            num += i*(int(temp[i]))

    print(num)

rule1()