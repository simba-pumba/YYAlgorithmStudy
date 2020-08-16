case = int(input())

for _ in range(case):
    network = set()
    F = int(input())
    past, size = 0, 2
    for i in range(F):
        network = network.union(set(input().split()))
        new_size = len(network)
        if (new_size%2) == 1:
            size +=1
        elif new_size == (size + 1):
            size += 1
        elif (i> 0) and (past == new_size):
            size += 2
        past = new_size
        print(size)

##########

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x!=y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
    
        union(x, y)
    print(number[find(x)])