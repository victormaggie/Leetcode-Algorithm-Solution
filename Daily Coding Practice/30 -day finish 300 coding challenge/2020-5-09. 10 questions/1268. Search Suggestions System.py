class Solution:
    def suggestedProducts(self, products, searchWord):
        # o(nlogn)
        products = sorted(products)
        res = []
        # o(n)
        for i in range(len(searchWord)):
            stack = []
            prestr = searchWord[:i+1]
            # o(m)
            for j in products:
                # o(k)
                if j.find(prestr) == 0:
                    stack.append(j)
                if len(stack) == 3:
                    break
            if stack:
                res.append(stack)
            else: res.append([])
        return res

# time complexity o(n *m * nlogn)
# space complexity o(n)


# sliding window avoid the repeat calculation
# Omg This algorithm is very effective !!
class Solution:
    def suggestedProducts(self, products, searchWord):
        low, high = 0, len(products)-1
        products = sorted(products)
        n = len(products)
        max_len = len(searchWord)
        res = []
        for i in range(max_len):
            while ((low <= high) and (len(products[low]) <= i or products[low][i] != searchWord[i])):
                low += 1
            while ((low <= high) and (len(products[high]) <= i or products[high][i] != searchWord[i])):
                high -= 1
            Min = min(low+3, high+1)
            temp = []
            for j in range(low, Min):
                temp.append(products[j]) 
            res.append(temp[:])
        return 

# time complexity o(n * m)
# space complexity o(n)

