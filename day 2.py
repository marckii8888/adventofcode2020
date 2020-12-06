def checktimes(password, start, end, letter):
    count = password.count(letter)
    if(count>= start and count <= end):
        return True
    else:
        return False

def checktimes2(password, start,end ,letter):
    if(password[start-1] == letter and password[end-1] != letter):
        return True
    elif(password[start-1] != letter and password[end-1] == letter):
        return True
    else:
        return False
def solution(passwords):
    output = 0
    for line in passwords:
        r,c,p = line.split()
        c = c.replace(':', '')
        start,end = r.split('-')
        if(checktimes2(p, int(start), int(end), c)):
            output+=1
        else:
            continue
    return output

f = open('q2.txt', 'r')
example = f.readlines()
print(solution(example))
f.close()
