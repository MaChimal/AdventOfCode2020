### Day 8: Handheld Halting ###

## Part 2

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

        ins, val = instructions[i]

        if ins == 'acc':
            accumulator += val

        elif ins == 'jmp':
            i += val-1

        i+=1

    return accumulator, repeat

change = { 'nop':'jmp', 'jmp':'nop' }

enumInstructions = enumerate(instructions)

for i, (ins, val) in enumInstructions:
    if ins in ['nop', 'jmp']:
        accum, rep = acc(instructions[:i] + [(change[ins], val)] + instructions[i + 1:])

        if not rep: 
            print(accum)