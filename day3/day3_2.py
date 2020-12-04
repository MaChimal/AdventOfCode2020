### Day 3: Toboggan Trajectory ###

## Part 2

answer = 1

map = []

for _x in open("day3.txt"):
    _x = _x.strip()
    map.append(_x)

row = 0
col = 0

m = len(map)

for x in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    row = 0
    col = 0
    trees = 0

    while row+1 < m:
        row += x[1]
        col += x[0]

        position = map[row][col % len(map[row])]
        if position == "#":
            trees += 1
    
    answer *= trees

print(answer)