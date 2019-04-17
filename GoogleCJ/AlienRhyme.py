class Node:
    def __init__(self, v, c):
        self.chd = []
        self.v = v
        self.c = c
        self.f = False

def insert(root, s):
    cur = root
    l = len(s)
    for i in reversed(range(l)):
        f = False
        for node in cur.chd:
            if s[i] == node.c:
                f = True
                cur = node
                cur.v = cur.v + 1
                if i == 0:
                    node.f = True
                break
        if not f:
            node = Node(1, s[i])
            cur.chd.append(node)
            cur = node
            if i == 0:
                node.f = True

def traverse(root):
    print('{},{}'.format(root.c, root.v))
    for node in root.chd:
        traverse(node)

def solve(root):
    if root.v == 1:
        return [0, 1]
    elif root.v == 2:
        return [2, 0]
    else:
        total = 0
        remain = 0
        for node in root.chd:
            t, r = solve(node)
            total = total + t
            remain = remain + r
        if root.f:
            remain = remain + 1
        if remain >= 2 and root.c != '':
            total = total + 2
            return [total, remain - 2]
        else:
            return [total, remain]

T = int(raw_input())
for i in range(1,T+1):
    root = Node(0, '')
    N = int(raw_input())
    for j in range(N):
        s = raw_input()
        insert(root, s)
    #traverse(root)
    print('Case #{}: {}'.format(i,solve(root)[0]))


