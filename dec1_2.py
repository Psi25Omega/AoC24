def sol():
    with open('dec1.txt', 'r') as f:
        lines = f.read().split('\n')
    
    #list comprehension instead of appending
    left, right = [int(line.split()[0]) for line in lines], [int(line.split()[1]) for line in lines]
    score = sum(num*right.count(num) for num in left)
    
    print(score)

sol()