import numpy as np

with open('dec4.txt', 'r') as f:
    lines = f.read().split('\n')
    matrix = []
    for line in lines:
        matrix.append(list(line))

def in_one_line(line):   
    c = line.count('XMAS') + line.count('SAMX')
    return c

def xmas():
    total = 0

    for line in lines:
        total += in_one_line(line)

    t_matrix = np.transpose(matrix)
    for row in t_matrix:
        new_line = ""
        for item in row:
            new_line += item
        
        total += in_one_line(new_line)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i+3 < len(matrix) and j+3 < len(matrix[i]):
                temp = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
                if temp == 'XMAS' or temp == 'SAMX':
                    total += 1
            if i+3 < len(matrix) and j-3 >= 0:
                temp = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
                if temp == 'XMAS' or temp == 'SAMX':
                    total += 1

    print(total)

def x_mas():
    xmas = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if j-1 >= 0 and i-1 >= 0 and matrix[i][j] == 'A':
                sam = ['SAM', 'MAS']
                diag_1 = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
                diag_2 = matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1]
                if diag_1 in sam and diag_2 in sam:
                    xmas += 1

    print(xmas)

x_mas()
