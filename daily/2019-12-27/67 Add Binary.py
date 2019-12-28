class Solution(object):
    def addBinary(self, a, b):
        return bin((int(a,2) + int(b,2)))[2:]

# time complexity o(m+n)
# Bit by Bit computation

    def addBinary2(self, a, b):
        n = max(len(a), len(b))
        # fill the string
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)
# o(max(m, n))

    def addBinary3(self, a, b):
        x, y = int(a,2), int(b,2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

# o(max(m, n))