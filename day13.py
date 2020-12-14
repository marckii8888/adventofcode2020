def solution1(arr):
    arr[1] = arr[1].replace('x,', '').split(',')
    arr[1] = [int(i) for i in arr[1]]
    # Return earliest bus ID * minutes to next bus
    result = {}
    target, bus_list = int(arr[0]), arr[1]
    for bus in bus_list:
        time_before_target = target - target%bus
        time_to_next_bus = (time_before_target + bus) - target
        result.update({time_to_next_bus : bus})
    shortest_time = min(result.keys())
    return shortest_time * result[shortest_time]

def solution2(arr):
    arr[1] = arr[1].split(',')
    array = ["x" if x=="x" else int(x) for x in arr[1]]
    '''
    let t = time stamp
    t % 7 == 0
    t+1 % 13 == 0
    t+4 % 59 == 0
    t+6 % 31 == 0
    t+7 % 31 == 0

    t % 7 = t + 1 % 13

    a mod n  ==  a - [n * int(a/n)]


    '''
    mods = {bus: -i % bus for i,bus in enumerate(array) if bus != "x"}
    print(mods)
    values = list(reversed(sorted(mods)))
    print(values)
    MAX = values[0]
    t = mods[MAX]
    for bus in values[1:]:
        while(t%bus != mods[bus]):
            t += MAX
        MAX *= bus

    return t

f = open('q13.txt', 'r')
arr = []
for line in f.readlines():
    arr.append(line.strip())
# Part 1
#print(solution1(arr))

# Part 2
print(solution2(arr))
