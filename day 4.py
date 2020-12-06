import re
def helper(d):
    for key,val in d.items():
        if(key=='byr'):
            try:
                birthyear = int(val)
                if(birthyear >= 1920 and birthyear <= 2002):
                    continue
                else:
                    return False
            except:
                return False
        if(key=='iyr'):
            try:
                issueyear = int(val)
                if(issueyear >= 2010 and issueyear<= 2020):
                    continue
                else:
                    return False
            except:
                return False
        if(key=='eyr'):
            try:
                expyear = int(val)
                if(expyear>=2020 and expyear<=2030):
                    continue
                else:
                    return False
            except:
                return False
        if(key=='hgt'):
            try:
                unit = val[-2:0]
                print(unit)
                height = int(val[:-2])
                if(unit == 'cm'):
                    if(height>=150 and height<=193):
                        continue
                    else:
                        return False
                elif(unit=='in'):
                    if(height>=59 and height<=76):
                        continue
                    else:
                        return False
                else:
                    return False
            except:
                return False
        if(key=='hcl'):
            try:
                if(val[0] == '#'):
                    pattern = r'[0-9a-f]{6}'
                    if(re.search(pattern, val[1:])):
                        continue
                    else:
                        return False
            except:
                return False
        if(key=='ecl'):
            options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if(val in options):
                continue
            else:
                return False
        if(key=='pid'):
            if(len(val) == 9 and val.isdigit()):
                continue
            else:
                return False
    return True

def newsolution(arr):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    optional =['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields.sort()
    optional.sort()
    res = 0
    for d in arr:
        l1 = list(d.keys())
        l1.sort()
        if(l1 == fields):
            if(helper(d)):
                res+=1
                print(f'valid = {d}')
                continue
            else:
                continue
        elif(l1 == optional):
            if(helper(d)):
                res+=1
                print(f'valid = {d}')
                continue
            else:
                continue
        else:
            continue
    return res


f = open("passwords.txt", "r")
passports = f.readlines()
filtered = []
res = {}
for line in passports:
    if(line == '\n'):
        filtered.append(res)
        res={}
    else:
        l=line.split()
        for field in l:
            key,val = field.split(':')
            res.update({key:val})

for key in filtered:
    print(key)

print(newsolution(filtered))
#print(solution(passports)) # Answer = 2
