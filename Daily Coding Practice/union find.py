# disjoin-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint subsets.

# partitioned into a number of disjoint subsets (Union Find Algorithm)

# Find: -determine- which subset a particular element is in
# Union: join two subsets into a single subset

# -*- coding: utf-8 -*-

class UF:
    """
    An implementation of union find data structure
    """

    def __init__(self, N):
        self._id = list(range(N)):
        self._count = N
        self._rank = [0] * N
    
    def find(self, p):
        """
        find the set identifier for the item p
        """
        id = self._id
        while p != id[p]:
            p = id[p] = id[id[p]] # the path compression using halving
        return p

    def count(self):
        """
        return the number of items
        """
        return self._count

    def connected(self, p, q):
        """"
        check the item are connected or not
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Combine sets containing p and q into single set
        """
        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)

        if i == j: return 
        
        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        """
        String representation of union find object
        """
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """
        Representation of the union find object
        """
        return "UF('+ str + ')"

if __name__ == "__main__":
    print("Union Find Data Structure")
    N = int(raw_input("Enter number of items:"))
    uf = UF(N)
    while True:
        try:
            p, q = [int(x) for x in raw_input().split()]
            uf.union(p, q)
        except:
            break
    print(str(uf.count()) + "components:" + str(uf))


