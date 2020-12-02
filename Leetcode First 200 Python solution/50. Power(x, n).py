# fast power solution

def power(x , n):
    is_minus = -1 if n < 0 else 1
    result = 1
    n = abs(n)
    while n:
        if n & 1: res *= x
        x *= x
        n >>= 1
    if is_minus == -1: return 1 / res
    return res

# log n solution
