with open('dec8.txt', 'r') as f:
    lines = f.read().split('\n')
    length = len(lines)
    breadth = len(lines[0])

antennas = {}

for line in lines:
    for i in range(len(line)):
        ch = line[i]
        if ch != '.':
            if ch not in antennas.keys():
                antennas[ch] = [[lines.index(line),i]]
            else:
                antennas[ch].append([lines.index(line),i])

#x = y+z/2, y = 2x-z
antinodes1 = set()
antenna_pos = set()

for antenna in antennas.keys():
    for pos1 in antennas[antenna]:
        antenna_pos.add((pos1[0],pos1[1]))
        for pos2 in antennas[antenna]:
            if pos1 != pos2:
                antenna_pos.add((pos2[0],pos2[1]))
                if pos1 != pos2:
                    a1 = [2*pos1[0] - pos2[0], 2*pos1[1] - pos2[1]]
                    a2 = [2*pos2[0] - pos1[0], 2*pos2[1] - pos1[1]]
                    if 0 <= a1[0] < length and 0 <= a1[1] < breadth:
                        antinodes1.add(tuple(a1))
                    if 0 <= a2[0] < length and 0 <= a2[1] < breadth:
                        antinodes1.add(tuple(a2))

print(len(antinodes1))

antinodes2 = set()

grid = [list(line) for line in lines]

for antenna in antennas.keys():
    for pos1 in antennas[antenna]:
        for pos2 in antennas[antenna]:
            if pos1 != pos2:
                a0 = 2*pos1[0] - pos2[0]
                a1 = 2*pos1[1] - pos2[1]
                i = 1
                while 0 <= a0 < length and 0 <= a1 < breadth:
                    antinodes2.add((a0,a1))
                    if grid[a0][a1] == ".":
                        grid[a0][a1] = '#'
                    a0 = (i+1)*pos1[0] - i*pos2[0]
                    a1 = (i+1)*pos1[1] - i*pos2[1]
                    i += 1

final = antenna_pos.union(antinodes2)
print(len(final))                    
