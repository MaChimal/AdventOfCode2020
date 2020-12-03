### Day 2: Password Philosophy ###

## Part 2

answer = 0

for data in open("day2.txt"):
    data = data.strip()
    range_, character, password = data.split()
    a, b = map(int, range_.split("-"))
    character = character[0]
    if (password[a-1]+password[b-1]).count(character)==1:
        answer += 1 

print(answer) 