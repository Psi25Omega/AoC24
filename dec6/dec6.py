import copy

with open('dec6.txt', 'r') as f:
    lines = f.read().split('\n')
    grid = []
    for line in lines:
        if "^" in line:
            start = [lines.index(line), line.index("^")]
        grid.append(list(line))
        
length, width = len(grid), len(grid[0])

directions = [[-1,0], [0,1], [1,0], [0,-1]]

def move(current_pos, dir, grid):
    new_pos = [current_pos[0] + directions[dir][0], current_pos[1] + directions[dir][1]]
    if 0 <= new_pos[0] < length and 0 <= new_pos[1] < width:
        if grid[new_pos[0]][new_pos[1]] == "#" or grid[new_pos[0]][new_pos[1]] == "O":
            dir = (dir + 1)%4
            return current_pos, dir
        else:
            return new_pos, dir
    else:
        return new_pos, dir

dir = 0
visited = set()

def visits():
    current_pos = start.copy()
    dir = 0
    while 0 <= current_pos[0] < length and 0 <= current_pos[1] < width:
        visited.add(tuple(current_pos))
        current_pos, dir = move(current_pos, dir, grid)

    print(len(visited))

def is_loop(new_grid):
    visited_dir = set()
    current_pos = start.copy()
    dir = 0
    while 0 <= current_pos[0] < length and 0 <= current_pos[1] < width:
        current_pos, dir = move(current_pos, dir, new_grid)
        if (current_pos[0],current_pos[1],dir) in visited_dir:
            return True
        else:
            visited_dir.add((current_pos[0],current_pos[1],dir))

    return False

visits()
    
obs = 0
for position in visited:
    if list[position] != start:
        new_grid = copy.deepcopy(grid)
        i, j = position[0], position[1]
        new_grid[i][j] = 'O'
        if is_loop(new_grid):
            obs += 1

print(obs)