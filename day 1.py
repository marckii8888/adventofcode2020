def solution(nums):
    target = 2020
    hashmap = {}
    for num in nums:
        if(num not in hashmap):
            hashmap.update({target-num:num})
        else:
            return num * hashmap.get(num)
    return []

def solution2(nums):
    target = 2020
    nums.sort()
    for i,a in enumerate(nums):
        if(i>0 and (a == nums[i-1])):
            continue
        left = i+1
        right = len(nums)-1
        while(left < right):
            s = a + nums[left] + nums[right]
            print(f's ={s}')
            if(s == target):
                print('found')
                return a*nums[left]*nums[right]
            elif(s<2020):
                left+=1
            elif(s>2020):
                right-=1
    return -1

f = open('q1.txt', 'r')
arr = []
for line in f.readlines():
    line = line.split('\n')
    arr.append(int(line[0]))
#print(solution(arr))
print(arr)
print(solution2(arr))

