'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')


# arr = [1, 2, 3, 4];
# arr = [3, 2, 1];


def check_order(arr):
    if not arr: return False
    if len(arr) == 1: return True
    for fast in range(1, len(arr)):
        if arr[fast] > arr[fast-1]: continue
        else: return False
    return True

index = bisect.bisect_left(arr[:memo], arr[memo])
arr[index], arr[memo] = arr[memo], arr[index]

def swap_once(arr):
    
    # 1. go check 
    if check_order(arr): return True
    
    # 2. get the index 
    memo = 0
    for fast in range(1, len(arr)):
        if arr[fast] > arr[fast-1]: continue
        memo = fast
    # 3. boundy  
    if (memo == len(arr) - 1): arr[-1], arr[-2] = arr[-2], arr[-1]
    else: arr[memo], arr[memo + 1] = arr[memo + 1], arr[memo]
    # [1, 2, 2, 3]
    
    if check_order(arr): return True
    
    return False
    
arr = [1, 2, 3, 5, 3]

print(swap_once(arr))
    