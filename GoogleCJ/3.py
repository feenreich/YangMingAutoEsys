def gcd(a,b):
    while(b != 0):
        r = a%b
        a = b
        b = r
    return a

T = int(input().strip())
for i in range(1, T+1):
    N, L = [int(s) for s in input().split()]
    nums = [int(s) for s in input().split()]
    primes = []
    my_dict = {}
    ans_int = [0]*(L+1)
    ans = ""
    for j in range(L):
        if nums[j] != nums[j+1]:
            ans_int[j+1] = gcd(nums[j],nums[j+1])
            primes.append(ans_int[j+1])
            break
    for k in reversed(range(j+1)):
        ans_int[k] = nums[k]/ans_int[k+1]
        if (not ans_int[k] in primes) and ans_int[k] > 1:
            primes.append(ans_int[k])
    for k in range(j+1,L):
        ans_int[k+1] = nums[k]/ans_int[k]
        if (not ans_int[k+1] in primes) and ans_int[k+1] > 1:
            primes.append(ans_int[k+1])
    if len(primes) != 26:
        continue
    primes.sort()
    C = 'A'
    for p in primes:
        my_dict[p] = C
        C = chr(ord(C)+1)
    for val in ans_int:
        ans = ans + my_dict[val]
    print("Case #{}: {}".format(i,ans))
    