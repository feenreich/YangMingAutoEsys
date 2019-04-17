import sys

def solve(R, C, f):
    if R == 2:
        for i in range(1, C+1):
            y = i+2
            if y > C:
                y = y-C
            ans.append([y,2])
            ans.append([i,1])
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
                ans.append([y,x])
            break
        for j in range(1, R+1):
            y = i + ((j+1)%2)*2
            if y > C:
                y = y - C
            ans.append([y,j])
        

def adj(a, b):
    if a[0] == b[0] or a[1] == b[1] or a[0]-a[1] == b[0]-b[1] or a[0]+a[1] == b[0]+b[1]:
        return True
    else:
        return False
    
def check(A):
    field = [0]*(R*C)
    if len(A) != R*C:
        return False
    for i in range(len(A)-1):
        if adj(A[i], A[i+1]):
            return False
    for elem in A:
        idx = (elem[0]-1)*R + (elem[1]-1)
        field[idx] = field[idx] + 1
        if field[idx] > 1:
            return False
    if not all(field):
        return False
    return True

for R in range(2, 21):
    for C in range(R, 21):
        ans = []
        if R == 2:
            f = (C >= 5)
        elif R == 3:
            f = (C >= 4)
        else:
            f = True
        if f:
            solve(R, C, 0)
            if not check(ans):
                print('Case :{} {}'.format(R, C))
                for elem in ans:
                    print('{} {}'.format(elem[0], elem[1]))
                sys.exit()