def solution(arr):
    res = 0
    for group in arr:
        choices = []
        for person in group:
            for choice in person:
                if(choice in choices):
                    continue
                else:
                    choices.append(choice)
                    res+=1
    return res

def solution2(arr):
    hashmap = {}
    res = 0
    a = []
    for group in arr:
        hashmap = {}
        numofperson = len(group)
        for person in group:
            for choice in person:
                if(choice in hashmap.keys()):
                    hashmap.update({choice: hashmap[choice]+1})
                else:
                    hashmap.update({choice:1})
        print(hashmap) 
        for k,v in hashmap.items():
            if(v == numofperson):
                res+=1
    return(res)

f = open('q6.txt', 'r')
arr = []
x = []
for line in f.readlines():
    if(line == '\n'):
        arr.append(x)
        x = []
        continue
    else:
        x.append(list(line)[:-1])
x.append(list(line))
arr.append(x)
print(solution2(arr))

