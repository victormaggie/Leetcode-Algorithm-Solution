def ConcatSwaps(input, size):

    if len(input) != sum(size): return ''

    stack = []

    start = 0
    for i in size:

        char = input[start:start + i]
        start += i
        stack.append(char)

    print(stack, '//')
    for i in range(0, len(stack)-1, 2):
        stack[i], stack[i+1] = stack[i+1], stack[i]

    return ''.join(stack)

input = "descognail"
size = [3, 2, 3, 1, 1]

print(ConcatSwaps(input, size))

