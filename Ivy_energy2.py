'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')


def bin_swap(input) :
    
    if not input: return 0
    
    array = [0] * 32
    bit = bin(input)[2:]
    count = -1
    
    # bit = '1011'
    # [0,0,0,0,0,0]
    # for i in range(len(bit)-1, -1, -1):
        # array[count] = bit[i]
        # count -= 1
        
    while abs(count) < len(bit):
        array[count] = bit[count]
        count -= 1
    
    # [0,0,1,0,1,1]
    # next step
    count = 0
    i = 0
    temp = array[-4]
    while count < 8:
        array[i] = array[i + 4]
        i += 4
        count += 1
    array[0] = temp
    
    return int(''.join(array), 2)
    
