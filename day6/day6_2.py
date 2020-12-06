### Day 6: Custom Customs ###

## Part 2

answer = 0

for x in open("day66.txt").read().split("\n\n"):
    letters = set.intersection(*[set(s) for s in x.split()])
    answer += len(letters)

print(answer)
