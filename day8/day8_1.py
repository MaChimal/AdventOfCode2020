### Day 8: Handheld Halting ###

## Part 1

instructions = []

for x in open('day8.txt'):
    ins, val  = x.split()
    val = int(val)
    instructions.append((ins, val))

def acc(instructions):
    repeat = False

    i = 0

    accumulator = i

    ran = set()
    while i < len(instructions):
        if i in ran:
            repeat = True
            break

        ran.add(i)

        op, val = instructions[i]

        if op == 'acc':accumulator += val

        elif op == 'jmp':i += val-1

        i+=1

    return accumulator, repeat

print(acc(instructions)[0])
