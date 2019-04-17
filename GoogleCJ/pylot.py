def solve(R, C, f):
    if R == 2:
        for i in range(1, C+1):
            y = i+2
            if y > C:
                y = y-C
            if f:
                print('{} {}'.format(y, 2))
                print('{} {}'.format(i, 1))
            else:
                print('{} {}'.format(2, y))
                print('{} {}'.format(1, i))
        return
    for i in range(1, C+1):
        if R == C and i == C and R%2 == 0:
            for j in range(2, R+2):
                if j%2 == 0:
                    y = 2
                else:
                    y = C
                x = j
                if x > R:
                    x = x - R
                if f:
                    print('{} {}'.format(y, x))
                else:
                    print('{} {}'.format(x, y))
            break
        for j in range(1, R+1):
            y = i + ((j+1)%2)*2
            if y > C:
                y = y - C
            if f:
                print('{} {}'.format(y,j))
            else:
                print('{} {}'.format(j,y))
        
T = int(input())
for i in range(T):
    R, C = [int(s) for s in input().split()]
    re = False
    if R > C:
        tmp = R
        R = C
        C = tmp
        re = True
    if R == 2:
        f = (C >= 5)
    elif R == 3:
        f = (C >= 4)
    else:
        f = True
    if f:
        print('Case #{}: POSSIBLE'.format(i+1))
        solve(R, C, re)
    else:
        print('Case #{}: IMPOSSIBLE'.format(i+1))
