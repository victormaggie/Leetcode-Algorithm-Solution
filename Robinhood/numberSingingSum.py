def numberSigningSum(n):

    if not n: return 0

    ans = 0

    n = str(n)
    count = 1
    for i in n:
        val = int(i) if count & 1 else -int(i)
        ans += val
        count += 1
    
    return ans


print(numberSigningSum(104956))