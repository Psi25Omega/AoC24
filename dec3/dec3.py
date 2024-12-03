import re

with open('dec3.txt', 'r') as f:
    lines = f.read().strip()

def add_sum(text):
    #\w+ - string of variable length without whitespace
    pattern = r"mul\((\w+),(\w+)\)"
    all_mul = re.findall(pattern, text)

    total = 0
    for i,j in all_mul:
        total += int(i)*int(j)
    
    return total

def check_do():
    separated_dict = {}
    l1 = lines.split('do()')
    for l2 in l1:
        if "don't()" in l2:
            temp = l2.split("don't()")
            separated_dict[temp[0]] = True
            separated_dict[temp[1]] = False
        else:
            separated_dict[l2] = True
    
    fsum = 0
    for item in separated_dict:
        if separated_dict[item]:
            fsum += add_sum(item)

    print(fsum)

check_do()