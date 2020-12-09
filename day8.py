# Day 8 solution
def solution1(arr):
    res, index = 0,0
    visited = []
    while(index < len(arr)):
        instruction = arr[index][0]
        if(index in visited):
            break
        elif(instruction == 'nop'):
            visited.append(index)
            index+=1
        elif(instruction == 'jmp'):
            visited.append(index)
            index += int(arr[index][1])
        elif(instruction == 'acc'):
            visited.append(index)
            res+=int(arr[index][1])
            index+=1
    return res

def helper(arr):
    res, index = 0,0
    visited = []

    while(index < len(arr)):
        instruction = arr[index][0]
        if(index in visited):
            return False
        elif(instruction == 'nop'):
            visited.append(index)
            index+=1
        elif(instruction == 'jmp'):
            visited.append(index)
            index += int(arr[index][1])
        elif(instruction == 'acc'):
            visited.append(index)
            res+=int(arr[index][1])
            index+=1
    if(index == len(arr)):
        return True
    else:
        return False

def solution2(arr):
    for instruction in arr:
        inst = instruction[0]
        if(inst == 'nop'):
            instruction[0] = 'jmp'
            if(helper(arr)):
                return solution1(arr)
            else:
                instruction[0] = 'nop'
                continue
        elif(inst == 'jmp'):
            instruction[0] = 'nop'
            if(helper(arr)):
                return solution1(arr)
            else:
                instruction[0] = 'jmp'
        else:
            continue
    return 0
f = open('q8.txt', 'r')

d=[]
for line in f.readlines():
    instruction , val = line.split(' ')
    d.append([instruction.strip(),val.strip()])
print(solution2(d))
