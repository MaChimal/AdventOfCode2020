### Day 4: Passport Processing ###

## Part 2

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
        dic = dict(data.split(':') for data in _y.split(' '))
        
        if 1920 <= int(dic['byr']) <= 2002 and 2010 <= int(dic['iyr']) <= 2020 and 2020 <= int(dic['eyr']) <= 2030 and dic['hcl'].startswith('#') and len(dic['hcl']) == 7 and dic['ecl'] in 'amb blu brn gry grn hzl oth' and len(dic['pid']) == 9:

            if dic['hgt'].endswith('in'):
                if 59 <= int(dic['hgt'][:-2]) <= 76:
                    answer += 1

            elif dic['hgt'].endswith('cm'):
                if 150 <= int(dic['hgt'][:-2]) <= 193:
                    answer += 1

            else:
                continue
                
print(answer)