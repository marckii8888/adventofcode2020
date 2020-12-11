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
    ptr, res = 0,0
    target= max(arr) + 3
    arr.append(0)
    arr.append(target)
    arr.sort()

    while(ptr < len(arr)):
        
        ptr+=1



f = open('q10.txt', 'r')
arr = []
for line in f.readlines():
    arr.append(int(line.strip()))
print(solution2(arr))
