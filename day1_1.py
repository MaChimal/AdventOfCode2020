### Day 1: Report Repair ###

## Part 1

years = []

for x in open("day1.txt"):
    y = int(x)
    years.append(y)

answer = 0

for year1 in years:
    for year2 in years:
        if year1 + year2 == 2020:
            answer = year1 * year2

print(answer)