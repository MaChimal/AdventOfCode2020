### Day 10: Adapter Array ###

## Part 1

data = []

for x in open("day10.txt"):
    x = x.strip()
    data.append(int(x))

data.sort()

i = 0
j = 0
k = 0

for num in data:
    difference = num - k

    if difference == 1:
        i += 1
    
    elif difference == 3:
        j += 1
    
    k = num

j += 1

answer = i * j

print(answer)