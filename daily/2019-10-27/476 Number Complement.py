# bit manipulation

class Solution:
    def findComplement(self, num):

        # construct all the bitwise number
        return num ^ ((1<<(len(num)-2))-1)

    def findComplement_1(self, num):

        comp_num = bin(num)[2::]
        complement = [i for i in map(lambda x: '0' if x == '1' else '0', comp_num)]
        return int(''.join(complement), 2)