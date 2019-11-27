import collections
class Solution:

    # Bug inside!!
    def fractionToDecimal(self, numerator, denominator):
        
        hash_table = collections.defaultdict(int)

        # Part I: can divide to integer !
        if numerator % denominator == 0:
            return str(int(numerator / denominator))

        # Part II: cannot divide into integer!

        loopstr = ''
        non_loopstr = ''
        res = []  # define a stack to store the decimal
        ans = ''  # the final answer string
        cnt = 1   # track the none repeated answer
        Flag = numerator * denominator > 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator:
            # track the integer part
            res.append(numerator//denominator)
            residual = numerator % denominator

            # calculate the fraction part
            while residual != 0:
                temp = residual * 10 // denominator
                residual = residual * 10 % denominator
                cnt += 1
                if residual not in hash_table:
                    # put into hash and track the index
                    hash_table[residual] = cnt
                    res.append(str(temp))
                else:
                    res.append(str(temp))
                    loopstr = ''.join(res[hash_table[residual]:cnt])
                    non_loopstr = ''.join(res[1:hash_table[residual]])
                    break
        if loopstr:
            ans = str(res[0]) + '.' + non_loopstr + '(' + loopstr + ')'
        else:
            ans = str(res[0]) + '.' + ''.join(res[1:])

        if not Flag:
            ans = '-' + ans
        return ans



