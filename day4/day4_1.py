### Day 4: Passport Processing ###

## Part 1

answer = 0

passports = []

for _x in open("day4.txt"):
    _x = _x.strip()
    passports.append(_x)

passports_ = []

x = 0

for i in range(len(passports)):
    if passports[i] == '':
        data = ' '.join(passports[x:i])
        passports_.append(data)
        x = i+1

for _y in passports_:
    if "byr" in _y and "iyr" in _y and "eyr" in _y and "hgt" in _y and "hcl" in _y and "ecl" in _y and "pid" in _y:
        answer += 1
                
print(answer)
