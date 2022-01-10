import re

with open('input') as file:
    lines = file.readlines()

passports = []
passport = {}
for line in lines:
    # If empty line (only \n) add existing passport to list and then reset it
    if line.strip() == '':
        passports.append(passport)
        passport = {}
        continue
    # Parse all elements in line
    for element in line.strip().split(' '):
        field, value = element.split(':')
        passport[field] = value
# If last last passport has fields, put it in list
if passport:
    passports.append(passport)

def part01():
    valid = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            valid += 1
    print(valid)

def part02():
    valid = 0
    # Add missing fields:
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for passport in passports:
        for field in fields:
            if field not in passport:
                # Junk value
                passport[field] = '0'
    for passport in passports:
        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue
        if  passport['hgt'][-2:] != 'cm' and  passport['hgt'][-2:] != 'in':
            continue
        if  passport['hgt'][-2:] == 'cm' and not 150 <= int(passport['hgt'][0:-2]) <= 193:
            continue
        if  passport['hgt'][-2:] == 'in' and not 59 <= int(passport['hgt'][0:-2]) <= 76:
            continue
        if not re.fullmatch(r'\#[0-9a-f]{6}', passport['hcl']):
            continue
        valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] not in valid_ecl:
            continue
        if not re.fullmatch(r'[0-9]{9}', passport['pid']):
            continue
        valid += 1
    print(valid)


part01()
part02()  