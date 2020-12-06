### Day 3: Toboggan Trajectory ###

## Part 1

answer = 0

map_ = []

for _x in open("day3.txt"):
    _x = _x.strip()
    map_.append(_x)

row = 0
col = 0

m = len(map_)

while row+1 < m:
    row += 1
    col += 3

    position = map_[row][col % len(map_[row])]
    if position == "#":
        answer += 1

print(answer)