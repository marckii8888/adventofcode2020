import copy

def print2D(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            print(f'{arr[row][col]}', end=" ")
        print('\n')

def checkadjneighbour(arr, row, col, emptyflag):
    MINROW, MINCOL, MAXROW, MAXCOL = 0,0, len(arr), len(arr[0])
    try:
        if(col-1 < 0):
            left = 'L'
        else:
            left = arr[row][col-1]
    except IndexError:
        left = 'L'

    try:
        right = arr[row][col+1]
    except IndexError:
        right = 'L'

    try:
        if(row-1 < 0):
            up = 'L'
        else:
            up = arr[row-1][col]
    except IndexError:
        up = 'L'
    try:
        down = arr[row+1][col]
    except IndexError:
        down = 'L'

    try:
        if(row-1 < 0):
            ne = 'L'
        else:
            ne = arr[row-1][col+1]
    except IndexError:
        ne = 'L'
    try:
        if(row -1 < 0 or col -1 < 0):
            nw = 'L'
        else:
            nw = arr[row-1][col-1]
    except IndexError:
        nw = 'L'

    try:
        se = arr[row+1][col+1]
    except IndexError:
        se = 'L'

    try:
        if(col-1<0):
            sw = 'L'
        else:
            sw = arr[row+1][col-1]
    except IndexError:
        sw = 'L'

    if(emptyflag):
        if(se != '#' and sw != '#' and ne != '#' and nw != '#' and down != '#' and up != '#' and left != '#' and right != '#'):
            return True
        else:
            return False
    else:
        a = [se, sw, ne, nw, down, up, left , right]
        occupied = a.count('#')
        if(occupied >= 4): #Change to 4 in part 1, 5 in part 2
            return True
        else:
            return False
def checkAdjNeighbour2(arr, row, col, emptyflag):
    MINROW, MINCOL, MAXROW, MAXCOL = 0,0, len(arr), len(arr[0])
    up, down, left, right, ne, nw, se, sw = True, True, True, True, True, True, True, True
    up_ptr = row - 1
    if(up_ptr < MINROW):
        up = True
    else:
        while(up_ptr >= MINROW):
            if(arr[up_ptr][col] != '.'):
                if(arr[up_ptr][col] == '#'):
                    up = False
                    break
                else:
                    break
            up_ptr -= 1

    down_ptr = row+1
    if(down_ptr >= MAXROW):
        down = True
    else:
        while(down_ptr < MAXROW):
            if(arr[down_ptr][col] != '.'):
                if(arr[down_ptr][col] == '#'):
                    down = False
                    break
                else:
                    break
            down_ptr +=1

    left_ptr = col-1
    if(left_ptr < MINCOL):
        left = True
    else:
        while(left_ptr >= MINCOL):
            if(arr[row][left_ptr] != '.'):
                if(arr[row][left_ptr] == '#'):
                    left = False
                    break
                else:
                    break
            left_ptr -= 1

    right_ptr = col + 1
    if(right_ptr >= MAXCOL):
        right = True
    else:
        while(right_ptr < MAXCOL):
            if(arr[row][right_ptr] != '.'):
                if(arr[row][right_ptr] == '#'):
                    right = False
                    break
                else:
                    break
            right_ptr +=1

    nw_row_ptr , nw_col_ptr = row-1, col-1
    if(nw_row_ptr < MINROW or nw_col_ptr < MINCOL):
        nw = True
    else:
        while(nw_row_ptr >= MINROW and nw_col_ptr >= MINCOL):
            if(arr[nw_row_ptr][nw_col_ptr] != '.'):
                if(arr[nw_row_ptr][nw_col_ptr] == '#'):
                    nw = False
                    break
                else:
                    break
            nw_row_ptr -=1
            nw_col_ptr -= 1


    ne_row_ptr , ne_col_ptr = row-1, col+1
    if(ne_row_ptr < MINROW or nw_col_ptr >= MAXCOL):
        ne = True
    else:
        while(ne_row_ptr >= MINROW and ne_col_ptr < MAXCOL):
            if(arr[ne_row_ptr][ne_col_ptr] != '.'):
                if(arr[ne_row_ptr][ne_col_ptr] == '#'):
                    ne = False
                    break
                else:
                    break
            ne_row_ptr -=1
            ne_col_ptr += 1


    se_row_ptr , se_col_ptr = row+1, col+1
    if(se_row_ptr >= MAXROW or se_col_ptr >= MAXCOL):
        se = True
    else:
        while(se_row_ptr < MAXROW and se_col_ptr < MAXCOL):
            if(arr[se_row_ptr][se_col_ptr] != '.'):
                if(arr[se_row_ptr][se_col_ptr] == '#'):
                    se = False
                    break
                else:
                    break
            se_row_ptr +=1
            se_col_ptr += 1


    sw_row_ptr , sw_col_ptr = row+1, col-1
    if(sw_row_ptr >= MAXROW or sw_col_ptr < MINCOL):
        sw = True
    else:
        while(sw_row_ptr < MAXROW and sw_col_ptr >= MINCOL):
            if(arr[sw_row_ptr][sw_col_ptr] != '.'):
                if(arr[sw_row_ptr][sw_col_ptr] == '#'):
                    sw = False
                    break
                else:
                    break
            sw_row_ptr +=1
            sw_col_ptr -= 1

    if(emptyflag):
        if(up == down == left == right == sw == se == ne == nw == True):
            return True
        else:
            return False
    else:
        a = [se, sw, ne, nw, down, up, left , right]
        occupied = a.count(False)
        if(occupied >= 5): #Change to 4 in part 1, 5 in part 2
            return True
        else:
            return False

def helper(arr):
    row, col, MAXROW, MAXCOL = 0,0, len(arr), len(arr[0])
    temp = copy.deepcopy(arr)
    dummy = copy.deepcopy(arr)
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if(temp[row][col] == 'L'):
                if(checkAdjNeighbour2(temp,row,col, True)): # For part 2
#                if(checkadjneighbour(temp, row, col, True)):
                    dummy[row][col] = '#'
                else:
                    continue
            elif(temp[row][col] == '#'):
                if(checkAdjNeighbour2(temp,row,col, False)):
#                if(checkadjneighbour(temp,row,col, False)):
                    dummy[row][col] = 'L'
                else:
                    continue
            else:
                continue
    return dummy

def solution(arr):
    change = True
    while(change):
        temp = copy.deepcopy(arr)
        arr = helper(arr)
        if(arr == temp):
            break
    count = 0
    for row in arr:
        count+= row.count('#')
    return count

f = open('q11.txt', 'r')
arr = []
for line in f.readlines():
    arr.append(list(line.strip()))

print(solution(arr))
