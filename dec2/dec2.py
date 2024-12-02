with open('dec2.txt', 'r') as f:
    lines = f.read().split('\n')

def is_safe(l):
    if sorted(l) != l and sorted(l, reverse=True) != l:
        return False

    for i in range(len(l)-1):
        diff = abs(l[i+1] - l[i]) 
        if diff < 1 or diff > 3:
            return False

    return True

def numsafe():
    safe = 0
    for line in lines:
        l = [int(x) for x in line.strip().split()]
        if is_safe(l):
            safe += 1

    print(safe)

def numtolerate():
    tsafe = 0

    for line in lines:
        l = [int(x) for x in line.strip().split()]
        if is_safe(l):
            tsafe += 1
        else:
            for i in range(len(l)):
                new_l = l[0:i] + l[i+1:len(l)]
                if is_safe(new_l):
                    tsafe += 1
                    break
    
    print(tsafe)

numsafe()
numtolerate()