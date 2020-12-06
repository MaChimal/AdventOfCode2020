### Day 5: Binary Boarding ###

## Part 1

answer = 0

data = []

ids = []

for x in open("day5.txt"):
    x = x.strip()
    data.append(x)

for s in data:
    rLow = 0
    rMid = 0
    rHigh = 127

    cLow = 0
    cMid = 0
    cHigh = 7

    for letter in s:
        if letter == "F":
            rMid = (rHigh + rLow) // 2
            rHigh = rMid

        elif letter == "B":
            rMid = (rHigh + rLow) // 2
            rLow = rMid

        elif letter == "R":
            cMid = (cHigh + cLow) // 2
            cLow = cMid

        elif letter == "L":
            cMid = (cHigh + cLow) // 2
            cHigh = cMid

    seatId = (rLow + 1) * 8 + cHigh
    
    answer = max(seatId, answer)

print(answer)
