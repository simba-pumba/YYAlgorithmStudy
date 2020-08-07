from math import log2

def pre_order(head):
    if head >= len(tree):
        return
    if tree[head] == ".":
        return
    print(tree[head], end='')
    pre_order(head*2+1)
    pre_order(head*2+2)

def in_order(head):
    if head >= len(tree):
        return
    if tree[head] == ".":
        return
    in_order(head*2+1)
    print(tree[head], end='')
    in_order(head*2+2)

def post_order(head):
    if head >= len(tree):
        return
    if tree[head] == ".":
        return
    post_order(head*2+1)
    post_order(head*2+2)
    print(tree[head], end='')

def main():
    n = int(input())

    tree = ['.' for i in range(int(2**((log2(n))+2)))]
    tree[0] = 'A'
    for i in range(n):
        line = input().split()
        loc = tree.index(line[0])
        try:
            tree[loc*2+1] = line[1]
        except:
            pass
        try:
            tree[loc*2+2] = line[2]
        except:
            pass
    pre_order(0)
    print()
    in_order(0)
    print()
    post_order(0)
    print()

main()