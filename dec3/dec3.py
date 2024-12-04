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
    #sum can be added directly during dictionary entry assignment instead of iterating
    #separated_dict = {}
    l1 = lines.split('do()')
    fsum = 0
    for l2 in l1:
        if "don't()" in l2:
            temp = l2.split("don't()")
            fsum += add_sum(temp[0])
            
        else:
            fsum += add_sum(l2)
    '''
        for item in separated_dict:
        if separated_dict[item]:
            fsum += add_sum(item)
    '''

    print(fsum)

check_do()