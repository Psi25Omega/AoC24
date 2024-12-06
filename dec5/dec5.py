with open('dec5.txt', 'r') as f:
    lines = f.read().split('\n')

rules = []
#lines[:] as copy of list because py doesnt account for changes to list when iterating over it
#it uses index to traverse so as list changes, elements get skipped
for line in lines[:]:
    if "|" in line:
        rule = [int(i) for i in line.split("|")]
        rules.append(rule)
        lines.remove(line)

lines.remove('')
sum_mid = 0

def is_ok(line):
    if "|" not in line and line != "":
        temp = [int(x) for x in line.split(',')]
        for rule in rules:
                if rule[0] in temp and rule[1] in temp:
                    if temp.index(rule[0]) > temp.index(rule[1]):
                        return False
        
        return True
    else:
        return False

def correct():
    for line in lines:
        if is_ok(line):
            sum_mid += int(line.split(',')[int((len(line.split(','))-1)/2)])

def wrong():
    sum_mid = 0
    for line in lines:
        if not is_ok(line):
            temp = [int(x) for x in line.split(',')]
            for i in range(len(temp)):
                for j in range(len(temp)):
                    if [temp[i],temp[j]] in rules:
                        temp[i], temp[j] = temp[j], temp[i]

            sum_mid += temp[int((len(temp)-1)/2)]

    print(sum_mid)
            
wrong()