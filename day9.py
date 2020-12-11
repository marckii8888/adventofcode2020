def helper(arr,target): 
    d = {}
    for num in arr:
        otherpair = target - num
        if(otherpair in arr and arr.index(otherpair)!= arr.index(num)):
            return True

    return False

def solution1(arr):
    index = 25
    window = arr[0:25]
    while(index < len(arr)):
        target = arr[index]
        if(helper(window,target)):
            window.append(target)
            window.pop(0)
            index+=1
            continue
        else:
            print(solution2(arr, target))
            return target
    return -1

def solution2(arr, target):
    for index in range(len(arr)):
        ptr = index+1
        res = arr[index] + arr[ptr]
        while(res <= target or ptr >= len(arr)):
            if(res == target):
                a = arr[index:ptr+1]
                return max(a) + min(a) 
            else:
                ptr+=1
                res += arr[ptr]


f = open('q9.txt','r')
arr = []
for line in f.readlines():
    line = line.strip()
    arr.append(int(line))

print(solution1(arr))
