import sys

def EUA(a, b):
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while(b > 0):
        r = a%b
        q = int(a/b)
        a = b
        b = r
        tmps = s1 - q*s2
        tmpt = t1 - q*t2
        s1 = s2
        s2 = tmps
        t1 = t2
        t2 = tmpt
    return [s1, t1]

def CRT(p1, p2, r1, r2):
    m1, m2 = EUA(p1, p2)
    return (r1*m2*p2 + r2*m1*p1) % (p1*p2)

primes = [8,9,5,7,11,13,17]
rem = [0]*7

T, N, M = [int(s) for s in input().split()]
for i in range(T):
    for j in range(7):
        p = primes[j]
        print((str(p) + ' ') * 18)
        sys.stdout.flush()
        nums = [int(s) for s in input().split()]
        if nums[0] == -1:
            sys.exit(1)
        r = 0
        for n in nums:
            r = r + n
        r = r%p
        rem[j] = r
    p = primes[0]
    r = rem[0]
    for j in range(1, 7):
        ans = CRT(p, primes[j], r, rem[j])
        p = p * primes[j]
        r = ans
    print(ans)
    sys.stdout.flush()
    correct = int(input())
    if correct == -1:
        sys.exit(rem)
    