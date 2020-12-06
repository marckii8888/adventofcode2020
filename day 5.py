# 0101100 ->  FBFBBFF F = 0 B = 1
# 101 -> RLR R = 1 L = 0
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def convert(s):
    row_string = s[:7]
    col_string = s[7:10]
    row =""
    col = ""
    for char in row_string:
        if(char == 'F'):
            row += '0'
        elif(char =='B'):
            row += '1'

    for char in col_string:
        if(char == 'R'):
            col += '1'
        elif(char == 'L'):
            col += '0'

    r = binaryToDecimal(int(row))
    c = binaryToDecimal(int(col))
    return [r,c]


def convertToId(s):
    arr = convert(s)
    row, col = arr[0], arr[1]
    return (row*8 + col)

def convertToId2(arr):
    row, col = arr[0], arr[1]
    return (row*8 + col)

def solution1(arr):
    res = []
    for item in arr:
       res.append(convertToId(item))
    return max(res)

def solution2(arr):
    MAXROW = 128
    MAXCOL = 8
    matrix = []
    for row in range(1,MAXROW-1):

        for col in range(MAXCOL):
            matrix.append([row,col])

    for item in arr:
        x = convert(item)
        matrix.remove(x)
    arr = []
    for i in matrix:
        seatid = convertToId2(i)
        arr.append(seatid)
    
    index = 1 
    while(index < len(arr)):
        if(arr[index] == arr[index-1]+1):
            index+=1
        elif(arr[index]+1 == arr[index+1]):
            index+=1
        else:
            return arr[index]


f = open('q5.txt', 'r')
arr = f.readlines()
print(solution2(arr))
