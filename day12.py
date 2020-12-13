'''
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.

Start facing east. Find Manhattan distance, add abs value of north and east
'''

def solution(arr):
    start = [0,0]
    directions = ['N', 'E', 'S', 'W']
    face = 'E'
    for instruction in arr:
        action, value = instruction[0], int(instruction[1:])
        if(action == 'F'):
            if(face == 'N'):
                start[0] += value
            elif(face == 'S'):
                start[0] -= value
            elif(face == 'E'):
                start[1] += value
            elif(face == 'W'):
                start[1] -= value
        elif(action == 'N'):
            start[0] += value
        elif(action =='S'):
            start[0] -= value
        elif(action == 'E'):
            start[1] += value
        elif(action =='W'):
            start[1] -= value
        elif(action == 'R'):
            ptr = value/90 % 4
            new_index = (directions.index(face) + int(ptr)) % 4
            face = directions[new_index]
        elif(action == 'L'):
            ptr = value/90 % 4
            new_index = (directions.index(face) - int(ptr)) % 4
            face = directions[new_index]

    return abs(start[0]) + abs(start[1])

'''
Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.

Start 10 units east, 1 unit North. Find Manhattan distance, add abs value of north and east
'''

def solution2(arr):
    waypoint, ship_position = [1, 10], [0,0]
    for instruction in arr:
        direction, val = instruction[0], int(instruction[1:])
        if(direction == 'N'):
            waypoint[0] += val
        elif(direction == 'S'):
            waypoint[0] -= val
        elif(direction == 'E'):
            waypoint[1] += val
        elif(direction == 'W'):
            waypoint[1] -= val
        elif(direction == 'L'):
            numofrotation = (val/90 % 4)
            '''
            Start [4,10]
            1 time -> [4,10] -> [10, -4]
            2 time -> [4,10] -> [10,-44] -> [-4,-10]
            3 time -> [4,10] -> [10,-4] -> [-4,-10] -> [-10,4]
            '''
            if(numofrotation == 3):
                waypoint = [-1*(waypoint[1]), waypoint[0]]
            elif(numofrotation == 2):
                waypoint = [(-1*waypoint[0]) , (-1*waypoint[1])]
            elif(numofrotation == 1):
                waypoint = [waypoint[1], (-1*waypoint[0])]
            elif(numofrotation == 0):
                continue
        elif(direction == 'R'):
            numofrotation = (val/90 % 4)
            '''
            Start [4,10]
            1 time -> [4,10] -> [-10, 4]
            2 time -> [4,10] -> [-10,4] -> [-4,-10]
            3 time -> [4,10] -> [-10,4] -> [-4,-10] -> [10,-4]
            '''
            if(numofrotation == 1):
                waypoint = [-1*(waypoint[1]), waypoint[0]]
            elif(numofrotation == 2):
                waypoint = [(-1*waypoint[0]) , (-1*waypoint[1])]
            elif(numofrotation == 3):
                waypoint = [waypoint[1], (-1*waypoint[0])]
            elif(numofrotation == 0):
                continue
        elif(direction == 'F'):
            ship_displacement = [val*waypoint[0], val*waypoint[1]]
            ship_position = [ship_displacement[0]+ship_position[0] , ship_displacement[1]+ship_position[1]]
    return abs(ship_position[0]) + abs(ship_position[1])

arr = []
f = open('q12.txt', 'r')
for line in f.readlines():
    arr.append(line.strip())

# Part 1
# print(solution(arr))

# Part 2
print(solution2(arr))
