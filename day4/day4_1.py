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

for line in passports_:
    if "byr" in line and "iyr" in line and "eyr" in line and "hgt" in line and "hcl" in line and "ecl" in line and "pid" in line:
        answer += 1
                
print(answer)
