### Day 6: Custom Customs ###

## Part 1

answer = 0

for x in open("day6.txt").read().split("\n\n"):
    letters = set(x)-{"\n"}
    answer += len(letters)

print(answer)
