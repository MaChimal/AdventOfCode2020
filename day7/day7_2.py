### Day 7: Handy Haversacks ###

## Part 2

data = []

for _x in open("day7.txt"):
    _x = _x.strip()
    data.append(_x)

def s_bag(color):
    bag = ''
    
    for rule in data:
        if rule[:rule.index(' bags')] == color:
            bag = rule
    
    if "no" in bag:
        return 1

    bag = bag[bag.index("contain")+8: ]
    bag = bag.split()

    result = 0

    x0 = 0

    while x0 < len(bag):
        num = int(bag[x0])
        color = bag[x0 + 1] + " " + bag[x0 + 2]

        result += num * s_bag(color)

        x0 += 4

    return result + 1

answer = s_bag('shiny gold')

print(answer - 1)

