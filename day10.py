def solution1(arr):
    onediff, threediff = 0,0
    arr.append(0)
    arr.sort()
    for num in arr:
        if(num+1 in arr):
            onediff += 1
        elif(num+3 in arr):
            threediff +=1
    threediff += 1 # For the highest rated adapter

    print(f'There are {onediff} differences of 1 jolt and {threediff} differences of 3')
    return onediff * threediff


def solution2(arr):
    arr.append(max(arr)+3) # Account for 3 more than highest jolt
    arr.sort()
    res = {0:1} # Start with 0
    for num in arr:
        res.update({num:0})
        if((num - 1) in res):
            new_count = res[num] + res[num-1]
            res.update({num: new_count})
        if((num-2) in res):
            new_count = res[num] + res[num-2]
            res.update({num: new_count})
        if((num-3) in res):
            new_count = res[num] + res[num-3]
            res.update({num: new_count})

    return res[max(arr)]
f = open('q10.txt', 'r')
arr = []
for line in f.readlines():
    arr.append(int(line.strip()))
print(solution2(arr))
