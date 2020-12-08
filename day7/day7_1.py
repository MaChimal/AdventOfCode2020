### Day 7: Handy Haversacks ###

## Part 1

data = []

for _x in open("day7.txt"):
    _x = _x.strip()
    data.append(_x)

def bags(color):
    rules = [ rule for rule in data if color in rule and rule.index(color) != 0 ]

    bag_colors = []

    colors = [ rule[:rule.index('bags')] for rule in rules]
    colors = [ color for color in colors if color not in bag_colors]

    for color in colors:
        bag_colors.append(color)
        bags_ = bags(color)

        bag_colors += bags_

    colors_ = []

    for color in bag_colors:
        if color not in colors_:
            colors_.append(color)

    return colors_
    

answer = bags('shiny gold')

print(len(answer))