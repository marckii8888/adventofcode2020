def solution(arr, right, down):
    row, col, target = 0,0,0
    climit = len(arr[0])
    print(f'clmit = {climit}')
    print(f'row limit = {len(arr)}')
    while(row+down < len(arr)):
        if(col+right >= climit):
            col = (col+right)%climit
        else:
            col += right
        row+=down
        print(f'Am at row {row} and col {col}')
        if(arr[row][col] == '#'):
            target+=1
    return target

def solution2(arr):
    result = solution(arr, 1, 1)
    result *= solution(arr,3,1)
    result *= solution(arr,5,1)
    result *= solution(arr,7,1)
    result *= solution(arr,1,2)
    return result

f = open('q3.txt', 'r')
arr = []
for line in f.readlines():
    line = line.split('\n')
    arr.append(list(line[0]))

#print(solution(arr, 3, 1))
print(solution2(arr))
