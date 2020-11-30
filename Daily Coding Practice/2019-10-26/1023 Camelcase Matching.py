

# Two pointer for the solution
# Hash map is not efficient to control the pointer
class solution:

    def ifcamelMatch(self, query, pattern):
        # define two pointers
        p_idx, p_len = 0, len(pattern)

        for letter in query:
            if p_idx < p_len and letter == pattern[p_idx]:
                p_idx += 1
            elif letter.islower():
                continue
            else:
                return False
        return p_idx == p_len
    
    def camelMatch(self, queries, pattern):
        return [self.ifcamelMatch(query, pattern) for query in queries]
            

# solution 2, we can use regular expression for pattern split

    def camelMatch2(self, queries, pattern):
        import re
        ps = re.findall("[A-Z][a-z]*", pattern)
        #num = len(queries)
        res = []

        for q in queries:
            qs = re.findall("[A-Z][a-z]*", q)
            hasFind = False
            if len(ps) == len(qs):
                if all(self.isSubSeq(q,p) for (q, p) in zip(qs, ps)):
                    hasFind = True
            res.append(hasFind)
        return res

    def isSubSeq(self, qu, pa):
        qu = iter(qu)
        return all(p in qu for p in pa)

