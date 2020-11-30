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


