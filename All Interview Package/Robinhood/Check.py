import collections

def check(n):
    if not n: return 0

    hashset = ['0', '2', '4']
    ans = 0
    for i in range(n+1):
        new = collections.Counter(str(i))
        for char in hashset:
            ans += new[char]
    return ans

print(check(22))

# o n^2


def countOccurence(n):
    cnts = [0] * (n+1)
    cnts[2] = cnts[4] = cnts[0] = 1

    # dynamic programming
    # o(n)
    for v in range(10, len(cnts)):
        r = v % 10
        d = v // 10
        curcnt = cnts[d]

        if r in [0, 2, 4]:
            curcnt += 1
        cnts[v] = curcnt
    
    print(cnts)
    return sum(cnts)

print(countOccurence(22))