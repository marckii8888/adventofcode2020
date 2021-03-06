from string import digits

def solution(tree_dict, target):
    secondary = []
    found = []
    secondary.append(target)
    res = 0
    while(secondary):
        item = secondary.pop(0)
        print(item) 
        for k,v in tree_dict.items():
            if(item in v and k not in found):
                secondary.append(k)
                found.append(k)
                res+=1
    return res

def DFS(tree_dict, target):
    res = 0
    try:
        children = tree_dict[target]
        for child in children:
            if(child[0]=='n'):
                return 0
            num = int(child[0])
            color = child[1:].strip()
            res += num + num*(DFS(tree_dict, color))
    except KeyError:
        return 0

    return res

def solution2(tree_dict, target):
    # Value = number color
    # Key = color (no bag)
    res = 0
    children = tree_dict[target] # 1 dark olive, 2 vibrant plum
    for child in children:
        num = int(child[0])
        color = child[1:].strip()
        res += num + num*(DFS(tree_dict, color))
    return res

tree_dict = {}
f = open('q7.txt', 'r')
for line in f.readlines():
    line = line.strip()
    line = line[:-1]
    parent, child = line.split('contain')
    parent = parent.replace('bags','').replace('bag','').strip()
    child = child.split(',')
    child = [ele.strip() for ele in child]
# For solution 1
#    child = [ele.translate(str.maketrans('', '', digits)).replace('bags', '').replace('bag','').strip() for ele in child]
    # For solution 2
child = [ele.replace('bags','').replace('bag', '').strip() for ele in child]
    tree_dict.update({parent: child})
#print(solution(tree_dict, 'shiny gold'))
print(solution2(tree_dict, 'shiny gold'))
